# 2252377 - Nguyen Minh Khoi
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))

    def test_keyword_if(self):
        self.assertTrue(TestLexer.checkLexeme("if","if,<EOF>",105))
    
    def test_keyword_else(self):
        self.assertTrue(TestLexer.checkLexeme("else","else,<EOF>",106))
    
    def test_keyword_for(self):
        self.assertTrue(TestLexer.checkLexeme("for","for,<EOF>",107))
    
    def test_keyword_return(self):
        self.assertTrue(TestLexer.checkLexeme("return","return,<EOF>",108))
    
    def test_keyword_type(self):
        self.assertTrue(TestLexer.checkLexeme("type","type,<EOF>",109))
    
    def test_keyword_struct(self):
        self.assertTrue(TestLexer.checkLexeme("struct","struct,<EOF>",110))
    
    def test_keyword_interface(self):
        self.assertTrue(TestLexer.checkLexeme("interface","interface,<EOF>",111))
    
    def test_keyword_string(self):
        self.assertTrue(TestLexer.checkLexeme("string","string,<EOF>",112))
    
    def test_keyword_int(self):
        self.assertTrue(TestLexer.checkLexeme("int","int,<EOF>",113))
    
    def test_keyword_float(self):
        self.assertTrue(TestLexer.checkLexeme("float","float,<EOF>",114))
    
    def test_keyword_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("boolean","boolean,<EOF>",115))
    
    def test_keyword_const(self):
        self.assertTrue(TestLexer.checkLexeme("const","const,<EOF>",116))
    
    def test_keyword_continue(self):
        self.assertTrue(TestLexer.checkLexeme("continue","continue,<EOF>",117))
    
    def test_keyword_break(self):
        self.assertTrue(TestLexer.checkLexeme("break","break,<EOF>",118))
    
    def test_keyword_range(self):
        self.assertTrue(TestLexer.checkLexeme("range","range,<EOF>",119))
    
    def test_keyword_nil(self):
        self.assertTrue(TestLexer.checkLexeme("nil","nil,<EOF>",120))
    
    def test_operator_add(self):
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>",121))
    
    def test_operator_sub(self):
        self.assertTrue(TestLexer.checkLexeme("-","-,<EOF>",122))
    
    def test_operator_mul(self):
        self.assertTrue(TestLexer.checkLexeme("*","*,<EOF>",123))
    
    def test_operator_div(self):
        self.assertTrue(TestLexer.checkLexeme("/","/,<EOF>",124))
    
    def test_operator_mod(self):
        self.assertTrue(TestLexer.checkLexeme("%","%,<EOF>",125))
    
    def test_operator_eq(self):
        self.assertTrue(TestLexer.checkLexeme("=","=,<EOF>",126))
    
    def test_operator_dbl_eq(self):
        self.assertTrue(TestLexer.checkLexeme("==","==,<EOF>",127))
    
    def test_operator_not_eq(self):
        self.assertTrue(TestLexer.checkLexeme("!=","!=,<EOF>",128))
    
    def test_operator_lt(self):
        self.assertTrue(TestLexer.checkLexeme("<","<,<EOF>",129))
    
    def test_operator_le(self):
        self.assertTrue(TestLexer.checkLexeme("<=","<=,<EOF>",130))
    
    def test_operator_gt(self):
        self.assertTrue(TestLexer.checkLexeme(">",">,<EOF>",131))
    
    def test_operator_ge(self):
        self.assertTrue(TestLexer.checkLexeme(">=",">=,<EOF>",132))
    
    def test_operator_and(self):
        self.assertTrue(TestLexer.checkLexeme("&&","&&,<EOF>",133))
    
    def test_operator_or(self):
        self.assertTrue(TestLexer.checkLexeme("||","||,<EOF>",134))
    
    def test_operator_not(self):
        self.assertTrue(TestLexer.checkLexeme("!","!,<EOF>",135))
        
    def test_newline_1(self):
        """Test single newline ignored"""
        self.assertTrue(TestLexer.checkLexeme("+\nxyz", "+,xyz,<EOF>", 136))
    
    def test_newline_2(self):
        """Test newline converted to semicolon"""
        self.assertTrue(TestLexer.checkLexeme("abc\nxyz", "abc,;,xyz,<EOF>", 137))
    
    def test_newline_3(self):
        """Test multiple newlines with different cases"""
        self.assertTrue(TestLexer.checkLexeme("123\n456\n+\nabc", "123,;,456,;,+,abc,<EOF>", 138))
    
    def test_newline_4(self):
        """Test newline after keyword"""
        self.assertTrue(TestLexer.checkLexeme("if\nxyz", "if,xyz,<EOF>", 139))
    
    def test_newline_5(self):
        """Test newline after return statement"""
        self.assertTrue(TestLexer.checkLexeme("return\n5", "return,;,5,<EOF>", 140))
    
    def test_newline_6(self):
        """Test newline inside function declaration"""
        self.assertTrue(TestLexer.checkLexeme("func\nabc()", "func,abc,(,),<EOF>", 141))
    
    def test_newline_7(self):
        """Test newline inside arithmetic expression"""
        self.assertTrue(TestLexer.checkLexeme("1+2\n3+4", "1,+,2,;,3,+,4,<EOF>", 142))
    
    def test_newline_8(self):
        """Test newline ignored between brackets"""
        self.assertTrue(TestLexer.checkLexeme("(\n)\n", "(,),;,<EOF>", 143))
    
    def test_newline_9(self):
        """Test newline conversion after continue statement"""
        self.assertTrue(TestLexer.checkLexeme("continue\nxyz", "continue,;,xyz,<EOF>", 144))
    
    def test_newline_10(self):
        """Test newline conversion after break statement"""
        self.assertTrue(TestLexer.checkLexeme("break\nxyz", "break,;,xyz,<EOF>", 145))
        
    def test_single_line_comment(self):
        """Test single-line comment"""
        self.assertTrue(TestLexer.checkLexeme("// this is a comment\nabc", "abc,<EOF>", 146))
    
    def test_multi_line_comment(self):
        """Test multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme("/* this is \n a comment */ abc", "abc,<EOF>", 147))
    
    def test_comment_between_code(self):
        """Test comment between valid code"""
        self.assertTrue(TestLexer.checkLexeme("abc // comment \n xyz", "abc,;,xyz,<EOF>", 148))
    
    def test_nested_multiline_comment(self):
        """Test nested multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme("/* Outer /* Inner */ Outer */ abc", "abc,<EOF>", 149))
    
    def test_comment_after_operator(self):
        """Test comment after an operator"""
        self.assertTrue(TestLexer.checkLexeme("a + b // sum of a and b\nc", "a,+,b,;,c,<EOF>", 150))
    
    def test_comment_within_expression(self):
        """Test comment inside an expression"""
        self.assertTrue(TestLexer.checkLexeme("(1 + /* ignore this */ 2) * 3", "(,1,+,2,),*,3,<EOF>", 151))
    
    def test_multiline_comment_between_statements(self):
        """Test multi-line comment between statements"""
        self.assertTrue(TestLexer.checkLexeme("return 5 /* comment */ + 6", "return,5,+,6,<EOF>", 152))
    
    def test_comment_before_block(self):
        """Test comment before a block"""
        self.assertTrue(TestLexer.checkLexeme("// function start\nfunc main() { return; }", "func,main,(,),{,return,;,},<EOF>", 153))
    
    def test_comment_with_keywords(self):
        """Test comment inside keyword sequence"""
        self.assertTrue(TestLexer.checkLexeme("if /* condition */ (x > 0) { return; }", "if,(,x,>,0,),{,return,;,},<EOF>", 154))
    
    def test_comment_before_newline_conversion(self):
        """Test comment before newline conversion"""
        self.assertTrue(TestLexer.checkLexeme("abc // comment\nxyz", "abc,;,xyz,<EOF>", 155))
    
    def test_comment_at_end_of_line(self):
        """Test comment at the end of a line"""
        self.assertTrue(TestLexer.checkLexeme("x = 5; // setting x\ny = 6;", "x,=,5,;,y,=,6,;,<EOF>", 156))
    
    def test_comment_after_block_end(self):
        """Test comment after block closing"""
        self.assertTrue(TestLexer.checkLexeme("} // end of function\nelse { x = 1; }", "},;,else,{,x,=,1,;,},<EOF>", 157))
    
    def test_comment_before_operator(self):
        """Test comment before an operator"""
        self.assertTrue(TestLexer.checkLexeme("a /* plus */ + b", "a,+,b,<EOF>", 158))
    
    def test_multiline_comment_with_operators(self):
        """Test multi-line comment with operators"""
        self.assertTrue(TestLexer.checkLexeme("a /* ignore */ + /* ignore */ b", "a,+,b,<EOF>", 159))
    
    def test_multiline_comment_with_keywords(self):
        """Test multi-line comment inside a keyword block"""
        self.assertTrue(TestLexer.checkLexeme("if (/* cond */ x > 0) return;", "if,(,x,>,0,),return,;,<EOF>", 160))
    
    def test_multiline_comment_with_numbers(self):
        """Test multi-line comment around numbers"""
        self.assertTrue(TestLexer.checkLexeme("123 /* number */ + 456", "123,+,456,<EOF>", 161))
    
    def test_comment_between_nested_brackets(self):
        """Test comment between nested brackets"""
        self.assertTrue(TestLexer.checkLexeme("func abc() { /* inside block */ return; }", "func,abc,(,),{,return,;,},<EOF>", 162))
    
    def test_comment_inside_function_arguments(self):
        """Test comment inside function argument list"""
        self.assertTrue(TestLexer.checkLexeme("print(1, /* ignore this */ 2, 3)", "print,(,1,,,2,,,3,),<EOF>", 163))
    
    def test_comment_inside_expression_with_newline(self):
        """Test comment inside expression with newline"""
        self.assertTrue(TestLexer.checkLexeme("(a + b /* mid-comment */\n) * c", "(,a,+,b,;,),*,c,<EOF>", 164))
    
    def test_complex_program_1(self):
        """Test a more complex program"""
        self.assertTrue(TestLexer.checkLexeme("func main() { var x int = 10; for i := 0; i < x; i += 1 { print(i); } }", "func,main,(,),{,var,x,int,=,10,;,for,i,:=,0,;,i,<,x,;,i,+=,1,{,print,(,i,),;,},},<EOF>", 165))
    
    def test_complex_program_2(self):
        """Test complex program with loops, functions, and structs"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            type Rectangle struct {
                Width int
                Height int
            }
            
            func (r Rectangle) Area() int {
                return r.Width * r.Height
            }
            
            func main() {
                var rect Rectangle = Rectangle{10, 5}
                print(rect.Area())
            }
            """,
            "type,Rectangle,struct,{,Width,int,;,Height,int,;,},;,func,(,r,Rectangle,),Area,(,),int,{,return,r,.,Width,*,r,.,Height,;,},;,func,main,(,),{,var,rect,Rectangle,=,Rectangle,{,10,,,5,},;,print,(,rect,.,Area,(,),),;,},;,<EOF>",
            166
        ))
    
    def test_complex_program_3(self):
        """Test complex program with interface and multiple functions"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            type Shape interface  {
                Area() float
                Perimeter() float
            }
            
            type Circle struct {
                Radius float
            }
            
            func (c Circle) Area() float {
                return 3.14 * c.Radius * c.Radius
            }
            
            func (c Circle) Perimeter() float {
                return 2 * 3.14 * c.Radius
            }
            
            func main() {
                var c Circle = Circle{5.0}
                print(c.Area())
                print(c.Perimeter())
            }
            """,
            "type,Shape,interface,{,Area,(,),float,;,Perimeter,(,),float,;,},;,type,Circle,struct,{,Radius,float,;,},;,func,(,c,Circle,),Area,(,),float,{,return,3.14,*,c,.,Radius,*,c,.,Radius,;,},;,func,(,c,Circle,),Perimeter,(,),float,{,return,2,*,3.14,*,c,.,Radius,;,},;,func,main,(,),{,var,c,Circle,=,Circle,{,5.0,},;,print,(,c,.,Area,(,),),;,print,(,c,.,Perimeter,(,),),;,},;,<EOF>",
            167
        ))        
    
    def test_nested_comment_with_loop(self):
        """Test nested comments inside a for loop"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            func main() {
                var x int = 10 /* Outer comment
                /* Nested comment */
                Still in outer comment */
                for x > 0 {
                    print(x)
                    x = x - 1
                }
            }
            """,
            "func,main,(,),{,var,x,int,=,10,;,for,x,>,0,{,print,(,x,),;,x,=,x,-,1,;,},;,},;,<EOF>",
            168
        ))
        
    def test_illegal_escape_upcase(self): 
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme("""check"string\\G" ""","""check,Illegal escape in string: "string\G""",169))
    
    def test_illegal_escape_lowcase(self): 
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme("""invalid"test\\y" ""","""invalid,Illegal escape in string: "test\y""",170))
    
    
    def test_simple_function(self):
        """Test simple function definition"""
        self.assertTrue(TestLexer.checkLexeme("func add(a int, b int) int { return a + b; }", "func,add,(,a,int,,,b,int,),int,{,return,a,+,b,;,},<EOF>", 171))
    
    def test_if_statement(self):
        """Test if statement"""
        self.assertTrue(TestLexer.checkLexeme("if x > 0 { return; }", "if,x,>,0,{,return,;,},<EOF>", 172))
    
    def test_for_loop(self):
        """Test for loop"""
        self.assertTrue(TestLexer.checkLexeme("for i := 0; i < 9; i += 1 { print(i); }", "for,i,:=,0,;,i,<,9,;,i,+=,1,{,print,(,i,),;,},<EOF>", 173))
    
    def test_struct_declaration(self):
        """Test struct declaration"""
        self.assertTrue(TestLexer.checkLexeme("type Person struct { Name string; Age int; }", "type,Person,struct,{,Name,string,;,Age,int,;,},<EOF>", 174))
    
    def test_function_call(self):
        """Test function call"""
        self.assertTrue(TestLexer.checkLexeme("result := add(3, 4)", "result,:=,add,(,3,,,4,),<EOF>", 175))
    
    def test_nested_if_else(self):
        """Test nested if-else statement"""
        self.assertTrue(TestLexer.checkLexeme("if x > 0 { if y > 0 { return x; } else { return y; } }", "if,x,>,0,{,if,y,>,0,{,return,x,;,},else,{,return,y,;,},},<EOF>", 176))
    
    def test_array_declaration(self):
        """Test array declaration"""
        self.assertTrue(TestLexer.checkLexeme("var arr [5]int", "var,arr,[,5,],int,<EOF>", 177))
    
    def test_multiline_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""
        x /* comment
        */ """, "x,<EOF>", 178))
    
    def test_illegal_escape_number(self): 
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" sample"text\\7" ""","""sample,Illegal escape in string: "text\\7""",179))
        
    def test_nested_comment_in_function(self):
        """Test nested comments inside a function"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            func example() {
                /* Outer comment
                /* Nested comment */
                End of outer comment */
                print("Hello World")
            }
            """,
            "func,example,(,),{,print,(,\"Hello World\",),;,},;,<EOF>",
            180
        ))

    def test_nested_comment_in_struct(self):
        """Test nested comments inside a struct definition"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            type Person struct {
                /* Name of person
                /* Nested description */
                More details */
                name string
                age int
            }
            """,
            "type,Person,struct,{,name,string,;,age,int,;,},;,<EOF>",
            181
        ))
    
    def test_nested_comment_with_if_else(self):
        """Test nested comments in an if-else block"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            func checkNumber(n int) bool {
                /* Checking number
                /* Nested checking */
                End of comment */
                if n > 0 {
                    return true
                } else {
                    return false
                }
            }
            """,
            "func,checkNumber,(,n,int,),bool,{,if,n,>,0,{,return,true,;,},else,{,return,false,;,},;,},;,<EOF>",
            182
        ))

    def test_nested_comment_with_for_loop(self):
        """Test nested comments inside a for loop"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            func loopExample() {
                /* Loop starts here
                /* Nested comment */
                End of comment */
                for i := 0; i < 10; i += 1 {
                    print(i)
                }
            }
            """,
            "func,loopExample,(,),{,for,i,:=,0,;,i,<,10,;,i,+=,1,{,print,(,i,),;,},;,},;,<EOF>",
            183
        ))
        
    def test_short_nested_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func foo() { /* Comment /* Nested */ */ return; }
        """, "func,foo,(,),{,return,;,},;,<EOF>", 184))
    
    def test_short_nested_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var x int /* Comment /* Nested */ */
        """, "var,x,int,;,<EOF>", 185))
    
    def test_short_nested_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* Start /* Inner */ End */ type A int
        """, "type,A,int,;,<EOF>", 186))
    
    def test_short_nested_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* /* */ */ var y float
        """, "var,y,float,;,<EOF>", 187))
    
    def test_short_nested_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* Outer /* Inner */ */ func bar() {}
        """, "func,bar,(,),{,},;,<EOF>", 188))
    
    def test_short_nested_comment_6(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* A /* B */ C */ return
        """, "return,;,<EOF>", 189))
    
    def test_short_nested_comment_7(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* /* */ */ if true {}
        """, "if,true,{,},;,<EOF>", 190))
    
    def test_short_nested_comment_8(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* Outer /* Inner */ */ break;
        """, "break,;,<EOF>", 191))
    
    def test_short_nested_comment_9(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* Test /* Case */ */ continue;
        """, "continue,;,<EOF>", 192))
    
    def test_short_nested_comment_10(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* Nested /* in */ comment */ func test() {}
        """, "func,test,(,),{,},;,<EOF>", 193))
        
    def test_unclose_string_1(self):
        self.assertTrue(TestLexer.checkLexeme("""var str string = "Hello world ;""", """var,str,string,=,Unclosed string: "Hello world ;""", 194))
    
    def test_unclose_string_2(self):
        self.assertTrue(TestLexer.checkLexeme("""Escaped newline "hello\nvar y = 10;""", """Escaped,newline,Unclosed string: "hello""", 195))
        
    def test_invalid_character_1(self):
        self.assertTrue(TestLexer.checkLexeme("#define", "ErrorToken #", 196))
    
    def test_invalid_character_2(self):
        self.assertTrue(TestLexer.checkLexeme("var a = 5 ^ 3;", "var,a,=,5,ErrorToken ^", 197))
    
    def test_invalid_character_3(self):
        self.assertTrue(TestLexer.checkLexeme("var x ~ 10;", "var,x,ErrorToken ~", 198))
    
    def test_invalid_character_4(self):
        self.assertTrue(TestLexer.checkLexeme("$specialVar = 42;", "ErrorToken $", 199))
        
    def test_illegal_escape_operator(self): 
        self.assertTrue(TestLexer.checkLexeme(""" error"case\\%" ""","""error,Illegal escape in string: "case\%""", 200))