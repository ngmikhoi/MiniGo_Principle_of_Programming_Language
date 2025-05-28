.source Calculator.java
.class public  Calculator
.super java/lang/Object
.field public x F

.method public <init>(F)V
.var 0 is this LCalculator; from Label0 to Label1
.var 1 is param_x F from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	fload_1
	putfield Calculator/x F
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LCalculator; from Label0 to Label1
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

.method public double()F
.var 0 is this LCalculator; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Calculator/x F
	fconst_2
	fmul
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
