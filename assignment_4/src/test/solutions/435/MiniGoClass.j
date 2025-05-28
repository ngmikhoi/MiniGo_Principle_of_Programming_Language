.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is x I from Label2 to Label3
	iconst_5
	istore_1
	iload_1
	iconst_5
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifne Label10
	bipush 10
	iconst_0
	idiv
	iconst_1
	if_icmple Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifne Label10
	goto Label11
Label10:
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label5
Label17:
	ldc "Safe"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label18:
	goto Label4
Label5:
Label4:
Label3:
Label1:
	return
.limit stack 4
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
