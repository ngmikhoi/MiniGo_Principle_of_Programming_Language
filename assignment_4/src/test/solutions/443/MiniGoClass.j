.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object

.method public static sum(I)I
Label0:
.var 0 is n I from Label0 to Label1
Label2:
	iload_0
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label8:
	iconst_0
	ireturn
Label9:
Label5:
Label4:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MiniGoClass/sum(I)I
	iadd
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
	iconst_3
	invokestatic MiniGoClass/sum(I)I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
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
