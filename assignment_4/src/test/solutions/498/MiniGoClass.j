.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object

.method public static sum([F)F
Label0:
.var 0 is arr [F from Label0 to Label1
Label2:
	aload_0
	iconst_0
	faload
	aload_0
	iconst_1
	faload
	fadd
	freturn
Label3:
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is arr [F from Label2 to Label3
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.5
	fastore
	dup
	iconst_1
	ldc 2.5
	fastore
	astore_1
	aload_1
	invokestatic MiniGoClass/sum([F)F
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 7
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
