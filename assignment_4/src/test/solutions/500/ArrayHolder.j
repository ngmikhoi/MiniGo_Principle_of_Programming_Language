.source ArrayHolder.java
.class public  ArrayHolder
.super java/lang/Object
.field public arr [I

.method public <init>([I)V
.var 0 is this LArrayHolder; from Label0 to Label1
.var 1 is param_arr [I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	aload_1
	putfield ArrayHolder/arr [I
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LArrayHolder; from Label0 to Label1
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

.method public sum()I
.var 0 is this LArrayHolder; from Label0 to Label1
Label0:
Label2:
.var 1 is sum I from Label2 to Label3
	iconst_0
	istore_1
.var 2 is i I from Label2 to Label3
	iconst_0
	istore_2
	iconst_0
	istore_2
Label6:
	iload_2
	iconst_3
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	iload_1
	aload_0
	getfield ArrayHolder/arr [I
	iload_2
	iaload
	iadd
	istore_1
Label10:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
	iload_1
	ireturn
Label3:
Label1:
.limit stack 4
.limit locals 3
.end method
