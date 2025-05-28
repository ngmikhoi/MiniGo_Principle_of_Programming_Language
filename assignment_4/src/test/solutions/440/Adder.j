.source Adder.java
.class public  Adder
.super java/lang/Object
.implements Calculator
.field public x F

.method public <init>(F)V
.var 0 is this LAdder; from Label0 to Label1
.var 1 is param_x F from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	fload_1
	putfield Adder/x F
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LAdder; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public calc()F
.var 0 is this LAdder; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Adder/x F
	fconst_1
	fadd
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
