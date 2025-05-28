.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is o LOuter; from Label2 to Label3
	new Outer
	dup
	iconst_2
	multianewarray [LInner; 1
	dup
	iconst_0
	new Inner
	dup
	iconst_1
	invokespecial Inner/<init>(I)V
	aastore
	dup
	iconst_1
	new Inner
	dup
	iconst_2
	invokespecial Inner/<init>(I)V
	aastore
	invokespecial Outer/<init>([LInner;)V
	astore_1
	aload_1
	getfield Outer/inners [LInner;
	iconst_1
	aaload
	getfield Inner/value I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 17
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label2:
Label3:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
