# 2252377 - Nguyen Minh Khoi
import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_401(self):
        input = """var a int = 1.2;"""
        self.assertTrue(TestChecker.test(input,"Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n",401))

    def test_402(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        self.assertTrue(TestChecker.test(input,"Undeclared Identifier: b\n",402))
        
    def test_403(self):
        input = """ 
            func Add(x int, y, a int, y string, b, c float) int {
                return x + y;
            }
        """
        expect = "Redeclared Parameter: y\n"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_404(self):
        """
        var bro = 1; 
        var bro = 2;
        """
        input = Program([VarDecl("bro", None,IntLiteral(1)),VarDecl("bro", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: bro\n", 404))

    def test_405(self):
        """
        var bro = 1; 
        const bro = 2;
        """
        input = Program([VarDecl("bro", None,IntLiteral(1)),ConstDecl("bro",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: bro\n", 405))

    def test_406(self):
        """
        const bro = 1; 
        var bro = 2;
        """
        input = Program([ConstDecl("bro",None,IntLiteral(1)),VarDecl("bro", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: bro\n", 406))

    def test_407(self):
        """
        const bro = 1; 
        func bro () {return;}
        """
        input = Program([ConstDecl("bro",None,IntLiteral(1)),FuncDecl("bro",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: bro\n", 407))

    def test_408(self):
        """ 
        func bro () {return;}
        var bro = 1;
        """
        input = Program([FuncDecl("bro",[],VoidType(),Block([Return(None)])),VarDecl("bro", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: bro\n", 408))

    def test_409(self):
        """ 
        var getInt = 1;
        """
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getInt\n", 409))

    def test_410(self):
        """ 
        type  bro struct {
            bro int;
        }
        type Broo struct {
            bro string;
            Broo int;
            Broo float;
        }
        """
        input = Program([StructType("bro",[("bro",IntType())],[]),StructType("Broo",[("bro",StringType()),("Broo",IntType()),("Broo",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: Broo\n", 410))

    def test_411(self):
        """ 
        func (v Broo) putIntLn () {return;}
        func (v Broo) getInt () {return;}
        func (v Broo) getInt () {return;}
        type Broo struct {
            bro int;
        }
        """
        input = Program([MethodDecl("v",Id("Broo"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("Broo"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("Broo"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))), StructType("Broo",[("bro",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt\n", 411))

    def test_412(self):
        """ 
        type bro interface {
            bro ();
            bro (a int);
        }
        """
        input = Program([InterfaceType("bro",[Prototype("bro",[],VoidType()),Prototype("bro",[IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: bro\n", 412))

    def test_413(self):
        """ 
        func bro (a, a int) {return;}
        """
        input = Program([FuncDecl("bro",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a\n", 413))

    def test_414(self):
        input = """ 
        func bro (b int) {
            var b = 1;
            var a = 1;
            const a = 1;
        }
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", 414))

    def test_415(self):
        """ 
        func bro (b int) {
            for var a = 1; a < 1; a += 1 {
                const a = 2;
            }
        }
        """
        input = Program([FuncDecl("bro",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", 415))

    def test_416(self):
        """ 
        type Broo struct {bro int;}
        type Broo interface {bro ();}

        """
        input = Program([StructType("Broo",[("bro",IntType())],[]),InterfaceType("Broo",[Prototype("bro",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: Broo\n", 416))
        
    def test_417(self):
        """ 
        var a = 1 + "haha";
        var b = a;
        var c = d;
        """
        input = Program([VarDecl("a",None,BinaryOp("+",IntLiteral(1),StringLiteral("haha"))),VarDecl("b",None,Id("a")),VarDecl("c",None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(IntLiteral(1),+,StringLiteral(haha))\n", 417))
    
    def test_418(self):
        """ 
        var a = 1 + 2;
        var b float = -a;
        var c = d;
        """
        input = Program([VarDecl("a",None,BinaryOp("+",IntLiteral(1),IntLiteral(2))),VarDecl("b",FloatType(),UnaryOp("-",Id("a"))),VarDecl("c",None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d\n", 418))
    
    def test_419(self):
        """ 
        var a = 1 + 2;
        var b int = -a;
        var c = d;
        """
        input = Program([VarDecl("a",None,BinaryOp("+",IntLiteral(1),IntLiteral(2))),VarDecl("b",IntType(),UnaryOp("-",Id("a"))),VarDecl("c",None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d\n", 419))
        
    def test_420(self):
        """ 
        var a = 1 + 2;
        var b string = -a;
        var c = d;
        """
        input = Program([VarDecl("a",None,BinaryOp("+",IntLiteral(1),IntLiteral(2))),VarDecl("b",StringType(),UnaryOp("-",Id("a"))),VarDecl("c",None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(b,StringType,UnaryOp(-,Id(a)))\n", 420))
        
    def test_421(self):
        """ 
        var a = 1 + 2.3;
        var b float = -a;
        var c = d;
        """
        input = Program([VarDecl("a",None,BinaryOp("+",IntLiteral(1),FloatLiteral(2.3))),VarDecl("b",FloatType(),UnaryOp("-",Id("a"))),VarDecl("c",None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d\n", 421))
        
    def test_422(self):
        """ 
        var a = 1 + 2.3;
        var b float = -a;
        var c = d;
        """
        input = Program([VarDecl("a",None,BinaryOp("+",IntLiteral(1),FloatLiteral(2.3))),VarDecl("b",IntType(),UnaryOp("-",Id("a"))),VarDecl("c",None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(b,IntType,UnaryOp(-,Id(a)))\n", 422))
    
    def test_423(self):
        """ 
        var a = 1;
        var b = a;
        var c = d;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d\n", 423))

    def test_424(self):
        """ 
        func bro () int {return 1;}

        fun foo () {
            var b = bro();
            foo_votine();
            return;
        }
        """
        input = Program([FuncDecl("bro",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("bro",[])),FuncCall("foo_votine",[]),Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_votine\n", 424))

    def test_425(self):
        """ 
        type Broo struct {
            bro int;
        }

        func (v Broo) getInt () {
            const c = v.bro;
            var d = v.Broo;
        }
        """
        input = Program([StructType("Broo",[("bro",IntType())],[]),MethodDecl("v",Id("Broo"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"bro")),VarDecl("d", None,FieldAccess(Id("v"),"Broo"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: Broo\n", 425))

    def test_426(self):
        """ 
        type Broo struct {
            bro int;
        }

        func (v Broo) getInt () {
            v.getInt ();
            v.putInt ();
        }
        """
        input = Program([StructType("Broo",[("bro",IntType())],[]),MethodDecl("v",Id("Broo"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: putInt\n", 426))

    def test_427(self):
        """ 
        type Broo struct {
            bro int;
        }

        func (v Broo) getInt () {
            var d = v.Broo;
        }
        """
        input = Program([StructType("Broo",[("bro",IntType())],[]),MethodDecl("v",Id("Broo"),FuncDecl("getInt",[],VoidType(),Block([VarDecl("d", None,FieldAccess(Id("v"),"Broo"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: Broo\n", 427))

    def test_428(self):
        """
            func factorial(n int) int {
                if (n + 0) {
                    return 1;
                } else {
                    return n * factorial(n - 1);
                }
            }
        """
        input = Program([
            FuncDecl("factorial", [ParamDecl("n", IntType())], IntType(), Block([
                If(BinaryOp("+", Id("n"), IntLiteral(0)),
                   Block([Return(IntLiteral(1))]),
                   Block([Return(BinaryOp("*", Id("n"), FuncCall("factorial", [BinaryOp("-", Id("n"), IntLiteral(1))])))])
                   )
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: If(BinaryOp(Id(n),+,IntLiteral(0)),Block([Return(IntLiteral(1))]),Block([Return(BinaryOp(Id(n),*,FuncCall(factorial,[BinaryOp(Id(n),-,IntLiteral(1))])))]))\n", 428))
        
    def test_429(self):
        """
            func sumArray(arr [10]int) int {
                var total = 0;
                for i := 0; i < 10; i += 1 {
                    total += arr[i];
                }
                return total;
            }
        """
        input = Program([
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
        self.assertTrue(TestChecker.test(input, "", 429))
        
    def test_430(self):
        """
            var A int;
            func (a A) b(x int){}
            type A struct{}
        """
        input = Program([VarDecl("A",IntType,None),MethodDecl("a",Id("A"),FuncDecl("b",[ParamDecl("x",IntType)],VoidType,Block([]))),StructType("A",[],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: A\n", 430))
        
    def test_431(self):
        """
        var arr [5]int = [5]int{1, 2, 3, 4, 5};
        """
        input = Program([
            VarDecl("arr", ArrayType([IntLiteral(5)], IntType()),
                    ArrayLiteral([IntLiteral(5)], IntType(),
                                 [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]))
        ])
        self.assertTrue(TestChecker.test(input, "", 431))
        
    def test_432(self):
        input = """
        var arr [5]int = [5]int{1, 2, 3, 4, 5};
        """
        self.assertTrue(TestChecker.test(input, "", 432))
        
    def test_433(self):
        """
        var arr [4]int = [5]int{1, 2, 3, 4, 5};
        """
        input = Program([
            VarDecl("arr", ArrayType([IntLiteral(4)], IntType()),
                    ArrayLiteral([IntLiteral(5)], IntType(),
                                 [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(4)]),ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))\n", 433))
    
    def test_434(self):
        input = """
        const x = 5
        var arr [x]int = [5]int{1, 2, 3, 4, 5};
        """
        self.assertTrue(TestChecker.test(input, "", 434))
    
    def test_435(self):
        input = """
        var x = 3
        var arr [x]int = [5]int{1, 2, 3, 4, 5};
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(arr,ArrayType(IntType,[Id(x)]),ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))\n", 435))
    
    def test_436(self):
        input = """
        type Person struct{
            name string
            age int
        }
        var q Person
        func main() string {
            var p Person
            var q float
            p := Person{name: "Alice", age: 30}
            q := Person{}
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Assign(Id(q),StructLiteral(Person,[]))\n", 436))
        
    def test_437(self):
        input = """
        type Person struct{
            name string
            age int
        }
        var q Person
        func main() string {
            var p Person
            var q float
            p := Person{}
            q := Person{name: "Alice", age: 30}
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(q),StructLiteral(Person,[(name,StringLiteral("Alice")),(age,IntLiteral(30))]))\n""", 437))
    
    def test_438(self):
        input = """
        type Person struct{
            name string
            age int
        }
        var q Person
        func main() string {
            var p Person
            var q float
            p := Person{name: 15, age: 21}
            q := 18
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: StructLiteral(Person,[(name,IntLiteral(15)),(age,IntLiteral(21))])\n""", 438))
    
    def test_439(self):
        input = """
        type Person struct{
            name string
            age int
        }
        var q Person
        func main() string {
            q := Person{name: "Minh", age: 21}
            var p Person
            var q float
            q := 18
            p := Person{name: "Khoi", age: 21}
            
        }
        """
        self.assertTrue(TestChecker.test(input, "", 439))
        
    def test_440(self):
        input = """
        type Person struct{
            name string
            age int
        }
        var q Person
        func main() string {
            q := Person{name: Minh, age: 21}
            var p Person
            var q float
            q := 18
            p := Person{name: "Khoi", age: 21}
            
        }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: Minh\n""", 440))
        
    def test_441(self):
        input = """
        func main() string {
            var arr = [3]int{10, 20, 30}
            var value int
            for index, value := range arr {
            // index: 0, 1, 2
            // value: 10, 20, 30
            } 
        }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: index\n""", 441))
        
    def test_442(self):
        input = """
        func main() string {
            var arr [3]int
            arr := [3]int{10, 20, 30}
            var index int
            for index, value := range arr {
                // value: 10, 20, 30
            }
        }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: value\n""", 442))
        
    def test_443(self):
        input = """
        func main() string {
            var arr [3]int
            arr := [3]int{10, 20, 30}
            for _, value := range arr {
                // value: 10, 20, 30
            }
        }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: value\n""", 443))
        
    def test_444(self):
        input = """
        func Ha(a string) float {
            var c int
        }
        func main() string {
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 30}
            var value int
            for _, value := range arr {
                // value: 10, 20, 30
            }
            var x = Ha(8) + 7
        }
        
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(Ha,[IntLiteral(8)])\n""", 444))
    
    def test_445(self):
        input = """
        func Ha(a string, b boolean) float {
            var c int
        }
        func main() string {
            var x = Ha(false, "ha") + 7
        }
        
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(Ha,[BooleanLiteral(false),StringLiteral("ha")])\n""", 445))
    
    def test_446(self):
        input = """
        func Ha(a string, b boolean) float {
            var c int
        }
        func main() string {
            var x = Ha("ha", 0) + 7
        }
        
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(Ha,[StringLiteral("ha"),IntLiteral(0)])\n""", 446))
        
    def test_447(self):
        input = """
        func main() string {
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 30}
            var value int
            for _, value := range arr {
                // value: 10, 20, 30
            }
            var x = Ha("hihi") + 7
        }
        func Ha(a string) float {
            var c int
            var x = Ha(9) + 7
            const s = "hello" + "haha"
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(Ha,[IntLiteral(9)])\n""", 447))
        
    def test_448(self):
        input = """
        func Y() string {
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 30}
            var value int
            for _, value := range arr {
                var idx = 1
                var ar = arr
            }
            var x = Ha(8) + 7
        }
        func Ha(a string) float {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(Ha,[IntLiteral(8)])\n""", 448))
        
    def test_449(self):
        input = """
        func Y() string {
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 30}
            var value int
            for _, value := range arr {
                var idx = 1
                var x = Ha("hihi") + 7
                var ar [2]int = arr
            }
            var x = Ha("hihi") + 7
        }
        func Ha(a string) float {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(ar,ArrayType(IntType,[IntLiteral(2)]),Id(arr))\n""", 449))
        
    def test_450(self):
        input = """
        func Y() string {
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 30}
            var value int
            for _, value := range arr {
                var idx = 2
                var y = arr[1 - idx + 3]
                var x = Ha("hihi") + 7
                var ar [3][1]int = arr
            }
            var x = Ha("hihi") + 7
        }
        func Ha(a string) float {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(ar,ArrayType(IntType,[IntLiteral(3),IntLiteral(1)]),Id(arr))\n""", 450))
    
    def test_451(self):
        input = """
        var a int;
        func main(){
            a:= "string"
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(a),StringLiteral("string"))\n""", 451))
    
    def test_452(self):
        input = """
        func main(){
            arr := [3]int{10, 20, 30}
            marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
            marr[1][2] := arr[2] + 1
            marr[1] := arr + 1
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp(Id(arr),+,IntLiteral(1))\n""", 452))
    
    def test_453(self):
        input = """
        func main(){
            var a = [2][1]int{{1},{2}}
            var b = [3]int{1,2,3}
            a[1][0] := b[2] + 1
            a[1] := b 
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(ArrayCell(Id(a),[IntLiteral(1)]),Id(b))\n""", 453))
    
    def test_454(self):
        input = """
        func foo(){
            return
        }
        func foo1(x int){
            return ;
        }
        func main(){
            foo1( foo())
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[])\n""", 454))
    
    def test_455(self):
        input = """
        func main() {
            var a int; var b int; var c int; for a,b := range c {var d int;}
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ForEach(Id(a),Id(b),Id(c),Block([VarDecl(d,IntType)]))\n""", 455))
        
    def test_456(self):
        input = """
        func Y() string {
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 30}
            var index int
            var value int
            for index, value := range arr {
                var idx = 2
                var x float = Ha("hihi") + 7
                var ar [4]int = arr
            }
            var x = Ha("hihi") + 7
        }
        func Ha(a string) float {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(ar,ArrayType(IntType,[IntLiteral(4)]),Id(arr))\n""", 456))
        
    def test_457(self):
        input = """
        func Y() string {
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 30}
            var value int
            for _, value := range arr {
                var idx = 2
                const c = 1
                const d = idx*2 - c
                var ar [3]int = arr
                var y [1]float = arr[idx - 1]
                var x = Ha("hihi") + 7
            }
            var x = Ha("hihi") + 7
        }
        func Ha(a string) float {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(y,ArrayType(FloatType,[IntLiteral(1)]),ArrayCell(Id(arr),[BinaryOp(Id(idx),-,IntLiteral(1))]))\n""", 457))
        
    def test_458(self):
        input = """
        func Y() string {
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 30}
            var value int
            for _, value := range arr {
                var idx = 2
                var y float = arr[idx - 2]
                var x = Ha("hihi") + 7
                const c = 2
                var ar [2]int = arr
            }
            var x = Ha("hihi") + 7
        }
        func Ha(a string) float {
            var d int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(ar,ArrayType(IntType,[IntLiteral(2)]),Id(arr))\n""", 458))
        
    def test_459(self):
        input = """
        func Y() string {
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 30}
            var value int
            for _, value := range arr {
                var idx = 2
                var y = arr[idx - 2][0]
                var x = Ha("hihi") + 7
                const c = 2 + idx/2
                var ar [c]int = arr
            }
            var x = Ha("hihi") + 7
        }
        func Ha(a string) float {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ArrayCell(Id(arr),[BinaryOp(Id(idx),-,IntLiteral(2)),IntLiteral(0)])\n""", 459))
        
    def test_460(self):
        input = """
        func Y() string {
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 30}
            var value int
            for _, value := range arr {
                var idx = 2
                var y = arr[idx - 1]
                var x = Ha("hihi") + 7
                const c = 2 + idx
                var ar [3][1]int = arr
            }
            var x = Ha("hihi") + 7
        }
        func Ha(a string) float {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(ar,ArrayType(IntType,[IntLiteral(3),IntLiteral(1)]),Id(arr))\n""", 460))
        
    def test_461(self):
        input = """
        func Y() string {
            var x = Ha("hihi") + 7
            var arr = [3]int{10, 20, 30}
            arr := [3]int{10, 20, 35}
            var value int
            for _, value := range arr {
                var idx = 2
                var y = arr[idx + 0]
                var x = Ha("hehe") + 6
                const o = 6/3
                const c = idx*2*2/4+7-6/idx-o*2+o/2
                var ar [3]int = arr
            }
        }
        func Ha(a string) float {
            var c int
            var x = Ha("flew","flown") + 7
            const s = "hello" + "haha"
            var u = Ha("flew","flown") + 7
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(Ha,[StringLiteral("flew"),StringLiteral("flown")])\n""", 461))

    def test_462(self):
        input = """
        func Y() string {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
            return "hihi"
        }
        func Ha(a string) float {
            He(8)
            return 1.0 + 1
        }
        func He(a int) {
            He(9)
            return
        }
        """
        self.assertTrue(TestChecker.test(input, """""", 462))
        
    def test_463(self):
        input = """
        func Y() string {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
            return 
        }
        func Ha(a string) float {
            He(8)
            return 1.0 + 1
        }
        func He(a int) {
            He(9)
            return
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return()\n""", 463))
        
    def test_464(self):
        input = """
        func Y() string {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
            return "hihi"
        }
        func Ha(a string) float {
            He(8)
            return Ha("huhu") + 1.0
        }
        func He(a int) {
            He(9)
            return
        }
        """
        self.assertTrue(TestChecker.test(input, """""", 464))
    
    def test_465(self):
        input = """
        func Y() string {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
            return "hihi"
        }
        func Ha(a string) int {
            He(8)
            return Ha("huhu") + 1.0
        }
        func He(a int) {
            He(9)
            return
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(BinaryOp(FuncCall(Ha,[StringLiteral("huhu")]),+,FloatLiteral(1.0)))\n""", 465))
    
    def test_466(self):
        input = """
        func Y() string {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
            return "hihi"
        }
        func Ha(a string) float {
            return Ha("huhu") + "hihi"
        }
        func He(a int) {
            He(8)
            He(9)
            return
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp(FuncCall(Ha,[StringLiteral("huhu")]),+,StringLiteral("hihi"))\n""", 466))
        
    def test_467(self):
        input = """
        func Y() string {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
            return "hehe" + Y() + "hihi"
        }
        func Ha(a string) float {
            return Ha("huhu")/2 + 1
        }
        func He(a int) {
            He(8)
            He(9)
            return
        }
        """
        self.assertTrue(TestChecker.test(input, """""", 467))
    
    def test_468(self):
        input = """
        func Y() string {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
            return "hehe" + Y() + "hihi"
        }
        func Ha(a string) float {
            return Ha("huhu")/2.0 + 1*4.5
        }
        func He(a int) {
            He(8)
            He(9)
            return
        }
        """
        self.assertTrue(TestChecker.test(input, """""", 468))
        
    def test_469(self):
        input = """
        func Y() string {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
            return "hehe" + Y() + "hihi"
        }
        func Ha(a string) float {
            return Ha("huhu")/2.0 + 1*4.5
        }
        func Boo(a int, b float, c boolean, d string) boolean{
            He(10)
            return Boo(2,4.0,true,"heh") && 1 + 2.0 < Ha("hi") || Y() >= "hihi"
        }
        func He(a int) {
            He(8)
            He(9)
            var x = Boo(2,4.0,true,"heh") && 1 + 2 < 7 || "haha" >= "hihi"
            return
        }
        """
        self.assertTrue(TestChecker.test(input, """""", 469))
        
    def test_470(self):
        input = """
        func Y() string {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
            return "hehe" + Y() + "hihi"
        }
        func Ha(a string) float {
            return Ha("huhu")/2.0 + 1*4.5
        }
        func He(a int) {
            He(8)
            He(9)
            return
        }
        func (a A) Boo(i int, b float, c boolean, d string) boolean{
            He(10)
            return a.Boo(2,4.0,true,"heh") && 1 + 2 < 7 || "haha" >= "hihi"
        }
        type A struct{
            i int
            b boolean
            f float
            s string
        }
        """
        self.assertTrue(TestChecker.test(input, """""", 470))
        
    def test_471(self):
        input = """
        func Y() string {
            var c int
            var x = Ha("fly") + 7
            const s = "hello" + "haha"
            return "hehe" + Y() + "hihi"
        }
        func Ha(a string) float {
            return Ha("huhu")/2.0 + 1*4.5
        }
        func He(v int) {
            He(8)
            He(9)
            var a A
            if (a.Boo(3,4.0,false,"heh")){
                return
            }
            return
        }
        func (a A) Boo(i int, b float, c boolean, d string) boolean{
            He(10)
            return a.Boo(2,4.0,true,"heh") && 1 + 2 < 7 || "haha" >= "hihi"
        }
        type A struct{
            i int
            b boolean
            f float
            s string
        }
        """
        self.assertTrue(TestChecker.test(input, """""", 471))
    
    def test_472(self):
        input = """
        func main(){
            var arr [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}}
            var b = arr[1];
            var c float = arr[1][1]
            var d string = b[2]
        }
        
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(d,StringType,ArrayCell(Id(b),[IntLiteral(2)]))\n""", 472))
    
    def test_473(self):
        input = """
        func main(){
            var arr [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}}
            var b = arr[1];
            var c float = arr[1][1]
            var d = b[1][3]
        }
        
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ArrayCell(Id(b),[IntLiteral(1),IntLiteral(3)])\n""", 473))
    
    def test_474(self):
        input = """
        func main(){
            var arr [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}}
            var b = arr[1];
            var c [3]float = b
        }
        
        """
        self.assertTrue(TestChecker.test(input, """""", 474))
    
    def test_475(self):
        input = """
        func main(){
            var arr [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}}
            var b = arr[1];
            var c float = arr[1][2]
        }
        
        """
        self.assertTrue(TestChecker.test(input, """""", 475))
    
    def test_476(self):
        input = """
        func main(){
            var arr [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}}
            var b = arr[1];
            var c [3]boolean = b
        }
        
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(c,ArrayType(BoolType,[IntLiteral(3)]),Id(b))\n""", 476))
    
    def test_477(self):
        input = """
        func main(){
            var arr [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}}
            var b = arr;
            var c [2][2]int = b
        }
        
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(2),IntLiteral(2)]),Id(b))\n""", 477))
        
    def test_478(self):
        input = """
        var arr = [2]int{10, 20}
        var marr = [2][3]int{{1, 2, 3}, {4, 5, 6}}
        func main(){
            marr[0] := arr
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(ArrayCell(Id(marr),[IntLiteral(0)]),Id(arr))\n""", 478))
    
    def test_479(self):
        input = """
        var arr = [3]int{10, 20, 30}
        var marr = [2][3]int{{1, 2, 3}, {4, 5, 6}}
        func main(){
            marr[0] := arr
        }
        """
        self.assertTrue(TestChecker.test(input, """""", 479))
    
    def test_480(self):
        input = """
        var arr = [3]int{10, 20, 30}
        var marr = [2][3]int{{1, 2, 3}, {4, 5, 6}}
        func main(){
            marr := arr[2]
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(marr),ArrayCell(Id(arr),[IntLiteral(2)]))\n""", 480))
    
    def test_481(self):
        input = """
        var arr = [3]int{10, 20, 30}
        var marr = [2][3]int{{1, 2, 3}, {4, 5, 6}}
        func main(){
            marr := arr
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(marr),Id(arr))\n""", 481))
       
    def test_482(self):
        input = """
        type A struct { i int; }
        var A int
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: A\n""", 482))
        
    def test_483(self):
        input = """
        type A struct { i int; }
        var a = A
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: A\n""", 483))
        
    def test_484(self):
        input = """
        type A struct { i int; }
        func X() {
            var a = A
        }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: A\n""", 484))
        
    def test_485(self):
        input = """
        func main(){
            for i := 0; i < 10; c += 1 {
                var c = 5
                i += 1 
            }
        }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: c\n""", 485)) 
        
    def test_486(self):
        input = """
        func foo() int {
            return 1;
            var x string = 1;
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(x,StringType,IntLiteral(1))\n""", 486))
    
    def test_487(self):
        input = """
        var a int;
        type a struct {
            name string
        }
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Type: a\n""", 487))
    
    def test_488(self):
        input = """
        func main() {
            const a = 3
            var arr [2]int = [a]int{1, 2, 3}
            return
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(2)]),ArrayLiteral([Id(a)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))\n""", 488))
       
    def test_489(self):
        input = """
        func foo(a int) {
            foo(1);
            var foo = 1;
            foo(2); // error
            }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo\n""", 489))
        
    def test_490(self):
        input = """
        func Add() {
           return
        }
        func main(){
            var a = Add()  + 3 
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(Add,[])\n""", 490))
        
    def test_491(self):
        input = """
        func Add() {
           return
        }
        func main(){
            var a = Add()  + 3 
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(Add,[])\n""", 491))
        
    def test_492(self):
        """
        const a = 2
        func foo(){
            const a = 1
            for var a = 1; a < 1; b += b + 2{
                const b = 1
            }
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("b"),BinaryOp("+", Id("b"), IntLiteral(2))),Block([ConstDecl("b",None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: b\n", 492))


    def test_493(self):
        input = """
        func main(){
            var a int
            a := a + "str"
        }
        """
        self.assertTrue(TestChecker.test(input,"""Type Mismatch: BinaryOp(Id(a),+,StringLiteral("str"))\n""",493))
    
    
    def test_999(self):
        input = """
        var a int; 
        type b struct {
            c int;
        };
        func (x b) a() {
            var y = 0
        };
        func (x b) c() {
            var z = 0
        };
        """
        self.assertTrue(TestChecker.test(input,"""Redeclared Method: c\n""",494))
        
    def test_495(self):
        input = """
        var a int; 
        type b struct {
            c int;
        };
        func (x b) a() {
            var y = 0
        };
        """
        self.assertTrue(TestChecker.test(input,"""""",495))
        
    def test_496(self):
        input = """
        var a int; 
        type b struct {
            b int;
        };
        func (x b) a() {
            var y = 0
        };
        """
        self.assertTrue(TestChecker.test(input,"""""",496))
        
    def test_497(self): 
        input = """
        var y int = 4;
        func Add(x int) int {
            y := 3;
            var y = 5;
            return 4;
        }
        """
        self.assertTrue(TestChecker.test(input, """""", 497))
        
    def test_498(self): 
        input = """
        func Add(x int) int {
            for y := 1; y<5; y += 1 {
                var y = 10;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: y\n""", 498))
        
    def test_499(self): # 216
        """
        var foo = 1;
        func foo1() int {
            return foo()
        }
        """
        input = Program([VarDecl("foo", None,IntLiteral(1)),FuncDecl("foo1",[],IntType(),Block([Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo\n""", 499))
        
    def test_500(self):
        input = """
            var a int; 
            func (x b) c() {
                return
            };
            
            func (x b) z() {
                return;
            }; 
            type b struct {
                z string;
                a int;
            }; 
            
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Method: z\n""", 500))
        
    def test_501(self):
        input = """
            var a int;
            var arr [2][3] string
            
            func (x b) c() {
                arr[2][a] := "haha"
                return
            };
            
            func (x b) z() {
                return;
            }; 
            type b struct {
                z string;
                a int;
            }; 
            
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Method: z\n""", 501))
        
    def test_502(self):
        input = """
            var a string;
            var arr [2][3] string
            
            func (x b) c() {
                arr[2][a] := "haha"
                return
            };
            
            func (x b) z() {
                return;
            }; 
            type b struct {
                y string;
                a int;
            }; 
            
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ArrayCell(Id(arr),[IntLiteral(2),Id(a)])\n""", 502))
        
    def test_503(self):
        input = """
            var c int = 2
            var a int = 2 - c;
            var arr [2][3] string
            
            
            func (x b) c() {
                arr[1][a] := "haha" + "hehe"
                arr[a][c] := arr[c][a] + "hehe"
                return
            };
            
            func (x b) z() {
                x.a := 2
                a := 1.0
                return;
            }; 
            type b struct {
                y string;
                a int;
            }; 
            
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(a),FloatLiteral(1.0))\n""", 503))
        
    def test_504(self):
        input = """
            var c int = 2
            var a int = 2 - c;
            var arr [2][3] string
            
            
            func (x b) c() float{
                arr[1][a] := "haha" + "hehe"
                arr[a][c] := arr[c][a] + "hehe"
                return a + 1.0
            };
            func (x b) d() int{
                arr[1][a] := "haha" + "hehe"
                arr[a][c] := arr[c][a] + "hehe"
                return a
            };
            
            func (x b) z() {
                x.a := x.d()
                x.a := 1.0
                return;
            }; 
            type b struct {
                y string;
                a int;
            }; 
            
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(FieldAccess(Id(x),a),FloatLiteral(1.0))\n""", 504))
        
    def test_505(self):
        input = """
            var c int = 2
            var a int = 2 - c;
            var arr [2][3] string
            
            
            func (x b) c() float{
                arr[1][a] := "haha" + "hehe"
                arr[a][c] := arr[c][a] + "hehe"
                x.z()
                return a + 1.0
            };
            func (x b) d() int{
                arr[1][a] := "haha" + "hehe"
                arr[a][c] := arr[c][a] + "hehe"
                x.z()
                return a
            };
            
            func (x b) z() {
                x.a := x.d()
                x.a := x.c()
                return;
            }; 
            type b struct {
                y string;
                a int;
            }; 
            
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(FieldAccess(Id(x),a),MethodCall(Id(x),c,[]))\n""", 505))
        
    def test_506(self):
        input = """
            var c int = 2
            var a int = 2 - c;
            var arr [2][3] string
            func (x b) c() float{
                arr[1][a] := "haha" + "hehe"
                arr[a][c] := arr[c][a] + "hehe"
                x.z()
                return a + 1.0
            };
            func (x b) d() int{
                arr[1][a] := "haha" + "hehe"
                arr[a][c] := arr[c][a] + "hehe"
                x.z()
                return a
            };
            
            func (x b) z() {
                x.i := 2 + x.d() + 1
                x.i := 1 + x.c()
                return;
            }; 
            type b struct {
                y string;
                i int;
            }; 
            
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(FieldAccess(Id(x),i),BinaryOp(IntLiteral(1),+,MethodCall(Id(x),c,[])))\n""", 506))
        
        
    def test_507(self):
        input = """
            var c int = 2
            var a int = 2 - c;
            var arr [2][3] string
            var af [2][3] float 
            var ai [2][3] int
            
            func (x b) c() float{
                arr[1][a] := "haha" + "hehe"
                arr[a][c] := arr[c][a] + "hehe"
                x.z()
                return a + 1.0
            };
            func (x b) d() int{
                arr[1][a] := "haha" + "hehe"
                arr[a][c] := arr[c][a] + "hehe"
                x.z()
                return a
            };
            
            func (x b) z() {
                x.a := 2 + x.d() + 1
                af := ai
                return;
                ai := af
            }; 
            
            type b struct {
                y string;
                a int;
            }; 
            
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(ai),Id(af))\n""", 507))
