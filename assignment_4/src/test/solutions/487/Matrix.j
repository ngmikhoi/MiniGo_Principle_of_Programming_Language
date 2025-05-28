.source Matrix.java
.class public  Matrix
.super java/lang/Object
.field public data [[I

.method public <init>([[I)V
.var 0 is this LMatrix; from Label0 to Label1
.var 1 is param_data [[I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	aload_1
	putfield Matrix/data [[I
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMatrix; from Label0 to Label1
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

.method public getElement(II)I
.var 0 is this LMatrix; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Matrix/data [[I
	iload_1
	aaload
	iload_2
	iaload
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 3
.end method
