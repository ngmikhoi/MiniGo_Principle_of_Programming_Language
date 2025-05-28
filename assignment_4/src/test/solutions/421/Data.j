.source Data.java
.class public  Data
.super java/lang/Object
.implements Processor
.field public value I

.method public <init>(I)V
.var 0 is this LData; from Label0 to Label1
.var 1 is param_value I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	iload_1
	putfield Data/value I
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LData; from Label0 to Label1
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

.method public process()I
.var 0 is this LData; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Data/value I
	iconst_1
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
