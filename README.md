# MiniGo Compiler
This project is part of the *Principles of Programming Languages (CO3005)* course at *Ho Chi Minh University of Technology*.
## Overview
MiniGo is a simplified version of the Go programming language, designed for students to practice compiler development. It retains the core concepts of Go, such as basic data types, structs, and interfaces, while omitting more complex features like goroutines, channels, and the extensive standard library. The goal of MiniGo is to provide a manageable subset of Go that allows students to focus on fundamental concepts of programming language implementation, including:

- Lexical Analysis
- Parsing
- Semantic Checking
- Code Generation

By working with MiniGo, students gain hands-on experience in implementing a programming language, helping them understand the underlying principles of language design and compiler construction.

## Features
- **Statically Typed:** Supports primitive types (int, float, boolean, string) and composite types (struct, interface, array).
- **Control Structures:** Includes if-else statements and for loops with different forms (basic condition, initialization, and range-based iteration).
- **Functions & Methods:** Supports function and method declarations with optional return types.
- **Operators:** Arithmetic, relational, and logical operators for basic computations.
- **Built-in Functions:** Provides essential I/O functions.

## MiniGo Syntax Overview
### Variable Declaration
```go
var x int = 10;
var y = "Hello";
```
### Constant Declaration
```go
const Pi = 3.14;
```
### Function Definition
```go
func Add(x int, y int) int {
    return x + y;
}
```
### Struct Definition
```go
type Person struct {
    name string;
    age int;
}
```
### Control Flow
```go
if (x > 10) {
    putStringLn("x is greater than 10");
} else {
    putStringLn("x is 10 or less");
}
```
```go
for i := 0; i < 10; i += 1 {
    putIntLn(i);
}
```

## How to Run
- Change current directory to assigment_1/src, assigment_2/src, assigment_3/src, assigment_4/src where there is file run.py
- Type: python run.py gen

assigment_1/src type: python run.py test LexerSuite
assigment_1/src type: python run.py test ParserSuite
assigment_2/src type: python run.py test ASTGenSuite
assigment_3/src type: python run.py test CheckSuite
assigment_4/src type: python run.py test CodeGenSuite
