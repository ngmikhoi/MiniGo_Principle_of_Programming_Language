.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
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
.var 3 is j I from Label9 to Label10
	iconst_0
	istore_3
	iconst_0
	istore_3
Label13:
	iload_3
	iconst_3
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
Label16:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_4
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label19
Label22:
	goto Label12
Label23:
	goto Label18
Label19:
Label18:
Label17:
Label11:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label13
Label12:
	iload_1
	iconst_4
	if_icmpne Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label25
Label28:
	goto Label5
Label29:
	goto Label24
Label25:
Label24:
Label10:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
	iload_1
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 4
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
