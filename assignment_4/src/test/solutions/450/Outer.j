.source Outer.java
.class public  Outer
.super java/lang/Object
.field public arr [LInner;

.method public <init>([LInner;)V
.var 0 is this LOuter; from Label0 to Label1
.var 1 is param_arr [LInner; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	aload_1
	putfield Outer/arr [LInner;
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LOuter; from Label0 to Label1
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
