.source Container.java
.class public  Container
.super java/lang/Object
.field public arr [I

.method public <init>([I)V
.var 0 is this LContainer; from Label0 to Label1
.var 1 is param_arr [I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	aload_1
	putfield Container/arr [I
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LContainer; from Label0 to Label1
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
