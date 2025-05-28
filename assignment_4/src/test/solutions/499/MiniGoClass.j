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
	ifne Label4
	invokestatic MiniGoClass/foo()Z
	ifne Label4
	goto Label5
Label4:
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	putstatic MiniGoClass/x Z
Label3:
Label7:
Label8:
Label1:
	return
.limit stack 4
.limit locals 0
.end method
