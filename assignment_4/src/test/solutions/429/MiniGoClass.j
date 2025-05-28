.source MiniGoClass.java
.class public  MiniGoClass
.super java/lang/Object

.method public static update(LBox;)V
Label0:
.var 0 is b LBox; from Label0 to Label1
Label2:
	aload_0
	bipush 100
	putfield Box/value I
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is b LBox; from Label2 to Label3
	new Box
	dup
	bipush 50
	invokespecial Box/<init>(I)V
	astore_1
	aload_1
	invokestatic MiniGoClass/update(LBox;)V
	aload_1
	getfield Box/value I
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
