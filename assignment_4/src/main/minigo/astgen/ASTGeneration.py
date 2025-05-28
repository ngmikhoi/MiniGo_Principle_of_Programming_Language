from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
# 2252377 - Nguyen Minh Khoi
class ASTGeneration(MiniGoVisitor):
    # Visit a parse tree produced by MiniGoParser#int_lit.
    # int_lit: DEC | BIN | OCT | HEX;
    def visitInt_lit(self, ctx:MiniGoParser.Int_litContext):
        # if ctx.DEC():
        #     return IntLiteral(int(ctx.DEC().getText()))
        # elif ctx.BIN():
        #     return IntLiteral(int(ctx.BIN().getText()[2:], 2))
        # elif ctx.OCT():
        #     return IntLiteral(int(ctx.OCT().getText()[2:], 8))
        # elif ctx.HEX():
        #     return IntLiteral(int(ctx.HEX().getText()[2:], 16))
        
        # return IntLiteral(ctx.getChild(0).getText())
        
        return IntLiteral(int(ctx.getChild(0).getText(), base = 0))


    # Visit a parse tree produced by MiniGoParser#bool_lit.
    # bool_lit: TRUE | FALSE;
    def visitBool_lit(self, ctx:MiniGoParser.Bool_litContext):
        if ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        # return BooleanLiteral(ctx.getChild(0).getText())
            


    # Visit a parse tree produced by MiniGoParser#program.
    # program  : manydecl EOF ;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.manydecl()))


    # Visit a parse tree produced by MiniGoParser#manydecl.
    # manydecl: decl manydecl | decl;
    def visitManydecl(self, ctx:MiniGoParser.ManydeclContext):        
        mems = []
        if ctx.decl():
            mem = self.visit(ctx.decl())
            mems.append(mem)
        if ctx.manydecl():
            mems_tail = self.visit(ctx.manydecl())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#stmt.
    # stmt:   var_decl | const_decl
    #     | assign_stmt | func_call_stmt | if_stmt | for_stmt
    #     | break_stmt | continue_stmt | return_stmt
    #     ;
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        elif ctx.const_decl():
            return self.visit(ctx.const_decl())
        elif ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.func_call_stmt():
            return self.visit(ctx.func_call_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        

    # Visit a parse tree produced by MiniGoParser#stmt_block.
    # stmt_block: stmt stmt_block | stmt;
    def visitStmt_block(self, ctx:MiniGoParser.Stmt_blockContext):
        mems = []
        if ctx.stmt():
            mem = self.visit(ctx.stmt())
            mems.append(mem)
        if ctx.stmt_block():
            mems_tail = self.visit(ctx.stmt_block())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#decl.
    # decl: var_decl | const_decl |func_decl | struct_decl |interface_decl;
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        elif ctx.const_decl():
            return self.visit(ctx.const_decl())
        elif ctx.func_decl():
            return self.visit(ctx.func_decl())
        elif ctx.struct_decl():
            return self.visit(ctx.struct_decl())
        elif ctx.interface_decl():
            return self.visit(ctx.interface_decl())


    # Visit a parse tree produced by MiniGoParser#var_decl.
    # var_decl: var_decl_init | var_decl_uninit;
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        if ctx.var_decl_init():
            return self.visit(ctx.var_decl_init())
        elif ctx.var_decl_uninit():
            return self.visit(ctx.var_decl_uninit())


    # Visit a parse tree produced by MiniGoParser#var_decl_init.
    # var_decl_init: VAR ID (all_type | ) EQ expr1 SECO;
    def visitVar_decl_init(self, ctx:MiniGoParser.Var_decl_initContext):
        varName = ctx.ID().getText()
        varType = self.visit(ctx.all_type()) if ctx.all_type() else None
        varInit = self.visit(ctx.expr1())
        return VarDecl(varName, varType, varInit)


    # Visit a parse tree produced by MiniGoParser#var_decl_uninit.
    # var_decl_uninit: VAR ID all_type SECO;
    def visitVar_decl_uninit(self, ctx:MiniGoParser.Var_decl_uninitContext):
        varName = ctx.ID().getText()
        varType = self.visit(ctx.all_type())
        varInit = None
        return VarDecl(varName, varType, varInit)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    # const_decl: CONST ID EQ expr1 SECO;
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        conName = ctx.ID().getText()
        conType = None
        iniExpr = self.visit(ctx.expr1())
        return ConstDecl(conName, conType, iniExpr)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    # func_decl:  function_decl | method_decl;
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        if ctx.method_decl():
            return self.visit(ctx.method_decl())
        elif ctx.function_decl():
            return self.visit(ctx.function_decl())


    # Visit a parse tree produced by MiniGoParser#function_decl.
    # function_decl: FUNC ID LCIB (list_para_func | ) RCIB (all_type | ) LCUB stmt_block RCUB SECO;
    def visitFunction_decl(self, ctx:MiniGoParser.Function_declContext):
        name = ctx.ID().getText()
        params = []
        if ctx.list_para_func():
            params = self.visit(ctx.list_para_func())
            for idx in range(len(params) - 2, -1, -1):
                if params[idx].parType == Id("_Dont_have_any_type_MK37_"):
                    params[idx].parType = params[idx + 1].parType
        typ = self.visit(ctx.all_type()) if ctx.all_type() else VoidType()
        body = Block(self.visit(ctx.stmt_block()))
        return FuncDecl(name, params, typ, body)
        

    # Visit a parse tree produced by MiniGoParser#method_decl.
    # method_decl: FUNC LCIB rec rec_type RCIB ID LCIB (list_para_func | ) RCIB (all_type | ) LCUB stmt_block RCUB SECO;
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        name = ctx.ID().getText()
        params = []
        if ctx.list_para_func():
            params = self.visit(ctx.list_para_func())
            for idx in range(len(params) - 2, -1, -1):
                if params[idx].parType == Id("_Dont_have_any_type_MK37_"):
                    params[idx].parType = params[idx + 1].parType
        typ = self.visit(ctx.all_type()) if ctx.all_type() else VoidType()
        body = Block(self.visit(ctx.stmt_block()))
        func =  FuncDecl(name, params, typ, body)
        return MethodDecl(self.visit(ctx.rec()), self.visit(ctx.rec_type()), func)        


    # Visit a parse tree produced by MiniGoParser#rec.
    # rec: ID;
    def visitRec(self, ctx:MiniGoParser.RecContext):
        return ctx.ID().getText()


    # Visit a parse tree produced by MiniGoParser#rec_type.
    # rec_type: ID;
    def visitRec_type(self, ctx:MiniGoParser.Rec_typeContext):
        return Id(ctx.ID().getText())
    
    # Visit a parse tree produced by MiniGoParser#not_last_para_func.
    # not_last_para_func: para_func tail_para_func;
    def visitNot_last_para_func(self, ctx:MiniGoParser.Not_last_para_funcContext):
        mems = []
        if ctx.para_func():
            mem = self.visit(ctx.para_func())
            mems.append(mem)
        if ctx.tail_para_func():
            mems_tail = self.visit(ctx.tail_para_func())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#tail_para_func.
    # tail_para_func: COMMA para_func tail_para_func | ;
    def visitTail_para_func(self, ctx:MiniGoParser.Tail_para_funcContext):
        mems = []
        if ctx.para_func():
            mem = self.visit(ctx.para_func())
            mems.append(mem)
        if ctx.tail_para_func():
            mems_tail = self.visit(ctx.tail_para_func())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#para_func.
    # para_func: ID all_type | ID;
    def visitPara_func(self, ctx:MiniGoParser.Para_funcContext):
        parName = ctx.ID().getText()
        parType = self.visit(ctx.all_type()) if ctx.all_type() else Id("_Dont_have_any_type_MK37_")
        return ParamDecl(parName, parType)


    # Visit a parse tree produced by MiniGoParser#last_para_func.
    # last_para_func: ID all_type;
    def visitLast_para_func(self, ctx:MiniGoParser.Last_para_funcContext):
        parName = ctx.ID().getText()
        parType = self.visit(ctx.all_type())
        return ParamDecl(parName, parType)


    # Visit a parse tree produced by MiniGoParser#list_para_func.
    # list_para_func: not_last_para_func COMMA last_para_func | last_para_func; 
    def visitList_para_func(self, ctx:MiniGoParser.List_para_funcContext):
        mems = []
        if ctx.not_last_para_func():
            mems_head = self.visit(ctx.not_last_para_func())
            mems.extend(mems_head)
        if ctx.last_para_func():
            mem = self.visit(ctx.last_para_func())
            mems.append(mem)
        return mems


    # Visit a parse tree produced by MiniGoParser#star_func_call_dot.
    # star_func_call_dot: star_func_call_dot func_call DOT  | ;
    def visitStar_func_call_dot(self, ctx:MiniGoParser.Star_func_call_dotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniGoParser#func_call_stmt.
    # func_call_stmt: star_func_call_dot func_call SECO;
    def visitFunc_call_stmt(self, ctx:MiniGoParser.Func_call_stmtContext):
        return self.visit(ctx.func_call())


    # Visit a parse tree produced by MiniGoParser#func_call.
    # func_call:  function_call | method_call;
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        if ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.method_call():
            return self.visit(ctx.method_call())


    # Visit a parse tree produced by MiniGoParser#function_call.
    # function_call: ID LCIB (list_arg | ) RCIB;
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.list_arg()) if ctx.list_arg() else []
        return FuncCall(name, args)


    # Visit a parse tree produced by MiniGoParser#method_call.
    # method_call: lhs DOT ID LCIB (list_arg | ) RCIB;
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        receiver = self.visit(ctx.lhs())
        name = ctx.ID().getText()
        args = self.visit(ctx.list_arg()) if ctx.list_arg() else []
        return MethCall(receiver, name, args)


    # Visit a parse tree produced by MiniGoParser#list_arg.
    # list_arg: arg tail_arg | arg;
    def visitList_arg(self, ctx:MiniGoParser.List_argContext):
        mems = []
        if ctx.arg():
            mem = self.visit(ctx.arg())
            mems.append(mem)
        if ctx.tail_arg():
            mems_tail = self.visit(ctx.tail_arg())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#tail_arg.
    # tail_arg: COMMA arg tail_arg | ;
    def visitTail_arg(self, ctx:MiniGoParser.Tail_argContext):
        mems = []
        if ctx.arg():
            mem = self.visit(ctx.arg())
            mems.append(mem)
        if ctx.tail_arg():
            mems_tail = self.visit(ctx.tail_arg())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#arg.
    # arg: expr1;
    def visitArg(self, ctx:MiniGoParser.ArgContext):
        return self.visit(ctx.expr1())


    # Visit a parse tree produced by MiniGoParser#arr_dim_decl.
    # arr_dim_decl: arr_dim_decl (LSQB (int_lit | ID) RSQB)  | (LSQB (int_lit | ID) RSQB);
    def visitArr_dim_decl(self, ctx:MiniGoParser.Arr_dim_declContext):
        mems = []
        if ctx.arr_dim_decl():
            mems_head = self.visit(ctx.arr_dim_decl())
            mems.extend(mems_head)
        if ctx.int_lit():
            mem = self.visit(ctx.int_lit())
            mems.append(mem)
        elif ctx.ID():
            mem = Id(ctx.ID().getText())
            mems.append(mem)
        return mems


    # Visit a parse tree produced by MiniGoParser#arr_type.
    # arr_type: arr_dim_decl (primi | ID) ;
    def visitArr_type(self, ctx:MiniGoParser.Arr_typeContext):
        dimens = self.visit(ctx.arr_dim_decl())
        eleType = self.visit(ctx.primi()) if ctx.primi() else Id(ctx.ID().getText())
        return ArrayType(dimens, eleType)


    # Visit a parse tree produced by MiniGoParser#arr_lit.
    # arr_lit: arr_dim_decl (primi | ID) LCUB list_ele_arr RCUB;
    def visitArr_lit(self, ctx:MiniGoParser.Arr_litContext):
        dimens = self.visit(ctx.arr_dim_decl())
        eleType = self.visit(ctx.primi()) if ctx.primi() else Id(ctx.ID().getText())
        value = self.visit(ctx.list_ele_arr())
        return ArrayLiteral(dimens, eleType, value)


    # Visit a parse tree produced by MiniGoParser#list_ele_arr.
    # list_ele_arr: ele_arr tail_ele_arr | ele_arr;
    def visitList_ele_arr(self, ctx:MiniGoParser.List_ele_arrContext):
        mems = []
        if ctx.ele_arr():
            mem = self.visit(ctx.ele_arr())
            mems.append(mem)
        if ctx.tail_ele_arr():
            mems_tail = self.visit(ctx.tail_ele_arr())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#tail_ele_arr.
    # tail_ele_arr: COMMA ele_arr tail_ele_arr | ;
    def visitTail_ele_arr(self, ctx:MiniGoParser.Tail_ele_arrContext):
        mems = []
        if ctx.ele_arr():
            mem = self.visit(ctx.ele_arr())
            mems.append(mem)
        if ctx.tail_ele_arr():
            mems_tail = self.visit(ctx.tail_ele_arr())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#ele_arr.
    # ele_arr: int_lit | FLOAT_LIT | STRING_LIT | bool_lit | NIL | struct_lit | ID | LCUB list_ele_arr RCUB;
    def visitEle_arr(self, ctx:MiniGoParser.Ele_arrContext):
        if ctx.int_lit():
            return self.visit(ctx.int_lit())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
            # return FloatLiteral(ctx.FLOAT_LIT().getText())
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.bool_lit():
            return self.visit(ctx.bool_lit())
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.struct_lit():
            return self.visit(ctx.struct_lit())
        elif ctx.list_ele_arr():
            return self.visit(ctx.list_ele_arr())


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    # struct_decl: TYPE ID STRUCT LCUB star_struct_ele_decl RCUB SECO;
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        name = ctx.ID().getText()
        elements = self.visit(ctx.star_struct_ele_decl()) if ctx.star_struct_ele_decl() else [];
        methods = [];
        return StructType(name, elements, methods)
        

    # Visit a parse tree produced by MiniGoParser#star_struct_ele_decl.
    # star_struct_ele_decl: attr_decl star_struct_ele_decl | attr_decl;
    def visitStar_struct_ele_decl(self, ctx:MiniGoParser.Star_struct_ele_declContext):
        mems = []
        if ctx.attr_decl():
            mem = self.visit(ctx.attr_decl())
            mems.append(mem)
        if ctx.star_struct_ele_decl():
            mems_tail = self.visit(ctx.star_struct_ele_decl())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#attr_decl.
    # attr_decl: ID all_type SECO;
    def visitAttr_decl(self, ctx:MiniGoParser.Attr_declContext):
        return (ctx.ID().getText(), self.visit(ctx.all_type()))


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    # struct_lit: ID LCUB (list_ele_struct| ) RCUB;
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        name = ctx.ID().getText()
        elements = self.visit(ctx.list_ele_struct()) if ctx.list_ele_struct() else [];
        return StructLiteral(name, elements)


    # Visit a parse tree produced by MiniGoParser#list_ele_struct.
    # list_ele_struct: ele_struct tail_ele_struct | ele_struct;
    def visitList_ele_struct(self, ctx:MiniGoParser.List_ele_structContext):
        mems = []
        if ctx.ele_struct():
            mem = self.visit(ctx.ele_struct())
            mems.append(mem)
        if ctx.tail_ele_struct():
            mems_tail = self.visit(ctx.tail_ele_struct())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#tail_ele_struct.
    # tail_ele_struct: COMMA ele_struct tail_ele_struct | ;
    def visitTail_ele_struct(self, ctx:MiniGoParser.Tail_ele_structContext):
        mems = []
        if ctx.ele_struct():
            mem = self.visit(ctx.ele_struct())
            mems.append(mem)
        if ctx.tail_ele_struct():
            mems_tail = self.visit(ctx.tail_ele_struct())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#ele_struct.
    # ele_struct: ID COLON expr1;
    def visitEle_struct(self, ctx:MiniGoParser.Ele_structContext):
        return (ctx.ID().getText(), self.visit(ctx.expr1()))
    
    
    # Visit a parse tree produced by MiniGoParser#method_interface.
    # method_interface: ID LCIB (list_para | ) RCIB (all_type | ) SECO;
    def visitMethod_interface(self, ctx:MiniGoParser.Method_interfaceContext):
        name = ctx.ID().getText()
        params = []
        if ctx.list_para():
            params = self.visit(ctx.list_para())
            for idx in range(len(params) - 2, -1, -1):
                if params[idx] == Id("_Dont_have_any_type_MK37_"):
                    params[idx] = params[idx + 1]
            
        retType = self.visit(ctx.all_type()) if ctx.all_type() else VoidType()
        return Prototype(name, params, retType)

    # Visit a parse tree produced by MiniGoParser#star_interface_method_decl.
    # star_interface_method_decl: method_interface star_interface_method_decl | method_interface;
    def visitStar_interface_method_decl(self, ctx:MiniGoParser.Star_interface_method_declContext):
        mems = []
        if ctx.method_interface():
            mem = self.visit(ctx.method_interface())
            mems.append(mem)
        if ctx.star_interface_method_decl():
            mems_tail = self.visit(ctx.star_interface_method_decl())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    # interface_decl: TYPE ID INTERFACE LCUB star_interface_method_decl  RCUB SECO;
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        name = ctx.ID().getText()
        methods = self.visit(ctx.star_interface_method_decl())
        return InterfaceType(name, methods)
        

    # Visit a parse tree produced by MiniGoParser#not_last_para.
    # not_last_para: para tail_para;
    def visitNot_last_para(self, ctx:MiniGoParser.Not_last_paraContext):
        mems = []
        if ctx.para():
            mem = self.visit(ctx.para())
            mems.append(mem)
        if ctx.tail_para():
            mems_tail = self.visit(ctx.tail_para())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#tail_para.
    # tail_para: COMMA para tail_para | ;
    def visitTail_para(self, ctx:MiniGoParser.Tail_paraContext):
        mems = []
        if ctx.para():
            mem = self.visit(ctx.para())
            mems.append(mem)
        if ctx.tail_para():
            mems_tail = self.visit(ctx.tail_para())
            mems.extend(mems_tail)
        return mems


    # Visit a parse tree produced by MiniGoParser#para.
    # para: ID all_type | ID;
    def visitPara(self, ctx:MiniGoParser.ParaContext):
        if ctx.all_type():
            return self.visit(ctx.all_type())
        else:
            return Id("_Dont_have_any_type_MK37_")


    # Visit a parse tree produced by MiniGoParser#last_para.
    # last_para: ID all_type;
    def visitLast_para(self, ctx:MiniGoParser.Last_paraContext):
        return self.visit(ctx.all_type())


    # Visit a parse tree produced by MiniGoParser#list_para.
    # list_para: not_last_para COMMA last_para | last_para; 
    def visitList_para(self, ctx:MiniGoParser.List_paraContext):
        mems = []
        if ctx.not_last_para():
            mems_head = self.visit(ctx.not_last_para())
            mems.extend(mems_head)
        if ctx.last_para():
            mem = self.visit(ctx.last_para())
            mems.append(mem)
        return mems


    # Visit a parse tree produced by MiniGoParser#assign_stmt.
    # assign_stmt: lhs assign_op expr1 SECO;
    def visitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr1());
        if self.visit(ctx.assign_op()) != ":=":
            op = self.visit(ctx.assign_op())[0:1]
            rhs = BinaryOp(op, lhs, rhs)
        return Assign(lhs, rhs)

    # Visit a parse tree produced by MiniGoParser#assign_op.
    # assign_op: AS_EQ | ADD_EQ | SUB_EQ | MUL_EQ | DIV_EQ | MOD_EQ;
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        return ctx.getChild(0).getText() 


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    # if_stmt: IF LCIB condit RCIB LCUB stmt_block RCUB else_if SECO;    
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        expr = self.visit(ctx.condit())
        thenStmt = Block(self.visit(ctx.stmt_block()))
        elseStmt = self.visit(ctx.else_if())
        return If(expr, thenStmt, elseStmt)


    # Visit a parse tree produced by MiniGoParser#else_if.
    # else_if: ELSE IF LCIB condit RCIB LCUB stmt_block RCUB else_if | else_stmt;
    def visitElse_if(self, ctx:MiniGoParser.Else_ifContext):
        if ctx.else_stmt():
            return self.visit(ctx.else_stmt())
        else:
            expr = self.visit(ctx.condit())
            thenStmt = Block(self.visit(ctx.stmt_block()))
            elseStmt = self.visit(ctx.else_if())
            return If(expr, thenStmt, elseStmt)


    # Visit a parse tree produced by MiniGoParser#else_stmt.
    # else_stmt: ELSE LCUB stmt_block RCUB | ;
    def visitElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        if ctx.ELSE():
            return Block(self.visit(ctx.stmt_block()))
        else:
            return None

    # Visit a parse tree produced by MiniGoParser#for_stmt.
    # for_stmt: basic_for | init_for | range_for;
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        if ctx.basic_for():
            return self.visit(ctx.basic_for())
        elif ctx.init_for():
            return self.visit(ctx.init_for())
        elif ctx.range_for():
            return self.visit(ctx.range_for())


    # Visit a parse tree produced by MiniGoParser#basic_for.
    # basic_for: FOR condit  LCUB stmt_block RCUB SECO;
    def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        cond = self.visit(ctx.condit())
        loop = Block(self.visit(ctx.stmt_block()))
        return ForBasic(cond,loop)


    # Visit a parse tree produced by MiniGoParser#init_for.
    # init_for: FOR init condit SECO update LCUB stmt_block RCUB SECO;
    def visitInit_for(self, ctx:MiniGoParser.Init_forContext):
        init = self.visit(ctx.init())
        cond = self.visit(ctx.condit())
        upda = self.visit(ctx.update())
        loop = Block(self.visit(ctx.stmt_block()))
        return ForStep(init, cond, upda, loop)


    # Visit a parse tree produced by MiniGoParser#init.
    # init: assign_stmt | var_decl_init;
    def visitInit(self, ctx:MiniGoParser.InitContext):
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.var_decl_init():
            return self.visit(ctx.var_decl_init())


    # Visit a parse tree produced by MiniGoParser#condit.
    # condit: expr1;
    def visitCondit(self, ctx:MiniGoParser.ConditContext):
        return self.visit(ctx.expr1())


    # Visit a parse tree produced by MiniGoParser#update.
    # update: lhs assign_op expr1;
    def visitUpdate(self, ctx:MiniGoParser.UpdateContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr1());
        if self.visit(ctx.assign_op()) != ":=":
            op = self.visit(ctx.assign_op())[0:1]
            rhs = BinaryOp(op, lhs, rhs)
        return Assign(lhs, rhs)


    # Visit a parse tree produced by MiniGoParser#range_for.
    # range_for: FOR (index | blank) COMMA value AS_EQ RANGE array_id LCUB stmt_block RCUB SECO;
    def visitRange_for(self, ctx:MiniGoParser.Range_forContext):
        # idx = self.visit(ctx.index()) if ctx.index() else self.visit(ctx.blank())
        idx = self.visit(ctx.index())
        value = self.visit(ctx.value())
        arr = self.visit(ctx.array_id())
        loop = Block(self.visit(ctx.stmt_block()))
        return ForEach(idx, value, arr, loop)


    # Visit a parse tree produced by MiniGoParser#index.
    # index: ID;
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return Id(ctx.ID().getText())


    # # Visit a parse tree produced by MiniGoParser#blank.
    # # blank: '_';
    # def visitBlank(self, ctx:MiniGoParser.BlankContext):
    #     return None


    # Visit a parse tree produced by MiniGoParser#value.
    # value: ID;
    def visitValue(self, ctx:MiniGoParser.ValueContext):
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#array_id.
    # array_id: expr1;
    def visitArray_id(self, ctx:MiniGoParser.Array_idContext):
        return self.visit(ctx.expr1())


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    # break_stmt: BREAK SECO; 
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    # continue_stmt: CONTINUE SECO;
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    # return_stmt: RETURN (expr1 | ) SECO;
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        if ctx.expr1():
            return Return(self.visit(ctx.expr1()))
        else:
            return Return(None)


    # Visit a parse tree produced by MiniGoParser#rela_op.
    # rela_op: DBL_EQ | NOT_EQ | LT | LE | GT | GE ;
    def visitRela_op(self, ctx:MiniGoParser.Rela_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#addsub.
    def visitAddsub(self, ctx:MiniGoParser.AddsubContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#mudimo.
    def visitMudimo(self, ctx:MiniGoParser.MudimoContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#unary.
    def visitUnary(self, ctx:MiniGoParser.UnaryContext):
        return ctx.getChild(0).getText()
    

    # Visit a parse tree produced by MiniGoParser#expr1.
    # expr1: expr1 OR expr2 | expr2;
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        if ctx.OR():
            op = ctx.OR().getText()
            left = self.visit(ctx.expr1())
            right = self.visit(ctx.expr2())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr2())


    # Visit a parse tree produced by MiniGoParser#expr2.
    # expr2: expr2 AND expr3 | expr3;
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        if ctx.AND():
            op = op = ctx.AND().getText()
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr3())


    # Visit a parse tree produced by MiniGoParser#expr3.
    # expr3: expr3 rela_op expr4 | expr4;
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        if ctx.rela_op():
            op = self.visit(ctx.rela_op())
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr4())


    # Visit a parse tree produced by MiniGoParser#expr4.
    # expr4: expr4 addsub expr5 | expr5;
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        if ctx.addsub():
            op = self.visit(ctx.addsub())
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr5())


    # Visit a parse tree produced by MiniGoParser#expr5.
    # expr5: expr5 mudimo expr6 | expr6;
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        if ctx.mudimo():
            op = self.visit(ctx.mudimo())
            left = self.visit(ctx.expr5())
            right = self.visit(ctx.expr6())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr6())


    # Visit a parse tree produced by MiniGoParser#expr6.
    # expr6: unary expr6 | expr7;
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        if ctx.unary():
            op = self.visit(ctx.unary())
            body = self.visit(ctx.expr6())
            return UnaryOp(op, body)
        else:
            return self.visit(ctx.expr7())


    # Visit a parse tree produced by MiniGoParser#expr7.
    # expr7: expr7 DOT field | expr7 DOT function_call | expr7 dims | operand;
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        if ctx.operand():
            return self.visit(ctx.operand())
        elif ctx.dims():
            arr = self.visit(ctx.expr7())
            idx = self.visit(ctx.dims())
            return ArrayCell(arr, idx)
        elif ctx.field():
            receiver = self.visit(ctx.expr7())
            field = self.visit(ctx.field())
            return FieldAccess(receiver, field)
        elif ctx.function_call():
            receiver = self.visit(ctx.expr7())
            func = self.visit(ctx.function_call())
            return MethCall(receiver, func.funName, func.args)
            

    # Visit a parse tree produced by MiniGoParser#operand.
    # operand: lit | ID | function_call | LCIB expr1 RCIB;
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        if ctx.lit():
            return self.visit(ctx.lit())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.expr1():
            return self.visit(ctx.expr1())
        elif ctx.ID():
            return Id(ctx.ID().getText())

    # Visit a parse tree produced by MiniGoParser#lit.
    # lit: int_lit | FLOAT_LIT | STRING_LIT | bool_lit | NIL | struct_lit | arr_lit;
    def visitLit(self, ctx:MiniGoParser.LitContext):
        if ctx.int_lit():
            return self.visit(ctx.int_lit())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))        
            # return FloatLiteral(ctx.FLOAT_LIT().getText())
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.bool_lit():
            return self.visit(ctx.bool_lit())
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.struct_lit():
            return self.visit(ctx.struct_lit())
        elif ctx.arr_lit():
            return self.visit(ctx.arr_lit())


    # Visit a parse tree produced by MiniGoParser#primi.
    # primi: INT | FLOAT | BOOLEAN | STRING;
    def visitPrimi(self, ctx:MiniGoParser.PrimiContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()


    # Visit a parse tree produced by MiniGoParser#all_type.
    # all_type: ID | primi | arr_type;
    def visitAll_type(self, ctx:MiniGoParser.All_typeContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.primi():
            return self.visit(ctx.primi())
        elif ctx.arr_type():
            return self.visit(ctx.arr_type())
        
        
     # Visit a parse tree produced by MiniGoParser#lhs.
    # lhs: lhs DOT field | lhs dims | ID;
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.field():
            receiver = self.visit(ctx.lhs())
            field = self.visit(ctx.field())
            return FieldAccess(receiver, field)
        elif ctx.dims():
            arr = self.visit(ctx.lhs())
            idx = self.visit(ctx.dims())
            return ArrayCell(arr, idx)
        elif ctx.ID():
            return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#field.
    # field: ID;
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return ctx.ID().getText()


    # Visit a parse tree produced by MiniGoParser#dims.
    # dims: dims dim | dim;
    def visitDims(self, ctx:MiniGoParser.DimsContext):
        mems = []
        if ctx.dims():
            mems_head = self.visit(ctx.dims())
            mems.extend(mems_head)
        if ctx.dim():
            mem = self.visit(ctx.dim())
            mems.append(mem)
        return mems


    # Visit a parse tree produced by MiniGoParser#dim.
    # dim: LSQB expr1 RSQB;
    def visitDim(self, ctx:MiniGoParser.DimContext):
        return self.visit(ctx.expr1())