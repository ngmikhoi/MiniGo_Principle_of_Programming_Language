.source Holder.java
.class public  Holder
.super java/lang/Object
.field public arr [I

.method public <init>([I)V
.var 0 is this LHolder; from Label0 to Label1
.var 1 is param_arr [I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	aload_1
	putfield Holder/arr [I
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LHolder; from Label0 to Label1
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

.method public getFirst()I
.var 0 is this LHolder; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Holder/arr [I
	iconst_0
	iaload
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
