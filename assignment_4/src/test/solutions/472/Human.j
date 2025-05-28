.source Human.java
.class public  Human
.super java/lang/Object
.implements Worker
.field public name Ljava/lang/String;

.method public <init>(Ljava/lang/String;)V
.var 0 is this LHuman; from Label0 to Label1
.var 1 is param_name Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	aload_1
	putfield Human/name Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LHuman; from Label0 to Label1
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

.method public work()Ljava/lang/String;
.var 0 is this LHuman; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Human/name Ljava/lang/String;
	areturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
