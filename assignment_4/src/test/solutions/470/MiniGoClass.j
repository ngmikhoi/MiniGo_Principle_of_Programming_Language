.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object

.method public static getX(LPoint;)I
Label0:
.var 0 is p LPoint; from Label0 to Label1
Label2:
	aload_0
	getfield Point/x I
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is p LPoint; from Label2 to Label3
	new Point
	dup
	bipush 15
	invokespecial Point/<init>(I)V
	astore_1
	aload_1
	invokestatic MiniGoClass/getX(LPoint;)I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 6
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
