.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object

.method public static process([LItem;)I
Label0:
.var 0 is items [LItem; from Label0 to Label1
Label2:
	aload_0
	iconst_1
	aaload
	getfield Item/id I
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is items [LItem; from Label2 to Label3
	iconst_2
	multianewarray [LItem; 1
	dup
	iconst_0
	new Item
	dup
	iconst_1
	invokespecial Item/<init>(I)V
	aastore
	dup
	iconst_1
	new Item
	dup
	iconst_2
	invokespecial Item/<init>(I)V
	aastore
	astore_1
	aload_1
	invokestatic MiniGoClass/process([LItem;)I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 13
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
