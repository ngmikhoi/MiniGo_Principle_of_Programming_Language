.source Worker.java
.class public  Worker
.super java/lang/Object
.implements Processor
.field public id I

.method public <init>(I)V
.var 0 is this LWorker; from Label0 to Label1
.var 1 is param_id I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	iload_1
	putfield Worker/id I
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LWorker; from Label0 to Label1
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

.method public process(LData;)I
.var 0 is this LWorker; from Label0 to Label1
.var 1 is d LData; from Label0 to Label1
Label0:
Label2:
	aload_1
	getfield Data/value I
	aload_0
	getfield Worker/id I
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method
