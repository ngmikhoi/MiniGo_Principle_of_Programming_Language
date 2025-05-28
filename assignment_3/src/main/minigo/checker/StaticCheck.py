# 2252377 - Nguyen Minh Khoi
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
        
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
            [],
            [],
            [
            Symbol("putLn",MType([],VoidType()),0),
            Symbol("putIntLn",MType([IntType()],VoidType()),0),
            Symbol("putFloatLn",MType([FloatType()],VoidType()),0),
            Symbol("putBoolLn",MType([BoolType()],VoidType()),0),
            Symbol("putStringLn",MType([StringType()],VoidType()),0),
            
            Symbol("getInt",MType([],IntType()),0),
            Symbol("putInt",MType([IntType()],VoidType()),0),
            
            Symbol("getFloat",MType([],FloatType()),0),
            Symbol("putFloat",MType([FloatType()],VoidType()),0),
            
            Symbol("getBool",MType([],BoolType()),False),
            Symbol("putBool",MType([BoolType()],VoidType()),0),
            
            Symbol("getString",MType([],StringType()),""),
            Symbol("putString",MType([StringType()],VoidType()),0),
            ]
        ]
 
    
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast,c):
        names = [
                "putLn",
                "getInt","putInt","putIntLn",
                "getFloat","putFloat","putFloatLn",
                "getBool","putBool","putBoolLn",
                "getString","putString","putStringLn",
                ]
        for decl in ast.decl:
            if isinstance(decl,VarDecl):
                if decl.varName in names:
                    raise Redeclared(Variable(),decl.varName)
                else:
                    names += [decl.varName]
            elif isinstance(decl,ConstDecl):
                if decl.conName in names:
                    raise Redeclared(Constant(),decl.conName)
                else:
                    names += [decl.conName]
            elif isinstance(decl,FuncDecl):
                if decl.name in names:
                    raise Redeclared(Function(),decl.name)
                else:
                    names += [decl.name]
            elif isinstance(decl,StructType) or isinstance(decl,InterfaceType):
                if decl.name in names:
                    raise Redeclared(Type(),decl.name)
                else:
                    names += [decl.name]
        for decl in ast.decl:
            if isinstance(decl,StructType):
                c[-2] += [Symbol(decl.name,StructType(decl.name,decl.elements,[]),0)]
            elif isinstance(decl,InterfaceType):
                methods = reduce(lambda a,e: self.visit(e,a),decl.methods,[])
                c[-2] += [Symbol(decl.name,InterfaceType(decl.name,methods),0)]
            elif isinstance(decl,FuncDecl):
                params = reduce(lambda a,e: self.visit(e,a),decl.params,[])
                paramsType = list(map(lambda a: a.mtype,params))
                c[-1] += [Symbol(decl.name,MType(paramsType,decl.retType),self.retVal(decl.retType))]
        
        for decl in ast.decl:
            if isinstance(decl,MethodDecl):
                if not isinstance(decl.recType,Id):
                    raise TypeMismatch(ast)
                fun = decl.fun
                recTypeName = decl.recType.name
                recType = None
                idx = 0
                for e in c[-2]:
                    if e.name == recTypeName:
                        recType = e
                        break
                    idx += 1
                if recType is None:
                    raise Undeclared(Identifier(),recTypeName)
                if not (isinstance(recType.mtype,StructType) or isinstance(recType.mtype,InterfaceType)):
                    raise TypeMismatch(ast)
                res = self.lookup(fun.name,recType.mtype.methods,lambda x: x.name)
                if not res is None:
                    raise Redeclared(Method(),fun.name)
                
                if isinstance(recType.mtype,StructType):
                    for ele in recType.mtype.elements:
                        if ele[0] == fun.name:
                            raise Redeclared(Method(),fun.name)
                
                params = reduce(lambda a,e: self.visit(e,a),fun.params,[])
                paramsType = list(map(lambda a: a.mtype,params))                
                c[-2][idx].mtype.methods += [Symbol(fun.name,MType(paramsType,fun.retType),self.retVal(fun.retType))]
                
        reduce(lambda acc,ele: self.visit(ele,acc),ast.decl,c)
        return c    

    def visitVarDecl(self,ast,c):
        look = []
        if len(c) > 3:
            look = c[0]
            res = self.lookup(ast.varName,look,lambda x: x.name)
            if not res is None:
                raise Redeclared(Variable(),ast.varName)
        
        value = self.retVal(ast.varType)
        if ast.varInit:
            if ast.varType is None and isinstance(ast.varInit,NilLiteral):
                c[0] += [Symbol(ast.varName,ast.varType,0)]
                return c
            if isinstance(ast.varInit,NilLiteral) and not isinstance(ast.varType,Id):
                raise TypeMismatch(ast)             
            c[-1][0].value = "expr"
            rhs = self.visit(ast.varInit,c)
            c[-1][0].value = 0
            if rhs.mtype is None:
                rhs.mtype = ast.varType
                rhs.value = self.retVal(rhs.mtype)
            value = rhs.value
            if ast.varType is None:
                ast.varType = rhs.mtype
            if isinstance(ast.varType,ArrayType) and isinstance(rhs.mtype,ArrayType):
                if isinstance(ast.varType.eleType,Id) and isinstance(rhs.mtype.eleType,Id):
                    if ast.varType.eleType.name != rhs.mtype.eleType.name:
                        raise TypeMismatch(ast)
                if not ((type(ast.varType.eleType) is type(rhs.mtype.eleType)) or (isinstance(ast.varType.eleType,FloatType) and isinstance(rhs.mtype.eleType,IntType))):
                    raise TypeMismatch(ast)                
                if (len(ast.varType.dimens) != len(rhs.mtype.dimens)):
                    raise TypeMismatch(ast)
                for idx in range(len(ast.varType.dimens)):
                    c[-1][0].value = "expr"
                    a = self.visit(ast.varType.dimens[idx],c)
                    b = self.visit(rhs.mtype.dimens[idx],c)
                    if not isinstance(a.mtype,IntType):
                        raise TypeMismatch(ast.varType)
                    if not isinstance(b.mtype,IntType):
                        raise TypeMismatch(rhs.mtype)
                    if a.value != b.value:
                        raise TypeMismatch(ast)
                    c[-1][0].value = 0
            elif isinstance(ast.varType,Id) and isinstance(rhs.mtype,Id):
                if ast.varType.name != rhs.mtype.name:                    
                    typeA = None
                    typeB = None
                    for e in c[-2]:
                        if e.name == ast.varType.name:
                            typeA = e
                        elif e.name == rhs.mtype.name:
                            typeB = e
                    if isinstance(typeA.mtype,InterfaceType) and isinstance(typeB.mtype,StructType):
                        for methA in typeA.mtype.methods:
                            inB = False
                            for methB in typeB.mtype.methods:
                                if methA.name == methB.name:
                                    if len(methA.mtype.partype) == len(methB.mtype.partype):
                                        matchRet = False
                                        if type(methA.mtype.rettype) is type(methB.mtype.rettype):
                                            if isinstance(methA.mtype.rettype,Id) and isinstance(methB.mtype.rettype,Id):
                                                if methA.mtype.rettype.name == methB.mtype.rettype.name:                                                    
                                                    matchRet = True
                                            elif isinstance(methA.mtype.rettype,ArrayType) and isinstance(methB.mtype.rettype,ArrayType):
                                                A = methA.mtype.rettype
                                                B = methB.mtype.rettype
                                                if type(A.eleType) is type(B.eleType):
                                                    if (not isinstance(A.eleType,Id)) or (isinstance(A.eleType,Id) and A.eleType.name == B.eleType.name):
                                                        if len(A.dimens) == len(B.dimens):                                                        
                                                            c[-1][0].value = "expr"
                                                            count = 0
                                                            for idx in range(len(A.dimens)):
                                                                a = self.visit(A.dimens[idx],c)
                                                                b = self.visit(B.dimens[idx],c)
                                                                if (isinstance(a.mtype,IntType) and isinstance(b.mtype,IntType)):
                                                                    if a.value == b.value:
                                                                        count +=1
                                                            if count == len(A.dimens):
                                                                matchRet = True
                                                            c[-1][0].value = 0
                                            else:
                                                matchRet = True
                                        countParam = 0
                                        for i in range(len(methA.mtype.partype)):
                                            if type(methA.mtype.partype[i]) is type(methB.mtype.partype[i]):
                                                if isinstance(methA.mtype.partype[i],Id) and isinstance(methB.mtype.partype[i],Id):
                                                    if methA.mtype.partype[i].name == methB.mtype.partype[i].name:                                                    
                                                        countParam += 1
                                                elif isinstance(methA.mtype.partype[i],ArrayType) and isinstance(methB.mtype.partype[i],ArrayType):
                                                    A = methA.mtype.partype[i]
                                                    B = methB.mtype.partype[i]
                                                    if type(A.eleType) is type(B.eleType):
                                                        if (not isinstance(A.eleType,Id)) or (isinstance(A.eleType,Id) and A.eleType.name == B.eleType.name):
                                                            if len(A.dimens) == len(B.dimens):
                                                                c[-1][0].value = "expr"
                                                                count = 0
                                                                for idx in range(len(A.dimens)):
                                                                    a = self.visit(A.dimens[idx],c)
                                                                    b = self.visit(B.dimens[idx],c)
                                                                    if (isinstance(a.mtype,IntType) and isinstance(b.mtype,IntType)):
                                                                        if a.value == b.value:
                                                                            count +=1
                                                                if count == len(A.dimens):
                                                                    countParam += 1
                                                                c[-1][0].value = 0
                                                else:
                                                    countParam += 1
                                        if matchRet and countParam == len(methA.mtype.partype):
                                            inB = True                            
                            if inB == False:
                                raise TypeMismatch(ast) 
                    else:
                        raise TypeMismatch(ast)
            elif not ((type(ast.varType) is type(rhs.mtype)) or (isinstance(ast.varType,FloatType) and isinstance(rhs.mtype,IntType))):
                raise TypeMismatch(ast)
            
        symType = ast.varType
        if isinstance(symType,ArrayType):
            dimVals = []
            c[-1][0].value = "expr"
            for dim in symType.dimens:
                val = self.visit(dim,c).value
                dimVals += [IntLiteral(val)]
            symType = ArrayType(dimVals,symType.eleType)
            c[-1][0].value = 0  
        c[0] += [Symbol(ast.varName,symType,value)]
        return c
    
    def visitConstDecl(self,ast,c):
        look = []
        if len(c) > 3:
            look = c[0]
            res = self.lookup(ast.conName,look,lambda x: x.name)
            if not res is None:
                raise Redeclared(Constant(),ast.conName)        
        value = self.retVal(ast.conType)
        if ast.iniExpr:
            if ast.conType is None and isinstance(ast.iniExpr,NilLiteral):
                c[0] += [Symbol(ast.conName,ast.conType,0)]
                return c
            if isinstance(ast.iniExpr,NilLiteral) and not isinstance(ast.conType,Id):
                raise TypeMismatch(ast)
            c[-1][0].value = "expr"
            rhs = self.visit(ast.iniExpr,c)
            c[-1][0].value = 0
            if rhs.mtype is None:
                rhs.mtype = ast.conType
                rhs.value = self.retVal(rhs.mtype)
            value = rhs.value
            if ast.conType is None:
                ast.conType = rhs.mtype
            if isinstance(ast.conType,ArrayType) and isinstance(rhs.mtype,ArrayType):
                if isinstance(ast.conType.eleType,Id) and isinstance(rhs.mtype.eleType,Id):
                    if ast.conType.eleType.name != rhs.mtype.eleType.name:
                        raise TypeMismatch(ast)
                if not ((type(ast.conType.eleType) is type(rhs.mtype.eleType)) or (isinstance(ast.conType.eleType,FloatType) and isinstance(rhs.mtype.eleType,IntType))):
                    raise TypeMismatch(ast)
                if (len(ast.conType.dimens) != len(rhs.mtype.dimens)):
                    raise TypeMismatch(ast)
                for idx in range(len(ast.conType.dimens)):
                    c[-1][0].value = "expr"
                    a = self.visit(ast.conType.dimens[idx],c)
                    b = self.visit(rhs.mtype.dimens[idx],c)
                    if not isinstance(a.mtype,IntType):
                        raise TypeMismatch(ast.conType)
                    if not isinstance(b.mtype,IntType):
                        raise TypeMismatch(rhs.mtype)
                    if a.value != b.value:
                        raise TypeMismatch(ast)
                    c[-1][0].value = 0
            elif isinstance(ast.conType,Id) and isinstance(rhs.mtype,Id):
                if ast.conType.name != rhs.mtype.name:                    
                    typeA = None
                    typeB = None
                    for e in c[-2]:
                        if e.name == ast.conType.name:
                            typeA = e
                        elif e.name == rhs.mtype.name:
                            typeB = e
                    if isinstance(typeA.mtype,InterfaceType) and isinstance(typeB.mtype,StructType):
                        for methA in typeA.mtype.methods:
                            inB = False
                            for methB in typeB.mtype.methods:
                                if methA.name == methB.name:
                                    if len(methA.mtype.partype) == len(methB.mtype.partype):
                                        matchRet = False
                                        if type(methA.mtype.rettype) is type(methB.mtype.rettype):
                                            if isinstance(methA.mtype.rettype,Id) and isinstance(methB.mtype.rettype,Id):
                                                if methA.mtype.rettype.name == methB.mtype.rettype.name:                                                    
                                                    matchRet = True
                                            elif isinstance(methA.mtype.rettype,ArrayType) and isinstance(methB.mtype.rettype,ArrayType):
                                                A = methA.mtype.rettype
                                                B = methB.mtype.rettype
                                                if type(A.eleType) is type(B.eleType):
                                                    if (not isinstance(A.eleType,Id)) or (isinstance(A.eleType,Id) and A.eleType.name == B.eleType.name):
                                                        if len(A.dimens) == len(B.dimens):                                                        
                                                            c[-1][0].value = "expr"
                                                            count = 0
                                                            for idx in range(len(A.dimens)):
                                                                a = self.visit(A.dimens[idx],c)
                                                                b = self.visit(B.dimens[idx],c)
                                                                if (isinstance(a.mtype,IntType) and isinstance(b.mtype,IntType)):
                                                                    if a.value == b.value:
                                                                        count +=1
                                                            if count == len(A.dimens):
                                                                matchRet = True
                                                            c[-1][0].value = 0
                                            else:
                                                matchRet = True
                                        countParam = 0
                                        for i in range(len(methA.mtype.partype)):
                                            if type(methA.mtype.partype[i]) is type(methB.mtype.partype[i]):
                                                if isinstance(methA.mtype.partype[i],Id) and isinstance(methB.mtype.partype[i],Id):
                                                    if methA.mtype.partype[i].name == methB.mtype.partype[i].name:                                                    
                                                        countParam += 1
                                                elif isinstance(methA.mtype.partype[i],ArrayType) and isinstance(methB.mtype.partype[i],ArrayType):
                                                    A = methA.mtype.partype[i]
                                                    B = methB.mtype.partype[i]
                                                    if type(A.eleType) is type(B.eleType):
                                                        if (not isinstance(A.eleType,Id)) or (isinstance(A.eleType,Id) and A.eleType.name == B.eleType.name):
                                                            if len(A.dimens) == len(B.dimens):
                                                                c[-1][0].value = "expr"
                                                                count = 0
                                                                for idx in range(len(A.dimens)):
                                                                    a = self.visit(A.dimens[idx],c)
                                                                    b = self.visit(B.dimens[idx],c)
                                                                    if (isinstance(a.mtype,IntType) and isinstance(b.mtype,IntType)):
                                                                        if a.value == b.value:
                                                                            count +=1
                                                                if count == len(A.dimens):
                                                                    countParam += 1
                                                                c[-1][0].value = 0
                                                else:
                                                    countParam += 1
                                        if matchRet and countParam == len(methA.mtype.partype):
                                            inB = True                            
                            if inB == False:
                                raise TypeMismatch(ast) 
                    else:
                        raise TypeMismatch(ast)
            elif not ((type(ast.conType) is type(rhs.mtype)) or (isinstance(ast.conType,FloatType) and isinstance(rhs.mtype,IntType))):
                raise TypeMismatch(ast)
        symType = ast.conType
        if isinstance(symType,ArrayType):
            dimVals = []
            c[-1][0].value = "expr"
            for dim in symType.dimens:
                val = self.visit(dim,c).value
                dimVals += [IntLiteral(val)]
            symType = ArrayType(dimVals,symType.eleType)
            c[-1][0].value = 0      
        c[0] += [Symbol(ast.conName,symType,value)]
        return c
    
    def visitParamDecl(self,ast,c):
        res = self.lookup(ast.parName,c,lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(),ast.parName) 
        return c + [Symbol(ast.parName,ast.parType,self.retVal(ast.parType))]
            
    def visitBlock(self,ast,c):
        reduce(lambda a,e: self.visit(e,a),ast.member,c)
        return c
        
    def visitReturn(self,ast,c):
        if isinstance(ast.expr,NilLiteral):
            if isinstance(c[-1][1].value,Id):
                return c
            else:
                raise TypeMismatch(ast)
        c[-1][0].value = "expr"
        ret = Symbol(None,VoidType(),0)
        if not ast.expr is None:
            ret = self.visit(ast.expr,c)
        parType = c[-1][1].value
        argType = ret.mtype
        if type(parType) != type(argType):
            raise TypeMismatch(ast)
        elif isinstance(parType,Id) and isinstance(argType,Id):
            if parType.name != argType.name:
                raise TypeMismatch(ast)
        elif isinstance(parType,ArrayType) and isinstance(argType,ArrayType):
            if type(parType.eleType) != type(argType.eleType):
                raise TypeMismatch(ast)
            if isinstance(parType.eleType,Id) and isinstance(argType.eleType,Id):
                if parType.eleType.name != argType.eleType.name:
                    raise TypeMismatch(ast)
            if len(parType.dimens) != len(argType.dimens):
                raise TypeMismatch(ast)
            for idx in range(len(parType.dimens)):
                a = self.visit(parType.dimens[idx],c)
                b = self.visit(argType.dimens[idx],c)
                if not (isinstance(a.mtype,IntType) and isinstance(b.mtype,IntType)):
                    raise TypeMismatch(ast)
                if a.value != b.value:
                    raise TypeMismatch(ast)
        c[-1][0].value = 0     
        return c
    
    def visitFuncDecl(self,ast,c):    
        params = reduce(lambda a,e: self.visit(e,a),ast.params,[])
        paraPos = 0
        for para in params:
            symType = para.mtype
            if isinstance(symType,ArrayType):
                dimVals = []
                c[-1][0].value = "expr"
                for dim in symType.dimens:
                    val = self.visit(dim,c).value
                    dimVals += [IntLiteral(val)]
                symType = ArrayType(dimVals,symType.eleType)
                c[-1][0].value = 0  
                params[paraPos].mtype = symType
            paraPos += 1
        
        funcpos = 0
        for e in c[-1]:
            if e.name == ast.name:
                break
            funcpos += 1
           
        paramsType = list(map(lambda a: a.mtype,params))
        c[-1][funcpos] = Symbol(ast.name,MType(paramsType,ast.retType),self.retVal(ast.retType))
                
        c[-1][1].value = ast.retType
        self.visit(ast.body,[[],params,c[-3],c[-2],c[-1]])
        c[-1][1].value = 0
        return c

    def visitMethodDecl(self,ast,c):
        params = reduce(lambda a,e: self.visit(e,a),ast.fun.params,[])
        
        paraPos = 0
        for para in params:
            symType = para.mtype
            if isinstance(symType,ArrayType):
                dimVals = []
                c[-1][0].value = "expr"
                for dim in symType.dimens:
                    val = self.visit(dim,c).value
                    dimVals += [IntLiteral(val)]
                symType = ArrayType(dimVals,symType.eleType)
                c[-1][0].value = 0  
                params[paraPos].mtype = symType
            paraPos += 1
        
        recTypeName = ast.recType.name
        recType = None
        idx = 0
        for e in c[-2]:
            if e.name == recTypeName:
                recType = e
                break
            idx += 1

        funcpos = 0
        for e in recType.mtype.methods:
            if e.name == ast.fun.name:
                break
            funcpos += 1
           
        paramsType = list(map(lambda a: a.mtype,params))
        c[-2][idx].mtype.methods[funcpos] = Symbol(ast.fun.name,MType(paramsType,ast.fun.retType),self.retVal(ast.fun.retType))
        
        c[-1][1].value = ast.fun.retType
        self.visit(ast.fun.body,[[],params,[Symbol(ast.receiver,ast.recType,self.retVal(ast.recType))],c[-3],c[-2],c[-1]])
        c[-1][1].value = 0
        return c

    def visitPrototype(self,ast,c):
        res = self.lookup(ast.name,c,lambda x: x.name)
        if not res is None:
            raise Redeclared(Prototype(),ast.name)
        return c + [Symbol(ast.name,MType(ast.params,ast.retType),self.retVal(ast.retType))]
    
    def visitIntType(self,ast,c):
        return Symbol(None,IntType(),0)
    
    def visitFloatType(self,ast,c):
        return Symbol(None,FloatType(),0)
    
    def visitBoolType(self,ast,c):
        return Symbol(None,BoolType(),False)
    
    def visitStringType(self,ast,c):
        return Symbol(None,StringType(),"")
    
    def visitVoidType(self,ast,c):
        return Symbol(None,VoidType(),0)        
    
    def visitArrayType(self,ast,c):
        start = c[-1][0].value
        c[-1][0].value = "expr"
        for dim in ast.dimens:
            dim = self.visit(dim,c)
            if not isinstance(dim.mtype,IntType):
                raise TypeMismatch(ast)
        c[-1][0].value = start
        return Symbol(None,ast,0)
    
    def visitStructType(self,ast,c):
        eleNames = []
        for e in ast.elements:
            if e[0] in eleNames:
                raise Redeclared(Field(),e[0])
            else:
                eleNames += [e[0]]
        return c
        
    def visitInterfaceType(self,ast,c):
        return c
        
    def visitAssign(self,ast,c):
        c[-1][0].value = "expr"
        lhs = None
        if isinstance(ast.lhs,Id):
            look = []
            for idx in range(len(c)-2):
                look += c[idx]
            for e in look:
                if ast.lhs.name == e.name:
                    lhs = e
                    break
            if lhs is None:
                rhs = self.visit(ast.rhs,c)
                symType = rhs.mtype
                if isinstance(symType,ArrayType):
                    dimVals = []
                    c[-1][0].value = "expr"
                    for dim in symType.dimens:
                        val = self.visit(dim,c).value
                        dimVals += [IntLiteral(val)]
                    symType = ArrayType(dimVals,symType.eleType)
                    c[-1][0].value = 0
                lhs = Symbol(ast.lhs.name,symType,rhs.value)
                c[0] += [lhs]
        else:
            lhs = self.visit(ast.lhs,c)
        rhs = self.visit(ast.rhs,c)
        c[-1][0].value = 0
        
        if lhs.mtype is None and isinstance(ast.rhs,NilLiteral):
            return c
        if isinstance(ast.rhs,NilLiteral) and isinstance(lhs.mtype,Id):
            return c
        if isinstance(lhs.mtype,VoidType):
            raise TypeMismatch(ast)
        if lhs.mtype is None:
            lhs.mtype = rhs.mtype
            
        if isinstance(lhs.mtype,ArrayType) and isinstance(rhs.mtype,ArrayType):
            if isinstance(lhs.mtype.eleType,Id) and isinstance(rhs.mtype.eleType,Id):
                if lhs.mtype.eleType.name != rhs.mtype.eleType.name:
                    raise TypeMismatch(ast)
            if not ((type(lhs.mtype.eleType) is type(rhs.mtype.eleType)) or (isinstance(lhs.mtype.eleType,FloatType) and isinstance(rhs.mtype.eleType,IntType))):
                raise TypeMismatch(ast)
            if (len(lhs.mtype.dimens) != len(rhs.mtype.dimens)):
                raise TypeMismatch(ast)
            for idx in range(len(lhs.mtype.dimens)):
                c[-1][0].value = "expr"
                a = self.visit(lhs.mtype.dimens[idx],c)
                b = self.visit(rhs.mtype.dimens[idx],c)
                if not isinstance(a.mtype,IntType):
                    raise TypeMismatch(lhs.mtype)
                if not isinstance(b.mtype,IntType):
                    raise TypeMismatch(rhs.mtype)
                if a.value != b.value:
                    raise TypeMismatch(ast)
                c[-1][0].value = 0
        elif isinstance(lhs.mtype,Id) and isinstance(rhs.mtype,Id):
            if lhs.mtype.name != rhs.mtype.name:                    
                typeA = None
                typeB = None
                for e in c[-2]:
                    if e.name == lhs.mtype.name:
                        typeA = e
                    elif e.name == rhs.mtype.name:
                        typeB = e
                if isinstance(typeA.mtype,InterfaceType) and isinstance(typeB.mtype,StructType):
                    for methA in typeA.mtype.methods:
                        inB = False
                        for methB in typeB.mtype.methods:
                            if methA.name == methB.name:
                                if len(methA.mtype.partype) == len(methB.mtype.partype):
                                    matchRet = False
                                    if type(methA.mtype.rettype) is type(methB.mtype.rettype):
                                        if isinstance(methA.mtype.rettype,Id) and isinstance(methB.mtype.rettype,Id):
                                            if methA.mtype.rettype.name == methB.mtype.rettype.name:                                                    
                                                matchRet = True
                                        elif isinstance(methA.mtype.rettype,ArrayType) and isinstance(methB.mtype.rettype,ArrayType):
                                            A = methA.mtype.rettype
                                            B = methB.mtype.rettype
                                            if type(A.eleType) is type(B.eleType):
                                                if (not isinstance(A.eleType,Id)) or (isinstance(A.eleType,Id) and A.eleType.name == B.eleType.name):
                                                    if len(A.dimens) == len(B.dimens):                                                        
                                                        c[-1][0].value = "expr"
                                                        count = 0
                                                        for idx in range(len(A.dimens)):
                                                            a = self.visit(A.dimens[idx],c)
                                                            b = self.visit(B.dimens[idx],c)
                                                            if (isinstance(a.mtype,IntType) and isinstance(b.mtype,IntType)):
                                                                if a.value == b.value:
                                                                    count +=1
                                                        if count == len(A.dimens):
                                                            matchRet = True
                                                        c[-1][0].value = 0
                                        else:
                                            matchRet = True
                                    countParam = 0
                                    for i in range(len(methA.mtype.partype)):
                                        if type(methA.mtype.partype[i]) is type(methB.mtype.partype[i]):
                                            if isinstance(methA.mtype.partype[i],Id) and isinstance(methB.mtype.partype[i],Id):
                                                if methA.mtype.partype[i].name == methB.mtype.partype[i].name:                                                    
                                                    countParam += 1
                                            elif isinstance(methA.mtype.partype[i],ArrayType) and isinstance(methB.mtype.partype[i],ArrayType):
                                                A = methA.mtype.partype[i]
                                                B = methB.mtype.partype[i]
                                                if type(A.eleType) is type(B.eleType):
                                                    if (not isinstance(A.eleType,Id)) or (isinstance(A.eleType,Id) and A.eleType.name == B.eleType.name):
                                                        if len(A.dimens) == len(B.dimens):
                                                            c[-1][0].value = "expr"
                                                            count = 0
                                                            for idx in range(len(A.dimens)):
                                                                a = self.visit(A.dimens[idx],c)
                                                                b = self.visit(B.dimens[idx],c)
                                                                if (isinstance(a.mtype,IntType) and isinstance(b.mtype,IntType)):
                                                                    if a.value == b.value:
                                                                        count +=1
                                                            if count == len(A.dimens):
                                                                countParam += 1
                                                            c[-1][0].value = 0
                                            else:
                                                countParam += 1
                                    if matchRet and countParam == len(methA.mtype.partype):
                                        inB = True                            
                        if inB == False:
                            raise TypeMismatch(ast) 
                else:
                    raise TypeMismatch(ast)
        elif not ((type(lhs.mtype) is type(rhs.mtype)) or (isinstance(lhs.mtype,FloatType) and isinstance(rhs.mtype,IntType))):
            raise TypeMismatch(ast)        
        return c
   
    def visitIf(self,ast,c):
        c[-1][0].value = "expr"
        cond = self.visit(ast.expr,c)
        c[-1][0].value = 0
        if not isinstance(cond.mtype,BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.thenStmt,[[]] + c)
        if not ast.elseStmt is None:
            self.visit(ast.elseStmt,[[]] + c)
        return c     
    
    def visitForBasic(self,ast,c):
        c[-1][0].value = "expr"
        cond = self.visit(ast.cond,c)
        c[-1][0].value = 0
        if not isinstance(cond.mtype,BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.loop,[[]] + c)
        return c
 
    def visitForStep(self,ast,c):
        c[-1][0].value = "expr"
        sym = None
        lst = []
        if isinstance(ast.init,VarDecl):
            rhs = self.visit(ast.init.varInit,c)
            sym = Symbol(ast.init.varName,rhs.mtype,rhs.value)
            lst += [sym]
        elif isinstance(ast.init,Assign):
            rhs = self.visit(ast.init.rhs,c)
            look = []
            for i in range(len(c)-2):
                look += c[i]
            for e in look:
                if ast.init.lhs.name == e.name:
                    sym = e
                    break
            if sym is None:
                sym = Symbol(ast.init.lhs.name,rhs.mtype,rhs.value)
                lst += [sym]
                          
        cond = self.visit(ast.cond,[lst] + c)
        if not isinstance(cond.mtype,BoolType):
            raise TypeMismatch(ast)
        
        tmp = self.visit(ast.upda,[lst] + c)
        c[-1][0].value = 0
        self.visit(ast.loop,tmp)
        return c
    def visitForEach(self,ast,c):
        c[-1][0].value = "expr"
        arr = self.visit(ast.arr,c)
        c[-1][0].value = 0
        if not isinstance(arr.mtype,ArrayType):
            raise TypeMismatch(ast)
        
        look = []
        for i in range(len(c)-2):
            look += c[i]
        
        lst = []
        
        idx = None
        if ast.idx.name != "_":
            for e in look:
                if ast.idx.name == e.name:
                    idx = e
                    break
            if idx is None:
                idx = Symbol(ast.idx.name,IntType(),0)
                lst += [idx]
                raise Undeclared(Identifier(),ast.idx.name)
            elif not isinstance(idx.mtype,IntType):
                raise TypeMismatch(ast)
        
        value = None
        for e in look:
            if ast.value.name == e.name:
                value = e
                break
        if value is None:
            value = Symbol(ast.value.name,arr.mtype.eleType,self.retVal(arr.mtype.eleType))
            lst += [value]
            raise Undeclared(Identifier(),ast.value.name)
        elif type(arr.mtype.eleType) != type(value.mtype):
            raise TypeMismatch(ast)
        elif isinstance(arr.mtype.eleType,Id) and isinstance(value.mtype,Id):
            if arr.mtype.eleType.name != value.mtype.name:
                raise TypeMismatch(ast)
        
        
        self.visit(ast.loop,[lst] + c)
        return c

    def visitContinue(self,ast,c):
        return c
    
    def visitBreak(self,ast,c):
        return c

    def visitBinaryOp(self,ast,c):
        e1 = self.visit(ast.left,c)
        e2 = self.visit(ast.right,c)
        if ast.op in ['+']:
            if isinstance(e1.mtype,StringType) and isinstance(e2.mtype,StringType):
                return Symbol(None,StringType(),e1.value + e2.value)
            elif isinstance(e1.mtype,IntType) and isinstance(e2.mtype,IntType):
                return Symbol(None,IntType(),e1.value + e2.value)
            elif (isinstance(e1.mtype,FloatType) or isinstance(e1.mtype,IntType)) and (isinstance(e2.mtype,FloatType) or isinstance(e2.mtype,IntType)):
                return Symbol(None,FloatType(),e1.value + e2.value)
            else:
                raise TypeMismatch(ast)
        elif ast.op in ['-','*','/']:
            if isinstance(e1.mtype,IntType) and isinstance(e2.mtype,IntType):
                if ast.op == '-':
                    return Symbol(None,IntType(),e1.value - e2.value)
                elif ast.op == '*':
                    return Symbol(None,IntType(),e1.value * e2.value)
                elif ast.op == '/':
                    if e2.value == 0:
                        raise TypeMismatch(ast)
                    return Symbol(None,IntType(),int(e1.value / e2.value))
            elif (isinstance(e1.mtype,FloatType) or isinstance(e1.mtype,IntType)) and (isinstance(e2.mtype,FloatType) or isinstance(e2.mtype,IntType)):
                if ast.op == '-':
                    return Symbol(None,FloatType(),e1.value - e2.value)
                elif ast.op == '*':
                    return Symbol(None,FloatType(),e1.value * e2.value)
                elif ast.op == '/':
                    if e2.value == 0:
                        raise TypeMismatch(ast)
                    return Symbol(None,FloatType(),e1.value / e2.value)
            else:
                raise TypeMismatch(ast)
        elif ast.op in ['%']:
            if isinstance(e1.mtype,IntType) and isinstance(e2.mtype,IntType):
                return Symbol(None,IntType(),e1.value % e2.value)
            else:
                raise TypeMismatch(ast)
        elif ast.op in ['&&','||']:
            if isinstance(e1.mtype,BoolType) and isinstance(e2.mtype,BoolType):
                if ast.op == '&&':
                    return Symbol(None,BoolType(),e1.value and e2.value)
                elif ast.op == '||':
                    return Symbol(None,BoolType(),e1.value or e2.value)
            else:
                raise TypeMismatch(ast)
        elif ast.op in ['==','!=','<','>','<=','>=']:
            if (isinstance(e1.mtype,StringType) and isinstance(e2.mtype,StringType)) or (isinstance(e1.mtype,IntType) and isinstance(e2.mtype,IntType)) or (isinstance(e1.mtype,FloatType) and isinstance(e2.mtype,FloatType)):
                if ast.op == '==':
                    return Symbol(None,BoolType(),e1.value == e2.value)
                elif ast.op == '!=':
                    return Symbol(None,BoolType(),e1.value != e2.value)
                elif ast.op == '<':
                    return Symbol(None,BoolType(),e1.value < e2.value)
                elif ast.op == '>':
                    return Symbol(None,BoolType(),e1.value > e2.value)
                elif ast.op == '<=':
                    return Symbol(None,BoolType(),e1.value <= e2.value)
                elif ast.op == '>=':
                    return Symbol(None,BoolType(),e1.value >= e2.value)
            else:
                raise TypeMismatch(ast)
            
        
    def visitUnaryOp(self,ast,c):
        e = self.visit(ast.body,c)
        if ast.op in ['-']:
            if not isinstance(e.mtype,FloatType) and not isinstance(e.mtype,IntType):
                raise TypeMismatch(ast)
            return Symbol(None,IntType(),-e.value) if isinstance(e.mtype,IntType) else Symbol(None,FloatType(),-e.value)
        elif ast.op in ['!']:
            if not isinstance(e.mtype,BoolType):
                raise TypeMismatch(ast)
            return Symbol(None,BoolType(),not e.value)
        
    def retVal(self,typ):
        if isinstance(typ,StringType):
            return ""
        elif isinstance(typ,BoolType):
            return False
        return 0
        
    def visitFuncCall(self,ast,c):
        start = c[-1][0].value
        c[-1][0].value = "expr"
        func = None
        look = []
        for i in range(len(c)):
            look += c[i]
        for e in look:
            if ast.funName == e.name:
                func = e
                break
        if func is None:
            raise Undeclared(Function(),ast.funName)
        if not isinstance(func.mtype,MType):
            raise Undeclared(Function(),ast.funName)
        
        if len(ast.args) != len(func.mtype.partype):
            raise TypeMismatch(ast)
        for i in range(len(ast.args)):
            parType = func.mtype.partype[i]
            argType = self.visit(ast.args[i],c).mtype
            
            if isinstance(parType,Id) and argType is None:
                pass
            elif type(parType) != type(argType):
                raise TypeMismatch(ast)
            elif isinstance(parType,Id) and isinstance(argType,Id):
                if parType.name != argType.name:
                    raise TypeMismatch(ast)
            elif isinstance(parType,ArrayType) and isinstance(argType,ArrayType):
                if type(parType.eleType) != type(argType.eleType):
                    raise TypeMismatch(ast)
                if isinstance(parType.eleType,Id) and isinstance(argType.eleType,Id):
                    if parType.eleType.name != argType.eleType.name:
                        raise TypeMismatch(ast)
                if len(parType.dimens) != len(argType.dimens):
                    raise TypeMismatch(ast)
                for idx in range(len(parType.dimens)):
                    a = self.visit(parType.dimens[idx],c)
                    b = self.visit(argType.dimens[idx],c)
                    if not (isinstance(a.mtype,IntType) and isinstance(b.mtype,IntType)):
                        raise TypeMismatch(ast)
                    if a.value != b.value:
                        raise TypeMismatch(ast)        
        c[-1][0].value = start   
        if c[-1][0].value == "expr" and not isinstance(func.mtype.rettype,VoidType):
            return Symbol(func.name,func.mtype.rettype,self.retVal(func.mtype.rettype))
        elif c[-1][0].value != "expr" and isinstance(func.mtype.rettype,VoidType): 
            return c
        elif c[-1][0].value != "expr" and not isinstance(func.mtype.rettype,VoidType):
            raise TypeMismatch(ast)
        elif c[-1][0].value == "expr" and isinstance(func.mtype.rettype,VoidType):
            raise TypeMismatch(ast)

    def visitMethCall(self,ast,c):
        start = c[-1][0].value
        c[-1][0].value = "expr"
        receiver = self.visit(ast.receiver,c)
        if not isinstance(receiver.mtype,Id):
            raise TypeMismatch(ast)
        recTypeName = receiver.mtype.name
        recType = None
        for e in c[-2]:
            if e.name == recTypeName:
                recType = e
                break
        if recType is None:
            raise Undeclared(Identifier(),recTypeName)
        method = None
        for e in recType.mtype.methods:
            if ast.metName == e.name:
                method = e
                break
        if method is None:
            raise Undeclared(Method(),ast.metName)
        if not isinstance(method.mtype,MType):
            raise Undeclared(Function(),ast.metName)
        
        if len(ast.args) != len(method.mtype.partype):
            raise TypeMismatch(ast)
        for i in range(len(ast.args)):
            parType = method.mtype.partype[i]
            argType = self.visit(ast.args[i],c).mtype
            
            if isinstance(parType,Id) and argType is None:
                pass
            elif type(parType) != type(argType):
                raise TypeMismatch(ast)
            elif isinstance(parType,Id) and isinstance(argType,Id):
                if parType.name != argType.name:
                    raise TypeMismatch(ast)
            elif isinstance(parType,ArrayType) and isinstance(argType,ArrayType):
                if type(parType.eleType) != type(argType.eleType):
                    raise TypeMismatch(ast)
                if isinstance(parType.eleType,Id) and isinstance(argType.eleType,Id):
                    if parType.eleType.name != argType.eleType.name:
                        raise TypeMismatch(ast)
                if len(parType.dimens) != len(argType.dimens):
                    raise TypeMismatch(ast)
                for idx in range(len(parType.dimens)):
                    a = self.visit(parType.dimens[idx],c)
                    b = self.visit(argType.dimens[idx],c)
                    if not (isinstance(a.mtype,IntType) and isinstance(b.mtype,IntType)):
                        raise TypeMismatch(ast)
                    if a.value != b.value:
                        raise TypeMismatch(ast)    
        c[-1][0].value = start
        if c[-1][0].value == "expr" and not isinstance(method.mtype.rettype,VoidType):
            return Symbol(method.name,method.mtype.rettype,self.retVal(method.mtype.rettype))
        elif c[-1][0].value != "expr" and isinstance(method.mtype.rettype,VoidType): 
            return c
        elif c[-1][0].value != "expr" and not isinstance(method.mtype.rettype,VoidType):
            raise TypeMismatch(ast)
        elif c[-1][0].value == "expr" and isinstance(method.mtype.rettype,VoidType):
            raise TypeMismatch(ast)
    
    def visitId(self,ast,c):
        look = []
        for idx in range(len(c)-2):
            look += c[idx]
        res = None
        for e in look:
            if ast.name == e.name:
                res = e
                break
        if res is None:
            raise Undeclared(Identifier(),ast.name)
        return Symbol(res.name,res.mtype,res.value)
    
    def visitArrayCell(self,ast,c):
        c[-1][0].value = "expr"
        arr = self.visit(ast.arr,c)
        if not isinstance(arr.mtype,ArrayType):
            raise TypeMismatch(ast)
        numDim = len(arr.mtype.dimens)
        count = 0
        for j in range(len(ast.idx)):
            if count >= numDim:
                raise TypeMismatch(ast)
            i = self.visit(ast.idx[j],c)
            if not isinstance(i.mtype,IntType):
                raise TypeMismatch(ast)
            # if i.value >= self.visit(arr.mtype.dimens[j],c).value or i.value < 0:
            #     raise TypeMismatch(ast)
            count += 1
        c[-1][0].value = 0    
        if count == numDim:
            return Symbol(None,arr.mtype.eleType,self.retVal(arr.mtype.eleType))
        else:
            dimens = arr.mtype.dimens[count:]
            return Symbol(None,ArrayType(dimens,arr.mtype.eleType),0)
    
    def visitFieldAccess(self,ast,c):
        receiver = self.visit(ast.receiver,c)
        if not isinstance(receiver.mtype,Id):
            raise TypeMismatch(ast)
        structName = receiver.mtype.name
        struct = None
        for e in c[-2]:
            if e.name == structName:
                struct = e
                break
        if struct is None:
            raise Undeclared(Identifier(),structName)
        if not isinstance(struct.mtype,StructType):
            raise TypeMismatch(ast)
        field = None
        for e in struct.mtype.elements:
            if e[0] == ast.field:
                field = e
                break
        if field is None:
            raise Undeclared(Field(),ast.field)
        return Symbol(None,field[1],self.retVal(field[1]))
                
    def visitIntLiteral(self,ast,c):
        return Symbol(None,IntType(),ast.value)
    
    def visitFloatLiteral(self,ast,c):
        return Symbol(None,FloatType(),ast.value)
    
    def visitBooleanLiteral(self,ast,c):
        return Symbol(None,BoolType(),ast.value)
    
    def visitStringLiteral(self,ast,c):
        return Symbol(None,StringType(),ast.value)
    
    def flatten(self,lst):
        return reduce(lambda a,e: a + (self.flatten(e) if isinstance(e,list) else [e]),lst,[])
    
    def visitArrayLiteral(self,ast,c):
        for dimen in ast.dimens:
            dim = self.visit(dimen,c)
            if not isinstance(dim.mtype,IntType):
                raise TypeMismatch(ast)     
        
        value = self.flatten(ast.value)
        for e in value:
            val = self.visit(e,c)
            if isinstance(ast.eleType,Id) and isinstance(val.mtype,Id):
                if ast.eleType.name != val.mtype.name:
                    raise TypeMismatch(ast)
            elif not ((type(ast.eleType) is type(val.mtype)) or (isinstance(ast.eleType,FloatType) and isinstance(val.mtype,IntType))):
                raise TypeMismatch(ast)
        
        symType = ArrayType(ast.dimens,ast.eleType)
        if isinstance(symType,ArrayType):
            dimVals = []
            c[-1][0].value = "expr"
            for dim in symType.dimens:
                val = self.visit(dim,c).value
                dimVals += [IntLiteral(val)]
            symType = ArrayType(dimVals,symType.eleType)
            c[-1][0].value = 0 
        
        return Symbol(None,symType,0)

    def visitStructLiteral(self,ast,c):
        structName = ast.name
        struct = None
        for e in c[-2]:
            if e.name == structName:
                struct = e
                break
        if struct is None:
            raise Undeclared(Identifier(),structName)
        if not isinstance(struct.mtype,StructType):
            raise TypeMismatch(ast)
        for e in ast.elements:
            field = None
            for i in struct.mtype.elements:
                if i[0] == e[0]:
                    field = i
                    lit = self.visit(e[1],c)
                    if type(lit.mtype) != type(field[1]):
                        raise TypeMismatch(ast)
                    elif isinstance(lit.mtype,Id) and isinstance(field[1],Id):
                        if lit.mtype.name != field[1].name:
                            raise TypeMismatch(ast)                    
                    elif isinstance(lit.mtype,ArrayType) and isinstance(field[1],ArrayType):
                        if type(lit.mtype.eleType) != type(field[1].eleType):
                            raise TypeMismatch(ast)
                        if isinstance(lit.mtype.eleType,Id) and isinstance(field[1].eleType,Id):
                            if lit.mtype.eleType.name != field[1].eleType.name:
                                raise TypeMismatch(ast)
                        if len(lit.mtype.dimens) != len(field[1].dimens):
                            raise TypeMismatch(ast)
                        for idx in range(len(lit.mtype.dimens)):
                            a = self.visit(lit.mtype.dimens[idx],c)
                            b = self.visit(field[1].dimens[idx],c)
                            if not (isinstance(a.mtype,IntType) and isinstance(b.mtype,IntType)):
                                raise TypeMismatch(ast)
                            if a.value != b.value:
                                raise TypeMismatch(ast)
                        
            if field is None:
                raise Undeclared(Field(),e[0])
        return Symbol(None,Id(ast.name),0)

    def visitNilLiteral(self,ast,c):
        return Symbol(None,None,0)
