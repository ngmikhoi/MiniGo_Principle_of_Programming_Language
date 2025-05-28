# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u028e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u00a0\n\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00ab\n\6\3\7\3\7\3\7\3\7")
        buf.write("\5\7\u00b1\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u00b8\n\b\3\t\3")
        buf.write("\t\5\t\u00bc\n\t\3\n\3\n\3\n\3\n\5\n\u00c2\n\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00d9\n\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00df\n\r\3\r\3\r\3\r\5\r\u00e4\n\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u00f0\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00fc\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u0103\n\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\5\22\u010b\n\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u0112\n\23\3\24\3\24\3\25\3\25\3")
        buf.write("\25\5\25\u0119\n\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u0121\n\25\3\25\5\25\u0124\n\25\3\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u0132\n\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u0139\n\31\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0146")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u0154\n\34\3\35\3\35\3\35\3\35\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u015e\n\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0166\n\37\3 \3 \3 \3 \3 \5 \u016d\n \3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0177\n\"\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\5%\u0189\n%\3&\3&\3&\5")
        buf.write("&\u018e\n&\3\'\3\'\3\'\3(\3(\3(\3(\5(\u0197\n(\3(\3(\3")
        buf.write(")\3)\3)\3)\5)\u019f\n)\3)\3)\3)\5)\u01a4\n)\3)\3)\3*\3")
        buf.write("*\3*\3*\3*\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5")
        buf.write(",\u01bb\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5")
        buf.write("-\u01cb\n-\3-\3-\3.\3.\3.\5.\u01d2\n.\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\5\61\u01e7\n\61\3\62\3\62\3\63\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\64\5\64\u01f2\n\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\39\3:\3:\3:\3;\3;\3;\5;\u020f\n;\3;")
        buf.write("\3;\3<\3<\3=\3=\3=\3=\3=\3=\7=\u021b\n=\f=\16=\u021e\13")
        buf.write("=\3>\3>\3>\3>\3>\3>\7>\u0226\n>\f>\16>\u0229\13>\3?\3")
        buf.write("?\3?\3?\3?\3?\3?\7?\u0232\n?\f?\16?\u0235\13?\3@\3@\3")
        buf.write("@\3@\3@\3@\7@\u023d\n@\f@\16@\u0240\13@\3A\3A\3A\3A\3")
        buf.write("A\3A\7A\u0248\nA\fA\16A\u024b\13A\3B\3B\3B\5B\u0250\n")
        buf.write("B\3C\3C\3C\3C\3C\3C\3C\5C\u0259\nC\3C\3C\3C\3C\3C\7C\u0260")
        buf.write("\nC\fC\16C\u0263\13C\3D\3D\3D\5D\u0268\nD\3D\3D\5D\u026c")
        buf.write("\nD\3E\3E\3E\3F\3F\3F\3F\3G\3G\3G\3G\3G\3G\3G\5G\u027c")
        buf.write("\nG\3H\3H\3H\3H\3H\3H\3H\5H\u0285\nH\3I\3I\3J\3J\3J\5")
        buf.write("J\u028c\nJ\3J\2\bxz|~\u0080\u0084K\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\u008a\u008c\u008e\u0090\u0092\2\n\3\2<?\3\2\32\33\3\2")
        buf.write("*/\3\2!&\3\2\34\35\3\2\36 \4\2\35\35))\3\2\20\23\2\u028f")
        buf.write("\2\u0094\3\2\2\2\4\u0096\3\2\2\2\6\u0098\3\2\2\2\b\u009f")
        buf.write("\3\2\2\2\n\u00aa\3\2\2\2\f\u00b0\3\2\2\2\16\u00b7\3\2")
        buf.write("\2\2\20\u00bb\3\2\2\2\22\u00bd\3\2\2\2\24\u00c7\3\2\2")
        buf.write("\2\26\u00cc\3\2\2\2\30\u00d2\3\2\2\2\32\u00ef\3\2\2\2")
        buf.write("\34\u00f1\3\2\2\2\36\u00fb\3\2\2\2 \u00fd\3\2\2\2\"\u010a")
        buf.write("\3\2\2\2$\u0111\3\2\2\2&\u0113\3\2\2\2(\u0123\3\2\2\2")
        buf.write("*\u0125\3\2\2\2,\u0128\3\2\2\2.\u0131\3\2\2\2\60\u0138")
        buf.write("\3\2\2\2\62\u0145\3\2\2\2\64\u0147\3\2\2\2\66\u0153\3")
        buf.write("\2\2\28\u0155\3\2\2\2:\u0159\3\2\2\2<\u0165\3\2\2\2>\u016c")
        buf.write("\3\2\2\2@\u016e\3\2\2\2B\u0176\3\2\2\2D\u0178\3\2\2\2")
        buf.write("F\u0180\3\2\2\2H\u0188\3\2\2\2J\u018a\3\2\2\2L\u018f\3")
        buf.write("\2\2\2N\u0196\3\2\2\2P\u019a\3\2\2\2R\u01a7\3\2\2\2T\u01ac")
        buf.write("\3\2\2\2V\u01ba\3\2\2\2X\u01bc\3\2\2\2Z\u01d1\3\2\2\2")
        buf.write("\\\u01d3\3\2\2\2^\u01da\3\2\2\2`\u01e6\3\2\2\2b\u01e8")
        buf.write("\3\2\2\2d\u01ea\3\2\2\2f\u01ee\3\2\2\2h\u01fd\3\2\2\2")
        buf.write("j\u01ff\3\2\2\2l\u0201\3\2\2\2n\u0203\3\2\2\2p\u0205\3")
        buf.write("\2\2\2r\u0208\3\2\2\2t\u020b\3\2\2\2v\u0212\3\2\2\2x\u0214")
        buf.write("\3\2\2\2z\u021f\3\2\2\2|\u022a\3\2\2\2~\u0236\3\2\2\2")
        buf.write("\u0080\u0241\3\2\2\2\u0082\u024f\3\2\2\2\u0084\u0251\3")
        buf.write("\2\2\2\u0086\u026b\3\2\2\2\u0088\u026d\3\2\2\2\u008a\u0270")
        buf.write("\3\2\2\2\u008c\u027b\3\2\2\2\u008e\u0284\3\2\2\2\u0090")
        buf.write("\u0286\3\2\2\2\u0092\u028b\3\2\2\2\u0094\u0095\t\2\2\2")
        buf.write("\u0095\3\3\2\2\2\u0096\u0097\t\3\2\2\u0097\5\3\2\2\2\u0098")
        buf.write("\u0099\5\b\5\2\u0099\u009a\7\2\2\3\u009a\7\3\2\2\2\u009b")
        buf.write("\u009c\5\16\b\2\u009c\u009d\5\b\5\2\u009d\u00a0\3\2\2")
        buf.write("\2\u009e\u00a0\5\16\b\2\u009f\u009b\3\2\2\2\u009f\u009e")
        buf.write("\3\2\2\2\u00a0\t\3\2\2\2\u00a1\u00ab\5\20\t\2\u00a2\u00ab")
        buf.write("\5\26\f\2\u00a3\u00ab\5R*\2\u00a4\u00ab\5\34\17\2\u00a5")
        buf.write("\u00ab\5X-\2\u00a6\u00ab\5Z.\2\u00a7\u00ab\5p9\2\u00a8")
        buf.write("\u00ab\5r:\2\u00a9\u00ab\5t;\2\u00aa\u00a1\3\2\2\2\u00aa")
        buf.write("\u00a2\3\2\2\2\u00aa\u00a3\3\2\2\2\u00aa\u00a4\3\2\2\2")
        buf.write("\u00aa\u00a5\3\2\2\2\u00aa\u00a6\3\2\2\2\u00aa\u00a7\3")
        buf.write("\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\13")
        buf.write("\3\2\2\2\u00ac\u00ad\5\n\6\2\u00ad\u00ae\5\f\7\2\u00ae")
        buf.write("\u00b1\3\2\2\2\u00af\u00b1\5\n\6\2\u00b0\u00ac\3\2\2\2")
        buf.write("\u00b0\u00af\3\2\2\2\u00b1\r\3\2\2\2\u00b2\u00b8\5\20")
        buf.write("\t\2\u00b3\u00b8\5\26\f\2\u00b4\u00b8\5\30\r\2\u00b5\u00b8")
        buf.write("\5\64\33\2\u00b6\u00b8\5D#\2\u00b7\u00b2\3\2\2\2\u00b7")
        buf.write("\u00b3\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b7\u00b5\3\2\2\2")
        buf.write("\u00b7\u00b6\3\2\2\2\u00b8\17\3\2\2\2\u00b9\u00bc\5\22")
        buf.write("\n\2\u00ba\u00bc\5\24\13\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bc\21\3\2\2\2\u00bd\u00be\7\25\2\2\u00be\u00c1")
        buf.write("\7;\2\2\u00bf\u00c2\5\u0092J\2\u00c0\u00c2\3\2\2\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\u00c4\7\60\2\2\u00c4\u00c5\5x=\2\u00c5\u00c6\7")
        buf.write("9\2\2\u00c6\23\3\2\2\2\u00c7\u00c8\7\25\2\2\u00c8\u00c9")
        buf.write("\7;\2\2\u00c9\u00ca\5\u0092J\2\u00ca\u00cb\79\2\2\u00cb")
        buf.write("\25\3\2\2\2\u00cc\u00cd\7\24\2\2\u00cd\u00ce\7;\2\2\u00ce")
        buf.write("\u00cf\7\60\2\2\u00cf\u00d0\5x=\2\u00d0\u00d1\79\2\2\u00d1")
        buf.write("\27\3\2\2\2\u00d2\u00d8\7\f\2\2\u00d3\u00d4\7\62\2\2\u00d4")
        buf.write("\u00d5\7;\2\2\u00d5\u00d6\7;\2\2\u00d6\u00d9\7\63\2\2")
        buf.write("\u00d7\u00d9\3\2\2\2\u00d8\u00d3\3\2\2\2\u00d8\u00d7\3")
        buf.write("\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\7;\2\2\u00db\u00de")
        buf.write("\7\62\2\2\u00dc\u00df\5N(\2\u00dd\u00df\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e3\7\63\2\2\u00e1\u00e4\5\u0092J\2\u00e2\u00e4")
        buf.write("\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4")
        buf.write("\u00e5\3\2\2\2\u00e5\u00e6\7\64\2\2\u00e6\u00e7\5\f\7")
        buf.write("\2\u00e7\u00e8\7\65\2\2\u00e8\u00e9\79\2\2\u00e9\31\3")
        buf.write("\2\2\2\u00ea\u00eb\7\61\2\2\u00eb\u00ec\5 \21\2\u00ec")
        buf.write("\u00ed\5\32\16\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0\3\2\2")
        buf.write("\2\u00ef\u00ea\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0\33\3")
        buf.write("\2\2\2\u00f1\u00f2\5 \21\2\u00f2\u00f3\5\32\16\2\u00f3")
        buf.write("\u00f4\79\2\2\u00f4\35\3\2\2\2\u00f5\u00f6\5\u0088E\2")
        buf.write("\u00f6\u00f7\7\61\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9")
        buf.write("\5\36\20\2\u00f9\u00fc\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb")
        buf.write("\u00f5\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\37\3\2\2\2\u00fd")
        buf.write("\u00fe\5\36\20\2\u00fe\u00ff\7;\2\2\u00ff\u0102\7\62\2")
        buf.write("\2\u0100\u0103\5\"\22\2\u0101\u0103\3\2\2\2\u0102\u0100")
        buf.write("\3\2\2\2\u0102\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\u0105\7\63\2\2\u0105!\3\2\2\2\u0106\u0107\5&\24\2\u0107")
        buf.write("\u0108\5$\23\2\u0108\u010b\3\2\2\2\u0109\u010b\5&\24\2")
        buf.write("\u010a\u0106\3\2\2\2\u010a\u0109\3\2\2\2\u010b#\3\2\2")
        buf.write("\2\u010c\u010d\78\2\2\u010d\u010e\5&\24\2\u010e\u010f")
        buf.write("\5$\23\2\u010f\u0112\3\2\2\2\u0110\u0112\3\2\2\2\u0111")
        buf.write("\u010c\3\2\2\2\u0111\u0110\3\2\2\2\u0112%\3\2\2\2\u0113")
        buf.write("\u0114\5x=\2\u0114\'\3\2\2\2\u0115\u0118\7\66\2\2\u0116")
        buf.write("\u0119\5\2\2\2\u0117\u0119\7;\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\7")
        buf.write("\67\2\2\u011b\u011c\3\2\2\2\u011c\u0124\5(\25\2\u011d")
        buf.write("\u0120\7\66\2\2\u011e\u0121\5\2\2\2\u011f\u0121\7;\2\2")
        buf.write("\u0120\u011e\3\2\2\2\u0120\u011f\3\2\2\2\u0121\u0122\3")
        buf.write("\2\2\2\u0122\u0124\7\67\2\2\u0123\u0115\3\2\2\2\u0123")
        buf.write("\u011d\3\2\2\2\u0124)\3\2\2\2\u0125\u0126\5(\25\2\u0126")
        buf.write("\u0127\5\u0092J\2\u0127+\3\2\2\2\u0128\u0129\5*\26\2\u0129")
        buf.write("\u012a\7\64\2\2\u012a\u012b\5.\30\2\u012b\u012c\7\65\2")
        buf.write("\2\u012c-\3\2\2\2\u012d\u012e\5\62\32\2\u012e\u012f\5")
        buf.write("\60\31\2\u012f\u0132\3\2\2\2\u0130\u0132\5\62\32\2\u0131")
        buf.write("\u012d\3\2\2\2\u0131\u0130\3\2\2\2\u0132/\3\2\2\2\u0133")
        buf.write("\u0134\78\2\2\u0134\u0135\5\62\32\2\u0135\u0136\5\60\31")
        buf.write("\2\u0136\u0139\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u0133")
        buf.write("\3\2\2\2\u0138\u0137\3\2\2\2\u0139\61\3\2\2\2\u013a\u0146")
        buf.write("\5\2\2\2\u013b\u0146\7@\2\2\u013c\u0146\7A\2\2\u013d\u0146")
        buf.write("\5\4\3\2\u013e\u0146\7\31\2\2\u013f\u0146\5:\36\2\u0140")
        buf.write("\u0146\7;\2\2\u0141\u0142\7\64\2\2\u0142\u0143\5.\30\2")
        buf.write("\u0143\u0144\7\65\2\2\u0144\u0146\3\2\2\2\u0145\u013a")
        buf.write("\3\2\2\2\u0145\u013b\3\2\2\2\u0145\u013c\3\2\2\2\u0145")
        buf.write("\u013d\3\2\2\2\u0145\u013e\3\2\2\2\u0145\u013f\3\2\2\2")
        buf.write("\u0145\u0140\3\2\2\2\u0145\u0141\3\2\2\2\u0146\63\3\2")
        buf.write("\2\2\u0147\u0148\7\r\2\2\u0148\u0149\7;\2\2\u0149\u014a")
        buf.write("\7\16\2\2\u014a\u014b\7\64\2\2\u014b\u014c\5\66\34\2\u014c")
        buf.write("\u014d\7\65\2\2\u014d\u014e\79\2\2\u014e\65\3\2\2\2\u014f")
        buf.write("\u0150\58\35\2\u0150\u0151\5\66\34\2\u0151\u0154\3\2\2")
        buf.write("\2\u0152\u0154\58\35\2\u0153\u014f\3\2\2\2\u0153\u0152")
        buf.write("\3\2\2\2\u0154\67\3\2\2\2\u0155\u0156\7;\2\2\u0156\u0157")
        buf.write("\5\u0092J\2\u0157\u0158\79\2\2\u01589\3\2\2\2\u0159\u015a")
        buf.write("\7;\2\2\u015a\u015d\7\64\2\2\u015b\u015e\5<\37\2\u015c")
        buf.write("\u015e\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015c\3\2\2\2")
        buf.write("\u015e\u015f\3\2\2\2\u015f\u0160\7\65\2\2\u0160;\3\2\2")
        buf.write("\2\u0161\u0162\5@!\2\u0162\u0163\5> \2\u0163\u0166\3\2")
        buf.write("\2\2\u0164\u0166\5@!\2\u0165\u0161\3\2\2\2\u0165\u0164")
        buf.write("\3\2\2\2\u0166=\3\2\2\2\u0167\u0168\78\2\2\u0168\u0169")
        buf.write("\5@!\2\u0169\u016a\5> \2\u016a\u016d\3\2\2\2\u016b\u016d")
        buf.write("\3\2\2\2\u016c\u0167\3\2\2\2\u016c\u016b\3\2\2\2\u016d")
        buf.write("?\3\2\2\2\u016e\u016f\7;\2\2\u016f\u0170\7:\2\2\u0170")
        buf.write("\u0171\5x=\2\u0171A\3\2\2\2\u0172\u0173\5P)\2\u0173\u0174")
        buf.write("\5B\"\2\u0174\u0177\3\2\2\2\u0175\u0177\5P)\2\u0176\u0172")
        buf.write("\3\2\2\2\u0176\u0175\3\2\2\2\u0177C\3\2\2\2\u0178\u0179")
        buf.write("\7\r\2\2\u0179\u017a\7;\2\2\u017a\u017b\7\17\2\2\u017b")
        buf.write("\u017c\7\64\2\2\u017c\u017d\5B\"\2\u017d\u017e\7\65\2")
        buf.write("\2\u017e\u017f\79\2\2\u017fE\3\2\2\2\u0180\u0181\5J&\2")
        buf.write("\u0181\u0182\5H%\2\u0182G\3\2\2\2\u0183\u0184\78\2\2\u0184")
        buf.write("\u0185\5J&\2\u0185\u0186\5H%\2\u0186\u0189\3\2\2\2\u0187")
        buf.write("\u0189\3\2\2\2\u0188\u0183\3\2\2\2\u0188\u0187\3\2\2\2")
        buf.write("\u0189I\3\2\2\2\u018a\u018d\7;\2\2\u018b\u018e\5\u0092")
        buf.write("J\2\u018c\u018e\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018eK\3\2\2\2\u018f\u0190\7;\2\2\u0190\u0191")
        buf.write("\5\u0092J\2\u0191M\3\2\2\2\u0192\u0193\5F$\2\u0193\u0194")
        buf.write("\78\2\2\u0194\u0197\3\2\2\2\u0195\u0197\3\2\2\2\u0196")
        buf.write("\u0192\3\2\2\2\u0196\u0195\3\2\2\2\u0197\u0198\3\2\2\2")
        buf.write("\u0198\u0199\5L\'\2\u0199O\3\2\2\2\u019a\u019b\7;\2\2")
        buf.write("\u019b\u019e\7\62\2\2\u019c\u019f\5N(\2\u019d\u019f\3")
        buf.write("\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d\3\2\2\2\u019f\u01a0")
        buf.write("\3\2\2\2\u01a0\u01a3\7\63\2\2\u01a1\u01a4\5\u0092J\2\u01a2")
        buf.write("\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a6\79\2\2\u01a6Q\3\2\2\2")
        buf.write("\u01a7\u01a8\5\u0088E\2\u01a8\u01a9\5T+\2\u01a9\u01aa")
        buf.write("\5x=\2\u01aa\u01ab\79\2\2\u01abS\3\2\2\2\u01ac\u01ad\t")
        buf.write("\4\2\2\u01adU\3\2\2\2\u01ae\u01af\7\t\2\2\u01af\u01b0")
        buf.write("\7\b\2\2\u01b0\u01b1\7\62\2\2\u01b1\u01b2\5b\62\2\u01b2")
        buf.write("\u01b3\7\63\2\2\u01b3\u01b4\7\64\2\2\u01b4\u01b5\5\f\7")
        buf.write("\2\u01b5\u01b6\7\65\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8")
        buf.write("\5V,\2\u01b8\u01bb\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01ae")
        buf.write("\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbW\3\2\2\2\u01bc\u01bd")
        buf.write("\7\b\2\2\u01bd\u01be\7\62\2\2\u01be\u01bf\5b\62\2\u01bf")
        buf.write("\u01c0\7\63\2\2\u01c0\u01c1\7\64\2\2\u01c1\u01c2\5\f\7")
        buf.write("\2\u01c2\u01c3\7\65\2\2\u01c3\u01ca\5V,\2\u01c4\u01c5")
        buf.write("\7\t\2\2\u01c5\u01c6\7\64\2\2\u01c6\u01c7\5\f\7\2\u01c7")
        buf.write("\u01c8\7\65\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01cb\3\2\2")
        buf.write("\2\u01ca\u01c4\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cb\u01cc")
        buf.write("\3\2\2\2\u01cc\u01cd\79\2\2\u01cdY\3\2\2\2\u01ce\u01d2")
        buf.write("\5\\/\2\u01cf\u01d2\5^\60\2\u01d0\u01d2\5f\64\2\u01d1")
        buf.write("\u01ce\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d0\3\2\2\2")
        buf.write("\u01d2[\3\2\2\2\u01d3\u01d4\7\n\2\2\u01d4\u01d5\5b\62")
        buf.write("\2\u01d5\u01d6\7\64\2\2\u01d6\u01d7\5\f\7\2\u01d7\u01d8")
        buf.write("\7\65\2\2\u01d8\u01d9\79\2\2\u01d9]\3\2\2\2\u01da\u01db")
        buf.write("\7\n\2\2\u01db\u01dc\5`\61\2\u01dc\u01dd\5b\62\2\u01dd")
        buf.write("\u01de\79\2\2\u01de\u01df\5d\63\2\u01df\u01e0\7\64\2\2")
        buf.write("\u01e0\u01e1\5\f\7\2\u01e1\u01e2\7\65\2\2\u01e2\u01e3")
        buf.write("\79\2\2\u01e3_\3\2\2\2\u01e4\u01e7\5R*\2\u01e5\u01e7\5")
        buf.write("\22\n\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7")
        buf.write("a\3\2\2\2\u01e8\u01e9\5x=\2\u01e9c\3\2\2\2\u01ea\u01eb")
        buf.write("\5\u0088E\2\u01eb\u01ec\5T+\2\u01ec\u01ed\5x=\2\u01ed")
        buf.write("e\3\2\2\2\u01ee\u01f1\7\n\2\2\u01ef\u01f2\5h\65\2\u01f0")
        buf.write("\u01f2\5j\66\2\u01f1\u01ef\3\2\2\2\u01f1\u01f0\3\2\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3\u01f4\78\2\2\u01f4\u01f5\5")
        buf.write("l\67\2\u01f5\u01f6\7*\2\2\u01f6\u01f7\7\30\2\2\u01f7\u01f8")
        buf.write("\5n8\2\u01f8\u01f9\7\64\2\2\u01f9\u01fa\5\f\7\2\u01fa")
        buf.write("\u01fb\7\65\2\2\u01fb\u01fc\79\2\2\u01fcg\3\2\2\2\u01fd")
        buf.write("\u01fe\7;\2\2\u01fei\3\2\2\2\u01ff\u0200\7\3\2\2\u0200")
        buf.write("k\3\2\2\2\u0201\u0202\7;\2\2\u0202m\3\2\2\2\u0203\u0204")
        buf.write("\5x=\2\u0204o\3\2\2\2\u0205\u0206\7\27\2\2\u0206\u0207")
        buf.write("\79\2\2\u0207q\3\2\2\2\u0208\u0209\7\26\2\2\u0209\u020a")
        buf.write("\79\2\2\u020as\3\2\2\2\u020b\u020e\7\13\2\2\u020c\u020f")
        buf.write("\5x=\2\u020d\u020f\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020d")
        buf.write("\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0211\79\2\2\u0211")
        buf.write("u\3\2\2\2\u0212\u0213\t\5\2\2\u0213w\3\2\2\2\u0214\u0215")
        buf.write("\b=\1\2\u0215\u0216\5z>\2\u0216\u021c\3\2\2\2\u0217\u0218")
        buf.write("\f\4\2\2\u0218\u0219\7(\2\2\u0219\u021b\5z>\2\u021a\u0217")
        buf.write("\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2\u021c")
        buf.write("\u021d\3\2\2\2\u021dy\3\2\2\2\u021e\u021c\3\2\2\2\u021f")
        buf.write("\u0220\b>\1\2\u0220\u0221\5|?\2\u0221\u0227\3\2\2\2\u0222")
        buf.write("\u0223\f\4\2\2\u0223\u0224\7\'\2\2\u0224\u0226\5|?\2\u0225")
        buf.write("\u0222\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2")
        buf.write("\u0227\u0228\3\2\2\2\u0228{\3\2\2\2\u0229\u0227\3\2\2")
        buf.write("\2\u022a\u022b\b?\1\2\u022b\u022c\5~@\2\u022c\u0233\3")
        buf.write("\2\2\2\u022d\u022e\f\4\2\2\u022e\u022f\5v<\2\u022f\u0230")
        buf.write("\5~@\2\u0230\u0232\3\2\2\2\u0231\u022d\3\2\2\2\u0232\u0235")
        buf.write("\3\2\2\2\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234")
        buf.write("}\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0237\b@\1\2\u0237")
        buf.write("\u0238\5\u0080A\2\u0238\u023e\3\2\2\2\u0239\u023a\f\4")
        buf.write("\2\2\u023a\u023b\t\6\2\2\u023b\u023d\5\u0080A\2\u023c")
        buf.write("\u0239\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c\3\2\2\2")
        buf.write("\u023e\u023f\3\2\2\2\u023f\177\3\2\2\2\u0240\u023e\3\2")
        buf.write("\2\2\u0241\u0242\bA\1\2\u0242\u0243\5\u0082B\2\u0243\u0249")
        buf.write("\3\2\2\2\u0244\u0245\f\4\2\2\u0245\u0246\t\7\2\2\u0246")
        buf.write("\u0248\5\u0082B\2\u0247\u0244\3\2\2\2\u0248\u024b\3\2")
        buf.write("\2\2\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u0081")
        buf.write("\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024d\t\b\2\2\u024d")
        buf.write("\u0250\5\u0082B\2\u024e\u0250\5\u0084C\2\u024f\u024c\3")
        buf.write("\2\2\2\u024f\u024e\3\2\2\2\u0250\u0083\3\2\2\2\u0251\u0252")
        buf.write("\bC\1\2\u0252\u0253\5\u008cG\2\u0253\u0261\3\2\2\2\u0254")
        buf.write("\u0255\f\5\2\2\u0255\u0258\7\61\2\2\u0256\u0259\7;\2\2")
        buf.write("\u0257\u0259\5 \21\2\u0258\u0256\3\2\2\2\u0258\u0257\3")
        buf.write("\2\2\2\u0259\u0260\3\2\2\2\u025a\u025b\f\4\2\2\u025b\u025c")
        buf.write("\7\66\2\2\u025c\u025d\5x=\2\u025d\u025e\7\67\2\2\u025e")
        buf.write("\u0260\3\2\2\2\u025f\u0254\3\2\2\2\u025f\u025a\3\2\2\2")
        buf.write("\u0260\u0263\3\2\2\2\u0261\u025f\3\2\2\2\u0261\u0262\3")
        buf.write("\2\2\2\u0262\u0085\3\2\2\2\u0263\u0261\3\2\2\2\u0264\u0265")
        buf.write("\7\61\2\2\u0265\u0268\7;\2\2\u0266\u0268\5\u008aF\2\u0267")
        buf.write("\u0264\3\2\2\2\u0267\u0266\3\2\2\2\u0268\u0269\3\2\2\2")
        buf.write("\u0269\u026c\5\u0086D\2\u026a\u026c\3\2\2\2\u026b\u0267")
        buf.write("\3\2\2\2\u026b\u026a\3\2\2\2\u026c\u0087\3\2\2\2\u026d")
        buf.write("\u026e\7;\2\2\u026e\u026f\5\u0086D\2\u026f\u0089\3\2\2")
        buf.write("\2\u0270\u0271\7\66\2\2\u0271\u0272\5x=\2\u0272\u0273")
        buf.write("\7\67\2\2\u0273\u008b\3\2\2\2\u0274\u027c\5\u008eH\2\u0275")
        buf.write("\u027c\7;\2\2\u0276\u027c\5 \21\2\u0277\u0278\7\62\2\2")
        buf.write("\u0278\u0279\5x=\2\u0279\u027a\7\63\2\2\u027a\u027c\3")
        buf.write("\2\2\2\u027b\u0274\3\2\2\2\u027b\u0275\3\2\2\2\u027b\u0276")
        buf.write("\3\2\2\2\u027b\u0277\3\2\2\2\u027c\u008d\3\2\2\2\u027d")
        buf.write("\u0285\5\2\2\2\u027e\u0285\7@\2\2\u027f\u0285\7A\2\2\u0280")
        buf.write("\u0285\5\4\3\2\u0281\u0285\7\31\2\2\u0282\u0285\5:\36")
        buf.write("\2\u0283\u0285\5,\27\2\u0284\u027d\3\2\2\2\u0284\u027e")
        buf.write("\3\2\2\2\u0284\u027f\3\2\2\2\u0284\u0280\3\2\2\2\u0284")
        buf.write("\u0281\3\2\2\2\u0284\u0282\3\2\2\2\u0284\u0283\3\2\2\2")
        buf.write("\u0285\u008f\3\2\2\2\u0286\u0287\t\t\2\2\u0287\u0091\3")
        buf.write("\2\2\2\u0288\u028c\7;\2\2\u0289\u028c\5\u0090I\2\u028a")
        buf.write("\u028c\5*\26\2\u028b\u0288\3\2\2\2\u028b\u0289\3\2\2\2")
        buf.write("\u028b\u028a\3\2\2\2\u028c\u0093\3\2\2\2\64\u009f\u00aa")
        buf.write("\u00b0\u00b7\u00bb\u00c1\u00d8\u00de\u00e3\u00ef\u00fb")
        buf.write("\u0102\u010a\u0111\u0118\u0120\u0123\u0131\u0138\u0145")
        buf.write("\u0153\u015d\u0165\u016c\u0176\u0188\u018d\u0196\u019e")
        buf.write("\u01a3\u01ba\u01ca\u01d1\u01e6\u01f1\u020e\u021c\u0227")
        buf.write("\u0233\u023e\u0249\u024f\u0258\u025f\u0261\u0267\u026b")
        buf.write("\u027b\u0284\u028b")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NL", "WS", "SG_CMT", "MUL_CMT", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
                      "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "DBL_EQ", "NOT_EQ", "LT", "LE", "GT", "GE", "AND", 
                      "OR", "NOT", "AS_EQ", "ADD_EQ", "SUB_EQ", "MUL_EQ", 
                      "DIV_EQ", "MOD_EQ", "EQ", "DOT", "LCIB", "RCIB", "LCUB", 
                      "RCUB", "LSQB", "RSQB", "COMMA", "SECO", "COLON", 
                      "ID", "DEC", "BIN", "OCT", "HEX", "FLOAT_LIT", "STRING_LIT", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_int_lit = 0
    RULE_bool_lit = 1
    RULE_program = 2
    RULE_manydecl = 3
    RULE_stmt = 4
    RULE_stmt_block = 5
    RULE_decl = 6
    RULE_var_decl = 7
    RULE_var_decl_init = 8
    RULE_var_decl_uninit = 9
    RULE_const_decl = 10
    RULE_func_decl = 11
    RULE_star_dot_func_call = 12
    RULE_func_call_stmt = 13
    RULE_star_lhs_dot = 14
    RULE_func_call = 15
    RULE_list_arg = 16
    RULE_tail_arg = 17
    RULE_arg = 18
    RULE_arr_dim_decl = 19
    RULE_arr_type = 20
    RULE_arr_lit = 21
    RULE_list_ele_arr = 22
    RULE_tail_ele_arr = 23
    RULE_ele_arr = 24
    RULE_struct_decl = 25
    RULE_star_struct_ele_decl = 26
    RULE_attr_decl = 27
    RULE_struct_lit = 28
    RULE_list_ele_struct = 29
    RULE_tail_ele_struct = 30
    RULE_ele_struct = 31
    RULE_star_interface_method_decl = 32
    RULE_interface_decl = 33
    RULE_not_last_para = 34
    RULE_tail_para = 35
    RULE_para = 36
    RULE_last_para = 37
    RULE_list_para = 38
    RULE_method_interface = 39
    RULE_assign_stmt = 40
    RULE_assign_op = 41
    RULE_else_if = 42
    RULE_if_stmt = 43
    RULE_for_stmt = 44
    RULE_basic_for = 45
    RULE_init_for = 46
    RULE_init = 47
    RULE_condit = 48
    RULE_update = 49
    RULE_range_for = 50
    RULE_index = 51
    RULE_blank = 52
    RULE_value = 53
    RULE_array_id = 54
    RULE_break_stmt = 55
    RULE_continue_stmt = 56
    RULE_return_stmt = 57
    RULE_rela_op = 58
    RULE_expr1 = 59
    RULE_expr2 = 60
    RULE_expr3 = 61
    RULE_expr4 = 62
    RULE_expr5 = 63
    RULE_expr6 = 64
    RULE_expr7 = 65
    RULE_star_dot_dim = 66
    RULE_lhs = 67
    RULE_dim = 68
    RULE_operand = 69
    RULE_lit = 70
    RULE_primi = 71
    RULE_all_type = 72

    ruleNames =  [ "int_lit", "bool_lit", "program", "manydecl", "stmt", 
                   "stmt_block", "decl", "var_decl", "var_decl_init", "var_decl_uninit", 
                   "const_decl", "func_decl", "star_dot_func_call", "func_call_stmt", 
                   "star_lhs_dot", "func_call", "list_arg", "tail_arg", 
                   "arg", "arr_dim_decl", "arr_type", "arr_lit", "list_ele_arr", 
                   "tail_ele_arr", "ele_arr", "struct_decl", "star_struct_ele_decl", 
                   "attr_decl", "struct_lit", "list_ele_struct", "tail_ele_struct", 
                   "ele_struct", "star_interface_method_decl", "interface_decl", 
                   "not_last_para", "tail_para", "para", "last_para", "list_para", 
                   "method_interface", "assign_stmt", "assign_op", "else_if", 
                   "if_stmt", "for_stmt", "basic_for", "init_for", "init", 
                   "condit", "update", "range_for", "index", "blank", "value", 
                   "array_id", "break_stmt", "continue_stmt", "return_stmt", 
                   "rela_op", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "star_dot_dim", "lhs", "dim", "operand", 
                   "lit", "primi", "all_type" ]

    EOF = Token.EOF
    T__0=1
    NL=2
    WS=3
    SG_CMT=4
    MUL_CMT=5
    IF=6
    ELSE=7
    FOR=8
    RETURN=9
    FUNC=10
    TYPE=11
    STRUCT=12
    INTERFACE=13
    STRING=14
    INT=15
    FLOAT=16
    BOOLEAN=17
    CONST=18
    VAR=19
    CONTINUE=20
    BREAK=21
    RANGE=22
    NIL=23
    TRUE=24
    FALSE=25
    ADD=26
    SUB=27
    MUL=28
    DIV=29
    MOD=30
    DBL_EQ=31
    NOT_EQ=32
    LT=33
    LE=34
    GT=35
    GE=36
    AND=37
    OR=38
    NOT=39
    AS_EQ=40
    ADD_EQ=41
    SUB_EQ=42
    MUL_EQ=43
    DIV_EQ=44
    MOD_EQ=45
    EQ=46
    DOT=47
    LCIB=48
    RCIB=49
    LCUB=50
    RCUB=51
    LSQB=52
    RSQB=53
    COMMA=54
    SECO=55
    COLON=56
    ID=57
    DEC=58
    BIN=59
    OCT=60
    HEX=61
    FLOAT_LIT=62
    STRING_LIT=63
    ERROR_CHAR=64
    ILLEGAL_ESCAPE=65
    UNCLOSE_STRING=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Int_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC(self):
            return self.getToken(MiniGoParser.DEC, 0)

        def BIN(self):
            return self.getToken(MiniGoParser.BIN, 0)

        def OCT(self):
            return self.getToken(MiniGoParser.OCT, 0)

        def HEX(self):
            return self.getToken(MiniGoParser.HEX, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_int_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lit" ):
                return visitor.visitInt_lit(self)
            else:
                return visitor.visitChildren(self)




    def int_lit(self):

        localctx = MiniGoParser.Int_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_int_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DEC) | (1 << MiniGoParser.BIN) | (1 << MiniGoParser.OCT) | (1 << MiniGoParser.HEX))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = MiniGoParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.TRUE or _la==MiniGoParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def manydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ManydeclContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.manydecl()
            self.state = 151
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def manydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ManydeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_manydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManydecl" ):
                return visitor.visitManydecl(self)
            else:
                return visitor.visitChildren(self)




    def manydecl(self):

        localctx = MiniGoParser.ManydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_manydecl)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.decl()
                self.state = 154
                self.manydecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def func_call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.func_call_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.if_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 164
                self.for_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 165
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 166
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 167
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = MiniGoParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt_block)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.stmt()
                self.state = 171
                self.stmt_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.struct_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 180
                self.interface_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_initContext,0)


        def var_decl_uninit(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_uninitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_decl)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.var_decl_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.var_decl_uninit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_init" ):
                return visitor.visitVar_decl_init(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_init(self):

        localctx = MiniGoParser.Var_decl_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_decl_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MiniGoParser.VAR)
            self.state = 188
            self.match(MiniGoParser.ID)
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSQB, MiniGoParser.ID]:
                self.state = 189
                self.all_type()
                pass
            elif token in [MiniGoParser.EQ]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 193
            self.match(MiniGoParser.EQ)
            self.state = 194
            self.expr1(0)
            self.state = 195
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_uninitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_uninit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_uninit" ):
                return visitor.visitVar_decl_uninit(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_uninit(self):

        localctx = MiniGoParser.Var_decl_uninitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_decl_uninit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MiniGoParser.VAR)
            self.state = 198
            self.match(MiniGoParser.ID)
            self.state = 199
            self.all_type()
            self.state = 200
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MiniGoParser.CONST)
            self.state = 203
            self.match(MiniGoParser.ID)
            self.state = 204
            self.match(MiniGoParser.EQ)
            self.state = 205
            self.expr1(0)
            self.state = 206
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LCIB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LCIB)
            else:
                return self.getToken(MiniGoParser.LCIB, i)

        def RCIB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RCIB)
            else:
                return self.getToken(MiniGoParser.RCIB, i)

        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def list_para(self):
            return self.getTypedRuleContext(MiniGoParser.List_paraContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MiniGoParser.FUNC)
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LCIB]:
                self.state = 209
                self.match(MiniGoParser.LCIB)
                self.state = 210
                self.match(MiniGoParser.ID)
                self.state = 211
                self.match(MiniGoParser.ID)
                self.state = 212
                self.match(MiniGoParser.RCIB)
                pass
            elif token in [MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 216
            self.match(MiniGoParser.ID)
            self.state = 217
            self.match(MiniGoParser.LCIB)
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 218
                self.list_para()
                pass
            elif token in [MiniGoParser.RCIB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 222
            self.match(MiniGoParser.RCIB)
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSQB, MiniGoParser.ID]:
                self.state = 223
                self.all_type()
                pass
            elif token in [MiniGoParser.LCUB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 227
            self.match(MiniGoParser.LCUB)
            self.state = 228
            self.stmt_block()
            self.state = 229
            self.match(MiniGoParser.RCUB)
            self.state = 230
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Star_dot_func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def star_dot_func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Star_dot_func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_star_dot_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar_dot_func_call" ):
                return visitor.visitStar_dot_func_call(self)
            else:
                return visitor.visitChildren(self)




    def star_dot_func_call(self):

        localctx = MiniGoParser.Star_dot_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_star_dot_func_call)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(MiniGoParser.DOT)
                self.state = 233
                self.func_call()
                self.state = 234
                self.star_dot_func_call()
                pass
            elif token in [MiniGoParser.SECO]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def star_dot_func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Star_dot_func_callContext,0)


        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stmt(self):

        localctx = MiniGoParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.func_call()
            self.state = 240
            self.star_dot_func_call()
            self.state = 241
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Star_lhs_dotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_lhs_dot(self):
            return self.getTypedRuleContext(MiniGoParser.Star_lhs_dotContext,0)


        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_star_lhs_dot

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar_lhs_dot" ):
                return visitor.visitStar_lhs_dot(self)
            else:
                return visitor.visitChildren(self)




    def star_lhs_dot(self):

        localctx = MiniGoParser.Star_lhs_dotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_star_lhs_dot)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.lhs()
                self.state = 244
                self.match(MiniGoParser.DOT)
                self.state = 246
                self.star_lhs_dot()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_lhs_dot(self):
            return self.getTypedRuleContext(MiniGoParser.Star_lhs_dotContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCIB(self):
            return self.getToken(MiniGoParser.LCIB, 0)

        def RCIB(self):
            return self.getToken(MiniGoParser.RCIB, 0)

        def list_arg(self):
            return self.getTypedRuleContext(MiniGoParser.List_argContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.star_lhs_dot()
            self.state = 252
            self.match(MiniGoParser.ID)
            self.state = 253
            self.match(MiniGoParser.LCIB)
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LCIB, MiniGoParser.LSQB, MiniGoParser.ID, MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 254
                self.list_arg()
                pass
            elif token in [MiniGoParser.RCIB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 258
            self.match(MiniGoParser.RCIB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self):
            return self.getTypedRuleContext(MiniGoParser.ArgContext,0)


        def tail_arg(self):
            return self.getTypedRuleContext(MiniGoParser.Tail_argContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_arg" ):
                return visitor.visitList_arg(self)
            else:
                return visitor.visitChildren(self)




    def list_arg(self):

        localctx = MiniGoParser.List_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_arg)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.arg()
                self.state = 261
                self.tail_arg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.arg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tail_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arg(self):
            return self.getTypedRuleContext(MiniGoParser.ArgContext,0)


        def tail_arg(self):
            return self.getTypedRuleContext(MiniGoParser.Tail_argContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_tail_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail_arg" ):
                return visitor.visitTail_arg(self)
            else:
                return visitor.visitChildren(self)




    def tail_arg(self):

        localctx = MiniGoParser.Tail_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_tail_arg)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(MiniGoParser.COMMA)
                self.state = 267
                self.arg()
                self.state = 268
                self.tail_arg()
                pass
            elif token in [MiniGoParser.RCIB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = MiniGoParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.expr1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_dim_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_dim_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_dim_declContext,0)


        def LSQB(self):
            return self.getToken(MiniGoParser.LSQB, 0)

        def RSQB(self):
            return self.getToken(MiniGoParser.RSQB, 0)

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_dim_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_dim_decl" ):
                return visitor.visitArr_dim_decl(self)
            else:
                return visitor.visitChildren(self)




    def arr_dim_decl(self):

        localctx = MiniGoParser.Arr_dim_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arr_dim_decl)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(MiniGoParser.LSQB)
                self.state = 278
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX]:
                    self.state = 276
                    self.int_lit()
                    pass
                elif token in [MiniGoParser.ID]:
                    self.state = 277
                    self.match(MiniGoParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 280
                self.match(MiniGoParser.RSQB)
                self.state = 282
                self.arr_dim_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.match(MiniGoParser.LSQB)
                self.state = 286
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX]:
                    self.state = 284
                    self.int_lit()
                    pass
                elif token in [MiniGoParser.ID]:
                    self.state = 285
                    self.match(MiniGoParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 288
                self.match(MiniGoParser.RSQB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_dim_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_dim_declContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = MiniGoParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.arr_dim_decl()
            self.state = 292
            self.all_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_typeContext,0)


        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def list_ele_arr(self):
            return self.getTypedRuleContext(MiniGoParser.List_ele_arrContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = MiniGoParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.arr_type()
            self.state = 295
            self.match(MiniGoParser.LCUB)
            self.state = 296
            self.list_ele_arr()
            self.state = 297
            self.match(MiniGoParser.RCUB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_ele_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ele_arr(self):
            return self.getTypedRuleContext(MiniGoParser.Ele_arrContext,0)


        def tail_ele_arr(self):
            return self.getTypedRuleContext(MiniGoParser.Tail_ele_arrContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ele_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ele_arr" ):
                return visitor.visitList_ele_arr(self)
            else:
                return visitor.visitChildren(self)




    def list_ele_arr(self):

        localctx = MiniGoParser.List_ele_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_ele_arr)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.ele_arr()
                self.state = 300
                self.tail_ele_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.ele_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tail_ele_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ele_arr(self):
            return self.getTypedRuleContext(MiniGoParser.Ele_arrContext,0)


        def tail_ele_arr(self):
            return self.getTypedRuleContext(MiniGoParser.Tail_ele_arrContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_tail_ele_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail_ele_arr" ):
                return visitor.visitTail_ele_arr(self)
            else:
                return visitor.visitChildren(self)




    def tail_ele_arr(self):

        localctx = MiniGoParser.Tail_ele_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_tail_ele_arr)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(MiniGoParser.COMMA)
                self.state = 306
                self.ele_arr()
                self.state = 307
                self.tail_ele_arr()
                pass
            elif token in [MiniGoParser.RCUB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ele_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Bool_litContext,0)


        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def list_ele_arr(self):
            return self.getTypedRuleContext(MiniGoParser.List_ele_arrContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ele_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle_arr" ):
                return visitor.visitEle_arr(self)
            else:
                return visitor.visitChildren(self)




    def ele_arr(self):

        localctx = MiniGoParser.Ele_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ele_arr)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.int_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
                self.bool_lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 316
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 317
                self.struct_lit()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 318
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 319
                self.match(MiniGoParser.LCUB)
                self.state = 320
                self.list_ele_arr()
                self.state = 321
                self.match(MiniGoParser.RCUB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def star_struct_ele_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Star_struct_ele_declContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MiniGoParser.TYPE)
            self.state = 326
            self.match(MiniGoParser.ID)
            self.state = 327
            self.match(MiniGoParser.STRUCT)
            self.state = 328
            self.match(MiniGoParser.LCUB)
            self.state = 329
            self.star_struct_ele_decl()
            self.state = 330
            self.match(MiniGoParser.RCUB)
            self.state = 331
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Star_struct_ele_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Attr_declContext,0)


        def star_struct_ele_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Star_struct_ele_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_star_struct_ele_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar_struct_ele_decl" ):
                return visitor.visitStar_struct_ele_decl(self)
            else:
                return visitor.visitChildren(self)




    def star_struct_ele_decl(self):

        localctx = MiniGoParser.Star_struct_ele_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_star_struct_ele_decl)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.attr_decl()
                self.state = 334
                self.star_struct_ele_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.attr_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl" ):
                return visitor.visitAttr_decl(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl(self):

        localctx = MiniGoParser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_attr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(MiniGoParser.ID)
            self.state = 340
            self.all_type()
            self.state = 341
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def list_ele_struct(self):
            return self.getTypedRuleContext(MiniGoParser.List_ele_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(MiniGoParser.ID)
            self.state = 344
            self.match(MiniGoParser.LCUB)
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 345
                self.list_ele_struct()
                pass
            elif token in [MiniGoParser.RCUB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 349
            self.match(MiniGoParser.RCUB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_ele_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ele_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Ele_structContext,0)


        def tail_ele_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Tail_ele_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ele_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ele_struct" ):
                return visitor.visitList_ele_struct(self)
            else:
                return visitor.visitChildren(self)




    def list_ele_struct(self):

        localctx = MiniGoParser.List_ele_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_list_ele_struct)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.ele_struct()
                self.state = 352
                self.tail_ele_struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.ele_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tail_ele_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ele_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Ele_structContext,0)


        def tail_ele_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Tail_ele_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_tail_ele_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail_ele_struct" ):
                return visitor.visitTail_ele_struct(self)
            else:
                return visitor.visitChildren(self)




    def tail_ele_struct(self):

        localctx = MiniGoParser.Tail_ele_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_tail_ele_struct)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(MiniGoParser.COMMA)
                self.state = 358
                self.ele_struct()
                self.state = 359
                self.tail_ele_struct()
                pass
            elif token in [MiniGoParser.RCUB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ele_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ele_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle_struct" ):
                return visitor.visitEle_struct(self)
            else:
                return visitor.visitChildren(self)




    def ele_struct(self):

        localctx = MiniGoParser.Ele_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_ele_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MiniGoParser.ID)
            self.state = 365
            self.match(MiniGoParser.COLON)
            self.state = 366
            self.expr1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Star_interface_method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_interface(self):
            return self.getTypedRuleContext(MiniGoParser.Method_interfaceContext,0)


        def star_interface_method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Star_interface_method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_star_interface_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar_interface_method_decl" ):
                return visitor.visitStar_interface_method_decl(self)
            else:
                return visitor.visitChildren(self)




    def star_interface_method_decl(self):

        localctx = MiniGoParser.Star_interface_method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_star_interface_method_decl)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.method_interface()
                self.state = 369
                self.star_interface_method_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.method_interface()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def star_interface_method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Star_interface_method_declContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(MiniGoParser.TYPE)
            self.state = 375
            self.match(MiniGoParser.ID)
            self.state = 376
            self.match(MiniGoParser.INTERFACE)
            self.state = 377
            self.match(MiniGoParser.LCUB)
            self.state = 378
            self.star_interface_method_decl()
            self.state = 379
            self.match(MiniGoParser.RCUB)
            self.state = 380
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_last_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(MiniGoParser.ParaContext,0)


        def tail_para(self):
            return self.getTypedRuleContext(MiniGoParser.Tail_paraContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_not_last_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_last_para" ):
                return visitor.visitNot_last_para(self)
            else:
                return visitor.visitChildren(self)




    def not_last_para(self):

        localctx = MiniGoParser.Not_last_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_not_last_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.para()
            self.state = 383
            self.tail_para()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tail_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def para(self):
            return self.getTypedRuleContext(MiniGoParser.ParaContext,0)


        def tail_para(self):
            return self.getTypedRuleContext(MiniGoParser.Tail_paraContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_tail_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail_para" ):
                return visitor.visitTail_para(self)
            else:
                return visitor.visitChildren(self)




    def tail_para(self):

        localctx = MiniGoParser.Tail_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_tail_para)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(MiniGoParser.COMMA)
                self.state = 386
                self.para()
                self.state = 387
                self.tail_para()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MiniGoParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MiniGoParser.ID)
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSQB, MiniGoParser.ID]:
                self.state = 393
                self.all_type()
                pass
            elif token in [MiniGoParser.COMMA]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Last_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_last_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLast_para" ):
                return visitor.visitLast_para(self)
            else:
                return visitor.visitChildren(self)




    def last_para(self):

        localctx = MiniGoParser.Last_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_last_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(MiniGoParser.ID)
            self.state = 398
            self.all_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def last_para(self):
            return self.getTypedRuleContext(MiniGoParser.Last_paraContext,0)


        def not_last_para(self):
            return self.getTypedRuleContext(MiniGoParser.Not_last_paraContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_para" ):
                return visitor.visitList_para(self)
            else:
                return visitor.visitChildren(self)




    def list_para(self):

        localctx = MiniGoParser.List_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_list_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 400
                self.not_last_para()
                self.state = 401
                self.match(MiniGoParser.COMMA)
                pass

            elif la_ == 2:
                pass


            self.state = 406
            self.last_para()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_interfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCIB(self):
            return self.getToken(MiniGoParser.LCIB, 0)

        def RCIB(self):
            return self.getToken(MiniGoParser.RCIB, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def list_para(self):
            return self.getTypedRuleContext(MiniGoParser.List_paraContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_interface" ):
                return visitor.visitMethod_interface(self)
            else:
                return visitor.visitChildren(self)




    def method_interface(self):

        localctx = MiniGoParser.Method_interfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_method_interface)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MiniGoParser.ID)
            self.state = 409
            self.match(MiniGoParser.LCIB)
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 410
                self.list_para()
                pass
            elif token in [MiniGoParser.RCIB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 414
            self.match(MiniGoParser.RCIB)
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSQB, MiniGoParser.ID]:
                self.state = 415
                self.all_type()
                pass
            elif token in [MiniGoParser.SECO]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 419
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MiniGoParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.lhs()
            self.state = 422
            self.assign_op()
            self.state = 423
            self.expr1(0)
            self.state = 424
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AS_EQ(self):
            return self.getToken(MiniGoParser.AS_EQ, 0)

        def ADD_EQ(self):
            return self.getToken(MiniGoParser.ADD_EQ, 0)

        def SUB_EQ(self):
            return self.getToken(MiniGoParser.SUB_EQ, 0)

        def MUL_EQ(self):
            return self.getToken(MiniGoParser.MUL_EQ, 0)

        def DIV_EQ(self):
            return self.getToken(MiniGoParser.DIV_EQ, 0)

        def MOD_EQ(self):
            return self.getToken(MiniGoParser.MOD_EQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_op" ):
                return visitor.visitAssign_op(self)
            else:
                return visitor.visitChildren(self)




    def assign_op(self):

        localctx = MiniGoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.AS_EQ) | (1 << MiniGoParser.ADD_EQ) | (1 << MiniGoParser.SUB_EQ) | (1 << MiniGoParser.MUL_EQ) | (1 << MiniGoParser.DIV_EQ) | (1 << MiniGoParser.MOD_EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LCIB(self):
            return self.getToken(MiniGoParser.LCIB, 0)

        def condit(self):
            return self.getTypedRuleContext(MiniGoParser.ConditContext,0)


        def RCIB(self):
            return self.getToken(MiniGoParser.RCIB, 0)

        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = MiniGoParser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_else_if)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(MiniGoParser.ELSE)
                self.state = 429
                self.match(MiniGoParser.IF)
                self.state = 430
                self.match(MiniGoParser.LCIB)
                self.state = 431
                self.condit()
                self.state = 432
                self.match(MiniGoParser.RCIB)
                self.state = 433
                self.match(MiniGoParser.LCUB)
                self.state = 434
                self.stmt_block()
                self.state = 435
                self.match(MiniGoParser.RCUB)
                self.state = 437
                self.else_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LCIB(self):
            return self.getToken(MiniGoParser.LCIB, 0)

        def condit(self):
            return self.getTypedRuleContext(MiniGoParser.ConditContext,0)


        def RCIB(self):
            return self.getToken(MiniGoParser.RCIB, 0)

        def LCUB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LCUB)
            else:
                return self.getToken(MiniGoParser.LCUB, i)

        def stmt_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Stmt_blockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,i)


        def RCUB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RCUB)
            else:
                return self.getToken(MiniGoParser.RCUB, i)

        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(MiniGoParser.IF)
            self.state = 443
            self.match(MiniGoParser.LCIB)
            self.state = 444
            self.condit()
            self.state = 445
            self.match(MiniGoParser.RCIB)
            self.state = 446
            self.match(MiniGoParser.LCUB)
            self.state = 447
            self.stmt_block()
            self.state = 448
            self.match(MiniGoParser.RCUB)
            self.state = 449
            self.else_if()
            self.state = 456
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.state = 450
                self.match(MiniGoParser.ELSE)
                self.state = 451
                self.match(MiniGoParser.LCUB)
                self.state = 452
                self.stmt_block()
                self.state = 453
                self.match(MiniGoParser.RCUB)
                pass
            elif token in [MiniGoParser.SECO]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 458
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_for(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_forContext,0)


        def init_for(self):
            return self.getTypedRuleContext(MiniGoParser.Init_forContext,0)


        def range_for(self):
            return self.getTypedRuleContext(MiniGoParser.Range_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_for_stmt)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.basic_for()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.init_for()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.range_for()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def condit(self):
            return self.getTypedRuleContext(MiniGoParser.ConditContext,0)


        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for" ):
                return visitor.visitBasic_for(self)
            else:
                return visitor.visitChildren(self)




    def basic_for(self):

        localctx = MiniGoParser.Basic_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_basic_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(MiniGoParser.FOR)
            self.state = 466
            self.condit()
            self.state = 467
            self.match(MiniGoParser.LCUB)
            self.state = 468
            self.stmt_block()
            self.state = 469
            self.match(MiniGoParser.RCUB)
            self.state = 470
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def condit(self):
            return self.getTypedRuleContext(MiniGoParser.ConditContext,0)


        def SECO(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SECO)
            else:
                return self.getToken(MiniGoParser.SECO, i)

        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_init_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_for" ):
                return visitor.visitInit_for(self)
            else:
                return visitor.visitChildren(self)




    def init_for(self):

        localctx = MiniGoParser.Init_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(MiniGoParser.FOR)
            self.state = 473
            self.init()
            self.state = 474
            self.condit()
            self.state = 475
            self.match(MiniGoParser.SECO)
            self.state = 476
            self.update()
            self.state = 477
            self.match(MiniGoParser.LCUB)
            self.state = 478
            self.stmt_block()
            self.state = 479
            self.match(MiniGoParser.RCUB)
            self.state = 480
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def var_decl_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = MiniGoParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_init)
        try:
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.assign_stmt()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.var_decl_init()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondit" ):
                return visitor.visitCondit(self)
            else:
                return visitor.visitChildren(self)




    def condit(self):

        localctx = MiniGoParser.ConditContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_condit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.expr1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.lhs()
            self.state = 489
            self.assign_op()
            self.state = 490
            self.expr1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def value(self):
            return self.getTypedRuleContext(MiniGoParser.ValueContext,0)


        def AS_EQ(self):
            return self.getToken(MiniGoParser.AS_EQ, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def array_id(self):
            return self.getTypedRuleContext(MiniGoParser.Array_idContext,0)


        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def blank(self):
            return self.getTypedRuleContext(MiniGoParser.BlankContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_for" ):
                return visitor.visitRange_for(self)
            else:
                return visitor.visitChildren(self)




    def range_for(self):

        localctx = MiniGoParser.Range_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_range_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(MiniGoParser.FOR)
            self.state = 495
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 493
                self.index()
                pass
            elif token in [MiniGoParser.T__0]:
                self.state = 494
                self.blank()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 497
            self.match(MiniGoParser.COMMA)
            self.state = 498
            self.value()
            self.state = 499
            self.match(MiniGoParser.AS_EQ)
            self.state = 500
            self.match(MiniGoParser.RANGE)
            self.state = 501
            self.array_id()
            self.state = 502
            self.match(MiniGoParser.LCUB)
            self.state = 503
            self.stmt_block()
            self.state = 504
            self.match(MiniGoParser.RCUB)
            self.state = 505
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = MiniGoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlankContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_blank

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)




    def blank(self):

        localctx = MiniGoParser.BlankContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_blank)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(MiniGoParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MiniGoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_id" ):
                return visitor.visitArray_id(self)
            else:
                return visitor.visitChildren(self)




    def array_id(self):

        localctx = MiniGoParser.Array_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_array_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.expr1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(MiniGoParser.BREAK)
            self.state = 516
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(MiniGoParser.CONTINUE)
            self.state = 519
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(MiniGoParser.RETURN)
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LCIB, MiniGoParser.LSQB, MiniGoParser.ID, MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 522
                self.expr1(0)
                pass
            elif token in [MiniGoParser.SECO]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 526
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rela_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DBL_EQ(self):
            return self.getToken(MiniGoParser.DBL_EQ, 0)

        def NOT_EQ(self):
            return self.getToken(MiniGoParser.NOT_EQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_rela_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRela_op" ):
                return visitor.visitRela_op(self)
            else:
                return visitor.visitChildren(self)




    def rela_op(self):

        localctx = MiniGoParser.Rela_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_rela_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DBL_EQ) | (1 << MiniGoParser.NOT_EQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 538
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 533
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 534
                    self.match(MiniGoParser.OR)
                    self.state = 535
                    self.expr2(0) 
                self.state = 540
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 544
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 545
                    self.match(MiniGoParser.AND)
                    self.state = 546
                    self.expr3(0) 
                self.state = 551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def rela_op(self):
            return self.getTypedRuleContext(MiniGoParser.Rela_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 561
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 555
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 556
                    self.rela_op()
                    self.state = 557
                    self.expr4(0) 
                self.state = 563
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 572
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 567
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 568
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 569
                    self.expr5(0) 
                self.state = 574
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 126
        self.enterRecursionRule(localctx, 126, self.RULE_expr5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 583
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 578
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 579
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 580
                    self.expr6() 
                self.state = 585
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_expr6)
        self._la = 0 # Token type
        try:
            self.state = 589
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 586
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 587
                self.expr6()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LCIB, MiniGoParser.LSQB, MiniGoParser.ID, MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def LSQB(self):
            return self.getToken(MiniGoParser.LSQB, 0)

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def RSQB(self):
            return self.getToken(MiniGoParser.RSQB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 607
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 605
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 594
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 595
                        self.match(MiniGoParser.DOT)
                        self.state = 598
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                        if la_ == 1:
                            self.state = 596
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 597
                            self.func_call()
                            pass


                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 600
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 601
                        self.match(MiniGoParser.LSQB)
                        self.state = 602
                        self.expr1(0)
                        self.state = 603
                        self.match(MiniGoParser.RSQB)
                        pass

             
                self.state = 609
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Star_dot_dimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_dot_dim(self):
            return self.getTypedRuleContext(MiniGoParser.Star_dot_dimContext,0)


        def dim(self):
            return self.getTypedRuleContext(MiniGoParser.DimContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_star_dot_dim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar_dot_dim" ):
                return visitor.visitStar_dot_dim(self)
            else:
                return visitor.visitChildren(self)




    def star_dot_dim(self):

        localctx = MiniGoParser.Star_dot_dimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_star_dot_dim)
        try:
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 613
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.DOT]:
                    self.state = 610
                    self.match(MiniGoParser.DOT)
                    self.state = 611
                    self.match(MiniGoParser.ID)
                    pass
                elif token in [MiniGoParser.LSQB]:
                    self.state = 612
                    self.dim()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 615
                self.star_dot_dim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def star_dot_dim(self):
            return self.getTypedRuleContext(MiniGoParser.Star_dot_dimContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.match(MiniGoParser.ID)
            self.state = 620
            self.star_dot_dim()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQB(self):
            return self.getToken(MiniGoParser.LSQB, 0)

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def RSQB(self):
            return self.getToken(MiniGoParser.RSQB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim" ):
                return visitor.visitDim(self)
            else:
                return visitor.visitChildren(self)




    def dim(self):

        localctx = MiniGoParser.DimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.match(MiniGoParser.LSQB)
            self.state = 623
            self.expr1(0)
            self.state = 624
            self.match(MiniGoParser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(MiniGoParser.LitContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def LCIB(self):
            return self.getToken(MiniGoParser.LCIB, 0)

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def RCIB(self):
            return self.getToken(MiniGoParser.RCIB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_operand)
        try:
            self.state = 633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                self.lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 627
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 628
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 629
                self.match(MiniGoParser.LCIB)
                self.state = 630
                self.expr1(0)
                self.state = 631
                self.match(MiniGoParser.RCIB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Bool_litContext,0)


        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def arr_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = MiniGoParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_lit)
        try:
            self.state = 642
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 635
                self.int_lit()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 636
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 637
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 638
                self.bool_lit()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 639
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 640
                self.struct_lit()
                pass
            elif token in [MiniGoParser.LSQB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 641
                self.arr_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimi" ):
                return visitor.visitPrimi(self)
            else:
                return visitor.visitChildren(self)




    def primi(self):

        localctx = MiniGoParser.PrimiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_primi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def primi(self):
            return self.getTypedRuleContext(MiniGoParser.PrimiContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_all_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_type" ):
                return visitor.visitAll_type(self)
            else:
                return visitor.visitChildren(self)




    def all_type(self):

        localctx = MiniGoParser.All_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_all_type)
        try:
            self.state = 649
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 646
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 647
                self.primi()
                pass
            elif token in [MiniGoParser.LSQB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 648
                self.arr_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[59] = self.expr1_sempred
        self._predicates[60] = self.expr2_sempred
        self._predicates[61] = self.expr3_sempred
        self._predicates[62] = self.expr4_sempred
        self._predicates[63] = self.expr5_sempred
        self._predicates[65] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




