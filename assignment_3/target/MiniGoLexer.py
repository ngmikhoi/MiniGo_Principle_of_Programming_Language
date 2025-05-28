# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
# 2252377 - Nguyen Minh Khoi



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01e4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\5\2\u008d\n\2\3\2\3\2\3\3\6\3\u0092")
        buf.write("\n\3\r\3\16\3\u0093\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u009c")
        buf.write("\n\4\f\4\16\4\u009f\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\7\5\u00aa\n\5\f\5\16\5\u00ad\13\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\79\u0175\n9\f9\169\u0178\13")
        buf.write("9\3:\3:\3:\7:\u017d\n:\f:\16:\u0180\13:\5:\u0182\n:\3")
        buf.write(";\3;\3;\6;\u0187\n;\r;\16;\u0188\3<\3<\3<\6<\u018e\n<")
        buf.write("\r<\16<\u018f\3=\3=\3=\6=\u0195\n=\r=\16=\u0196\3>\6>")
        buf.write("\u019a\n>\r>\16>\u019b\3>\3>\7>\u01a0\n>\f>\16>\u01a3")
        buf.write("\13>\3>\3>\5>\u01a7\n>\3>\6>\u01aa\n>\r>\16>\u01ab\5>")
        buf.write("\u01ae\n>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u01ba\n?\3")
        buf.write("@\3@\5@\u01be\n@\3A\3A\7A\u01c2\nA\fA\16A\u01c5\13A\3")
        buf.write("A\3A\3B\3B\3B\3C\3C\7C\u01ce\nC\fC\16C\u01d1\13C\3C\3")
        buf.write("C\3C\3C\3D\3D\7D\u01d9\nD\fD\16D\u01dc\13D\3D\3D\3D\5")
        buf.write("D\u01e1\nD\3D\3D\2\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;u<w=y>{?}\2\177\2\u0081@\u0083A\u0085")
        buf.write("B\u0087C\3\2\25\5\2\13\13\16\17\"\"\4\2\f\f\17\17\3\2")
        buf.write(",,\3\2\61\61\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62")
        buf.write(";\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CH")
        buf.write("ch\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\3\3")
        buf.write("\f\f\2\u01fb\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2")
        buf.write("\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u008c\3\2\2\2\5\u0091")
        buf.write("\3\2\2\2\7\u0097\3\2\2\2\t\u00a2\3\2\2\2\13\u00b3\3\2")
        buf.write("\2\2\r\u00b6\3\2\2\2\17\u00bb\3\2\2\2\21\u00bf\3\2\2\2")
        buf.write("\23\u00c6\3\2\2\2\25\u00cb\3\2\2\2\27\u00d0\3\2\2\2\31")
        buf.write("\u00d7\3\2\2\2\33\u00e1\3\2\2\2\35\u00e8\3\2\2\2\37\u00ec")
        buf.write("\3\2\2\2!\u00f2\3\2\2\2#\u00fa\3\2\2\2%\u0100\3\2\2\2")
        buf.write("\'\u0104\3\2\2\2)\u010d\3\2\2\2+\u0113\3\2\2\2-\u0119")
        buf.write("\3\2\2\2/\u011d\3\2\2\2\61\u0122\3\2\2\2\63\u0128\3\2")
        buf.write("\2\2\65\u012a\3\2\2\2\67\u012c\3\2\2\29\u012e\3\2\2\2")
        buf.write(";\u0130\3\2\2\2=\u0132\3\2\2\2?\u0135\3\2\2\2A\u0138\3")
        buf.write("\2\2\2C\u013a\3\2\2\2E\u013d\3\2\2\2G\u013f\3\2\2\2I\u0142")
        buf.write("\3\2\2\2K\u0145\3\2\2\2M\u0148\3\2\2\2O\u014a\3\2\2\2")
        buf.write("Q\u014d\3\2\2\2S\u0150\3\2\2\2U\u0153\3\2\2\2W\u0156\3")
        buf.write("\2\2\2Y\u0159\3\2\2\2[\u015c\3\2\2\2]\u015e\3\2\2\2_\u0160")
        buf.write("\3\2\2\2a\u0162\3\2\2\2c\u0164\3\2\2\2e\u0166\3\2\2\2")
        buf.write("g\u0168\3\2\2\2i\u016a\3\2\2\2k\u016c\3\2\2\2m\u016e\3")
        buf.write("\2\2\2o\u0170\3\2\2\2q\u0172\3\2\2\2s\u0181\3\2\2\2u\u0183")
        buf.write("\3\2\2\2w\u018a\3\2\2\2y\u0191\3\2\2\2{\u0199\3\2\2\2")
        buf.write("}\u01b9\3\2\2\2\177\u01bd\3\2\2\2\u0081\u01bf\3\2\2\2")
        buf.write("\u0083\u01c8\3\2\2\2\u0085\u01cb\3\2\2\2\u0087\u01d6\3")
        buf.write("\2\2\2\u0089\u008d\7\f\2\2\u008a\u008b\7\17\2\2\u008b")
        buf.write("\u008d\7\f\2\2\u008c\u0089\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u008f\b\2\2\2\u008f\4\3\2\2")
        buf.write("\2\u0090\u0092\t\2\2\2\u0091\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0096\b\3\3\2\u0096\6\3\2\2\2\u0097")
        buf.write("\u0098\7\61\2\2\u0098\u0099\7\61\2\2\u0099\u009d\3\2\2")
        buf.write("\2\u009a\u009c\n\3\2\2\u009b\u009a\3\2\2\2\u009c\u009f")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1\b\4\3\2")
        buf.write("\u00a1\b\3\2\2\2\u00a2\u00a3\7\61\2\2\u00a3\u00a4\7,\2")
        buf.write("\2\u00a4\u00ab\3\2\2\2\u00a5\u00aa\5\t\5\2\u00a6\u00aa")
        buf.write("\n\4\2\2\u00a7\u00a8\7,\2\2\u00a8\u00aa\n\5\2\2\u00a9")
        buf.write("\u00a5\3\2\2\2\u00a9\u00a6\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3")
        buf.write("\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af")
        buf.write("\7,\2\2\u00af\u00b0\7\61\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\u00b2\b\5\3\2\u00b2\n\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4")
        buf.write("\u00b5\7h\2\2\u00b5\f\3\2\2\2\u00b6\u00b7\7g\2\2\u00b7")
        buf.write("\u00b8\7n\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba\7g\2\2\u00ba")
        buf.write("\16\3\2\2\2\u00bb\u00bc\7h\2\2\u00bc\u00bd\7q\2\2\u00bd")
        buf.write("\u00be\7t\2\2\u00be\20\3\2\2\2\u00bf\u00c0\7t\2\2\u00c0")
        buf.write("\u00c1\7g\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7w\2\2\u00c3")
        buf.write("\u00c4\7t\2\2\u00c4\u00c5\7p\2\2\u00c5\22\3\2\2\2\u00c6")
        buf.write("\u00c7\7h\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7p\2\2\u00c9")
        buf.write("\u00ca\7e\2\2\u00ca\24\3\2\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\u00cd\7{\2\2\u00cd\u00ce\7r\2\2\u00ce\u00cf\7g\2\2\u00cf")
        buf.write("\26\3\2\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2\7v\2\2\u00d2")
        buf.write("\u00d3\7t\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5\7e\2\2\u00d5")
        buf.write("\u00d6\7v\2\2\u00d6\30\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8")
        buf.write("\u00d9\7p\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7g\2\2\u00db")
        buf.write("\u00dc\7t\2\2\u00dc\u00dd\7h\2\2\u00dd\u00de\7c\2\2\u00de")
        buf.write("\u00df\7e\2\2\u00df\u00e0\7g\2\2\u00e0\32\3\2\2\2\u00e1")
        buf.write("\u00e2\7u\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\7t\2\2\u00e4")
        buf.write("\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7i\2\2\u00e7")
        buf.write("\34\3\2\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7p\2\2\u00ea")
        buf.write("\u00eb\7v\2\2\u00eb\36\3\2\2\2\u00ec\u00ed\7h\2\2\u00ed")
        buf.write("\u00ee\7n\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7c\2\2\u00f0")
        buf.write("\u00f1\7v\2\2\u00f1 \3\2\2\2\u00f2\u00f3\7d\2\2\u00f3")
        buf.write("\u00f4\7q\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7n\2\2\u00f6")
        buf.write("\u00f7\7g\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7p\2\2\u00f9")
        buf.write("\"\3\2\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc\7q\2\2\u00fc")
        buf.write("\u00fd\7p\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff\7v\2\2\u00ff")
        buf.write("$\3\2\2\2\u0100\u0101\7x\2\2\u0101\u0102\7c\2\2\u0102")
        buf.write("\u0103\7t\2\2\u0103&\3\2\2\2\u0104\u0105\7e\2\2\u0105")
        buf.write("\u0106\7q\2\2\u0106\u0107\7p\2\2\u0107\u0108\7v\2\2\u0108")
        buf.write("\u0109\7k\2\2\u0109\u010a\7p\2\2\u010a\u010b\7w\2\2\u010b")
        buf.write("\u010c\7g\2\2\u010c(\3\2\2\2\u010d\u010e\7d\2\2\u010e")
        buf.write("\u010f\7t\2\2\u010f\u0110\7g\2\2\u0110\u0111\7c\2\2\u0111")
        buf.write("\u0112\7m\2\2\u0112*\3\2\2\2\u0113\u0114\7t\2\2\u0114")
        buf.write("\u0115\7c\2\2\u0115\u0116\7p\2\2\u0116\u0117\7i\2\2\u0117")
        buf.write("\u0118\7g\2\2\u0118,\3\2\2\2\u0119\u011a\7p\2\2\u011a")
        buf.write("\u011b\7k\2\2\u011b\u011c\7n\2\2\u011c.\3\2\2\2\u011d")
        buf.write("\u011e\7v\2\2\u011e\u011f\7t\2\2\u011f\u0120\7w\2\2\u0120")
        buf.write("\u0121\7g\2\2\u0121\60\3\2\2\2\u0122\u0123\7h\2\2\u0123")
        buf.write("\u0124\7c\2\2\u0124\u0125\7n\2\2\u0125\u0126\7u\2\2\u0126")
        buf.write("\u0127\7g\2\2\u0127\62\3\2\2\2\u0128\u0129\7-\2\2\u0129")
        buf.write("\64\3\2\2\2\u012a\u012b\7/\2\2\u012b\66\3\2\2\2\u012c")
        buf.write("\u012d\7,\2\2\u012d8\3\2\2\2\u012e\u012f\7\61\2\2\u012f")
        buf.write(":\3\2\2\2\u0130\u0131\7\'\2\2\u0131<\3\2\2\2\u0132\u0133")
        buf.write("\7?\2\2\u0133\u0134\7?\2\2\u0134>\3\2\2\2\u0135\u0136")
        buf.write("\7#\2\2\u0136\u0137\7?\2\2\u0137@\3\2\2\2\u0138\u0139")
        buf.write("\7>\2\2\u0139B\3\2\2\2\u013a\u013b\7>\2\2\u013b\u013c")
        buf.write("\7?\2\2\u013cD\3\2\2\2\u013d\u013e\7@\2\2\u013eF\3\2\2")
        buf.write("\2\u013f\u0140\7@\2\2\u0140\u0141\7?\2\2\u0141H\3\2\2")
        buf.write("\2\u0142\u0143\7(\2\2\u0143\u0144\7(\2\2\u0144J\3\2\2")
        buf.write("\2\u0145\u0146\7~\2\2\u0146\u0147\7~\2\2\u0147L\3\2\2")
        buf.write("\2\u0148\u0149\7#\2\2\u0149N\3\2\2\2\u014a\u014b\7<\2")
        buf.write("\2\u014b\u014c\7?\2\2\u014cP\3\2\2\2\u014d\u014e\7-\2")
        buf.write("\2\u014e\u014f\7?\2\2\u014fR\3\2\2\2\u0150\u0151\7/\2")
        buf.write("\2\u0151\u0152\7?\2\2\u0152T\3\2\2\2\u0153\u0154\7,\2")
        buf.write("\2\u0154\u0155\7?\2\2\u0155V\3\2\2\2\u0156\u0157\7\61")
        buf.write("\2\2\u0157\u0158\7?\2\2\u0158X\3\2\2\2\u0159\u015a\7\'")
        buf.write("\2\2\u015a\u015b\7?\2\2\u015bZ\3\2\2\2\u015c\u015d\7?")
        buf.write("\2\2\u015d\\\3\2\2\2\u015e\u015f\7\60\2\2\u015f^\3\2\2")
        buf.write("\2\u0160\u0161\7*\2\2\u0161`\3\2\2\2\u0162\u0163\7+\2")
        buf.write("\2\u0163b\3\2\2\2\u0164\u0165\7}\2\2\u0165d\3\2\2\2\u0166")
        buf.write("\u0167\7\177\2\2\u0167f\3\2\2\2\u0168\u0169\7]\2\2\u0169")
        buf.write("h\3\2\2\2\u016a\u016b\7_\2\2\u016bj\3\2\2\2\u016c\u016d")
        buf.write("\7.\2\2\u016dl\3\2\2\2\u016e\u016f\7=\2\2\u016fn\3\2\2")
        buf.write("\2\u0170\u0171\7<\2\2\u0171p\3\2\2\2\u0172\u0176\t\6\2")
        buf.write("\2\u0173\u0175\t\7\2\2\u0174\u0173\3\2\2\2\u0175\u0178")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177")
        buf.write("r\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u0182\7\62\2\2\u017a")
        buf.write("\u017e\t\b\2\2\u017b\u017d\t\t\2\2\u017c\u017b\3\2\2\2")
        buf.write("\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3")
        buf.write("\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0179")
        buf.write("\3\2\2\2\u0181\u017a\3\2\2\2\u0182t\3\2\2\2\u0183\u0184")
        buf.write("\7\62\2\2\u0184\u0186\t\n\2\2\u0185\u0187\t\13\2\2\u0186")
        buf.write("\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0186\3\2\2\2")
        buf.write("\u0188\u0189\3\2\2\2\u0189v\3\2\2\2\u018a\u018b\7\62\2")
        buf.write("\2\u018b\u018d\t\f\2\2\u018c\u018e\t\r\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190x\3\2\2\2\u0191\u0192\7\62\2\2\u0192")
        buf.write("\u0194\t\16\2\2\u0193\u0195\t\17\2\2\u0194\u0193\3\2\2")
        buf.write("\2\u0195\u0196\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197z\3\2\2\2\u0198\u019a\t\t\2\2\u0199\u0198")
        buf.write("\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u01a1\7\60\2")
        buf.write("\2\u019e\u01a0\t\t\2\2\u019f\u019e\3\2\2\2\u01a0\u01a3")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01ad\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a6\t\20\2")
        buf.write("\2\u01a5\u01a7\t\21\2\2\u01a6\u01a5\3\2\2\2\u01a6\u01a7")
        buf.write("\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01aa\t\t\2\2\u01a9")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01a4\3")
        buf.write("\2\2\2\u01ad\u01ae\3\2\2\2\u01ae|\3\2\2\2\u01af\u01b0")
        buf.write("\7^\2\2\u01b0\u01ba\7p\2\2\u01b1\u01b2\7^\2\2\u01b2\u01ba")
        buf.write("\7v\2\2\u01b3\u01b4\7^\2\2\u01b4\u01ba\7t\2\2\u01b5\u01b6")
        buf.write("\7^\2\2\u01b6\u01ba\7$\2\2\u01b7\u01b8\7^\2\2\u01b8\u01ba")
        buf.write("\7^\2\2\u01b9\u01af\3\2\2\2\u01b9\u01b1\3\2\2\2\u01b9")
        buf.write("\u01b3\3\2\2\2\u01b9\u01b5\3\2\2\2\u01b9\u01b7\3\2\2\2")
        buf.write("\u01ba~\3\2\2\2\u01bb\u01be\5}?\2\u01bc\u01be\n\22\2\2")
        buf.write("\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be\u0080\3")
        buf.write("\2\2\2\u01bf\u01c3\7$\2\2\u01c0\u01c2\5\177@\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c4\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c6\u01c7\7$\2\2\u01c7\u0082\3\2\2\2\u01c8\u01c9\13")
        buf.write("\2\2\2\u01c9\u01ca\bB\4\2\u01ca\u0084\3\2\2\2\u01cb\u01cf")
        buf.write("\7$\2\2\u01cc\u01ce\5\177@\2\u01cd\u01cc\3\2\2\2\u01ce")
        buf.write("\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2")
        buf.write("\u01d0\u01d2\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3\7")
        buf.write("^\2\2\u01d3\u01d4\n\23\2\2\u01d4\u01d5\bC\5\2\u01d5\u0086")
        buf.write("\3\2\2\2\u01d6\u01da\7$\2\2\u01d7\u01d9\5\177@\2\u01d8")
        buf.write("\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2")
        buf.write("\u01da\u01db\3\2\2\2\u01db\u01e0\3\2\2\2\u01dc\u01da\3")
        buf.write("\2\2\2\u01dd\u01de\7\17\2\2\u01de\u01e1\7\f\2\2\u01df")
        buf.write("\u01e1\t\24\2\2\u01e0\u01dd\3\2\2\2\u01e0\u01df\3\2\2")
        buf.write("\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\bD\6\2\u01e3\u0088")
        buf.write("\3\2\2\2\31\2\u008c\u0093\u009d\u00a9\u00ab\u0176\u017e")
        buf.write("\u0181\u0188\u018f\u0196\u019b\u01a1\u01a6\u01ab\u01ad")
        buf.write("\u01b9\u01bd\u01c3\u01cf\u01da\u01e0\7\3\2\2\b\2\2\3B")
        buf.write("\3\3C\4\3D\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NL = 1
    WS = 2
    SG_CMT = 3
    MUL_CMT = 4
    IF = 5
    ELSE = 6
    FOR = 7
    RETURN = 8
    FUNC = 9
    TYPE = 10
    STRUCT = 11
    INTERFACE = 12
    STRING = 13
    INT = 14
    FLOAT = 15
    BOOLEAN = 16
    CONST = 17
    VAR = 18
    CONTINUE = 19
    BREAK = 20
    RANGE = 21
    NIL = 22
    TRUE = 23
    FALSE = 24
    ADD = 25
    SUB = 26
    MUL = 27
    DIV = 28
    MOD = 29
    DBL_EQ = 30
    NOT_EQ = 31
    LT = 32
    LE = 33
    GT = 34
    GE = 35
    AND = 36
    OR = 37
    NOT = 38
    AS_EQ = 39
    ADD_EQ = 40
    SUB_EQ = 41
    MUL_EQ = 42
    DIV_EQ = 43
    MOD_EQ = 44
    EQ = 45
    DOT = 46
    LCIB = 47
    RCIB = 48
    LCUB = 49
    RCUB = 50
    LSQB = 51
    RSQB = 52
    COMMA = 53
    SECO = 54
    COLON = 55
    ID = 56
    DEC = 57
    BIN = 58
    OCT = 59
    HEX = 60
    FLOAT_LIT = 61
    STRING_LIT = 62
    ERROR_CHAR = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "NL", "WS", "SG_CMT", "MUL_CMT", "IF", "ELSE", "FOR", "RETURN", 
            "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
            "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
            "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "DBL_EQ", 
            "NOT_EQ", "LT", "LE", "GT", "GE", "AND", "OR", "NOT", "AS_EQ", 
            "ADD_EQ", "SUB_EQ", "MUL_EQ", "DIV_EQ", "MOD_EQ", "EQ", "DOT", 
            "LCIB", "RCIB", "LCUB", "RCUB", "LSQB", "RSQB", "COMMA", "SECO", 
            "COLON", "ID", "DEC", "BIN", "OCT", "HEX", "FLOAT_LIT", "STRING_LIT", 
            "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "NL", "WS", "SG_CMT", "MUL_CMT", "IF", "ELSE", "FOR", 
                  "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
                  "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "DBL_EQ", "NOT_EQ", "LT", "LE", "GT", 
                  "GE", "AND", "OR", "NOT", "AS_EQ", "ADD_EQ", "SUB_EQ", 
                  "MUL_EQ", "DIV_EQ", "MOD_EQ", "EQ", "DOT", "LCIB", "RCIB", 
                  "LCUB", "RCUB", "LSQB", "RSQB", "COMMA", "SECO", "COLON", 
                  "ID", "DEC", "BIN", "OCT", "HEX", "FLOAT_LIT", "ESC_SEQ", 
                  "STRING_SEQ", "STRING_LIT", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.NL_action 
            actions[64] = self.ERROR_CHAR_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.convertNL()
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[:-1])
                else:
                    raise UncloseString(self.text)

     


