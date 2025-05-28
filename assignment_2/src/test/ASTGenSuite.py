import unittest
from TestUtils import TestAST
from AST import *
# 2252377 - Nguyen Minh Khoi
class ASTGenSuite(unittest.TestCase):      
    def test_301(self):
        input = """
            func sum(a int, b int) int {
                return a + b;
            }
        """
        expect = Program([
            FuncDecl("sum", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 301))
    
    def test_302(self):
        input = """
            const pi = 3.1415;
        """
        expect = Program([
            ConstDecl("pi", None, FloatLiteral(3.1415))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 302))
    
    def test_303(self):
        input = """
            func compare(x, y int) boolean {
                return x > y;
            }
        """
        expect = Program([
            FuncDecl("compare", [ParamDecl("x", IntType()), ParamDecl("y", IntType())], BoolType(), Block([
                Return(BinaryOp(">", Id("x"), Id("y")))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 303))
    
    def test_304(self):
        input = """
            type Book struct {
                title string;
                pages int;
            }
        """
        expect = Program([
            StructType("Book", [("title", StringType()), ("pages", IntType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 304))
    
    def test_305(self):
        input = """
            func (Car c) drive() {
                print("Driving");
            }
        """
        expect = Program([
            MethodDecl("Car", Id("c"), FuncDecl("drive", [], VoidType(), Block([
                FuncCall("print", [StringLiteral('"Driving"')])
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 305))

    def test_306(self):
        input = """
            func loop() {
                for i := 0; i < 10; i += 1 {
                    print(i);
                }
            }
        """
        expect = Program([
            FuncDecl("loop", [], VoidType(), Block([
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),
                    BinaryOp("<", Id("i"), IntLiteral(10)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([FuncCall("print", [Id("i")])])
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 306))
    
    def test_307(self):
        input = """
            var arr [5]int = [5]int{1, 2, 3, 4, 5};
        """
        expect = Program([
            VarDecl("arr", ArrayType([IntLiteral(5)], IntType()),
                    ArrayLiteral([IntLiteral(5)], IntType(),
                                 [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 307))
    
    def test_308(self):
        input = """
            func factorial(n int) int {
                if (n == 0) {
                    return 1;
                } else {
                    return n * factorial(n - 1);
                }
            }
        """
        expect = Program([
            FuncDecl("factorial", [ParamDecl("n", IntType())], IntType(), Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)),
                   Block([Return(IntLiteral(1))]),
                   Block([Return(BinaryOp("*", Id("n"), FuncCall("factorial", [BinaryOp("-", Id("n"), IntLiteral(1))])))])
                   )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 308))

    def test_309(self):
        input = """
            const isTrue = !false;
        """
        expect = Program([
            ConstDecl("isTrue", None, UnaryOp("!", BooleanLiteral(False)))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 309))
    
    def test_310(self):
        input = """
            func (Rectangle r) area() float {
                return r.width * r.height;
            }
        """
        expect = Program([
            MethodDecl("Rectangle", Id("r"), FuncDecl("area", [], FloatType(), Block([
                Return(BinaryOp("*", FieldAccess(Id("r"), "width"), FieldAccess(Id("r"), "height")))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 310))
        
    def test_311(self):
        input = """
            func max(a int, b int) int {
                if (a > b) {
                    return a;
                } else {
                    return b;
                }
            }
        """
        expect = Program([
            FuncDecl("max", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                If(BinaryOp(">", Id("a"), Id("b")),
                   Block([Return(Id("a"))]),
                   Block([Return(Id("b"))])
                   )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 311))
        
    def test_312(self):
        input = """
            const flag = true || false;
        """
        expect = Program([
            ConstDecl("flag", None, BinaryOp("||", BooleanLiteral(True), BooleanLiteral(False)))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 312))
        
    def test_313(self):
        input = """
            func min(a int, b int) int {
                if (a < b) {
                    return a;
                } else {
                    return b;
                }
            }
        """
        expect = Program([
            FuncDecl("min", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                If(BinaryOp("<", Id("a"), Id("b")),
                   Block([Return(Id("a"))]),
                   Block([Return(Id("b"))])
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 313))
    
    def test_314(self):
        input = """
            const threshold = 100;
        """
        expect = Program([
            ConstDecl("threshold", None, IntLiteral(100))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 314))
    
    def test_315(self):
        input = """
            func checkEven(n int) boolean {
                return n % 2 == 0;
            }
        """
        expect = Program([
            FuncDecl("checkEven", [ParamDecl("n", IntType())], BoolType(), Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 315))
    
    def test_316(self):
        input = """
            type Point struct {
                x float;
                y float;
            }
        """
        expect = Program([
            StructType("Point", [("x", FloatType()), ("y", FloatType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 316))
    
    def test_317(self):
        input = """
            func (Point p) distance() float {
                return p.x * p.x + p.y * p.y;
            }
        """
        expect = Program([
            MethodDecl("Point", Id("p"), FuncDecl("distance", [], FloatType(), Block([
                Return(BinaryOp("+", BinaryOp("*", FieldAccess(Id("p"), "x"), FieldAccess(Id("p"), "x")),
                                BinaryOp("*", FieldAccess(Id("p"), "y"), FieldAccess(Id("p"), "y"))))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 317))
    
    def test_318(self):
        input = """
            func factorialLoop(n int) int {
                var result = 1;
                for i := 1; i <= n; i += 1 {
                    result *= i;
                }
                return result;
            }
        """
        expect = Program([
            FuncDecl("factorialLoop", [ParamDecl("n", IntType())], IntType(), Block([
                VarDecl("result", None, IntLiteral(1)),
                ForStep(
                    Assign(Id("i"), IntLiteral(1)),
                    BinaryOp("<=", Id("i"), Id("n")),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([Assign(Id("result"), BinaryOp("*", Id("result"), Id("i")))])
                ),
                Return(Id("result"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 318))
    
    def test_319(self):
        input = """
            func compute(a int, b int) int {
                return (a + (b * (a / b) - a) % b) + 5;
            }
        """
        expect = Program([
            FuncDecl("compute",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([
                Return(BinaryOp("+", BinaryOp("+", Id("a"), BinaryOp("%", BinaryOp("-", BinaryOp("*", Id("b"), BinaryOp("/", Id("a"), Id("b"))), Id("a")), Id("b"))), IntLiteral(5)))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 319))
    
    def test_320(self):
        input = """
            func greet(name string) string {
                return "Hello, " + name;
            }
        """
        expect = Program([
            FuncDecl("greet", [ParamDecl("name", StringType())], StringType(), Block([
                Return(BinaryOp("+", StringLiteral('"Hello, "'), Id("name")))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 320))
        

    def test_321(self):
        input = """
            func multiply(a int, b int) int {
                return a * b;
            }
        """
        expect = Program([
            FuncDecl("multiply", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                Return(BinaryOp("*", Id("a"), Id("b")))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 321))
    
    def test_322(self):
        input = """
            const gravity = 9.81;
        """
        expect = Program([
            ConstDecl("gravity", None, FloatLiteral(9.81))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 322))
    
    def test_32(self):
        input = """const p = Person{ name: \"Alice\", age: 30 };"""
        expect = Program([
            ConstDecl("p",None,StructLiteral("Person",[("name",StringLiteral('"Alice"')),("age",IntLiteral(30))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 323))
        
    def test_324(self):
        input = """
            type Circle struct {
                radius float;
            }
        """
        expect = Program([
            StructType("Circle", [("radius", FloatType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 324))
    
    def test_325(self):
        input = """
            func (Circle c) circumference() float {
                return 2 * 3.1415 * c.radius;
            }
        """
        expect = Program([
            MethodDecl("Circle", Id("c"), FuncDecl("circumference", [], FloatType(), Block([
                Return(BinaryOp("*", BinaryOp("*", IntLiteral(2), FloatLiteral(3.1415)), FieldAccess(Id("c"), "radius")))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 325))
    
    def test_326(self):
        input = """
            func fibonacci(n int) int {
                if (n <= 1) {
                    return n;
                } else {
                    return fibonacci(n - 1) + fibonacci(n - 2);
                }
            }
        """
        expect = Program([
            FuncDecl("fibonacci", [ParamDecl("n", IntType())], IntType(), Block([
                If(BinaryOp("<=", Id("n"), IntLiteral(1)),
                   Block([Return(Id("n"))]),
                   Block([Return(BinaryOp("+", FuncCall("fibonacci", [BinaryOp("-", Id("n"), IntLiteral(1))]),
                                           FuncCall("fibonacci", [BinaryOp("-", Id("n"), IntLiteral(2))])))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 326))
    
    def test_327(self):
        input = """
            func power(base int, exp int) int {
                var result = 1;
                for i := 0; i < exp; i += 1 {
                    result *= base;
                }
                return result;
            }
        """
        expect = Program([
            FuncDecl("power", [ParamDecl("base", IntType()), ParamDecl("exp", IntType())], IntType(), Block([
                VarDecl("result", None, IntLiteral(1)),
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),
                    BinaryOp("<", Id("i"), Id("exp")),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([Assign(Id("result"), BinaryOp("*", Id("result"), Id("base")))])
                ),
                Return(Id("result"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 327))
    
    def test_328(self):
        input = """
            func factorial(n int) int {
                if (n == 0) { return 1; }
                return n * factorial(n - 1);
            }
        """
        expect = Program([
            FuncDecl("factorial",[ParamDecl("n",IntType())],IntType(),Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([
                    Return(IntLiteral(1))
                ]), None),
                Return(BinaryOp("*", Id("n"), FuncCall("factorial",[BinaryOp("-", Id("n"), IntLiteral(1))])))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 328))
    
    def test_329(self):
        input = """
            func isEven(n int) bool {
                if (n == 0) { return true; }
                return isOdd(n - 1);
            }
        """
        expect = Program([
            FuncDecl("isEven",[ParamDecl("n",IntType())],Id("bool"),Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([
                    Return(BooleanLiteral(True))
                ]), None),
                Return(FuncCall("isOdd",[BinaryOp("-", Id("n"), IntLiteral(1))]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 329))
    
    def test_330(self):
        input = """
            func greetUser(name string) string {
                return "Hello, " + name + "!";
            }
        """
        expect = Program([
            FuncDecl("greetUser", [ParamDecl("name", StringType())], StringType(), Block([
                Return(BinaryOp("+", BinaryOp("+", StringLiteral('"Hello, "'), Id("name")), StringLiteral('"!"')))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 330))

    def test_331(self):
        input = """
            func divide(a int, b int) int {
                return a / b;
            }
        """
        expect = Program([
            FuncDecl("divide", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                Return(BinaryOp("/", Id("a"), Id("b")))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 331))
    
    def test_332(self):
        input = """
            const speedOfLight = 299792458;
        """
        expect = Program([
            ConstDecl("speedOfLight", None, IntLiteral(299792458))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 332))
    
    def test_333(self):
        input = """
            func inner() { 
                return
            } 
            
            func outer() {
                hehehe()
                hahaha()
                huhuhu()
            }
        """
        expect = Program([
            FuncDecl("inner",[],VoidType(),Block([
                Return(None)
            ])),
			FuncDecl("outer",[],VoidType(),Block([
                FuncCall("hehehe",[]),
                FuncCall("hahaha",[]),
                FuncCall("huhuhu",[])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 333))
    
    def test_334(self):
        input = """
            type Triangle struct {
                base float;
                height float;
            }
        """
        expect = Program([
            StructType("Triangle", [("base", FloatType()), ("height", FloatType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 334))
    
    def test_335(self):
        input = """
            func (Triangle t) area() float {
                return 0.5 * t.base * t.height;
            }
        """
        expect = Program([
            MethodDecl("Triangle", Id("t"), FuncDecl("area", [], FloatType(), Block([
                Return(BinaryOp("*", BinaryOp("*", FloatLiteral(0.5), FieldAccess(Id("t"), "base")), FieldAccess(Id("t"), "height")))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 335))
    
    def test_336(self):
        input = """
            func sumArray(arr [10]int) int {
                var total = 0;
                for i := 0; i < 10; i += 1 {
                    total += arr[i];
                }
                return total;
            }
        """
        expect = Program([
            FuncDecl("sumArray", [ParamDecl("arr", ArrayType([IntLiteral(10)], IntType()))], IntType(), Block([
                VarDecl("total", None, IntLiteral(0)),
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),
                    BinaryOp("<", Id("i"), IntLiteral(10)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([Assign(Id("total"), BinaryOp("+", Id("total"), ArrayCell(Id("arr"), [Id("i")])))])),
                Return(Id("total"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 336))
    
    def test_337(self):
        input = """
            func loop() {
                for true { 
                    print("Running"); 
                    break; 
                }
            }
        """
        expect = Program([
            FuncDecl("loop",[],VoidType(),Block([
                ForBasic(BooleanLiteral(True),Block([
                    FuncCall("print",[StringLiteral('"Running"')]),
                    Break()
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 337))
    
    def test_338(self):
        input = """
            func checkDepth(n int) {
                if (n > 0) { 
                    if (n > 1) { 
                        if (n > 2) { 
                            if (n > 3) { 
                                print("larger than 3")
                                return; 
                            } 
                            print("larger than 2")
                        } 
                        print("larger than 1")
                    } 
                    print("larger than 0")
                }
            }
        """
        expect = Program([
            FuncDecl("checkDepth",[ParamDecl("n",IntType())],VoidType(),Block([
                If(BinaryOp(">", Id("n"), IntLiteral(0)), Block([
                    If(BinaryOp(">", Id("n"), IntLiteral(1)), Block([
                        If(BinaryOp(">", Id("n"), IntLiteral(2)), Block([
                            If(BinaryOp(">", Id("n"), IntLiteral(3)), Block([
                                FuncCall("print",[StringLiteral('"larger than 3"')]),
                                Return(None)
                            ]), None),
                            FuncCall("print",[StringLiteral('"larger than 2"')])
                        ]), None),
                        FuncCall("print",[StringLiteral('"larger than 1"')])
                    ]), None),
                    FuncCall("print",[StringLiteral('"larger than 0"')])
                ]), None)
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 338))
    
    def test_339(self):
        input = """
            func loop() {
                for false { 
                    print("Running"); 
                    break; 
                }
            }
        """
        expect = Program([
            FuncDecl("loop",[],VoidType(),Block([
                ForBasic(BooleanLiteral(False),Block([
                    FuncCall("print",[StringLiteral('"Running"')]),
                    Break()
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 339))
        
    def test_340(self):
        input = """
            func test() {
                for i := 0; i < 5; i += 1 {
                    for j := 0; j < 3; j += 1 {
                        for k := 0; k < 2; k += 1 {
                            print(i, j, k);
                        }
                    }
                }
            }
        """
        expect = Program([
            FuncDecl("test",[],VoidType(),Block([
                ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(5)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([
                    ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<", Id("j"), IntLiteral(3)),Assign(Id("j"),BinaryOp("+", Id("j"), IntLiteral(1))),Block([
                        ForStep(Assign(Id("k"),IntLiteral(0)),BinaryOp("<", Id("k"), IntLiteral(2)),Assign(Id("k"),BinaryOp("+", Id("k"), IntLiteral(1))),Block([
                            FuncCall("print",[Id("i"),Id("j"),Id("k")])
                        ]))
                    ]))
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 340))
        
    def test_341(self):
        input = """
            func mod(a int, b int) int {
                return a % b;
            }
        """
        expect = Program([
            FuncDecl("mod", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                Return(BinaryOp("%", Id("a"), Id("b")))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 341))
    
    def test_342(self):
        input = """
            const piApprox = 3.14;
        """
        expect = Program([
            ConstDecl("piApprox", None, FloatLiteral(3.14))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 342))
    
    def test_343(self):
        input = """
            func kool(x int, y int) int { 
                return x + y; 
            };
        """
        expect = Program([
            FuncDecl("kool",[ParamDecl("x",IntType()),ParamDecl("y",IntType())],IntType(),Block([
                Return(BinaryOp("+", Id("x"), Id("y")))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 343))
    
    def test_344(self):
        input = """
            type Rectangle struct {
                width float;
                height float;
            }
        """
        expect = Program([
            StructType("Rectangle", [("width", FloatType()), ("height", FloatType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 344))
    
    def test_345(self):
        input = """
            func (Rectangle r) perimeter() float {
                return 2 * (r.width + r.height);
            }
        """
        expect = Program([
            MethodDecl("Rectangle", Id("r"), FuncDecl("perimeter", [], FloatType(), Block([
                Return(BinaryOp("*", IntLiteral(2), BinaryOp("+", FieldAccess(Id("r"), "width"), FieldAccess(Id("r"), "height"))))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 345))
    
    def test_346(self):
        input = """
            func kool() {
                a += 1;
                b -= 2
                c *= 3
            }
        """
        expect = Program([
            FuncDecl("kool",[],VoidType(),Block([
                Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),
                Assign(Id("b"),BinaryOp("-", Id("b"), IntLiteral(2))),
                Assign(Id("c"),BinaryOp("*", Id("c"), IntLiteral(3)))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 346))
    
    def test_347(self):
        input = """
            func concatenateStrings(a string, b string) string {
                return a + b;
            }
        """
        expect = Program([
            FuncDecl("concatenateStrings", [ParamDecl("a", StringType()), ParamDecl("b", StringType())], StringType(), Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 347))
    
    def test_348(self):
        input = """
            func kool() {
                a += 1;
            }
        """
        expect = Program([
            FuncDecl("kool",[],VoidType(),Block([
                Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1)))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 348))
    
    def test_349(self):
        input = """
            func kool() {
                break;
                continue;
            }
        """
        expect = Program([
            FuncDecl("kool",[],VoidType(),Block([
                Break(),
                Continue()
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 349))
        
    def test_350(self):
        input = """
            func getValue() string { 
                return "string"; 
            }
        """
        expect = Program([
            FuncDecl("getValue",[],StringType(),Block([
                Return(StringLiteral('"string"'))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 350))
         
    def test_351(self):
        input = """
            func factorialIter(n int) int {
                var result = 1;
                for n > 1 {
                    result *= n;
                    n -= 1;
                }
                return result;
            }
        """
        expect = Program([
            FuncDecl("factorialIter", [ParamDecl("n", IntType())], IntType(), Block([
                VarDecl("result", None, IntLiteral(1)),
                ForBasic(BinaryOp(">", Id("n"), IntLiteral(1)), Block([
                    Assign(Id("result"), BinaryOp("*", Id("result"), Id("n"))),
                    Assign(Id("n"), BinaryOp("-", Id("n"), IntLiteral(1)))
                ])),
                Return(Id("result"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 351))
    
    def test_352(self):
        input = """
            const goldenRatio = 1.618;
        """
        expect = Program([
            ConstDecl("goldenRatio", None, FloatLiteral(1.618))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 352))
    
    def test_353(self):
        input = """const QuangPhu = foo( a(),b.a(2, 3) ); """
        expect = Program([
            ConstDecl("QuangPhu",None,FuncCall("foo",[FuncCall("a",[]),MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 353))
    
    def test_354(self):
        input = """
            type Person struct {
                name string;
                age int;
            }
        """
        expect = Program([
            StructType("Person", [("name", StringType()), ("age", IntType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 354))
    
    def test_355(self):
        input = """
            func (Person p) getAge() int {
                return p.age;
            }
        """
        expect = Program([
            MethodDecl("Person", Id("p"), FuncDecl("getAge", [], IntType(), Block([
                Return(FieldAccess(Id("p"), "age"))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 355))
    
    def test_356(self):
        input = """
            func sumDigits(n int) int {
                var sum = 0;
                for n > 0 {
                    sum += n % 10;
                    n /= 10;
                }
                return sum;
            }
        """
        expect = Program([
            FuncDecl("sumDigits", [ParamDecl("n", IntType())], IntType(), Block([
                VarDecl("sum", None, IntLiteral(0)),
                ForBasic(BinaryOp(">", Id("n"), IntLiteral(0)), Block([
                    Assign(Id("sum"), BinaryOp("+", Id("sum"), BinaryOp("%", Id("n"), IntLiteral(10)))),
                    Assign(Id("n"), BinaryOp("/", Id("n"), IntLiteral(10)))
                ])),
                Return(Id("sum"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 356))
    
    def test_357(self):
        input = """
            func getPeople() [2]Person {
                return [2]Person{Person{name: "Alice"}, Person{name: "Bob"}};
            }
        """
        expect = Program([
            FuncDecl("getPeople",[],ArrayType([IntLiteral(2)],Id("Person")),Block([
                Return(ArrayLiteral([IntLiteral(2)],Id("Person"),[StructLiteral("Person",[("name",StringLiteral('"Alice"'))]),StructLiteral("Person",[("name",StringLiteral('"Bob"'))])]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 357))
    
    def test_358(self):
        input = """
            func sumRange(start int, end int) int {
                var total = 0;
                for i := start; i <= end; i += 1 {
                    total += i;
                }
                return total;
            }
        """
        expect = Program([
            FuncDecl("sumRange", [ParamDecl("start", IntType()), ParamDecl("end", IntType())], IntType(), Block([
                VarDecl("total", None, IntLiteral(0)),
                ForStep(
                    Assign(Id("i"), Id("start")),
                    BinaryOp("<=", Id("i"), Id("end")),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        Assign(Id("total"), BinaryOp("+", Id("total"), Id("i")))
                    ])
                ),
                Return(Id("total"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 358))
        
    def test_359(self):
        input = """
                func getValueDouble(num int) int { 
                    return num*2; 
                }
                """
        expect = Program([
            FuncDecl("getValueDouble",[ParamDecl("num",IntType())],IntType(),Block([
                Return(BinaryOp("*", Id("num"), IntLiteral(2)))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 359))

    def test_360(self):
        input = """
                func main() { 
                    greet(); 
                }
                """
        expect = Program([
            FuncDecl("main",[],VoidType(),Block([
                FuncCall("greet",[])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 360))
        
    def test_361(self):
        input = """
            func square(n int) int {
                return n * n;
            }
        """
        expect = Program([
            FuncDecl("square", [ParamDecl("n", IntType())], IntType(), Block([
                Return(BinaryOp("*", Id("n"), Id("n")))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 361))
    
    def test_362(self):
        input = """
            const avogadro = 6.022e+23;
        """
        expect = Program([
            ConstDecl("avogadro", None, FloatLiteral(6.022e+23))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 362))
    
    def test_363(self):
        input = """
            type Calculator struct {
                num1 int 
                num2 int
                op string 
                
            }
        """
        expect = Program([
            StructType("Calculator",[
                ("num1",IntType()),
                ("num2",IntType()),
                ("op",StringType())
            ],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 363))
    
    def test_364(self):
        input = """
            type Car struct {
                brand string;
                year int;
            }
        """
        expect = Program([
            StructType("Car", [("brand", StringType()), ("year", IntType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 364))
    
    def test_365(self):
        input = """
            func (Car c) getBrand() string {
                return c.brand;
            }
        """
        expect = Program([
            MethodDecl("Car", Id("c"), FuncDecl("getBrand", [], StringType(), Block([
                Return(FieldAccess(Id("c"), "brand"))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 365))
    
    def test_366(self):
        input = """
            func sumSquares(n int) int {
                var sum = 0;
                for i := 1; i <= n; i += 1 {
                    sum += i * i;
                }
                return sum;
            }
        """
        expect = Program([
            FuncDecl("sumSquares", [ParamDecl("n", IntType())], IntType(), Block([
                VarDecl("sum", None, IntLiteral(0)),
                ForStep(
                    Assign(Id("i"), IntLiteral(1)),
                    BinaryOp("<=", Id("i"), Id("n")),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        Assign(Id("sum"), BinaryOp("+", Id("sum"), BinaryOp("*", Id("i"), Id("i"))))
                    ])
                ),
                Return(Id("sum"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 366))
    
    def test_367(self):
        input = """
            func joinStrings(a string, b string, sep string) string {
                return a + sep + b;
            }
        """
        expect = Program([
            FuncDecl("joinStrings", [ParamDecl("a", StringType()), ParamDecl("b", StringType()), ParamDecl("sep", StringType())], StringType(), Block([
                Return(BinaryOp("+", BinaryOp("+", Id("a"), Id("sep")), Id("b")))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 367))
    
    def test_368(self):
        input = """
            type Team struct {
                members [5]Person;
            }
        """
        expect = Program([
            StructType("Team",[
                ("members",ArrayType([IntLiteral(5)],Id("Person")))
            ],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 368))
        
    def test_369(self):
        input = """
            type kool interface {
                Add() [2]string;
                Add() ID;
            }
            """
        expect = Program([InterfaceType("kool",[Prototype("Add",[],ArrayType([IntLiteral(2)],StringType())),Prototype("Add",[],Id("ID"))])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 369))

    def test_370(self):
        input = """
            type kool interface {
                Add();
            }
        """
        expect = Program([InterfaceType("kool",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 370))
        

    def test_371(self):
        input = """
            func cube(n int) int {
                return n * n * n;
            }
        """
        expect = Program([
            FuncDecl("cube", [ParamDecl("n", IntType())], IntType(), Block([
                Return(BinaryOp("*", BinaryOp("*", Id("n"), Id("n")), Id("n")))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 371))
    
    def test_372(self):
        input = """
            const planck = 6.626e-34;
        """
        expect = Program([
            ConstDecl("planck", None, FloatLiteral(6.626e-34))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 372))
    
    def test_373(self):
        input = """
            type Address struct {
                city string;
            }
            type Person struct {
                addr Address;
            }
            var cityName string = Person{}.addr.city;
        """
        expect = Program([
            StructType("Address",[
                ("city",StringType())
            ],[]),
			StructType("Person",[
                ("addr",Id("Address"))
            ],[]),
			VarDecl("cityName",StringType(),FieldAccess(FieldAccess(StructLiteral("Person",[]),"addr"),"city"))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 373))
    
    def test_374(self):
        input = """
            type Animal struct {
                species string;
                age int;
            }
        """
        expect = Program([
            StructType("Animal", [("species", StringType()), ("age", IntType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 374))
    
    def test_375(self):
        input = """
            func (Animal a) getSpecies() string {
                return a.species;
            }
        """
        expect = Program([
            MethodDecl("Animal", Id("a"), FuncDecl("getSpecies", [], StringType(), Block([
                Return(FieldAccess(Id("a"), "species"))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 375))
    
    def test_376(self):
        input = """
            func sumOfCubes(n int) int {
                var sum = 0;
                for i := 1; i <= n; i += 1 {
                    sum += i * i * i;
                }
                return sum;
            }
        """
        expect = Program([
            FuncDecl("sumOfCubes", [ParamDecl("n", IntType())], IntType(), Block([
                VarDecl("sum", None, IntLiteral(0)),
                ForStep(
                    Assign(Id("i"), IntLiteral(1)),
                    BinaryOp("<=", Id("i"), Id("n")),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        Assign(Id("sum"), BinaryOp("+", Id("sum"), BinaryOp("*", BinaryOp("*", Id("i"), Id("i")), Id("i"))))
                    ])
                ),
                Return(Id("sum"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 376))
    
    def test_377(self):
        input = """
            func broken() {
                var x int = 10;
            }
        """
        expect = Program([
            FuncDecl("broken",[],VoidType(),Block([
                VarDecl("x",IntType(),IntLiteral(10))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 377))
    
    def test_378(self):
        input = """
            func stringLength(s string) int {
                return len(s);
            }
        """
        expect = Program([
            FuncDecl("stringLength", [ParamDecl("s", StringType())], IntType(), Block([
                Return(FuncCall("len", [Id("s")]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 378))
    
    def test_379(self):
        input = """
            const result = a * 5 + 3;
        """
        expect = Program([
            ConstDecl("result",None,BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(5)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 379))
    
    def test_380(self):
        input = """
            func foo(a,b,c,d [ID][2][c] ID ){return;}
        """
        expect = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("b",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("c",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("d",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 380))
        
    def test_381(self):
        input = """
            func sayHello() { return "Hello"; }
        """
        expect = Program([
            FuncDecl("sayHello",[],VoidType(),Block([
                Return(StringLiteral('"Hello"'))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 381))
    
    def test_382(self):
        input = """
            const eulersNumber = 2.718;
        """
        expect = Program([
            ConstDecl("eulersNumber", None, FloatLiteral(2.718))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 382))
    
    def test_383(self):
        input = """
            func deepNest() {
                if (a > b) {
                    if (b > c) {
                        if (c > d) {
                            if (d > e) {
                                if (e > f) {
                                    if (f > g) {
                                        if (g > h) {
                                            if (h > i) {
                                                if (i > j) {
                                                    print("Too deep!");
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        """
        expect = Program([
            FuncDecl("deepNest",[],VoidType(),Block([
                If(BinaryOp(">", Id("a"), Id("b")), Block([
                    If(BinaryOp(">", Id("b"), Id("c")), Block([
                        If(BinaryOp(">", Id("c"), Id("d")), Block([
                            If(BinaryOp(">", Id("d"), Id("e")), Block([
                                If(BinaryOp(">", Id("e"), Id("f")), Block([
                                    If(BinaryOp(">", Id("f"), Id("g")), Block([
                                        If(BinaryOp(">", Id("g"), Id("h")), Block([
                                            If(BinaryOp(">", Id("h"), Id("i")), Block([
                                                If(BinaryOp(">", Id("i"), Id("j")), Block([
                                                    FuncCall("print",[StringLiteral('"Too deep!"')])
                                                ]), None)
                                            ]), None)
                                        ]), None)
                                    ]), None)
                                ]), None)
                            ]), None)
                        ]), None)
                    ]), None)
                ]), None)
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 383))
    
    def test_384(self):
        input = """
            type Student struct {
                name string;
                gpa float;
            }
        """
        expect = Program([
            StructType("Student", [("name", StringType()), ("gpa", FloatType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 384))
    
    def test_385(self):
        input = """
            func (Student s) getGPA() float {
                return s.gpa;
            }
        """
        expect = Program([
            MethodDecl("Student", Id("s"), FuncDecl("getGPA", [], FloatType(), Block([
                Return(FieldAccess(Id("s"), "gpa"))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 385))
        
    def test_386(self):
        input = """
            func infiniteRecursion() {
                infiniteRecursion();
            }
        """
        expect = Program([
            FuncDecl("infiniteRecursion",[],VoidType(),Block([
                FuncCall("infiniteRecursion",[])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 386))
    
    def test_387(self):
        input = """
            func sumFirstN(n int) int {
                return (n * (n + 1)) / 2;
            }
        """
        expect = Program([
            FuncDecl("sumFirstN", [ParamDecl("n", IntType())], IntType(), Block([
                Return(BinaryOp("/", BinaryOp("*", Id("n"), BinaryOp("+", Id("n"), IntLiteral(1))), IntLiteral(2)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 387))
    
    def test_388(self):
        input = """
            const x = 10
            const y = 20;
        """
        expect = Program([
            ConstDecl("x",None,IntLiteral(10)),
			ConstDecl("y",None,IntLiteral(20))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 388))
    
    def test_389(self):
        input = """
                const value = (a + b) * (c - d) / e
                """
        expect = Program([
            ConstDecl("value",None,BinaryOp("/", BinaryOp("*", BinaryOp("+", Id("a"), Id("b")), BinaryOp("-", Id("c"), Id("d"))), Id("e")))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 389))
    
    def test_390(self):
        input = """
            func kool() {
                for index, value := range array[2] {return;}
            }
        """
        expect = Program([
            FuncDecl("kool",[],VoidType(),Block([
                ForEach(Id("index"),Id("value"),ArrayCell(Id("array"),[IntLiteral(2)]),Block([
                    Return(None)
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 390))
        
    def test_391(self):
        input = """
            func sumFirstNNumbers(n int) int {
                var sum = 0;
                for i := 1; i <= n; i += 1 {
                    sum += i;
                }
                return sum;
            }
        """
        expect = Program([
            FuncDecl("sumFirstNNumbers", [ParamDecl("n", IntType())], IntType(), Block([
                VarDecl("sum", None, IntLiteral(0)),
                ForStep(
                    Assign(Id("i"), IntLiteral(1)),
                    BinaryOp("<=", Id("i"), Id("n")),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i")))
                    ])
                ),
                Return(Id("sum"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 391))

    def test_392(self):
        input = """
            const a = 1 && 2 || 3;
        """
        expect = Program([
            ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 392))

    def test_393(self):
        input = """
            const a = ID{a: [1]int{1}};
        """
        expect = Program([
            ConstDecl("a",None,StructLiteral("ID",[("a",ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 393))    
    
    def test_394(self):
        input = """
            const a = a[1 + 2];
        """
        expect = Program([
            ConstDecl("a",None,ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 394))
        
    def test_395(self):
        input = """
            func productOfArray(arr [5]int) int {
                var product = 1;
                for i := 0; i < 5; i += 1 {
                    product *= arr[i];
                }
                return product;
            }
        """
        expect = Program([
            FuncDecl("productOfArray", [ParamDecl("arr", ArrayType([IntLiteral(5)], IntType()))], IntType(), Block([
                VarDecl("product", None, IntLiteral(1)),
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),
                    BinaryOp("<", Id("i"), IntLiteral(5)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        Assign(Id("product"), BinaryOp("*", Id("product"), ArrayCell(Id("arr"), [Id("i")])))
                    ])
                ),
                Return(Id("product"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 395))
    
    def test_396(self):
        input = """
            func factorialLoop(n int) int {
                var result = 1;
                for i := 2; i <= n; i += 1 {
                    result *= i;
                }
                return result;
            }
        """
        expect = Program([
            FuncDecl("factorialLoop", [ParamDecl("n", IntType())], IntType(), Block([
                VarDecl("result", None, IntLiteral(1)),
                ForStep(
                    Assign(Id("i"), IntLiteral(2)),
                    BinaryOp("<=", Id("i"), Id("n")),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        Assign(Id("result"), BinaryOp("*", Id("result"), Id("i")))
                    ])
                ),
                Return(Id("result"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 396))
    
    def test_397(self):
        input = """
            type Node struct {
                value int;
            }
        """
        expect = Program([
            StructType("Node",[
                ("value",IntType())
            ],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 397))
        
    def test_398(self):
        input = """
            func sumOddNumbers(n int) int {
                var sum = 0;
                for i := 1; i <= n; i += 2 {
                    sum += i;
                }
                return sum;
            }
        """
        expect = Program([
            FuncDecl("sumOddNumbers", [ParamDecl("n", IntType())], IntType(), Block([
                VarDecl("sum", None, IntLiteral(0)),
                ForStep(
                    Assign(Id("i"), IntLiteral(1)),
                    BinaryOp("<=", Id("i"), Id("n")),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(2))),
                    Block([
                        Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i")))
                    ])
                ),
                Return(Id("sum"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 398))
    
    def test_399(self):
        input = """
            func arraySum(arr [10]int) int {
                var total = 0;
                for i := 0; i < 10; i += 1 {
                    total += arr[i];
                }
                return total;
            }
        """
        expect = Program([
            FuncDecl("arraySum", [ParamDecl("arr", ArrayType([IntLiteral(10)], IntType()))], IntType(), Block([
                VarDecl("total", None, IntLiteral(0)),
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),
                    BinaryOp("<", Id("i"), IntLiteral(10)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        Assign(Id("total"), BinaryOp("+", Id("total"), ArrayCell(Id("arr"), [Id("i")])))
                    ])
                ),
                Return(Id("total"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 399))
    
    def test_400(self):
        input = """
            func isLeapYear(year int) boolean {
                return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
            }
        """
        expect = Program([
            FuncDecl("isLeapYear", [ParamDecl("year", IntType())], BoolType(), Block([
                Return(BinaryOp("||", 
                        BinaryOp("&&", BinaryOp("==", BinaryOp("%", Id("year"), IntLiteral(4)), IntLiteral(0)),
                                      BinaryOp("!=", BinaryOp("%", Id("year"), IntLiteral(100)), IntLiteral(0))),
                        BinaryOp("==", BinaryOp("%", Id("year"), IntLiteral(400)), IntLiteral(0))
                    ))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 400))