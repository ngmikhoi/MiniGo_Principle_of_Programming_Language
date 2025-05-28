# 2252377 - Nguyen Minh Khoi
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce


class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.arrcell = None         
        self.eleArr = None
        self.funcPara = False
        self.type = None
        self.methFunc = None     
        self.symList = [] 

    def init(self):
        mem = [
            Symbol("getInt",MType([],IntType()),CName("io",True)),
            Symbol("getFloat",MType([],FloatType()),CName("io",True)),
            Symbol("getBool",MType([],BoolType()),CName("io",True)),
            Symbol("getString",MType([],StringType()),CName("io",True)),
            Symbol("putLn",MType([],VoidType()),CName("io",True)),
            Symbol("putInt",MType([IntType()],VoidType()),CName("io",True)),
            Symbol("putIntLn",MType([IntType()],VoidType()),CName("io",True)),
            Symbol("putFloat",MType([FloatType()],VoidType()),CName("io",True)),
            Symbol("putFloatLn",MType([FloatType()],VoidType()),CName("io",True)),
            Symbol("putBool",MType([BoolType()],VoidType()),CName("io",True)),
            Symbol("putBoolLn",MType([BoolType()],VoidType()),CName("io",True)),
            Symbol("putString",MType([StringType()],VoidType()),CName("io",True)),
            Symbol("putStringLn",MType([StringType()],VoidType()),CName("io",True)),           
        ]
        return mem
    
    def gen(self,ast,dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast,gl)
       
    def emitObjectInit(self):
        frame = Frame("<init>",VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>",MType([],VoidType()),False,frame))
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),"this",ClassType(self.className),frame.getStartLabel(),frame.getEndLabel(),frame))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))
        self.emit.printout(self.emit.emitREADVAR("this",ClassType(self.className),0,frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(),frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def visitProgram(self,ast,c):
        env = {}
        self.symList = c + [Symbol(sym.name,MType(reduce(lambda a,e: a + [e.parType],sym.params,[]),sym.retType),CName(self.className)) for sym in ast.decl if type(sym) is FuncDecl]
        self.namesDict = {decl.name: decl for decl in ast.decl if isinstance(decl,InterfaceType) or isinstance(decl,StructType)}
        env['env'] = [c]
        program = Emitter(self.path + "/" + self.className + ".j")
        self.emit = program
        self.emit.printout(self.emit.emitPROLOG(self.className,""))
        env = reduce(lambda acc,ele: self.visit(ele,acc) if isinstance(ele,ConstDecl) or isinstance(ele,VarDecl) else acc,ast.decl,env)
        def taskMeth(o,typ):
            if isinstance(typ,InterfaceType) or isinstance(typ,StructType):
                typ.methods = reduce(lambda a,e: a + [e] if (isinstance(e,MethodDecl) and isinstance(e.recType,Id) and e.recType.name == typ.name) else a, ast.decl, typ.methods if hasattr(typ,'methods') else [])
                self.type = typ
                self.emit = Emitter(self.path + "/" + typ.name + ".j")
                self.visit(typ,{'env': o['env']})
                self.emit.printout(self.emit.emitEPILOG())
            return o
        env = reduce(taskMeth,ast.decl,env)
        self.emit = program
        env = reduce(lambda acc,ele: self.visit(ele,acc) if type(ele) is FuncDecl else acc,ast.decl,env)
        self.emitObjectInit()
        self.emitClass(ast,env)
        self.emit.printout(self.emit.emitEPILOG())
        return env

    def visitFuncDecl(self,ast,o):
        frame = Frame(ast.name,ast.retType)
        self.methFunc = ast        
        if ast.name == "main":
            mtype = MType([ArrayType([None],StringType())],VoidType())
            ast.body = Block([] + ast.body.member)
        else:
            mtype = MType(reduce(lambda a,e: a + [e.parType],ast.params,[]),ast.retType)
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name,mtype,True,frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))
        env['env'] = [[]] + env['env']
        if ast.name == "main":
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),"args",ArrayType([None],StringType()),frame.getStartLabel(),frame.getEndLabel(),frame))
        else:
            tmp = self.funcPara
            self.funcPara = True
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
            self.funcPara = tmp
        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
        if isinstance(ast.retType,VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(),frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def visitVarDecl(self,ast,o):
        def defaultType(varType,o):
            if isinstance(varType,IntType):
                return IntLiteral(0)
            elif isinstance(varType,FloatType):
                return FloatLiteral(0.0)
            elif isinstance(varType,StringType):
                return StringLiteral("\"\"")
            elif isinstance(varType,BoolType):
                return BooleanLiteral(False)  
            elif isinstance(varType,Id):
                if varType.name in self.namesDict and isinstance(self.namesDict[varType.name],StructType):
                    return StructLiteral(varType.name,[])
                return NilLiteral()
            elif isinstance(varType,ArrayType):
                dimens = varType.dimens
                eleType = varType.eleType
                if not dimens:
                    dimens = [IntLiteral(1)]
                def changeInt(dim):
                    if dim is None:
                        return 1
                    elif isinstance(dim,int):
                        return dim
                    elif isinstance(dim,IntLiteral):
                        return dim.value
                    elif isinstance(dim,str):
                        return int(dim)
                    elif isinstance(dim,Id):
                        for decl in self.astTree.decl:
                            if isinstance(decl,ConstDecl) and decl.conName == dim.name:
                                if isinstance(decl.iniExpr,IntLiteral):
                                    return decl.iniExpr.value
                    return 1
                dimensInt = list(map(lambda x: changeInt(x), dimens))
                def arrayNest(dimensInt,eleType,deg=0):
                    if deg >= len(dimensInt):
                        return defaultType(eleType,o)
                    else:
                        return list(map(lambda x: arrayNest(dimensInt,eleType,deg+1), range(dimensInt[deg])))
                return ArrayLiteral(dimens,eleType,arrayNest(dimensInt,eleType))
            return None 
        varInit = ast.varInit
        varType = ast.varType
        if not varInit:
            varInit = defaultType(varType,o)
            ast.varInit = varInit
        env = o.copy()
        if 'frame' not in o:
            env['frame'] = Frame("<global>",VoidType())
        else:
            env['frame'] = o['frame']
        codeRhs = ""
        typeRhs = None
        frame = env['frame']
        if varInit:
            tmp = env.get('stmt',False)
            env['stmt'] = False            
            codeRhs,typeRhs = self.visit(varInit,env)            
            env['isLeft'] = False            
            if codeRhs is None:
                codeRhs = ""
        else:
            if isinstance(varType,ArrayType):
                dimens = varType.dimens
                eleType = varType.eleType                
                for dim in dimens:
                    if isinstance(dim,IntLiteral):
                        codeRhs += self.emit.emitPUSHCONST(str(dim.value),IntType(),frame)
                    else:
                        codeRhs += self.emit.emitGETSTATIC(f"{self.className}/{dim.name}",IntType(),frame)
                    frame.push()
                typeJVM = reduce(lambda a,e: a + "[", dimens, "")
                if isinstance(eleType,Id):
                    typeJVM += f"L{eleType.name};"
                elif isinstance(eleType,IntType):
                    typeJVM += "I"
                elif isinstance(eleType,FloatType):
                    typeJVM += "F"
                elif isinstance(eleType,BoolType):
                    typeJVM += "Z"
                elif isinstance(eleType,StringType):
                    typeJVM += "Ljava/lang/String;"
                codeRhs += self.emit.emitMULTIANEWARRAY(typeJVM,len(dimens),frame)
                list(map(lambda x: frame.pop(), dimens))
                frame.push()
                typeRhs = varType
        declType = varType if varType else typeRhs
        if 'frame' not in o:
            isConst = hasattr(ast,'conName')
            o['env'][0].append(Symbol(ast.varName,declType,CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName,declType,True,isConst,None))
        else:
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName,declType,Index(index)))
            emitTypeVar = ClassType(declType.name) if isinstance(declType,Id) else declType
            if isinstance(declType,ArrayType) and isinstance(declType.eleType,Id):
                emitTypeVar = ArrayType(declType.dimens,ClassType(declType.eleType.name))
            self.emit.printout(self.emit.emitVAR(index,ast.varName,emitTypeVar,frame.getStartLabel(),frame.getEndLabel(),frame))
            if codeRhs:
                if isinstance(declType,FloatType) and isinstance(typeRhs,IntType):
                    codeRhs += self.emit.emitI2F(frame)
            self.emit.printout(codeRhs)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName,declType,index,frame))
        return o
    
    def visitConstDecl(self,ast,o):
        return self.visit(VarDecl(ast.conName,ast.conType,ast.iniExpr),o)
    
    def visitFuncCall(self,ast,o):
        sym = next(filter(lambda x: x.name == ast.funName,self.symList),None)
        env = o.copy()
        env['stmt'] = False
        if o.get('stmt'):
            [self.emit.printout(self.visit(x,env)[0]) for x in ast.args]
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype,o['frame']))
            return o
        else:
            codeArgs = reduce(lambda a,e: a + str(self.visit(e,env)[0]),ast.args,"")
            codeArgs += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype,o['frame'])
            return codeArgs,sym.mtype.rettype

    def visitBlock(self,ast,o):
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(),env['frame']))
        for sth in ast.member:            
            sthEnv = env.copy()
            if (isinstance(sth,MethCall) or isinstance(sth,FuncCall)) and not isinstance(sth,Assign):
                sthEnv["stmt"] = True
            env = self.visit(sth,sthEnv)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(),env['frame']))
        env['frame'].exitScope()
        return o

    def visitId(self,ast,o):
        if isinstance(ast,Id) and self.type and not next(filter(lambda x: x.name == ast.name,[j for i in o['env'] for j in i]),None):
            typeThis = Id(self.type.name)
            if o.get('isLeft'):
                return self.emit.emitWRITEVAR("this",typeThis,0,o['frame']),typeThis
            return self.emit.emitREADVAR("this",typeThis,0,o['frame']),typeThis
        sym = next(filter(lambda x: x.name == ast.name,[j for i in o['env'] for j in i]),None)
        if sym is None:
            if self.type and not o.get('isLeft'):
                return self.emit.emitREADVAR("this",Id(self.type.name),0,o['frame']),Id(self.type.name)
        if o.get('isLeft'):
            if isinstance(sym.value,Index):
                return self.emit.emitWRITEVAR(ast.name,sym.mtype,sym.value.value,o['frame']),sym.mtype
            else:         
                lexeme = f"{sym.value.value}/{ast.name}"
                return self.emit.emitPUTSTATIC(lexeme,sym.mtype,o['frame']),sym.mtype
        elif isinstance(sym.value,Index):
            return self.emit.emitREADVAR(ast.name,sym.mtype,sym.value.value,o['frame']),sym.mtype
        else:         
            lexeme = f"{sym.value.value}/{ast.name}"
            return self.emit.emitGETSTATIC(lexeme,sym.mtype,o['frame']),sym.mtype
    
    def visitIntLiteral(self,ast,o):
        return self.emit.emitPUSHICONST(ast.value,o['frame']),IntType()
    
    def visitFloatLiteral(self,ast,o):
        return self.emit.emitPUSHFCONST(ast.value,o['frame']),FloatType()
    
    def visitStringLiteral(self,ast,o):
        return self.emit.emitPUSHCONST(ast.value,StringType(),o['frame']),StringType()
    
    def visitBooleanLiteral(self,ast,o):
        return self.emit.emitPUSHICONST(1 if (ast.value == "true" or ast.value == True) else 0,o['frame']),BoolType()
    
    def visitNilLiteral(self,ast,o):
        return self.emit.emitPUSHNULL(o['frame']),Id("")
    
    def visitUnaryOp(self,ast,o):
        ecode,etype = self.visit(ast.body,o)
        if ast.op == '-':
            return ecode + self.emit.emitNEGOP(etype,o['frame']),etype
        elif ast.op == '!':
            return ecode + self.emit.emitNOT(etype,o['frame']),etype
    
    def visitBinaryOp(self,ast,o):
        frame = o['frame']                
        lcode,ltype = self.visit(ast.left,o)
        rcode,rtype = self.visit(ast.right,o)        
        if ast.op in ['==','!='] and ((isinstance(ltype,Id) and isinstance(rtype,Id)) or isinstance(ltype,BoolType)):
            inLabel = frame.getNewLabel()
            outLabel = frame.getNewLabel()
            binCode = lcode + rcode
            frame.pop() 
            frame.pop() 
            if ast.op == '==':
                if isinstance(ltype,BoolType):
                    binCode += self.emit.jvm.emitIFICMPEQ(outLabel)
                else:
                    binCode += self.emit.jvm.emitIFACMPEQ(outLabel)
            else:
                if isinstance(ltype,BoolType):
                    binCode += self.emit.jvm.emitIFICMPNE(outLabel)
                else:
                    binCode += self.emit.jvm.emitIFACMPNE(outLabel)
            binCode += self.emit.emitPUSHICONST(0,frame)
            binCode += self.emit.emitGOTO(inLabel,frame)
            binCode += self.emit.emitLABEL(outLabel,frame)
            binCode += self.emit.emitPUSHICONST(1,frame)
            binCode += self.emit.emitLABEL(inLabel,frame)
            return binCode,BoolType()
        elif ast.op == '+' and isinstance(ltype,StringType):
            return lcode + rcode + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat",MType([StringType()],StringType()),frame),StringType()
        elif ast.op in ['==','!=','<','>','>=','<='] and isinstance(ltype,StringType):
            binCode = lcode + rcode + self.emit.emitINVOKEVIRTUAL("java/lang/String/compareTo",MType([StringType()],IntType()),frame)
            inLabel = frame.getNewLabel()
            outLabel = frame.getNewLabel()
            frame.pop()
            if ast.op == '>':
                binCode += self.emit.jvm.emitIFLE(inLabel)
            elif ast.op == '>=':
                binCode += self.emit.jvm.emitIFLT(inLabel)
            elif ast.op == '<':
                binCode += self.emit.jvm.emitIFGE(inLabel)
            elif ast.op == '<=':
                binCode += self.emit.jvm.emitIFGT(inLabel)
            elif ast.op == '==':
                binCode += self.emit.jvm.emitIFNE(inLabel)  
            elif ast.op == '!=':
                binCode += self.emit.jvm.emitIFEQ(inLabel)
            binCode += self.emit.emitPUSHICONST(1,frame)
            frame.pop()
            binCode += self.emit.emitGOTO(outLabel,frame)
            binCode += self.emit.emitLABEL(inLabel,frame)
            binCode += self.emit.emitPUSHICONST(0,frame)
            binCode += self.emit.emitLABEL(outLabel,frame)
            return binCode,BoolType()  
        elif ast.op in ['+','-'] and (isinstance(ltype,FloatType) or isinstance(ltype,IntType)):
            binType = IntType() if isinstance(ltype,IntType) and isinstance(rtype,IntType) else FloatType()
            if isinstance(binType,FloatType):
                if isinstance(ltype,IntType):
                    lcode += self.emit.emitI2F(frame)
                if isinstance(rtype,IntType):
                    rcode += self.emit.emitI2F(frame)            
            return lcode + rcode + self.emit.emitADDOP(ast.op,binType,frame),binType
        elif ast.op in ['*','/']:
            binType = IntType() if isinstance(ltype,IntType) and isinstance(rtype,IntType) else FloatType()
            if isinstance(binType,FloatType):
                if isinstance(ltype,IntType):
                    lcode += self.emit.emitI2F(frame)
                if isinstance(rtype,IntType):
                    rcode += self.emit.emitI2F(frame)        
            return lcode + rcode + self.emit.emitMULOP(ast.op,binType,frame),binType
        elif ast.op == '%':
            return lcode + rcode + self.emit.emitMOD(frame),IntType()
        elif ast.op in ['==','!=','<','>','>=','<='] and (isinstance(ltype,FloatType) or isinstance(ltype,IntType)):
            binType = BoolType()
            return lcode + rcode + self.emit.emitREOP(ast.op,ltype,frame),binType
        elif ast.op in ['||','&&']:
            trueLabel = frame.getNewLabel()
            falseLabel = frame.getNewLabel()
            outLabel = frame.getNewLabel()
            binCode = self.visit(ast.left,o)[0]
            if ast.op == '||':
                binCode += self.emit.emitIFNE(trueLabel,frame)
            else:
                binCode += self.emit.emitIFEQ(falseLabel,frame)
            envRight = o.copy()
            envRight['stmt'] = False
            binCode += self.visit(ast.right,envRight)[0]
            binCode += self.emit.emitIFNE(trueLabel,frame)
            binCode += self.emit.emitGOTO(falseLabel,frame)
            binCode += self.emit.emitLABEL(trueLabel,frame)
            binCode += self.emit.emitPUSHICONST(1,frame)
            binCode += self.emit.emitGOTO(outLabel,frame)
            binCode += self.emit.emitLABEL(falseLabel,frame)
            binCode += self.emit.emitPUSHICONST(0,frame)
            binCode += self.emit.emitLABEL(outLabel,frame)
            return binCode,BoolType()
    
    def isMatch(self,struct,interface,coupType):
        trueCoup = any(isinstance(interface,couple[0]) and isinstance(struct,couple[1]) for couple in coupType)
        if not trueCoup:
            return False
        elif not (isinstance(interface,InterfaceType) and isinstance(struct,StructType)):
            return False
        interMeths = interface.methods
        structMeths = getattr(struct,'methods',[])
        def sameMeth(interMeth,structMeth):
            if interMeth.name != structMeth.fun.name:
                return False
            elif not self.identical(interMeth.retType,structMeth.fun.retType):
                return False  
            interParams = [p for p in interMeth.params]
            structParams = [p.parType for p in structMeth.fun.params]
            if len(interParams) != len(structParams):
                return False
            return all(self.identical(interP,structP) for interP,structP in zip(interParams,structParams))
        for interMeth in interMeths:
            if not any(sameMeth(interMeth,structMeth) for structMeth in structMeths):
                return False
        return True
    
    def visitParamDecl(self,ast,o):
        num = o['frame'].getNewIndex()
        if num == 0 and not self.funcPara:
            num = o['frame'].getNewIndex()
        o['env'][0] += [Symbol(ast.parName,ast.parType,Index(num))]
        self.emit.printout(self.emit.emitVAR(num,ast.parName,ast.parType,o['frame'].getStartLabel() ,o['frame'].getEndLabel(),o['frame']))     
        return o
    
    def visitInterfaceType(self,ast,o):
        self.emit.printout(self.emit.emitPROLOG(ast.name,"",True))
        for meth in ast.methods:
            self.emit.printout(self.emit.emitMETHOD(meth.name,MType([x for x in meth.params],meth.retType),False,None,True) + self.emit.emitENDMETHOD2())
            
    def visitStructType(self,ast,o):
        self.emit.printout(self.emit.emitSTRUCT(ast.name))
        [self.emit.printout(self.emit.emitIMPLEMENTS(name)) for name in [sth.name for sth in self.namesDict.values() if isinstance(sth,InterfaceType) and self.isMatch(ast,sth,[(InterfaceType,StructType)])]]
        [self.emit.printout(self.emit.emitINSTANCEFIELD(e[0],e[1])) for e in ast.elements]
        self.visit(MethodDecl(None,Id(ast.name),FuncDecl("<init>",[ParamDecl(f"param_{e[0]}",e[1]) for e in ast.elements],VoidType(),Block([Assign(FieldAccess(Id("this"),e[0]),Id(f"param_{e[0]}")) for e in ast.elements]))),o)
        self.visit(MethodDecl(None,Id(ast.name),FuncDecl("<init>",[],VoidType(),Block([]))),o)
        [self.visit(sth,o) for sth in getattr(ast,'methods',[])]
    
    def emitClass(self,ast,o):
        frame = Frame("<clinit>",VoidType())
        self.emit.printout(self.emit.emitMETHOD("<clinit>",MType([],VoidType()),True,frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))
        envInit = o.copy()
        envInit['frame'] = frame 
        blockInstance = [] 
        for sth in ast.decl: 
            if (isinstance(sth,VarDecl) and sth.varInit is not None) or (isinstance(sth,ConstDecl) and sth.iniExpr is not None):
                nameVar = sth.conName if isinstance(sth,ConstDecl) else sth.varName
                instanceAssign = Assign(Id(nameVar),sth.varInit if isinstance(sth,VarDecl) else sth.iniExpr)
                blockInstance.append(instanceAssign)
        if blockInstance:
            self.visit(Block(blockInstance),envInit)
        self.emit.printout(self.emit.emitLABEL(frame.getNewLabel(),frame))
        self.emit.printout(self.emit.emitLABEL(frame.getNewLabel(),frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame)) 
        self.emit.printout(self.emit.emitRETURN(VoidType(),frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope() 
    
    def visitAssign(self,ast,o):
        flag = isinstance(ast.lhs,Id) and self.type and isinstance(ast.rhs,MethCall) and  isinstance(ast.rhs.receiver,Id) and ast.rhs.receiver.name == ast.lhs.name
        if isinstance(ast.lhs,Id) and not flag and not next(filter(lambda x: x.name == ast.lhs.name,[j for i in o['env'] for j in i]),None):
            o = self.visit(VarDecl(ast.lhs.name,None,ast.rhs),o)
            ast.lhs = Id(ast.lhs.name)
        rootStmt = o.get('stmt')
        o['stmt'] = False
        codeRhs,typeRhs = self.visit(ast.rhs,o)
        o['stmt'] = rootStmt
        frame = o['frame']
        if isinstance(ast.lhs,ArrayCell):
            o['isLeft'] = True
            codeLhs,typeLhs = self.visit(ast.lhs,o)
            o['isLeft'] = False
            if isinstance(typeLhs,FloatType) and isinstance(typeRhs,IntType):
                codeRhs += self.emit.emitI2F(frame)
            self.emit.printout(codeLhs)
            self.emit.printout(codeRhs) 
            self.emit.printout(self.emit.emitASTORE(self.eleArr,frame))
        elif isinstance(ast.lhs,FieldAccess):
            codeRec,typeRec = self.visit(ast.lhs.receiver,o)
            typLhs = next((x for x in self.namesDict.get(typeRec.name).elements if x[0] == ast.lhs.field),None)[1]
            if isinstance(typLhs,FloatType) and isinstance(typeRhs,IntType):
                codeRhs += self.emit.emitI2F(frame)
            frame.push()
            frame.push()
            self.emit.printout(codeRec)
            self.emit.printout(codeRhs)
            self.emit.printout(self.emit.emitPUTFIELD(f"{typeRec.name}/{ast.lhs.field}",typLhs,frame))
        else:
            o['isLeft'] = True
            codeLhs,typeLhs = self.visit(ast.lhs,o)
            o['isLeft'] = False
            if isinstance(typeLhs,FloatType) and isinstance(typeRhs,IntType):
                codeRhs += self.emit.emitI2F(frame)
            if (isinstance(typeLhs,ArrayType) and isinstance(typeLhs.eleType,FloatType) and isinstance(typeRhs,ArrayType) and isinstance(typeRhs.eleType,IntType)):        
                rhsAssign = codeRhs
                rhsAssign += self.emit.emitPUSHICONST(typeLhs.dimens[0].value,frame)
                frame.push() 
                rhsAssign += self.emit.emitNEWARRAY(FloatType(),frame)
                frame.pop() 
                frame.push() 
                loopLabel = frame.getNewLabel()
                outLabel = frame.getNewLabel()
                varIdx = frame.getNewIndex()
                rhsAssign += self.emit.emitPUSHICONST(0,frame)
                rhsAssign += self.emit.emitWRITEVAR("tmpIdx",IntType(),varIdx,frame)
                rhsAssign += self.emit.emitLABEL(loopLabel,frame)
                rhsAssign += self.emit.emitREADVAR("tmpIdx",IntType(),varIdx,frame)
                rhsAssign += self.emit.emitPUSHICONST(typeLhs.dimens[0].value,frame)
                rhsAssign += self.emit.emitIFICMPGE(outLabel,frame)
                rhsAssign += self.emit.emitDUP(frame)
                frame.push() 
                rhsAssign += self.emit.emitREADVAR("tmpIdx",IntType(),varIdx,frame)
                frame.push() 
                rhsAssign += codeRhs 
                rhsAssign += self.emit.emitREADVAR("tmpIdx",IntType(),varIdx,frame)
                rhsAssign += self.emit.emitALOAD(IntType(),frame)
                frame.push()
                rhsAssign += self.emit.emitI2F(frame)
                rhsAssign += self.emit.emitASTORE(FloatType(),frame)
                rhsAssign += self.emit.emitREADVAR("tmpIdx",IntType(),varIdx,frame)
                rhsAssign += self.emit.emitPUSHICONST(1,frame)
                rhsAssign += self.emit.emitADDOP("+",IntType(),frame)
                rhsAssign += self.emit.emitWRITEVAR("tmpIdx",IntType(),varIdx,frame)
                rhsAssign += self.emit.emitGOTO(loopLabel,frame)
                rhsAssign += self.emit.emitLABEL(outLabel,frame)
                self.emit.printout(rhsAssign)
                self.emit.printout(codeLhs)
            else:
                if flag and isinstance(ast.rhs,MethCall):
                    self.emit.printout(codeRhs)
                    if not isinstance(typeRhs,VoidType):
                        self.emit.printout(self.emit.emitPOP(frame))
                else:
                    self.emit.printout(codeRhs)
                    self.emit.printout(codeLhs)
        return o

    def visitIf(self,ast,o):
        outLabel = o['frame'].getNewLabel()
        ifEndLabel = o['frame'].getNewLabel()
        tmp = o.get('stmt',False)
        o['stmt'] = False
        codeCondition,_ = self.visit(ast.expr,o)
        o['stmt'] = tmp
        self.emit.printout(codeCondition)
        self.emit.printout(self.emit.emitIFFALSE(ifEndLabel,o['frame']))
        envThen = o.copy()
        self.visit(ast.thenStmt,envThen)
        if not (isinstance(ast.thenStmt,Return) or (isinstance(ast.thenStmt,Block) and any(isinstance(x,Return) for x in ast.thenStmt.member))):
            self.emit.printout(self.emit.emitGOTO(outLabel,o['frame']))
        self.emit.printout(self.emit.emitLABEL(ifEndLabel,o['frame']))
        if ast.elseStmt is None:
            self.emit.printout(self.emit.emitLABEL(outLabel,o['frame']))
        else:
            envElse = o.copy()
            self.visit(ast.elseStmt,envElse)
            if not (isinstance(ast.elseStmt,Return) or (isinstance(ast.elseStmt,Block) and any(isinstance(x,Return) for x in ast.elseStmt.member))):
                self.emit.printout(self.emit.emitLABEL(outLabel,o['frame']))
        return o
    
    def visitForBasic(self,ast,o):
        o['frame'].enterLoop()
        newLabel = o['frame'].getNewLabel()
        breakLabel = o['frame'].getBreakLabel() 
        contLabel = o['frame'].getContinueLabel()
        self.emit.printout(self.emit.emitLABEL(newLabel,o['frame']))
        self.emit.printout(self.visit(ast.cond,o)[0])
        self.emit.printout(self.emit.emitIFFALSE(breakLabel,o['frame']))
        envLoop = o.copy()
        self.visit(ast.loop,envLoop)
        self.emit.printout(self.emit.emitLABEL(contLabel,o['frame']))        
        self.emit.printout(self.emit.emitGOTO(newLabel,o['frame']))        
        self.emit.printout(self.emit.emitLABEL(breakLabel,o['frame']))                           
        o['frame'].exitLoop()
        return o
    
    def visitForStep(self,ast,o):    
        o['frame'].enterLoop()
        newLabel = o['frame'].getNewLabel()
        breakLabel = o['frame'].getBreakLabel()
        contLabel = o['frame'].getContinueLabel()        
        envInit = o.copy()
        envInit['stmt'] = True
        envInit['env'] = [[]] + envInit['env']
        self.visit(ast.init,envInit)
        self.emit.printout(self.emit.emitLABEL(newLabel,o['frame']))
        envCondit = envInit.copy() 
        envCondit['stmt'] = False 
        codeCondit,_ = self.visit(ast.cond,envCondit)
        self.emit.printout(codeCondit)
        self.emit.printout(self.emit.emitIFFALSE(breakLabel,o['frame']))
        envLoop = envInit.copy() 
        self.visit(ast.loop,envLoop)
        self.emit.printout(self.emit.emitLABEL(contLabel,o['frame']))
        envUpda = envInit.copy()
        envUpda['stmt'] = True
        self.visit(ast.upda,envUpda)
        self.emit.printout(self.emit.emitGOTO(newLabel,o['frame']))
        self.emit.printout(self.emit.emitLABEL(breakLabel,o['frame']))
        o['frame'].exitLoop()
        return o
    
    def visitBreak(self,ast,o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getBreakLabel(),o['frame']))
        return o
    
    def visitContinue(self,ast,o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getContinueLabel(),o['frame']))
        return o

    def visitReturn(self,ast,o):
        if ast.expr:
            rootStmt = o.get('stmt')
            o['stmt'] = False
            exprCode,exprType = self.visit(ast.expr,o)
            o['stmt'] = rootStmt
            self.emit.printout(exprCode if exprCode is not None else "")
            codeRet = self.emit.emitRETURN(exprType,o['frame'])
            self.emit.printout(codeRet if codeRet is not None else "")
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(),o['frame']))
        return o
    
    def visitArrayType(self,ast,o):
        list(map(lambda x: o['frame'].push(), ast.dimens))
        return reduce(lambda a,e: a + str(self.visit(e,o)[0]),ast.dimens,"") + self.emit.emitMULTIANEWARRAY(self.emit.getJVMType(ast),len(ast.dimens),o['frame']),ast
    
    def visitArrayLiteral(self,ast,o):
        def recurNest(arrVal,dimens,typeEle,frame):
            if not type(arrVal) is list:
                codeArrLit = self.visit(arrVal,o)[0]
                return codeArrLit if codeArrLit is not None else "",typeEle
            codeArrLit = ""
            if dimens and type(dimens[0]) is IntLiteral:
                codeArrLit += self.emit.emitPUSHCONST(str(dimens[0].value),IntType(),frame)
                frame.push()
            elif dimens and type(dimens[0]) is Id:
                sym = next((x for env in o['env'] for x in env if x.name == dimens[0].name),None)
                if type(sym.value) is Index:
                    codeArrLit += self.emit.emitREADVAR(dimens[0].name,IntType(),sym.value.value,frame)
                else:
                    codeArrLit += self.emit.emitGETSTATIC(f"{self.className}/{dimens[0].name}",IntType(),frame)
                frame.push()
            else:
                codeArrLit += self.emit.emitPUSHCONST(str(len(arrVal)),IntType(),frame)
                frame.push()
            if not type(arrVal[0]) is list:
                if type(typeEle) is Id:
                    typeJVM = f"[L{typeEle.name};"
                    codeArrLit += self.emit.emitMULTIANEWARRAY(typeJVM,1,frame)
                    frame.pop()
                    for i in range(len(arrVal)):
                        codeArrLit += self.emit.emitDUP(frame)
                        codeArrLit += self.emit.emitPUSHCONST(str(i),IntType(),frame)
                        frame.push()
                        sthCode = self.visit(arrVal[i],o)[0]
                        codeArrLit += sthCode if sthCode is not None else ""
                        codeArrLit += self.emit.emitASTORE(typeEle,frame)
                    return codeArrLit,ArrayType(dimens,typeEle)
                elif isinstance(typeEle,IntType) or isinstance(typeEle,BoolType) or isinstance(typeEle,FloatType):
                    codeArrLit += self.emit.emitNEWARRAY(typeEle,frame)
                    frame.pop()
                else:
                    codeArrLit += self.emit.emitANEWARRAY(typeEle,frame)
                    frame.pop()
                for i in range(len(arrVal)):
                    codeArrLit += self.emit.emitDUP(frame)
                    codeArrLit += self.emit.emitPUSHCONST(str(i),IntType(),frame)
                    frame.push()
                    sthCode = self.visit(arrVal[i],o)[0]
                    codeArrLit += sthCode if sthCode is not None else ""
                    codeArrLit += self.emit.emitASTORE(typeEle,frame)
                return codeArrLit,ArrayType(dimens,typeEle)
            typeSubArr = ArrayType(dimens[1:] if dimens else [],typeEle)
            codeArrLit += self.emit.emitANEWARRAY(typeSubArr,frame)
            frame.pop()
            for i in range(len(arrVal)):
                codeArrLit += self.emit.emitDUP(frame)
                codeArrLit += self.emit.emitPUSHCONST(str(i),IntType(),frame)
                frame.push()
                sthCode = recurNest(arrVal[i],dimens[1:] if dimens else [],typeEle,frame)[0]
                codeArrLit += sthCode if sthCode is not None else ""
                codeArrLit += self.emit.emitASTORE(typeSubArr,frame)
            return codeArrLit,ArrayType(dimens,typeEle)
        codeArrLit,typeRet = recurNest(ast.value,ast.dimens,ast.eleType,o['frame'])
        return codeArrLit if codeArrLit is not None else "",typeRet
    
    def visitArrayCell(self,ast,o):
        tmpO = o.copy()
        tmpO['isLeft'] = False
        codeArr,typeArr = self.visit(ast.arr,tmpO)
        tmptypeArr = typeArr
        for i in range(len(ast.idx)):
            codeArr += self.visit(ast.idx[i],tmpO)[0]
            o['frame'].push()
            if i != len(ast.idx) - 1:
                codeArr += self.emit.emitALOAD(tmptypeArr,o['frame'])
                tmptypeArr = ArrayType(tmptypeArr.dimens[1:],tmptypeArr.eleType)
                o['frame'].pop()
        retType = None
        if len(typeArr.dimens) == len(ast.idx):
            retType = typeArr.eleType 
            if not o.get('isLeft'):
                codeArr += self.emit.emitALOAD(retType,o['frame'])
                o['frame'].pop()
            else:
                self.arrcell = ast
                self.eleArr = retType
        else:
            retType = ArrayType(typeArr.dimens[len(ast.idx):],typeArr.eleType)
            if not o.get('isLeft'):
                codeArr += self.emit.emitALOAD(retType,o['frame'])
                o['frame'].pop()
            else:
                self.arrcell = ast
                self.eleArr = retType
        return codeArr,retType

    def visitStructLiteral(self,ast,o):
        frame = o['frame']
        codeStructLit = self.emit.emitNEW(ast.name,frame)
        frame.push()
        codeStructLit += self.emit.emitDUP(frame)
        frame.push()      
        fieldHad = {x: y for x,y in ast.elements}
        typeParams = []
        struct = self.namesDict.get(ast.name)
        for nameField,typeField in struct.elements:
            if nameField in fieldHad:
                codeStructLit += self.visit(fieldHad[nameField],o)[0]
                frame.push() 
            else:
                if isinstance(typeField,Id): 
                    codeStructLit += self.emit.emitPUSHNULL(frame)
                elif isinstance(typeField,IntType):
                    codeStructLit += self.emit.emitPUSHICONST(0,frame)
                elif isinstance(typeField,FloatType):
                    codeStructLit += self.emit.emitPUSHFCONST(0.0,frame)
                elif isinstance(typeField,BoolType):
                    codeStructLit += self.emit.emitPUSHICONST(0,frame)
                elif isinstance(typeField,StringType):
                    codeStructLit += self.emit.emitPUSHCONST("\"\"",StringType(),frame)
                frame.push()
            typeParams += [typeField]
        codeStructLit += self.emit.emitINVOKESPECIAL(frame,f"{ast.name}/<init>",MType(typeParams,VoidType()))
        list(map(lambda x: frame.pop(), typeParams))
        frame.pop()
        frame.push()
        return codeStructLit,Id(ast.name)
    
    def visitFieldAccess(self,ast,o):
        codeRec,typeRec = self.visit(ast.receiver,o)             
        nameAccess = f"{typeRec.name}/{ast.field}"
        typeAccess = next((x for x in self.namesDict.get(typeRec.name).elements if x[0] == ast.field),None)[1]
        return codeRec + self.emit.emitGETFIELD(nameAccess,typeAccess,o['frame']),typeAccess

    def identical(self,x,y):
        if type(x) != type(y):
            return False
        elif isinstance(x,Id):
            return x.name == y.name
        elif isinstance(x,ArrayType):
            return self.identical(x.eleType,y.eleType) and x.dimens == y.dimens
        return True 
        
    def visitMethodDecl(self,ast,o):
        self.methFunc = ast.fun
        frame = Frame(ast.fun.name,ast.fun.retType)
        mtype = MType([p.parType for p in ast.fun.params],ast.fun.retType)
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name,mtype,False,frame))
        frame.enterScope(True)
        typeThis = ast.recType
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),"this",ClassType(typeThis.name),frame.getStartLabel(),frame.getEndLabel(),frame))
        env['env'] = [[]] + env['env']
        env = reduce(lambda acc,e: self.visit(e,acc),ast.fun.params,env)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))
        if ast.fun.name == "<init>":
            self.emit.printout(self.emit.emitREADVAR("this",ClassType(typeThis.name),0,frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.visit(ast.fun.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
        if isinstance(ast.fun.retType,VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(),frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o  
    
    def visitMethCall(self,ast,o):
        frame = o['frame']
        codeCall,typCall = self.visit(ast.receiver,o)
        adType = self.namesDict.get(typCall.name)
        env = o.copy()
        env['stmt'] = False
        if isinstance(adType,InterfaceType):
            meth = next((x for x in adType.methods if x.name == ast.metName),None)
            frame.push()
            list(map(lambda x: frame.push(), ast.args))
            codeCall += reduce(lambda a,e: a + str(self.visit(e,env)[0]),ast.args,"")
            codeCall += self.emit.emitINVOKEINTERFACE(f"{typCall.name}/{ast.metName}",MType(meth.params,meth.retType),frame)
            list(map(lambda x: frame.pop(), meth.params))
            frame.pop()
            if not isinstance(meth.retType,VoidType):
                frame.push()
            if o.get('stmt'):
                self.emit.printout(codeCall)
                if not isinstance(meth.retType,VoidType):
                    self.emit.printout(self.emit.emitPOP(frame)) 
                    frame.pop()
                return o
            return codeCall,meth.retType
        elif isinstance(adType,StructType):
            meth = next((x for x in adType.methods if x.fun.name == ast.metName),None)
            frame.push()
            typeParams = [x.parType for x in meth.fun.params]
            list(map(lambda x: frame.push(), ast.args))
            codeCall += reduce(lambda a,e: a + str(self.visit(e,env)[0]),ast.args,"")
            codeCall += self.emit.emitINVOKEVIRTUAL(f"{typCall.name}/{ast.metName}",MType(typeParams,meth.fun.retType),frame)            
            list(map(lambda x: frame.pop(), typeParams))
            frame.pop()             
            if not isinstance(meth.fun.retType,VoidType):
                frame.push() 
            if o.get('stmt'):
                self.emit.printout(codeCall)
                if not isinstance(meth.fun.retType,VoidType):
                    self.emit.printout(self.emit.emitPOP(frame))  
                    frame.pop() 
                return o
            return codeCall,meth.fun.retType