# 2252377 - Nguyen Minh Khoi
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):    
    def test_201(self):
        """Interface"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                Add(x, y int) int;
                Subtract(a, b float, c int) float;
                Reset()
                SayHello(name string)
            }
        """, "successful", 201))

    def test_202(self):
        """Array with Mixed Types (Invalid)"""
        self.assertTrue(TestParser.checkParser("""var array = [4]int{2, 1.e-0, "hello", 3.14};""", "successful", 202))

    def test_203(self):
        """Unexpected Token in Function Declaration"""
        self.assertTrue(TestParser.checkParser("""
            func 123Invalid() {}
        """, "Error on line 2 col 18: 123", 203))

    def test_204(self):
        """Struct Declaration Without Identifier"""
        self.assertTrue(TestParser.checkParser("""
            type struct {
                name string;
            }
        """, "Error on line 2 col 18: struct", 204))

    def test_205(self):
        """Variable Declaration Without Identifier"""
        self.assertTrue(TestParser.checkParser("""
            var  int = 5;
        """, "Error on line 2 col 18: int", 205))

    def test_206(self):
        """Function with Missing Parentheses"""
        self.assertTrue(TestParser.checkParser("""
            func missingParam {
                return 42;
            }
        """, "Error on line 2 col 31: {", 206))

    def test_207(self):
        """Array Declaration with Missing Brackets"""
        self.assertTrue(TestParser.checkParser("""
            var arr 5]int;
        """, "Error on line 2 col 21: 5", 207))

    def test_208(self):
        """Misplaced Operator"""
        self.assertTrue(TestParser.checkParser("""
            var result = * 7 + 9;
        """, "Error on line 2 col 26: *", 208))

    def test_209(self):
        """For Loop with Missing Condition"""
        self.assertTrue(TestParser.checkParser("""
            for () {
                print("Hello");
            }
        """, "Error on line 2 col 13: for", 209))

    def test_210(self):
        """If Statement with Incorrect Syntax"""
        self.assertTrue(TestParser.checkParser("""
            if x > 5 {
                print("Wrong syntax");
            }
        """, "Error on line 2 col 13: if", 210))
    def test_211(self):
        """Unexpected Token in Expression"""
        self.assertTrue(TestParser.checkParser("""
            const value = 4 + * 8;
        """, "Error on line 2 col 31: *", 211))

    def test_212(self):
        """Invalid Function Declaration"""
        self.assertTrue(TestParser.checkParser("""
            func func() {
                return 10;
            }
        """, "Error on line 2 col 18: func", 212))
    
    def test_213(self):
        """Missing Colon in Struct Field"""
        self.assertTrue(TestParser.checkParser("""
            type Person struct {
                name string
                age int;
            }
        """, "successful", 213))
    
    def test_214(self):
        """Incorrect Assignment Operator"""
        self.assertTrue(TestParser.checkParser("""
            var x == 10;
        """, "Error on line 2 col 19: ==", 214))
    
    def test_215(self):
        """Invalid Array Initialization"""
        self.assertTrue(TestParser.checkParser("""
            var numbers [3] int = [1, 2, 3];
        """, "Error on line 2 col 37: ,", 215))
    
    def test_216(self):
        """Function Call Missing Parentheses"""
        self.assertTrue(TestParser.checkParser("""
            func main() {
                print "Hello, World!";
            }
        """, "Error on line 3 col 23: \"Hello, World!\"", 216))
    
    def test_217(self):
        """Unexpected Token After Return"""
        self.assertTrue(TestParser.checkParser("""
            func getValue() {
                return 5 6;
            }
        """, "Error on line 3 col 26: 6", 217))
    
    def test_218(self):
        """Unclosed String Literal"""
        self.assertTrue(TestParser.checkParser("""
            var message string = "Hello, world;";
        """, "successful", 218))
    
    def test_219(self):
        """Using a Reserved Keyword as Variable Name"""
        self.assertTrue(TestParser.checkParser("""
            var return int = 10;
        """, "Error on line 2 col 17: return", 219))
    
    def test_220(self):
        """Extra Brackets in Function Definition"""
        self.assertTrue(TestParser.checkParser("""
            func double((x int)) {
                return x * 2;
            }
        """, "Error on line 2 col 25: (", 220))
        
    def test_221(self):
        """Struct with Function Pointer"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator struct {
                add func(int, int) int;
            };
        """, "Error on line 3 col 21: func", 221))

    def test_222(self):
        """Function with Default Parameter (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            func greet(name string = "Guest") {
                print("Hello, " + name);
            }
        """, "Error on line 2 col 36: =", 222))

    def test_223(self):
        """Array with Incorrect Size Declaration"""
        self.assertTrue(TestParser.checkParser("""
            var nums []int = [3]int{1, 2, 3};
        """, "Error on line 2 col 23: ]", 223))

    def test_224(self):
        """Function Without Return Type (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            func mystery() {
                return 42;
            }
        """, "successful", 224))

    def test_225(self):
        """Excessive Semicolons"""
        self.assertTrue(TestParser.checkParser("""
            var x int = 10;;;;;
        """, "Error on line 2 col 28: ;", 225))

    def test_226(self):
        """Tuple Declaration (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            var pair (int, string) = (5, "hello");
        """, "Error on line 2 col 22: (", 226))

    def test_227(self):
        """Loop Without Condition (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            func main(){
                for () {
                    print("Looping...");
                }
            }
        """, "Error on line 3 col 22: )", 227))

    def test_228(self):
        """String Concatenation Without Operator"""
        self.assertTrue(TestParser.checkParser("""
            var message string = "Hello" "World";
        """, "Error on line 2 col 42: \"World\"", 228))

    def test_229(self):
        """Function with Too Many Parameters"""
        self.assertTrue(TestParser.checkParser("""
            func tooManyParams(a int, b int, c int, d int, e int, f int, g int, h int, i int, j int) {
                print("Too many parameters!");
            }
        """, "successful", 229))

    def test_230(self):
        """Constant Reassignment (Should Fail)"""
        self.assertTrue(TestParser.checkParser("""
            const pi = 3.14;
            pi = 3.14159;
        """, "Error on line 3 col 13: pi", 230))
        
    def test_231(self):
        """Function with No Return Type Specified"""
        self.assertTrue(TestParser.checkParser("""
            func noReturnType(x int, y int) {
                return x + y;
            }
        """, "successful", 231))

    def test_232(self):
        """Array Declaration with Incorrect Bracket Placement"""
        self.assertTrue(TestParser.checkParser("""
            var arr]5[int = {1, 2, 3, 4, 5};
        """, "Error on line 2 col 20: ]", 232))

    def test_233(self):
        """Struct Method Calling Itself Recursively"""
        self.assertTrue(TestParser.checkParser("""
            type Counter struct {
                count int;
                func increment() {
                    self.increment();
                }
            }
        """, "Error on line 4 col 17: func", 233))

    def test_234(self):
        """Invalid Use of Colon in Variable Declaration"""
        self.assertTrue(TestParser.checkParser("""
            var x: int = 10;
        """, "Error on line 2 col 18: :", 234))

    def test_235(self):
        """Function with No Parameters and No Parentheses"""
        self.assertTrue(TestParser.checkParser("""
            func missingParentheses {
                print("Hello");
            }
        """, "Error on line 2 col 37: {", 235))

    def test_236(self):
        """Array with Missing Commas Between Elements"""
        self.assertTrue(TestParser.checkParser("""
            var numbers [5]int = {1 2 3 4 5};
        """, "Error on line 2 col 34: {", 236))

    def test_237(self):
        """Method with Missing Receiver Type in Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Car struct {
                brand string;
            }
            func () drive() {
                print("Driving...");
            }
        """, "Error on line 5 col 19: )", 237))

    def test_238(self):
        """Function Returning Tuple"""
        self.assertTrue(TestParser.checkParser("""
            func getCoordinates() (int, int) {
                return (10, 20);
            }
        """, "Error on line 2 col 35: (", 238))

    def test_239(self):
        """Struct Extending Another Struct Incorrectly"""
        self.assertTrue(TestParser.checkParser("""
            type Animal struct {
                species string;
            }
            type Dog extends Animal {
                breed string;
            }
        """, "Error on line 5 col 22: extends", 239))

    def test_240(self):
        """Use of 'new' Keyword for Struct Initialization"""
        self.assertTrue(TestParser.checkParser("""
            var car = new Car();
        """, "Error on line 2 col 27: Car", 240))
        
    def test_241(self):
        """Struct with Nested Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Engine struct {
                horsepower int
                type string
            }
            
            type Car struct {
                model string
                engine Engine
            }
        """, "Error on line 4 col 17: type", 241))

    def test_242(self):
        """Invalid Variable Initialization"""
        self.assertTrue(TestParser.checkParser("""
            var x int :=;
        """, "Error on line 2 col 23: :=", 242))

    def test_243(self):
        """Struct with Default Values (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            type Phone struct {
                brand string = "Apple"
            }
        """, "Error on line 3 col 30: =", 243))

    def test_244(self):
        """Array with Unspecified Size"""
        self.assertTrue(TestParser.checkParser("""
            var list [3]int = {1, 2, 3};
        """, "Error on line 2 col 31: {", 244))

    def test_245(self):
        """Struct with Method"""
        self.assertTrue(TestParser.checkParser("""
            type Dog struct {
                name string
            }
            func (d Dog) Bark() {
                print("Woof!");
            }
        """, "successful", 245))

    def test_246(self):
        """Function with Incorrect Parameter Syntax"""
        self.assertTrue(TestParser.checkParser("""
            func sum(a int, b int,) int {
                return a + b;
            }
        """, "Error on line 2 col 35: )", 246))

    def test_247(self):
        """Nested If-Else Statement"""
        self.assertTrue(TestParser.checkParser("""
            func check(x int) {
                if (x > 0) {
                    if (x < 10) {
                        print("Single digit");
                    } else {
                        print("Double digit or more");
                    }
                }
            }
        """, "successful", 247))

    def test_248(self):
        """Invalid Return Type"""
        self.assertTrue(TestParser.checkParser("""
            func getData() unknownType {
                return 42;
            }
        """, "successful", 248))

    def test_249(self):
        """Using Reserved Keyword as Variable Name"""
        self.assertTrue(TestParser.checkParser("""
            var return int = 5;
        """, "Error on line 2 col 17: return", 249))

    def test_250(self):
        """Function with Missing Return"""
        self.assertTrue(TestParser.checkParser("""
            func getNumber() int {
                var x int = 10;
            }
        """, "successful", 250))

    def test_251(self):
        """Loop with No Condition"""
        self.assertTrue(TestParser.checkParser("""
            func main(){
                for {
                    print("Infinite Loop");
                }
            }            
        """, "Error on line 3 col 21: {", 251))

    def test_252(self):
        """Invalid Character in Variable Name"""
        self.assertTrue(TestParser.checkParser("""
            var num_ber int = 10;
        """, "successful", 252))

    def test_253(self):
        """Valid Interface Implementation"""
        self.assertTrue(TestParser.checkParser("""
            type Animal interface {
                Speak() string
            }
            
            type Cat struct {
                weight int
            }
            
            func (c Cat) Speak() string {
                return "Meow"
            }
        """, "successful", 253))

    def test_254(self):
        """Invalid Operator Usage"""
        self.assertTrue(TestParser.checkParser("""
            var result = 5 / * 2;
        """, "Error on line 2 col 30: *", 254))

    def test_255(self):
        """Function Without Parameters"""
        self.assertTrue(TestParser.checkParser("""
            func greet() {
                print("Hello!");
            }
        """, "successful", 255))

    def test_256(self):
        """Incorrect Use of Colon"""
        self.assertTrue(TestParser.checkParser("""
            var x : int = 10;
        """, "Error on line 2 col 19: :", 256))

    def test_257(self):
        """Nested for Loops"""
        self.assertTrue(TestParser.checkParser("""
            func nestedLoops() {
                var x int = 0;
                for (x < 10) {
                    var y int = 0;
                    for (y < 5) {
                        print(x, y);
                        y += 1;
                    }
                    x += 1;
                }
            }
        """, "successful", 257))

    def test_258(self):
        """Empty Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Empty struct {}
        """, "successful", 258))

    def test_259(self):
        """Unmatched Parentheses"""
        self.assertTrue(TestParser.checkParser("""
            var y = (5 + (3 * 2;
        """, "Error on line 2 col 32: ;", 259))

    def test_260(self):
        """Function Calling Itself"""
        self.assertTrue(TestParser.checkParser("""
            func recurse(x int) {
                if (x > 0) {
                    recurse(x - 1);
                }
            }
        """, "successful", 260))
        
    def test_261(self):
        """Integer Division"""
        self.assertTrue(TestParser.checkParser("const result = 10 / 2;", "successful", 261))

    def test_262(self):
        """Modulo Operation"""
        self.assertTrue(TestParser.checkParser("const remainder = 10 % 3;", "successful", 262))

    def test_263(self):
        """Bitwise AND Operation"""
        self.assertTrue(TestParser.checkParser("const bitwiseAnd = 5 && 3;", "successful", 263))

    def test_264(self):
        """Bitwise OR Operation"""
        self.assertTrue(TestParser.checkParser("const bitwiseOr = 5 || 3;", "successful", 264))

    def test_265(self):
        """Negative Number Constant"""
        self.assertTrue(TestParser.checkParser("const negValue = -100;", "successful", 265))

    def test_266(self):
        """Array with Mixed Types (Invalid)"""
        self.assertTrue(TestParser.checkParser("""var arr = [1, "hello", 3.14];""", "Error on line 1 col 13: ,", 266))

    def test_267(self):
        """Struct with Uninitialized Field"""
        self.assertTrue(TestParser.checkParser("""
            type Employee struct {
                name string;
                salary float;
            }
        """, "successful", 267))

    def test_268(self):
        """Function with No Return"""
        self.assertTrue(TestParser.checkParser("""
            func doSomething() {
                var x = 5;
                x += 10;
            }
        """, "successful", 268))

    def test_269(self):
        """Function Returning Struct"""
        self.assertTrue(TestParser.checkParser("""
            func createPerson() Person {
                return Person{name: "John", age: 30};
            }
        """, "successful", 269))

    def test_270(self):
        """While Loop"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                for x < 10 {
                    x += 1;
                }
            }
        """, "successful", 270))

    def test_271(self):
        """Invalid For Loop Syntax"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                for (x < 10) x += 1;
            }
        """, "Error on line 3 col 30: x", 271))

    def test_272(self):
        """Function with Multiple Return Types"""
        self.assertTrue(TestParser.checkParser("""
            func getData() (int, string) {
                return 10, "hello";
            }
        """, "Error on line 2 col 28: (", 272))

    def test_273(self):
        """Switch Case Statement"""
        self.assertTrue(TestParser.checkParser("""
            func checkValue(x int) {
                if (x) {
                    print("One");
                }else if(y){
                    print("Two");
                } else{
                    print("Other");
                }
            }
        """, "successful", 273))

    def test_274(self):
        """Nested If-Else Statement"""
        self.assertTrue(TestParser.checkParser("""
            func checkValue(x int) {
                if (x > 0) {
                    if (x < 10) {
                        print("Single digit positive");
                    } else {
                        print("Two-digit or more");
                    }
                } else {
                    print("Negative or zero");
                }
            }
        """, "successful", 274))

    def test_275(self):
        """Assigning Function Call to Variable"""
        self.assertTrue(TestParser.checkParser("""
            func getNumber() int {
                return 42;
            }
            var num = getNumber();
        """, "successful", 275))

    def test_276(self):
        """Accessing Array Out of Bounds (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            var arr [5]int;
            const value = arr[10];
        """, "successful", 276))

    def test_277(self):
        """Struct with Method Definition (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            type Car struct {
                func drive() {
                    print("Driving");
                }
            }
        """, "Error on line 3 col 17: func", 277))

    def test_278(self):
        """Using Struct as Function Argument"""
        self.assertTrue(TestParser.checkParser("""
            type Person struct {
                name string;
                age int;
            }
            func greet(p Person) {
                print("Hello " + p.name);
            }
        """, "successful", 278))

    def test_279(self):
        """Using Struct Inside Another Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Address struct {
                city string;
                zip int;
            }
            type Person struct {
                name string;
                addr Address;
            }
        """, "successful", 279))

    def test_280(self):
        """Function with Incorrect Return Type"""
        self.assertTrue(TestParser.checkParser("""
            func getName() int {
                return "John";
            }
        """, "successful", 280))
        
    def test_281(self):
        """Complex Arithmetic Expression"""
        self.assertTrue(TestParser.checkParser("""
            const result = ((a + b) * c) / (d - e) + f;
        """, "successful", 281))

    def test_282(self):
        """Struct with Nested Structs"""
        self.assertTrue(TestParser.checkParser("""
            type Address struct {
                street string;
                city string;
            }
            type Person struct {
                name string;
                address Address;
            }
        """, "successful", 282))

    def test_283(self):
        """Nested Array and Struct Access"""
        self.assertTrue(TestParser.checkParser("""
            func foo(){
                matrix[0][1+1] := [2][4]float{{1.1, a, 0., 7.e-9}, {3.13, 4.4, b, 2.0e10}}
                data[99-a*b+c/d%f].info.details[2] := StructType{field1: 10, field2: "text"};
            }

            func test_assign() {
                result := records[5].entries[i-7].compute(42,g,h,(u+7)*3,p-9);
            }
        """, "successful", 283))

    def test_284(self):
        """Array with Invalid Syntax"""
        self.assertTrue(TestParser.checkParser("var arr [5] = {1, 2, 3, 4, 5};", "Error on line 1 col 13: =", 284))

    def test_285(self):
        """Interface with Method"""
        self.assertTrue(TestParser.checkParser("""
            type Drawable interface {
                Draw() void;
            }
        """, "successful", 285))

    def test_286(self):
        """Invalid Function Definition with Missing Parentheses"""
        self.assertTrue(TestParser.checkParser("func sum a, b int { return a + b; }", "Error on line 1 col 10: a", 286))

    def test_287(self):
        """Valid for Loop"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                for (x < 10) {
                    x += 1;
                }
            }
        """, "successful", 287))

    def test_288(self):
        """Invalid While Loop Missing Condition"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                while {
                    x += 1;
                }
            }
        """, "Error on line 3 col 23: {", 288))

    def test_289(self):
        """Chained Function Calls"""
        self.assertTrue(TestParser.checkParser("const result = foo().bar()[4][5].baz();", "successful", 289))

    def test_290(self):
        """Function with Boolean Return"""
        self.assertTrue(TestParser.checkParser("""
            func isEven(num int) bool {
                return num % 2 == 0;
            }
        """, "successful", 290))

    def test_291(self):
        """Complex Logical Expression"""
        self.assertTrue(TestParser.checkParser("const check = (a && b) || !(c && d);", "successful", 291))

    def test_292(self):
        """Struct with Invalid Array Field"""
        self.assertTrue(TestParser.checkParser("""
            type Student struct {
                grades [int];
            }
        """, "Error on line 3 col 25: int", 292))

    def test_293(self):
        """Function with Parameter"""
        self.assertTrue(TestParser.checkParser("""
            func greet(name, home, file  string, year date) {
                print("Hello, " + name);
            }
        """, "successful", 293))

    def test_294(self):
        """Function with Default Parameter"""
        self.assertTrue(TestParser.checkParser("""
            func greet(name string = "Guest") {
                print("Hello, " + name);
            }
        """, "Error on line 2 col 36: =", 294))

    def test_295(self):
        """Struct Array Initialization"""
        self.assertTrue(TestParser.checkParser("""
            type Employee struct {
                name string;
            }
            var employees [3]Employee = [3]Employee{
                {"Alice","David"},
                {"Bob"},
                {"Charlie"}};
        """, "successful", 295))

    def test_296(self):
        """Loop with Array Iteration"""
        self.assertTrue(TestParser.checkParser("""
            func arrayLoop() {
                var arr [5]int = [5]int{1, 2, 3, 4, 5};
                for i := 0; i < 5; i += 1 {
                    print(arr[i]);
                }
            }
        """, "successful", 296))

    def test_297(self):
        """Loop with Struct Array"""
        self.assertTrue(TestParser.checkParser("""
            func structArrayLoop() {
                for i := 0; i < 10; i += 1 {
                    people[i].name := "Person" + str(i);
                }
            }
        """, "successful", 297))

    def test_298(self):
        """Loop with Function Call and Condition"""
        self.assertTrue(TestParser.checkParser("""
            func conditionalFunctionLoop() {
                for i := 0; i < 5; i += 1 {
                    if (checkValue(i)) {
                        print(i);
                    }
                }
            }
        """, "successful", 298))

    def test_299(self):
        """Nested Struct Initialization"""
        self.assertTrue(TestParser.checkParser("""
            type Engine struct {
                horsepower int;
            }
            type Car struct {
                model string;
                engine Engine;
            }
            const myCar = Car{a: "Tesla", b: Engine{c: 400}};
        """, "successful", 299))

    def test_300(self):
        """Invalid Missing Semicolon"""
        self.assertTrue(TestParser.checkParser("const x = 10 const y = 20;", "Error on line 1 col 14: const", 300))