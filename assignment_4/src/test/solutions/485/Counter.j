.source Counter.java
.class public  Counter
.super java/lang/Object
.field public value I

.method public <init>(I)V
.var 0 is this LCounter; from Label0 to Label1
.var 1 is param_value I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	iload_1
	putfield Counter/value I
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LCounter; from Label0 to Label1
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

.method public sumToN(I)I
.var 0 is this LCounter; from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
Label2:
.var 2 is sum I from Label2 to Label3
	iconst_0
	istore_2
.var 3 is i I from Label2 to Label3
	iconst_1
	istore_3
	iconst_1
	istore_3
Label6:
	iload_3
	iload_1
	if_icmpgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	iload_2
	aload_0
	getfield Counter/value I
	iadd
	istore_2
Label10:
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label6
Label5:
	iload_2
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 4
.end method
