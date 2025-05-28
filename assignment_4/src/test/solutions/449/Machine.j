.source Machine.java
.class public  Machine
.super java/lang/Object
.implements Worker
.field public id I

.method public <init>(I)V
.var 0 is this LMachine; from Label0 to Label1
.var 1 is param_id I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	iload_1
	putfield Machine/id I
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMachine; from Label0 to Label1
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

.method public start()I
.var 0 is this LMachine; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Machine/id I
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method

.method public stop()I
.var 0 is this LMachine; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Machine/id I
	iconst_1
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
