# 2252377 - Nguyen Minh Khoi
import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_401(self):
        """Tests basic integer addition and output."""
        input = """
        func main() {
            putIntLn(3 + 4)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "7\n", "401"))

    def test_402(self):
        """Tests float literal output."""
        input = """
        func main() {
            putFloatLn(2.718)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2.718\n", "402"))

    def test_403(self):
        """Tests string concatenation with global variable."""
        input = """
        var greeting string = "Hello"
        func main() {
            putStringLn(greeting + ", World!")
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Hello, World!\n", "403"))

    def test_404(self):
        """Tests boolean literal output with newline."""
        input = """
        func main() {
            putBoolLn(false)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "false\n", "404"))

    def test_405(self):
        """Tests local variable initialization and arithmetic."""
        input = """
        func main() {
            var x int = 10
            putIntLn(x * 2)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", "405"))

    def test_406(self):
        """Tests global constant usage."""
        input = """
        const pi = 3.14
        func main() {
            putFloatLn(pi)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3.14\n", "406"))

    def test_407(self):
        """Tests array initialization and indexing."""
        input = """
        func main() {
            var arr [3]int = [3]int{1, 2, 3}
            putIntLn(arr[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "407"))

    def test_408(self):
        """Tests two-dimensional array access."""
        input = """
        func main() {
            var matrix [2][2]int = [2][2]int{{1, 2}, {3, 4}}
            putIntLn(matrix[1][1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4\n", "408"))

    def test_409(self):
        """Tests struct field access."""
        input = """
        type Point struct { x int; y int; }
        func main() {
            var p Point = Point{x: 5, y: 10}
            putIntLn(p.y)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n", "409"))

    def test_410(self):
        """Tests interface method call."""
        input = """
        type Printer interface { print(); }
        type Message struct { text string; }
        func (m Message) print() { putStringLn(m.text); }
        func main() {
            var p Printer = Message{text: "Hello"}
            p.print()
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Hello\n", "410"))

    def test_411(self):
        """Tests for loop with array update."""
        input = """
        func main() {
            var arr [3]int = [3]int{1, 2, 3}
            for i := 0; i < 3; i += 1 {
                arr[i] := arr[i] * 2
            }
            putIntLn(arr[2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n", "411"))

    def test_412(self):
        """Tests if statement with comparison."""
        input = """
        func main() {
            var x int = 5
            if (x > 3) {
                putStringLn("Greater")
            } else {
                putStringLn("Less or Equal")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Greater\n", "412"))

    def test_413(self):
        """Tests function returning integer."""
        input = """
        func double(x int) int { return x * 2; }
        func main() {
            putIntLn(double(4))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "8\n", "413"))

    def test_414(self):
        """Tests variable shadowing in block."""
        input = """
        func main() {
            var x int = 10
            if (x < 11){
                var x int = 20
                putIntLn(x)
            }
            putIntLn(x)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n10\n", "414"))

    def test_415(self):
        """Tests array of structs."""
        input = """
        type Item struct { id int; }
        func main() {
            var items [2]Item = [2]Item{Item{id: 1}, Item{id: 2}}
            putIntLn(items[1].id)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "415"))

    def test_416(self):
        """Tests recursive function call."""
        input = """
        func fib(n int) int {
            if (n <= 1) { return n; }
            return fib(n - 1) + fib(n - 2);
        }
        func main() {
            putIntLn(fib(5))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5\n", "416"))

    def test_417(self):
        """Tests simple integer variable output."""
        input = """
        func main() {
            var x int = 42
            putIntLn(x)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "42\n", "417"))

    def test_418(self):
        """Tests logical AND with short-circuit evaluation."""
        input = """
        func main() {
            var x int = 0
            if (x != 0 && 10 / x > 1) {
                putStringLn("Should not print")
            } else {
                putStringLn("Safe")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Safe\n", "418"))

    def test_419(self):
        """Tests array initialization with constant size."""
        input = """
        const SIZE = 3
        func main() {
            var arr [SIZE]int = [SIZE]int{1, 2, 3}
            putIntLn(arr[2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3\n", "419"))

    def test_420(self):
        """Tests struct method modifying field."""
        input = """
        type Counter struct { value int; }
        func (c Counter) inc() { c.value += 1; }
        func main() {
            var c Counter = Counter{value: 5}
            c.inc()
            putIntLn(c.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n", "420"))

    def test_421(self):
        """Tests interface array with method calls."""
        input = """
        type Processor interface { process() int; }
        type Data struct { value int; }
        func (d Data) process() int { return d.value + 1; }
        func main() {
            var arr [2]Processor = [2]Processor{Data{value: 1}, Data{value: 2}}
            putIntLn(arr[0].process())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "421"))

    def test_422(self):
        """Tests nested loops with array updates."""
        input = """
        func main() {
            var a [2][2]int = [2][2]int{{1, 2}, {3, 4}}
            for i := 0; i < 2; i += 1 {
                for j := 0; j < 2; j += 1 {
                    a[i][j] := a[i][j] + 1
                }
            }
            putIntLn(a[1][1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5\n", "422"))

    def test_423(self):
        """Tests function returning struct."""
        input = """
        type Pair struct { x int; y int; }
        func createPair() Pair { return Pair{x: 1, y: 2}; }
        func main() {
            var p Pair = createPair()
            putIntLn(p.y)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "423"))

    def test_424(self):
        """Tests float arithmetic with division."""
        input = """
        func main() {
            var x float = 10.0
            putFloatLn(x / 2.0)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5.0\n", "424"))

    def test_425(self):
        """Tests while-like for loop."""
        input = """
        func main() {
            var x int = 3
            for x > 0 {
                putIntLn(x)
                x -= 1
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3\n2\n1\n", "425"))

    def test_426(self):
        """Tests modulo operation."""
        input = """
        func main() {
            var x int = 10
            putIntLn(x % 3)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n", "426"))

    def test_427(self):
        """Tests string comparison."""
        input = """
        func main() {
            putBoolLn("abc" < "def")
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", "427"))

    def test_428(self):
        """Tests array copy semantics."""
        input = """
        func main() {
            var a [2]int = [2]int{1, 2}
            var b [2]int = a
            b[0] := 10
            putIntLn(a[0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n", "428"))

    def test_429(self):
        """Tests struct pass-by-value."""
        input = """
        type Box struct { value int; }
        func update(b Box) { b.value := 100; }
        func main() {
            var b Box = Box{value: 50}
            update(b)
            putIntLn(b.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "100\n", "429"))

    def test_430(self):
        """Tests interface with multiple structs."""
        input = """
        type Worker interface { work() int; }
        type Robot struct { id int; }
        func (r Robot) work() int { return r.id; }
        func main() {
            var w Worker = Robot{id: 42}
            putIntLn(w.work())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "42\n", "430"))

    def test_431(self):
        """Tests nested if statements."""
        input = """
        func main() {
            var x int = 5
            if (x > 3) {
                if (x < 7) {
                    putStringLn("In range")
                }
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "In range\n", "431"))

    def test_432(self):
        """Tests function with multiple parameters."""
        input = """
        func add(a int, b int) int { return a + b; }
        func main() {
            putIntLn(add(3, 4))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "7\n", "432"))

    def test_433(self):
        """Tests array indexing with expression."""
        input = """
        func main() {
            var arr [3]int = [3]int{1, 2, 3}
            var i int = 1
            putIntLn(arr[i + 1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3\n", "433"))

    def test_434(self):
        """Tests struct array initialization."""
        input = """
        type Item struct { value int; }
        func main() {
            var items [2]Item = [2]Item{Item{value: 10}, Item{value: 20}}
            putIntLn(items[1].value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", "434"))

    def test_435(self):
        """Tests logical OR with short-circuit."""
        input = """
        func main() {
            var x int = 5
            if (x == 5 || 10 / 0 > 1) {
                putStringLn("Safe")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Safe\n", "435"))

    def test_436(self):
        """Tests three-dimensional array access."""
        input = """
        func main() {
            var arr [2][2][2]int = [2][2][2]int{{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}}
            putIntLn(arr[1][1][1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "8\n", "436"))

    def test_437(self):
        """Tests struct method returning value."""
        input = """
        type Math struct { x int; }
        func (m Math) square() int { return m.x * m.x; }
        func main() {
            var m Math = Math{x: 4}
            putIntLn(m.square())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "16\n", "437"))

    def test_438(self):
        """Tests function returning array."""
        input = """
        func createArray() [2]int { return [2]int{1, 2}; }
        func main() {
            var arr [2]int = createArray()
            putIntLn(arr[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "438"))

    def test_439(self):
        """Tests variable shadowing in loop."""
        input = """
        func main() {
            var i int = 10
            for i := 0; i < 2; i += 1 {
                putIntLn(i)
            }
            putIntLn(i)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0\n1\n2\n", "439"))

    def test_440(self):
        """Tests interface with float return."""
        input = """
        type Calculator interface { calc() float; }
        type Adder struct { x float; }
        func (a Adder) calc() float { return a.x + 1.0; }
        func main() {
            var c Calculator = Adder{x: 2.0}
            putFloatLn(c.calc())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3.0\n", "440"))

    def test_441(self):
        """Tests array update with conditional."""
        input = """
        func main() {
            var arr [3]int = [3]int{1, 2, 3}
            for i := 0; i < 3; i += 1 {
                if (arr[i] % 2 == 0) {
                    arr[i] := arr[i] * 2
                }
            }
            putIntLn(arr[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4\n", "441"))

    def test_442(self):
        """Tests basic array indexing."""
        input = """
        func main() {
            var arr [3]int = [3]int{10, 20, 30}
            putIntLn(arr[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", "442"))

    def test_443(self):
        """Tests recursive function with base case."""
        input = """
        func sum(n int) int {
            if (n == 0) { return 0; }
            return n + sum(n - 1);
        }
        func main() {
            putIntLn(sum(3))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n", "443"))

    def test_444(self):
        """Tests array of interfaces with loop."""
        input = """
        type Printer interface { print() int; }
        type Number struct { value int; }
        func (n Number) print() int { return n.value; }
        func main() {
            var arr [2]Printer = [2]Printer{Number{value: 1}, Number{value: 2}}
            for i := 0; i < 2; i += 1 {
                putIntLn(arr[i].print())
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n", "444"))

    def test_445(self):
        """Tests float comparison."""
        input = """
        func main() {
            var x float = 2.0
            putBoolLn(x == 2.0)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", "445"))

    def test_446(self):
        """Tests struct initialization with default values."""
        input = """
        type Data struct { value int; }
        func main() {
            var d Data
            putIntLn(d.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0\n", "446"))

    def test_447(self):
        """Tests function with string parameter."""
        input = """
        func greet(name string) string { return "Hello, " + name; }
        func main() {
            putStringLn(greet("Alice"))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Hello, Alice\n", "447"))

    def test_448(self):
        """Tests array update with computed index."""
        input = """
        func main() {
            var arr [3]int = [3]int{1, 2, 3}
            var i int = 1
            arr[i] := arr[i - 1] + arr[i]
            putIntLn(arr[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3\n", "448"))

    def test_449(self):
        """Tests interface with multiple methods."""
        input = """
        type Worker interface { start() int; stop() int; }
        type Machine struct { id int; }
        func (m Machine) start() int { return m.id; }
        func (m Machine) stop() int { return m.id + 1; }
        func main() {
            var w Worker = Machine{id: 10}
            putIntLn(w.stop())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "11\n", "449"))

    def test_450(self):
        """Tests nested struct array access."""
        input = """
        type Inner struct { value int; }
        type Outer struct { arr [2]Inner; }
        func main() {
            var o Outer = Outer{arr: [2]Inner{Inner{value: 1}, Inner{value: 2}}}
            putIntLn(o.arr[1].value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "450"))

    def test_451(self):
        """Tests function returning boolean."""
        input = """
        func isEven(n int) boolean { return n % 2 == 0; }
        func main() {
            putBoolLn(isEven(4))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", "451"))

    def test_452(self):
        """Tests array of structs with loop."""
        input = """
        type Item struct { id int; }
        func main() {
            var items [2]Item = [2]Item{Item{id: 1}, Item{id: 2}}
            for i := 0; i < 2; i += 1 {
                putIntLn(items[i].id)
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n", "452"))

    def test_453(self):
        """Tests float array initialization."""
        input = """
        func main() {
            var arr [2]float = [2]float{1.5, 2.5}
            putFloatLn(arr[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2.5\n", "453"))

    def test_454(self):
        """Tests struct method with parameter."""
        input = """
        type Counter struct { value int; }
        func (c Counter) add(n int) int { return c.value + n; }
        func main() {
            var c Counter = Counter{value: 10}
            putIntLn(c.add(5))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15\n", "454"))

    def test_455(self):
        """Tests interface with string method."""
        input = """
        type Greeter interface { greet() string; }
        type Person struct { name string; }
        func (p Person) greet() string { return "Hi, " + p.name; }
        func main() {
            var g Greeter = Person{name: "Bob"}
            putStringLn(g.greet())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Hi, Bob\n", "455"))

    def test_456(self):
        """Tests array update in nested loop."""
        input = """
        func main() {
            var arr [2][2]int = [2][2]int{{1, 2}, {3, 4}}
            for i := 0; i < 2; i += 1 {
                for j := 0; j < 2; j += 1 {
                    arr[i][j] := arr[i][j] * 2
                }
            }
            putIntLn(arr[0][1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4\n", "456"))

    def test_457(self):
        """Tests struct with array field."""
        input = """
        type Container struct { values [2]int; }
        func main() {
            var c Container = Container{values: [2]int{10, 20}}
            putIntLn(c.values[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", "457"))

    def test_458(self):
        """Tests function with array parameter."""
        input = """
        func sum(arr [2]int) int { return arr[0] + arr[1]; }
        func main() {
            var arr [2]int = [2]int{1, 2}
            putIntLn(sum(arr))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3\n", "458"))

    def test_459(self):
        """Tests logical NOT operator."""
        input = """
        func main() {
            var b boolean = true
            putBoolLn(!b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "false\n", "459"))

    def test_460(self):
        """Tests struct method modifying array field."""
        input = """
        type ArrayHolder struct { arr [2]int; }
        func (a ArrayHolder) update() { a.arr[0] := 100; }
        func main() {
            var h ArrayHolder = ArrayHolder{arr: [2]int{1, 2}}
            h.update()
            putIntLn(h.arr[0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "100\n", "460"))

    def test_461(self):
        """Tests interface with parameter."""
        input = """
        type Processor interface { process(x int) int; }
        type Multiplier struct { factor int; }
        func (m Multiplier) process(x int) int { return m.factor * x; }
        func main() {
            var p Processor = Multiplier{factor: 3}
            putIntLn(p.process(4))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "12\n", "461"))

    def test_462(self):
        """Tests simple string literal output."""
        input = """
        func main() {
            putStringLn("Hello")
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Hello\n", "462"))

    def test_463(self):
        """Tests struct with boolean field."""
        input = """
        type Flag struct { active boolean; }
        func main() {
            var f Flag = Flag{active: true}
            putBoolLn(f.active)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", "463"))

    def test_464(self):
        """Tests function returning float."""
        input = """
        func scale(x float) float { return x * 2.0; }
        func main() {
            putFloatLn(scale(1.5))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3.0\n", "464"))

    def test_465(self):
        """Tests array of booleans."""
        input = """
        func main() {
            var arr [2]boolean = [2]boolean{true, false}
            putBoolLn(arr[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "false\n", "465"))

    def test_466(self):
        """Tests struct method with conditional."""
        input = """
        type Checker struct { value int; }
        func (c Checker) isPositive() boolean { return c.value > 0; }
        func main() {
            var c Checker = Checker{value: 5}
            putBoolLn(c.isPositive())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", "466"))

    def test_467(self):
        """Tests simple float literal output."""
        input = """
        func main() {
            putFloatLn(3.14)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3.14\n", "467"))

    def test_468(self):
        """Tests nested loop with break."""
        input = """
        func main() {
            var sum int = 0
            for i := 0; i < 3; i += 1 {
                for j := 0; j < 3; j += 1 {
                    sum += 1
                    if (sum == 4) { break; }
                }
                if (sum == 4) { break; }
            }
            putIntLn(sum)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4\n", "468"))

    def test_469(self):
        """Tests struct with string array."""
        input = """
        type Holder struct { names [2]string; }
        func main() {
            var h Holder = Holder{names: [2]string{"Alice", "Bob"}}
            putStringLn(h.names[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Bob\n", "469"))

    def test_470(self):
        """Tests function with struct parameter."""
        input = """
        type Point struct { x int; }
        func getX(p Point) int { return p.x; }
        func main() {
            var p Point = Point{x: 15}
            putIntLn(getX(p))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15\n", "470"))

    def test_471(self):
        """Tests array update with loop and expression."""
        input = """
        func main() {
            var arr [3]int = [3]int{1, 2, 3}
            for i := 0; i < 2; i += 1 {
                arr[i + 1] := arr[i] + arr[i + 1]
            }
            putIntLn(arr[2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n", "471"))

    def test_472(self):
        """Tests interface with multiple implementations."""
        input = """
        type Worker interface { work() string; }
        type Robot struct { id int; }
        type Human struct { name string; }
        func (r Robot) work() string { return "Robot"; }
        func (h Human) work() string { return h.name; }
        func main() {
            var w Worker = Human{name: "Alice"}
            putStringLn(w.work())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Alice\n", "472"))

    def test_473(self):
        """Tests struct with nested struct array."""
        input = """
        type Inner struct { value int; }
        type Outer struct { inners [2]Inner; }
        func main() {
            var o Outer = Outer{inners: [2]Inner{Inner{value: 1}, Inner{value: 2}}}
            putIntLn(o.inners[1].value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "473"))

    def test_474(self):
        """Tests function returning struct with array."""
        input = """
        type Container struct { arr [2]int; }
        func create() Container { return Container{arr: [2]int{1, 2}}; }
        func main() {
            var c Container = create()
            putIntLn(c.arr[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "474"))

    def test_475(self):
        """Tests float arithmetic with precedence."""
        input = """
        func main() {
            var x float = 2.0
            putFloatLn(x * 3.0 + 1.0)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "7.0\n", "475"))

    def test_476(self):
        """Tests array of floats with loop."""
        input = """
        func main() {
            var arr [2]float = [2]float{1.0, 2.0}
            for i := 0; i < 2; i += 1 {
                arr[i] := arr[i] * 2.0
            }
            putFloatLn(arr[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4.0\n", "476"))

    def test_477(self):
        """Tests struct method with array access."""
        input = """
        type Holder struct { arr [2]int; }
        func (h Holder) getFirst() int { return h.arr[0]; }
        func main() {
            var h Holder = Holder{arr: [2]int{10, 20}}
            putIntLn(h.getFirst())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n", "477"))

    def test_478(self):
        """Tests interface with boolean method."""
        input = """
        type Checker interface { check() boolean; }
        type Data struct { value int; }
        func (d Data) check() boolean { return d.value > 0; }
        func main() {
            var c Checker = Data{value: 5}
            putBoolLn(c.check())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", "478"))

    def test_479(self):
        """Tests simple boolean variable output."""
        input = """
        func main() {
            var b boolean = true
            putBoolLn(b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", "479"))

    def test_480(self):
        """Tests short-circuit and"""
        input = """
        func foo() boolean {
            putStringLn("Not shortcut!");
            return true;
        }
        var x = !boo() && foo()
        func main() {
            putBoolLn(x)
        }
        func boo() boolean {
            putStringLn("Is shortcut!");
            return true;
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Is shortcut!\nfalse\n", "480"))

    def test_481(self):
        """Tests array update with conditional loop."""
        input = """
        func main() {
            var arr [3]int = [3]int{1, 2, 3}
            for i := 0; i < 3; i += 1 {
                if (arr[i] > 1) {
                    arr[i] := arr[i] + 1
                }
            }
            putIntLn(arr[2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4\n", "481"))

    def test_482(self):
        """Tests struct with float field."""
        input = """
        type Data struct { value float; }
        func main() {
            var d Data = Data{value: 3.14}
            putFloatLn(d.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3.14\n", "482"))

    def test_483(self):
        """Tests interface with struct parameter."""
        input = """
        type Processor interface { process(d Data) int; }
        type Data struct { value int; }
        type Worker struct { id int; }
        func (w Worker) process(d Data) int { return d.value + w.id; }
        func main() {
            var p Processor = Worker{id: 10}
            putIntLn(p.process(Data{value: 5}))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15\n", "483"))

    def test_484(self):
        """Tests array of strings with concatenation."""
        input = """
        func main() {
            var arr [2]string = [2]string{"Hello", "World"}
            putStringLn(arr[0] + " " + arr[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Hello World\n", "484"))

    def test_485(self):
        """Tests struct method with loop."""
        input = """
        type Counter struct { value int; }
        func (c Counter) sumToN(n int) int {
            var sum int = 0
            for i := 1; i <= n; i += 1 {
                sum += c.value
            }
            return sum
        }
        func main() {
            var c Counter = Counter{value: 2}
            putIntLn(c.sumToN(3))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n", "485"))

    def test_486(self):
        """Tests function with array return and loop."""
        input = """
        func createArray() [3]int { return [3]int{1, 2, 3}; }
        func main() {
            var arr [3]int = createArray()
            for i := 0; i < 3; i += 1 {
                putIntLn(arr[i])
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n3\n", "486"))

    def test_487(self):
        """Tests struct with nested array method."""
        input = """
        type Matrix struct { data [2][2]int; }
        func (m Matrix) getElement(i int, j int) int { return m.data[i][j]; }
        func main() {
            var m Matrix = Matrix{data: [2][2]int{{1, 2}, {3, 4}}}
            putIntLn(m.getElement(1, 1))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4\n", "487"))

    def test_488(self):
        """Tests interface with float parameter."""
        input = """
        type Scaler interface { scale(x float) float; }
        type Multiplier struct { factor float; }
        func (m Multiplier) scale(x float) float { return m.factor * x; }
        func main() {
            var s Scaler = Multiplier{factor: 2.0}
            putFloatLn(s.scale(3.0))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6.0\n", "488"))

    def test_489(self):
        """Tests array of structs with method call."""
        input = """
        type Item struct { value int; }
        func (i Item) getValue() int { return i.value; }
        func main() {
            var items [2]Item = [2]Item{Item{value: 10}, Item{value: 20}}
            putIntLn(items[1].getValue())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", "489"))

    def test_490(self):
        """Tests function with conditional return."""
        input = """
        func max(a int, b int) int {
            if (a > b) { return a; }
            return b;
        }
        func main() {
            putIntLn(max(5, 3))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5\n", "490"))

    def test_491(self):
        """Tests struct with array initialization."""
        input = """
        type Data struct { values [2]int; }
        func main() {
            var d Data = Data{values: [2]int{1, 2}}
            putIntLn(d.values[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "491"))

    def test_492(self):
        """Tests simple struct field access."""
        input = """
        type Person struct { name string; }
        func main() {
            var p Person = Person{name: "Alice"}
            putStringLn(p.name)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Alice\n", "492"))

    def test_493(self):
        """Tests array update with modulo."""
        input = """
        func main() {
            var arr [3]int = [3]int{1, 2, 3}
            for i := 0; i < 3; i += 1 {
                if (i % 2 == 0) {
                    arr[i] := arr[i] * 2
                }
            }
            putIntLn(arr[0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "493"))

    def test_494(self):
        """Tests struct method with float return."""
        input = """
        type Calculator struct { x float; }
        func (c Calculator) double() float { return c.x * 2.0; }
        func main() {
            var c Calculator = Calculator{x: 1.5}
            putFloatLn(c.double())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3.0\n", "494"))

    def test_495(self):
        """Tests function with array of structs."""
        input = """
        type Item struct { id int; }
        func process(items [2]Item) int { return items[1].id; }
        func main() {
            var items [2]Item = [2]Item{Item{id: 1}, Item{id: 2}}
            putIntLn(process(items))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", "495"))

    def test_496(self):
        """Tests interface with conditional method."""
        input = """
        type Checker interface { isValid() boolean; }
        type Data struct { value int; }
        func (d Data) isValid() boolean { return d.value > 0; }
        func main() {
            var c Checker = Data{value: -1}
            putBoolLn(c.isValid())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "false\n", "496"))

    def test_497(self):
        """Tests simple struct initialization."""
        input = """
        type Box struct { value int; }
        func main() {
            var b Box = Box{value: 100}
            putIntLn(b.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "100\n", "497"))

    def test_498(self):
        """Tests function with float array parameter."""
        input = """
        func sum(arr [2]float) float { return arr[0] + arr[1]; }
        func main() {
            var arr [2]float = [2]float{1.5, 2.5}
            putFloatLn(sum(arr))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4.0\n", "498"))
        
    def test_499(self):
        """Tests short-circuit or"""
        input = """
        func foo() boolean {
            putStringLn("Not shortcut!");
            return true;
        }
        func boo() boolean {
            putStringLn("Is shortcut!");
            return true;
        }
        var x = boo() || foo()
        func main() {
            putBoolLn(x)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Is shortcut!\ntrue\n", "499"))
        
    def test_500(self):
        """Tests struct with array method and loop."""
        input = """
        type ArrayHolder struct { arr [3]int; }
        func (a ArrayHolder) sum() int {
            var sum int = 0
            for i := 0; i < 3; i += 1 {
                sum += a.arr[i]
            }
            return sum
        }
        func main() {
            var h ArrayHolder = ArrayHolder{arr: [3]int{1, 2, 3}}
            putIntLn(h.sum())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n", "500"))