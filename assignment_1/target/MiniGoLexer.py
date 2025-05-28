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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01e8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\3\3\3\3\3\5\3\u0091\n\3\3\3\3")
        buf.write("\3\3\4\6\4\u0096\n\4\r\4\16\4\u0097\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\7\5\u00a0\n\5\f\5\16\5\u00a3\13\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\7\6\u00ae\n\6\f\6\16\6\u00b1\13")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3")
        buf.write("\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\7:\u0179")
        buf.write("\n:\f:\16:\u017c\13:\3;\3;\3;\7;\u0181\n;\f;\16;\u0184")
        buf.write("\13;\5;\u0186\n;\3<\3<\3<\6<\u018b\n<\r<\16<\u018c\3=")
        buf.write("\3=\3=\6=\u0192\n=\r=\16=\u0193\3>\3>\3>\6>\u0199\n>\r")
        buf.write(">\16>\u019a\3?\6?\u019e\n?\r?\16?\u019f\3?\3?\7?\u01a4")
        buf.write("\n?\f?\16?\u01a7\13?\3?\3?\5?\u01ab\n?\3?\6?\u01ae\n?")
        buf.write("\r?\16?\u01af\5?\u01b2\n?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\5@\u01be\n@\3A\3A\5A\u01c2\nA\3B\3B\7B\u01c6\nB\fB\16")
        buf.write("B\u01c9\13B\3B\3B\3C\3C\3C\3D\3D\7D\u01d2\nD\fD\16D\u01d5")
        buf.write("\13D\3D\3D\3D\3D\3E\3E\7E\u01dd\nE\fE\16E\u01e0\13E\3")
        buf.write("E\3E\3E\5E\u01e5\nE\3E\3E\2\2F\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177\2\u0081")
        buf.write("\2\u0083A\u0085B\u0087C\u0089D\3\2\25\5\2\13\13\16\17")
        buf.write("\"\"\4\2\f\f\17\17\3\2,,\3\2\61\61\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63\4\2QQqq\3\2")
        buf.write("\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\6\2\f\f\17\17")
        buf.write("$$^^\7\2$$^^ppttvv\3\3\f\f\2\u01ff\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\3\u008b\3\2\2\2\5\u0090\3\2\2\2\7\u0095\3\2\2")
        buf.write("\2\t\u009b\3\2\2\2\13\u00a6\3\2\2\2\r\u00b7\3\2\2\2\17")
        buf.write("\u00ba\3\2\2\2\21\u00bf\3\2\2\2\23\u00c3\3\2\2\2\25\u00ca")
        buf.write("\3\2\2\2\27\u00cf\3\2\2\2\31\u00d4\3\2\2\2\33\u00db\3")
        buf.write("\2\2\2\35\u00e5\3\2\2\2\37\u00ec\3\2\2\2!\u00f0\3\2\2")
        buf.write("\2#\u00f6\3\2\2\2%\u00fe\3\2\2\2\'\u0104\3\2\2\2)\u0108")
        buf.write("\3\2\2\2+\u0111\3\2\2\2-\u0117\3\2\2\2/\u011d\3\2\2\2")
        buf.write("\61\u0121\3\2\2\2\63\u0126\3\2\2\2\65\u012c\3\2\2\2\67")
        buf.write("\u012e\3\2\2\29\u0130\3\2\2\2;\u0132\3\2\2\2=\u0134\3")
        buf.write("\2\2\2?\u0136\3\2\2\2A\u0139\3\2\2\2C\u013c\3\2\2\2E\u013e")
        buf.write("\3\2\2\2G\u0141\3\2\2\2I\u0143\3\2\2\2K\u0146\3\2\2\2")
        buf.write("M\u0149\3\2\2\2O\u014c\3\2\2\2Q\u014e\3\2\2\2S\u0151\3")
        buf.write("\2\2\2U\u0154\3\2\2\2W\u0157\3\2\2\2Y\u015a\3\2\2\2[\u015d")
        buf.write("\3\2\2\2]\u0160\3\2\2\2_\u0162\3\2\2\2a\u0164\3\2\2\2")
        buf.write("c\u0166\3\2\2\2e\u0168\3\2\2\2g\u016a\3\2\2\2i\u016c\3")
        buf.write("\2\2\2k\u016e\3\2\2\2m\u0170\3\2\2\2o\u0172\3\2\2\2q\u0174")
        buf.write("\3\2\2\2s\u0176\3\2\2\2u\u0185\3\2\2\2w\u0187\3\2\2\2")
        buf.write("y\u018e\3\2\2\2{\u0195\3\2\2\2}\u019d\3\2\2\2\177\u01bd")
        buf.write("\3\2\2\2\u0081\u01c1\3\2\2\2\u0083\u01c3\3\2\2\2\u0085")
        buf.write("\u01cc\3\2\2\2\u0087\u01cf\3\2\2\2\u0089\u01da\3\2\2\2")
        buf.write("\u008b\u008c\7a\2\2\u008c\4\3\2\2\2\u008d\u0091\7\f\2")
        buf.write("\2\u008e\u008f\7\17\2\2\u008f\u0091\7\f\2\2\u0090\u008d")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\u0093\b\3\2\2\u0093\6\3\2\2\2\u0094\u0096\t\2\2\2\u0095")
        buf.write("\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\b")
        buf.write("\4\3\2\u009a\b\3\2\2\2\u009b\u009c\7\61\2\2\u009c\u009d")
        buf.write("\7\61\2\2\u009d\u00a1\3\2\2\2\u009e\u00a0\n\3\2\2\u009f")
        buf.write("\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2")
        buf.write("\u00a1\u00a2\3\2\2\2\u00a2\u00a4\3\2\2\2\u00a3\u00a1\3")
        buf.write("\2\2\2\u00a4\u00a5\b\5\3\2\u00a5\n\3\2\2\2\u00a6\u00a7")
        buf.write("\7\61\2\2\u00a7\u00a8\7,\2\2\u00a8\u00af\3\2\2\2\u00a9")
        buf.write("\u00ae\5\13\6\2\u00aa\u00ae\n\4\2\2\u00ab\u00ac\7,\2\2")
        buf.write("\u00ac\u00ae\n\5\2\2\u00ad\u00a9\3\2\2\2\u00ad\u00aa\3")
        buf.write("\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b2\u00b3\7,\2\2\u00b3\u00b4\7\61\2\2")
        buf.write("\u00b4\u00b5\3\2\2\2\u00b5\u00b6\b\6\3\2\u00b6\f\3\2\2")
        buf.write("\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7h\2\2\u00b9\16\3\2")
        buf.write("\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7n\2\2\u00bc\u00bd")
        buf.write("\7u\2\2\u00bd\u00be\7g\2\2\u00be\20\3\2\2\2\u00bf\u00c0")
        buf.write("\7h\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7t\2\2\u00c2\22")
        buf.write("\3\2\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\24\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc")
        buf.write("\7w\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7e\2\2\u00ce\26")
        buf.write("\3\2\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7{\2\2\u00d1\u00d2")
        buf.write("\7r\2\2\u00d2\u00d3\7g\2\2\u00d3\30\3\2\2\2\u00d4\u00d5")
        buf.write("\7u\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8")
        buf.write("\7w\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da\7v\2\2\u00da\32")
        buf.write("\3\2\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7h\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4")
        buf.write("\7g\2\2\u00e4\34\3\2\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7")
        buf.write("\7v\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7i\2\2\u00eb\36\3\2\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7v\2\2\u00ef \3")
        buf.write("\2\2\2\u00f0\u00f1\7h\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5\7v\2\2\u00f5\"")
        buf.write("\3\2\2\2\u00f6\u00f7\7d\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7q\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc")
        buf.write("\7c\2\2\u00fc\u00fd\7p\2\2\u00fd$\3\2\2\2\u00fe\u00ff")
        buf.write("\7e\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7p\2\2\u0101\u0102")
        buf.write("\7u\2\2\u0102\u0103\7v\2\2\u0103&\3\2\2\2\u0104\u0105")
        buf.write("\7x\2\2\u0105\u0106\7c\2\2\u0106\u0107\7t\2\2\u0107(\3")
        buf.write("\2\2\2\u0108\u0109\7e\2\2\u0109\u010a\7q\2\2\u010a\u010b")
        buf.write("\7p\2\2\u010b\u010c\7v\2\2\u010c\u010d\7k\2\2\u010d\u010e")
        buf.write("\7p\2\2\u010e\u010f\7w\2\2\u010f\u0110\7g\2\2\u0110*\3")
        buf.write("\2\2\2\u0111\u0112\7d\2\2\u0112\u0113\7t\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114\u0115\7c\2\2\u0115\u0116\7m\2\2\u0116,\3")
        buf.write("\2\2\2\u0117\u0118\7t\2\2\u0118\u0119\7c\2\2\u0119\u011a")
        buf.write("\7p\2\2\u011a\u011b\7i\2\2\u011b\u011c\7g\2\2\u011c.\3")
        buf.write("\2\2\2\u011d\u011e\7p\2\2\u011e\u011f\7k\2\2\u011f\u0120")
        buf.write("\7n\2\2\u0120\60\3\2\2\2\u0121\u0122\7v\2\2\u0122\u0123")
        buf.write("\7t\2\2\u0123\u0124\7w\2\2\u0124\u0125\7g\2\2\u0125\62")
        buf.write("\3\2\2\2\u0126\u0127\7h\2\2\u0127\u0128\7c\2\2\u0128\u0129")
        buf.write("\7n\2\2\u0129\u012a\7u\2\2\u012a\u012b\7g\2\2\u012b\64")
        buf.write("\3\2\2\2\u012c\u012d\7-\2\2\u012d\66\3\2\2\2\u012e\u012f")
        buf.write("\7/\2\2\u012f8\3\2\2\2\u0130\u0131\7,\2\2\u0131:\3\2\2")
        buf.write("\2\u0132\u0133\7\61\2\2\u0133<\3\2\2\2\u0134\u0135\7\'")
        buf.write("\2\2\u0135>\3\2\2\2\u0136\u0137\7?\2\2\u0137\u0138\7?")
        buf.write("\2\2\u0138@\3\2\2\2\u0139\u013a\7#\2\2\u013a\u013b\7?")
        buf.write("\2\2\u013bB\3\2\2\2\u013c\u013d\7>\2\2\u013dD\3\2\2\2")
        buf.write("\u013e\u013f\7>\2\2\u013f\u0140\7?\2\2\u0140F\3\2\2\2")
        buf.write("\u0141\u0142\7@\2\2\u0142H\3\2\2\2\u0143\u0144\7@\2\2")
        buf.write("\u0144\u0145\7?\2\2\u0145J\3\2\2\2\u0146\u0147\7(\2\2")
        buf.write("\u0147\u0148\7(\2\2\u0148L\3\2\2\2\u0149\u014a\7~\2\2")
        buf.write("\u014a\u014b\7~\2\2\u014bN\3\2\2\2\u014c\u014d\7#\2\2")
        buf.write("\u014dP\3\2\2\2\u014e\u014f\7<\2\2\u014f\u0150\7?\2\2")
        buf.write("\u0150R\3\2\2\2\u0151\u0152\7-\2\2\u0152\u0153\7?\2\2")
        buf.write("\u0153T\3\2\2\2\u0154\u0155\7/\2\2\u0155\u0156\7?\2\2")
        buf.write("\u0156V\3\2\2\2\u0157\u0158\7,\2\2\u0158\u0159\7?\2\2")
        buf.write("\u0159X\3\2\2\2\u015a\u015b\7\61\2\2\u015b\u015c\7?\2")
        buf.write("\2\u015cZ\3\2\2\2\u015d\u015e\7\'\2\2\u015e\u015f\7?\2")
        buf.write("\2\u015f\\\3\2\2\2\u0160\u0161\7?\2\2\u0161^\3\2\2\2\u0162")
        buf.write("\u0163\7\60\2\2\u0163`\3\2\2\2\u0164\u0165\7*\2\2\u0165")
        buf.write("b\3\2\2\2\u0166\u0167\7+\2\2\u0167d\3\2\2\2\u0168\u0169")
        buf.write("\7}\2\2\u0169f\3\2\2\2\u016a\u016b\7\177\2\2\u016bh\3")
        buf.write("\2\2\2\u016c\u016d\7]\2\2\u016dj\3\2\2\2\u016e\u016f\7")
        buf.write("_\2\2\u016fl\3\2\2\2\u0170\u0171\7.\2\2\u0171n\3\2\2\2")
        buf.write("\u0172\u0173\7=\2\2\u0173p\3\2\2\2\u0174\u0175\7<\2\2")
        buf.write("\u0175r\3\2\2\2\u0176\u017a\t\6\2\2\u0177\u0179\t\7\2")
        buf.write("\2\u0178\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017bt\3\2\2\2\u017c\u017a")
        buf.write("\3\2\2\2\u017d\u0186\7\62\2\2\u017e\u0182\t\b\2\2\u017f")
        buf.write("\u0181\t\t\2\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0186\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0185\u017d\3\2\2\2\u0185\u017e")
        buf.write("\3\2\2\2\u0186v\3\2\2\2\u0187\u0188\7\62\2\2\u0188\u018a")
        buf.write("\t\n\2\2\u0189\u018b\t\13\2\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2")
        buf.write("\u018dx\3\2\2\2\u018e\u018f\7\62\2\2\u018f\u0191\t\f\2")
        buf.write("\2\u0190\u0192\t\r\2\2\u0191\u0190\3\2\2\2\u0192\u0193")
        buf.write("\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("z\3\2\2\2\u0195\u0196\7\62\2\2\u0196\u0198\t\16\2\2\u0197")
        buf.write("\u0199\t\17\2\2\u0198\u0197\3\2\2\2\u0199\u019a\3\2\2")
        buf.write("\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b|\3\2")
        buf.write("\2\2\u019c\u019e\t\t\2\2\u019d\u019c\3\2\2\2\u019e\u019f")
        buf.write("\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1\u01a5\7\60\2\2\u01a2\u01a4\t\t\2")
        buf.write("\2\u01a3\u01a2\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01b1\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a8\u01aa\t\20\2\2\u01a9\u01ab\t\21\2")
        buf.write("\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad")
        buf.write("\3\2\2\2\u01ac\u01ae\t\t\2\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01b2\3\2\2\2\u01b1\u01a8\3\2\2\2\u01b1\u01b2\3")
        buf.write("\2\2\2\u01b2~\3\2\2\2\u01b3\u01b4\7^\2\2\u01b4\u01be\7")
        buf.write("p\2\2\u01b5\u01b6\7^\2\2\u01b6\u01be\7v\2\2\u01b7\u01b8")
        buf.write("\7^\2\2\u01b8\u01be\7t\2\2\u01b9\u01ba\7^\2\2\u01ba\u01be")
        buf.write("\7$\2\2\u01bb\u01bc\7^\2\2\u01bc\u01be\7^\2\2\u01bd\u01b3")
        buf.write("\3\2\2\2\u01bd\u01b5\3\2\2\2\u01bd\u01b7\3\2\2\2\u01bd")
        buf.write("\u01b9\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u0080\3\2\2\2")
        buf.write("\u01bf\u01c2\5\177@\2\u01c0\u01c2\n\22\2\2\u01c1\u01bf")
        buf.write("\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u0082\3\2\2\2\u01c3")
        buf.write("\u01c7\7$\2\2\u01c4\u01c6\5\u0081A\2\u01c5\u01c4\3\2\2")
        buf.write("\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca")
        buf.write("\u01cb\7$\2\2\u01cb\u0084\3\2\2\2\u01cc\u01cd\13\2\2\2")
        buf.write("\u01cd\u01ce\bC\4\2\u01ce\u0086\3\2\2\2\u01cf\u01d3\7")
        buf.write("$\2\2\u01d0\u01d2\5\u0081A\2\u01d1\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2")
        buf.write("\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\7")
        buf.write("^\2\2\u01d7\u01d8\n\23\2\2\u01d8\u01d9\bD\5\2\u01d9\u0088")
        buf.write("\3\2\2\2\u01da\u01de\7$\2\2\u01db\u01dd\5\u0081A\2\u01dc")
        buf.write("\u01db\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2")
        buf.write("\u01de\u01df\3\2\2\2\u01df\u01e4\3\2\2\2\u01e0\u01de\3")
        buf.write("\2\2\2\u01e1\u01e2\7\17\2\2\u01e2\u01e5\7\f\2\2\u01e3")
        buf.write("\u01e5\t\24\2\2\u01e4\u01e1\3\2\2\2\u01e4\u01e3\3\2\2")
        buf.write("\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\bE\6\2\u01e7\u008a")
        buf.write("\3\2\2\2\31\2\u0090\u0097\u00a1\u00ad\u00af\u017a\u0182")
        buf.write("\u0185\u018c\u0193\u019a\u019f\u01a5\u01aa\u01af\u01b1")
        buf.write("\u01bd\u01c1\u01c7\u01d3\u01de\u01e4\7\3\3\2\b\2\2\3C")
        buf.write("\3\3D\4\3E\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    NL = 2
    WS = 3
    SG_CMT = 4
    MUL_CMT = 5
    IF = 6
    ELSE = 7
    FOR = 8
    RETURN = 9
    FUNC = 10
    TYPE = 11
    STRUCT = 12
    INTERFACE = 13
    STRING = 14
    INT = 15
    FLOAT = 16
    BOOLEAN = 17
    CONST = 18
    VAR = 19
    CONTINUE = 20
    BREAK = 21
    RANGE = 22
    NIL = 23
    TRUE = 24
    FALSE = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    MOD = 30
    DBL_EQ = 31
    NOT_EQ = 32
    LT = 33
    LE = 34
    GT = 35
    GE = 36
    AND = 37
    OR = 38
    NOT = 39
    AS_EQ = 40
    ADD_EQ = 41
    SUB_EQ = 42
    MUL_EQ = 43
    DIV_EQ = 44
    MOD_EQ = 45
    EQ = 46
    DOT = 47
    LCIB = 48
    RCIB = 49
    LCUB = 50
    RCUB = 51
    LSQB = 52
    RSQB = 53
    COMMA = 54
    SECO = 55
    COLON = 56
    ID = 57
    DEC = 58
    BIN = 59
    OCT = 60
    HEX = 61
    FLOAT_LIT = 62
    STRING_LIT = 63
    ERROR_CHAR = 64
    ILLEGAL_ESCAPE = 65
    UNCLOSE_STRING = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'_'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
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

    ruleNames = [ "T__0", "NL", "WS", "SG_CMT", "MUL_CMT", "IF", "ELSE", 
                  "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                  "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
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
            actions[1] = self.NL_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.UNCLOSE_STRING_action 
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

     


