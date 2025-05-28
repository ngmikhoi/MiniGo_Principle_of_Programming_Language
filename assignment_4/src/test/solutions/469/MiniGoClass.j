.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is h LHolder; from Label2 to Label3
	new Holder
	dup
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Alice"
	aastore
	dup
	iconst_1
	ldc "Bob"
	aastore
	invokespecial Holder/<init>([Ljava/lang/String;)V
	astore_1
	aload_1
	getfield Holder/names [Ljava/lang/String;
	iconst_1
	aaload
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 11
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
