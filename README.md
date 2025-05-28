# MiniGo Compiler
This project is part of the *Principles of Programming Languages (CO3005)* course at *Ho Chi Minh University of Technology*.

## Overview
MiniGo is a simplified version of the Go programming language, designed for students to practice compiler development. It retains the core concepts of Go, such as basic data types, structs, and interfaces, while omitting more complex features like goroutines, channels, and the extensive standard library. The goal of MiniGo is to provide a manageable subset of Go that allows students to focus on fundamental concepts of programming language implementation, including:

- Lexer and Parser in assignemt 1 grade: 100/100 and 100/100
- Abstract Syntax Tree in assignemt 2 grade: 97/100
- Static Checker in assignemt 3 grade: 125/125
- Code Generator in assignemt 4 grade: 101/101

By working with MiniGo, students gain hands-on experience in implementing a programming language, helping them understand the underlying principles of language design and compiler construction.

## Features
- **Statically Typed:** Supports primitive types (int, float, boolean, string) and composite types (struct, interface, array).
- **Control Structures:** Includes if-else statements and for loops with different forms (basic condition, initialization, and range-based iteration).
- **Functions & Methods:** Supports function and method declarations with optional return types.
- **Operators:** Arithmetic, relational, and logical operators for basic computations.
- **Built-in Functions:** Provides essential I/O functions.

## How to Run
- Change current directory to assigment_1/src, assigment_2/src, assigment_3/src, assigment_4/src where there is file run.py type:
```python
python run.py gen
```

- Then:
  + assigment_1/src type: python run.py test LexerSuite
  + assigment_1/src type: python run.py test ParserSuite
  + assigment_2/src type: python run.py test ASTGenSuite
  + assigment_3/src type: python run.py test CheckSuite
  + assigment_4/src type: python run.py test CodeGenSuite
