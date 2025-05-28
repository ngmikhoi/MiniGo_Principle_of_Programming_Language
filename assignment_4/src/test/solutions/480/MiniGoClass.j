.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object
.field static x Z

.method public static foo()Z
Label0:
Label2:
	ldc "Not shortcut!"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/x Z
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static boo()Z
Label0:
Label2:
	ldc "Is shortcut!"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 0
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
	invokestatic MiniGoClass/boo()Z
	ifgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifeq Label7
	invokestatic MiniGoClass/foo()Z
	ifne Label6
	goto Label7
Label6:
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	putstatic MiniGoClass/x Z
Label3:
Label11:
Label12:
Label1:
	return
.limit stack 6
.limit locals 0
.end method
