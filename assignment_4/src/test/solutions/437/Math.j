.source Math.java
.class public  Math
.super java/lang/Object
.field public x I

.method public <init>(I)V
.var 0 is this LMath; from Label0 to Label1
.var 1 is param_x I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	iload_1
	putfield Math/x I
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMath; from Label0 to Label1
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

.method public square()I
.var 0 is this LMath; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Math/x I
	aload_0
	getfield Math/x I
	imul
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
