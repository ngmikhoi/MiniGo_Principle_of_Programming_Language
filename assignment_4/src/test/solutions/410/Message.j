.source Message.java
.class public  Message
.super java/lang/Object
.implements Printer
.field public text Ljava/lang/String;

.method public <init>(Ljava/lang/String;)V
.var 0 is this LMessage; from Label0 to Label1
.var 1 is param_text Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	aload_1
	putfield Message/text Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMessage; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public print()V
.var 0 is this LMessage; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Message/text Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
