.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object
.field static pi F

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/pi F
	invokestatic io/putFloatLn(F)V
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
	ldc 3.14
	putstatic MiniGoClass/pi F
Label3:
Label4:
Label5:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
