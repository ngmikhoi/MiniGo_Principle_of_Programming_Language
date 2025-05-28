.source Person.java
.class public  Person
.super java/lang/Object
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
