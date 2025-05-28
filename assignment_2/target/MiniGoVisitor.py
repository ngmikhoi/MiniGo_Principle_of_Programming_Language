# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#int_lit.
    def visitInt_lit(self, ctx:MiniGoParser.Int_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#bool_lit.
    def visitBool_lit(self, ctx:MiniGoParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#manydecl.
    def visitManydecl(self, ctx:MiniGoParser.ManydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_block.
    def visitStmt_block(self, ctx:MiniGoParser.Stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl_init.
    def visitVar_decl_init(self, ctx:MiniGoParser.Var_decl_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl_uninit.
    def visitVar_decl_uninit(self, ctx:MiniGoParser.Var_decl_uninitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_decl.
    def visitFunction_decl(self, ctx:MiniGoParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rec.
    def visitRec(self, ctx:MiniGoParser.RecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rec_type.
    def visitRec_type(self, ctx:MiniGoParser.Rec_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#not_last_para_func.
    def visitNot_last_para_func(self, ctx:MiniGoParser.Not_last_para_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#tail_para_func.
    def visitTail_para_func(self, ctx:MiniGoParser.Tail_para_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#para_func.
    def visitPara_func(self, ctx:MiniGoParser.Para_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#last_para_func.
    def visitLast_para_func(self, ctx:MiniGoParser.Last_para_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_para_func.
    def visitList_para_func(self, ctx:MiniGoParser.List_para_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#star_func_call_dot.
    def visitStar_func_call_dot(self, ctx:MiniGoParser.Star_func_call_dotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call_stmt.
    def visitFunc_call_stmt(self, ctx:MiniGoParser.Func_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_call.
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_call.
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_arg.
    def visitList_arg(self, ctx:MiniGoParser.List_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#tail_arg.
    def visitTail_arg(self, ctx:MiniGoParser.Tail_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arg.
    def visitArg(self, ctx:MiniGoParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_dim_decl.
    def visitArr_dim_decl(self, ctx:MiniGoParser.Arr_dim_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_type.
    def visitArr_type(self, ctx:MiniGoParser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_lit.
    def visitArr_lit(self, ctx:MiniGoParser.Arr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_ele_arr.
    def visitList_ele_arr(self, ctx:MiniGoParser.List_ele_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#tail_ele_arr.
    def visitTail_ele_arr(self, ctx:MiniGoParser.Tail_ele_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ele_arr.
    def visitEle_arr(self, ctx:MiniGoParser.Ele_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#star_struct_ele_decl.
    def visitStar_struct_ele_decl(self, ctx:MiniGoParser.Star_struct_ele_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#attr_decl.
    def visitAttr_decl(self, ctx:MiniGoParser.Attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_ele_struct.
    def visitList_ele_struct(self, ctx:MiniGoParser.List_ele_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#tail_ele_struct.
    def visitTail_ele_struct(self, ctx:MiniGoParser.Tail_ele_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ele_struct.
    def visitEle_struct(self, ctx:MiniGoParser.Ele_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_interface.
    def visitMethod_interface(self, ctx:MiniGoParser.Method_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#star_interface_method_decl.
    def visitStar_interface_method_decl(self, ctx:MiniGoParser.Star_interface_method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#not_last_para.
    def visitNot_last_para(self, ctx:MiniGoParser.Not_last_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#tail_para.
    def visitTail_para(self, ctx:MiniGoParser.Tail_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#para.
    def visitPara(self, ctx:MiniGoParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#last_para.
    def visitLast_para(self, ctx:MiniGoParser.Last_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_para.
    def visitList_para(self, ctx:MiniGoParser.List_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_op.
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if.
    def visitElse_if(self, ctx:MiniGoParser.Else_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_stmt.
    def visitElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_for.
    def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_for.
    def visitInit_for(self, ctx:MiniGoParser.Init_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init.
    def visitInit(self, ctx:MiniGoParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condit.
    def visitCondit(self, ctx:MiniGoParser.ConditContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#update.
    def visitUpdate(self, ctx:MiniGoParser.UpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_for.
    def visitRange_for(self, ctx:MiniGoParser.Range_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index.
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#value.
    def visitValue(self, ctx:MiniGoParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_id.
    def visitArray_id(self, ctx:MiniGoParser.Array_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rela_op.
    def visitRela_op(self, ctx:MiniGoParser.Rela_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#addsub.
    def visitAddsub(self, ctx:MiniGoParser.AddsubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mudimo.
    def visitMudimo(self, ctx:MiniGoParser.MudimoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unary.
    def visitUnary(self, ctx:MiniGoParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lit.
    def visitLit(self, ctx:MiniGoParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primi.
    def visitPrimi(self, ctx:MiniGoParser.PrimiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#all_type.
    def visitAll_type(self, ctx:MiniGoParser.All_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dims.
    def visitDims(self, ctx:MiniGoParser.DimsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dim.
    def visitDim(self, ctx:MiniGoParser.DimContext):
        return self.visitChildren(ctx)



del MiniGoParser