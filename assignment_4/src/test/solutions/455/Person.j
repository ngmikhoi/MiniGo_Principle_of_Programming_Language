.source Person.java
.class public  Person
.super java/lang/Object
.implements Greeter
.field public name Ljava/lang/String;

.method public <init>(Ljava/lang/String;)V
.var 0 is this LPerson; from Label0 to Label1
.var 1 is param_name Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	aload_1
	putfield Person/name Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LPerson; from Label0 to Label1
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

.method public greet()Ljava/lang/String;
.var 0 is this LPerson; from Label0 to Label1
Label0:
Label2:
	ldc "Hi, "
	aload_0
	getfield Person/name Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	areturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method
