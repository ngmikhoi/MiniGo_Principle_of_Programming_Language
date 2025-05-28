// 2252377 - Nguyen Minh Khoi
grammar MiniGo;
@lexer::header {
from lexererr import *
# 2252377 - Nguyen Minh Khoi
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.lastToken = None

def emit(self):
    tk = self.type
    self.lastToken = tk;
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();

def convertNL(self):
    if self.lastToken is not None and self.lastToken in {
        self.ID, self.INT, self.FLOAT, self.BOOLEAN, self.STRING,
        self.DEC, self.BIN, self.OCT, self.HEX, self.FLOAT_LIT, self.TRUE, self.FALSE, self.STRING_LIT, self.NIL,
        self.RETURN, self.CONTINUE, self.BREAK,
        self.RCIB, self.RSQB, self.RCUB
    }:
        self.type = self.SECO
        self.text = ";"
    else:
        self.skip()
}

options{
	language=Python3;
}

NL: ('\n' | '\r\n'){self.convertNL()};

WS : [ \t\r\f]+ -> skip ;

SG_CMT: '//' ~[\r\n]* -> skip;
MUL_CMT: '/*' (MUL_CMT | ~'*' | ('*' ~'/'))* '*/' -> skip;

IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

DBL_EQ: '==';
NOT_EQ: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';

AND: '&&';
OR: '||';
NOT: '!';

AS_EQ: ':=';
ADD_EQ: '+=';
SUB_EQ: '-=';
MUL_EQ: '*=';
DIV_EQ: '/=';
MOD_EQ: '%=';

EQ: '=';
DOT: '.';

LCIB: '(';
RCIB: ')';
LCUB: '{';
RCUB: '}';
LSQB: '[';
RSQB: ']';
COMMA: ',';
SECO: ';';

COLON: ':';

ID: [A-Za-z_][A-Za-z0-9_]*;

DEC: '0' | [1-9][0-9]*;
BIN: '0' [bB] [01]+;
OCT: '0' [oO] [0-7]+;
HEX: '0' [xX] [0-9a-fA-F]+;

int_lit: DEC | BIN | OCT | HEX;

FLOAT_LIT:  [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?;

fragment ESC_SEQ: '\\n' | '\\t' | '\\r' | '\\"' | ('\\' '\\');
fragment STRING_SEQ: ESC_SEQ | ~[\r\n\\"];
STRING_LIT: '"' STRING_SEQ* '"';

bool_lit: TRUE | FALSE;

ERROR_CHAR: . {raise ErrorToken(self.text)};

ILLEGAL_ESCAPE: '"' STRING_SEQ* '\\' ~[ntr"\\] {raise IllegalEscape(self.text)};

UNCLOSE_STRING: '"' STRING_SEQ* ('\r\n' | '\n' | EOF)
{
    if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[:-1])
    else:
        raise UncloseString(self.text)
};

//##################################   LEXER finish   ###################################################################################


//##################################   PARSER start   ###################################################################################
program  : manydecl EOF ;
manydecl: decl manydecl | decl;

//-------------------------------------------Statements------------------------------------------------------------------------------------------------------
stmt:   var_decl | const_decl
        | assign_stmt | func_call_stmt | if_stmt | for_stmt
        | break_stmt | continue_stmt | return_stmt
        ;

//----------------------------------------------Block-------------------------------------------------------------------------------------------

stmt_block: stmt stmt_block | stmt;

//-----------------------------------------Declarations----------------------------------------------------------------------------------------

decl: var_decl | const_decl |func_decl | struct_decl |interface_decl;

//---------------------------------------Variable declaration-----------------------------------------------------------------------------------

var_decl: var_decl_init | var_decl_uninit;

var_decl_init: VAR ID (all_type | ) EQ expr1 SECO;

var_decl_uninit: VAR ID all_type SECO;

//---------------------------------------Constant declaration-----------------------------------------------------------------------------------

const_decl: CONST ID EQ expr1 SECO;

//-----------------------------------------Function declaration--------------------------------------------------------------------------------------------------

func_decl: FUNC ((LCIB ID ID RCIB) | )  ID LCIB (list_para | ) RCIB (all_type | ) LCUB stmt_block RCUB SECO;

//------------------------------Function call statement-----------------------------------------------------------------------------------------

star_dot_func_call: DOT func_call star_dot_func_call | ;
func_call_stmt: func_call star_dot_func_call SECO;

star_lhs_dot: (lhs DOT) star_lhs_dot | ;
func_call:  star_lhs_dot ID LCIB (list_arg | ) RCIB;

list_arg: arg tail_arg | arg;
tail_arg: COMMA arg tail_arg | ;

arg: expr1;

//-------------------------------------------------Array declaration--------------------------------------------------------------------------------------------

arr_dim_decl: (LSQB (int_lit | ID) RSQB) arr_dim_decl | (LSQB (int_lit | ID) RSQB);

arr_type: arr_dim_decl all_type;

arr_lit: arr_type LCUB list_ele_arr RCUB;

list_ele_arr: ele_arr tail_ele_arr | ele_arr;
tail_ele_arr: COMMA ele_arr tail_ele_arr | ;

ele_arr: int_lit | FLOAT_LIT | STRING_LIT | bool_lit | NIL | struct_lit | ID | LCUB list_ele_arr RCUB;

//-------------------------------- Struct-Method declaration---------------------------------------------------------------------------------------------------------------------------

struct_decl: TYPE ID STRUCT LCUB star_struct_ele_decl RCUB SECO;

star_struct_ele_decl: attr_decl star_struct_ele_decl | attr_decl;

attr_decl: ID all_type SECO;

struct_lit: ID LCUB (list_ele_struct| ) RCUB;

list_ele_struct: ele_struct tail_ele_struct | ele_struct;
tail_ele_struct: COMMA ele_struct tail_ele_struct | ;

ele_struct: ID COLON expr1;

//-----------------------------------Interface declaration----------------------------------------------------------------------------------------------

star_interface_method_decl: method_interface star_interface_method_decl | method_interface;

interface_decl: TYPE ID INTERFACE LCUB star_interface_method_decl  RCUB SECO;

not_last_para: para tail_para;
tail_para: COMMA para tail_para | ;
para: ID (all_type | );
last_para: ID all_type;

list_para: ((not_last_para COMMA) | ) last_para; 
method_interface: ID LCIB (list_para | ) RCIB (all_type | ) SECO;

//--------------------------------------Assignment statement--------------------------------------------------------------------------------------

assign_stmt: lhs assign_op expr1 SECO;

assign_op: AS_EQ | ADD_EQ | SUB_EQ | MUL_EQ | DIV_EQ | MOD_EQ;

//-----------------------------------------If statement-----------------------------------------------------------------------------------------

else_if: (ELSE IF LCIB condit RCIB LCUB stmt_block RCUB) else_if | ;
if_stmt: IF LCIB condit RCIB LCUB stmt_block RCUB 
    else_if
    ((ELSE LCUB stmt_block RCUB) | )
    SECO;

//--------------------------------------For statement--------------------------------------------------------------------------------------------

for_stmt: basic_for | init_for | range_for;

basic_for: FOR condit  LCUB stmt_block RCUB SECO;

init_for: FOR init condit SECO update LCUB stmt_block RCUB SECO;
init: assign_stmt | var_decl_init;
condit: expr1;
update: lhs assign_op expr1;

range_for: FOR (index | blank) COMMA value AS_EQ RANGE array_id LCUB stmt_block RCUB SECO;
index: ID;
blank: '_';
value: ID;
array_id: expr1;

//-----------------------------------Other statement-------------------------------------------------------------------------------------------------
break_stmt: BREAK SECO; 
continue_stmt: CONTINUE SECO;
return_stmt: RETURN (expr1 | ) SECO;
//------------------------------------Expressions------------------------------------------------------------------------------------------------

rela_op: DBL_EQ | NOT_EQ | LT | LE | GT | GE ;

expr1: expr1 OR expr2 | expr2;
expr2: expr2 AND expr3 | expr3;
expr3: expr3 rela_op expr4 | expr4;
expr4: expr4 (ADD | SUB) expr5 | expr5;
expr5: expr5 (MUL | DIV | MOD) expr6 | expr6;
expr6: (NOT | SUB) expr6 | expr7;
expr7: expr7 DOT (ID | func_call) | expr7 LSQB expr1 RSQB | operand;

star_dot_dim: ((DOT ID) | dim) star_dot_dim | ;
lhs: ID star_dot_dim;

dim: LSQB expr1 RSQB;

operand: lit | ID | func_call | LCIB expr1 RCIB;

lit: int_lit | FLOAT_LIT | STRING_LIT | bool_lit | NIL | struct_lit | arr_lit;

primi: INT | FLOAT | BOOLEAN | STRING;

all_type: ID | primi | arr_type;