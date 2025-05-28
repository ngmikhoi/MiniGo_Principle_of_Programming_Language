.source Number.java
.class public  Number
.super java/lang/Object
.implements Printer
.field public value I

.method public <init>(I)V
.var 0 is this LNumber; from Label0 to Label1
.var 1 is param_value I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	iload_1
	putfield Number/value I
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LNumber; from Label0 to Label1
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

.method public print()I
.var 0 is this LNumber; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Number/value I
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
