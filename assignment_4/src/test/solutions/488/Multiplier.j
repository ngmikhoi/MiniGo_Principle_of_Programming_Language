.source Multiplier.java
.class public  Multiplier
.super java/lang/Object
.implements Scaler
.field public factor F

.method public <init>(F)V
.var 0 is this LMultiplier; from Label0 to Label1
.var 1 is param_factor F from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	fload_1
	putfield Multiplier/factor F
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMultiplier; from Label0 to Label1
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

.method public scale(F)F
.var 0 is this LMultiplier; from Label0 to Label1
.var 1 is x F from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Multiplier/factor F
	fload_1
	fmul
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method
