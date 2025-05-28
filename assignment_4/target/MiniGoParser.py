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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u02fa\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\5\5\u00bc\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u00c7\n\6\3\7\3\7\3\7\3\7\5\7\u00cd\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u00d4\n\b\3\t\3\t\5\t\u00d8\n\t\3\n\3\n")
        buf.write("\3\n\3\n\5\n\u00de\n\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u00f1\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\5\16\u00f8\n\16\3\16\3\16")
        buf.write("\3\16\5\16\u00fd\n\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u010d\n\17")
        buf.write("\3\17\3\17\3\17\5\17\u0112\n\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u0125\n\23\3\24\3\24\3\24\5\24\u012a\n")
        buf.write("\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\5\26\u0134")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\7\27\u013b\n\27\f\27\16")
        buf.write("\27\u013e\13\27\3\30\3\30\3\30\3\30\3\31\3\31\5\31\u0146")
        buf.write("\n\31\3\32\3\32\3\32\3\32\5\32\u014c\n\32\3\32\3\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\5\33\u0156\n\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u015e\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\5\35\u0165\n\35\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u016d\n\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0175")
        buf.write("\n\37\3\37\7\37\u0178\n\37\f\37\16\37\u017b\13\37\3 \3")
        buf.write(" \3 \3 \3 \3 \5 \u0183\n \3!\3!\3!\5!\u0188\n!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\5\"\u0192\n\"\3#\3#\3#\3#\3#\5#\u0199")
        buf.write("\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01a6\n$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\5&\u01b4\n&\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\5(\u01be\n(\3(\3(\3)\3)\3)\3)\5)\u01c6")
        buf.write("\n)\3*\3*\3*\3*\3*\5*\u01cd\n*\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\5,\u01d7\n,\3,\3,\3,\5,\u01dc\n,\3,\3,\3-\3-\3-\3-\5")
        buf.write("-\u01e4\n-\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\5\60\u01f6\n\60\3\61\3\61\3\61\5\61\u01fb")
        buf.write("\n\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\5\63\u0205")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0223\n\67\3")
        buf.write("8\38\38\38\38\38\58\u022b\n8\39\39\39\59\u0230\n9\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3<\3<\5")
        buf.write("<\u0245\n<\3=\3=\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3")
        buf.write("E\5E\u0268\nE\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3J\3")
        buf.write("J\3J\3J\7J\u027a\nJ\fJ\16J\u027d\13J\3K\3K\3K\3K\3K\3")
        buf.write("K\7K\u0285\nK\fK\16K\u0288\13K\3L\3L\3L\3L\3L\3L\3L\7")
        buf.write("L\u0291\nL\fL\16L\u0294\13L\3M\3M\3M\3M\3M\3M\3M\7M\u029d")
        buf.write("\nM\fM\16M\u02a0\13M\3N\3N\3N\3N\3N\3N\3N\7N\u02a9\nN")
        buf.write("\fN\16N\u02ac\13N\3O\3O\3O\3O\5O\u02b2\nO\3P\3P\3P\3P")
        buf.write("\3P\3P\3P\3P\3P\3P\3P\7P\u02bf\nP\fP\16P\u02c2\13P\3Q")
        buf.write("\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u02cb\nQ\3R\3R\3R\3R\3R\3R\3R\5")
        buf.write("R\u02d4\nR\3S\3S\3T\3T\3T\5T\u02db\nT\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\7U\u02e5\nU\fU\16U\u02e8\13U\3V\3V\3W\3W\3W\3")
        buf.write("W\3W\7W\u02f1\nW\fW\16W\u02f4\13W\3X\3X\3X\3X\3X\2\f,")
        buf.write("<\u0092\u0094\u0096\u0098\u009a\u009e\u00a8\u00acY\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write("\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8")
        buf.write("\u00aa\u00ac\u00ae\2\n\3\2;>\3\2\31\32\3\2).\3\2 %\3\2")
        buf.write("\33\34\3\2\35\37\4\2\34\34((\3\2\17\22\2\u02f5\2\u00b0")
        buf.write("\3\2\2\2\4\u00b2\3\2\2\2\6\u00b4\3\2\2\2\b\u00bb\3\2\2")
        buf.write("\2\n\u00c6\3\2\2\2\f\u00cc\3\2\2\2\16\u00d3\3\2\2\2\20")
        buf.write("\u00d7\3\2\2\2\22\u00d9\3\2\2\2\24\u00e3\3\2\2\2\26\u00e8")
        buf.write("\3\2\2\2\30\u00f0\3\2\2\2\32\u00f2\3\2\2\2\34\u0103\3")
        buf.write("\2\2\2\36\u0118\3\2\2\2 \u011a\3\2\2\2\"\u011c\3\2\2\2")
        buf.write("$\u0124\3\2\2\2&\u0129\3\2\2\2(\u012b\3\2\2\2*\u0133\3")
        buf.write("\2\2\2,\u0135\3\2\2\2.\u013f\3\2\2\2\60\u0145\3\2\2\2")
        buf.write("\62\u0147\3\2\2\2\64\u014f\3\2\2\2\66\u015d\3\2\2\28\u0164")
        buf.write("\3\2\2\2:\u0166\3\2\2\2<\u0168\3\2\2\2>\u0182\3\2\2\2")
        buf.write("@\u0184\3\2\2\2B\u0191\3\2\2\2D\u0198\3\2\2\2F\u01a5\3")
        buf.write("\2\2\2H\u01a7\3\2\2\2J\u01b3\3\2\2\2L\u01b5\3\2\2\2N\u01b9")
        buf.write("\3\2\2\2P\u01c5\3\2\2\2R\u01cc\3\2\2\2T\u01ce\3\2\2\2")
        buf.write("V\u01d2\3\2\2\2X\u01e3\3\2\2\2Z\u01e5\3\2\2\2\\\u01ed")
        buf.write("\3\2\2\2^\u01f5\3\2\2\2`\u01fa\3\2\2\2b\u01fc\3\2\2\2")
        buf.write("d\u0204\3\2\2\2f\u0206\3\2\2\2h\u020b\3\2\2\2j\u020d\3")
        buf.write("\2\2\2l\u0222\3\2\2\2n\u022a\3\2\2\2p\u022f\3\2\2\2r\u0231")
        buf.write("\3\2\2\2t\u0238\3\2\2\2v\u0244\3\2\2\2x\u0246\3\2\2\2")
        buf.write("z\u0248\3\2\2\2|\u024c\3\2\2\2~\u0258\3\2\2\2\u0080\u025a")
        buf.write("\3\2\2\2\u0082\u025c\3\2\2\2\u0084\u025e\3\2\2\2\u0086")
        buf.write("\u0261\3\2\2\2\u0088\u0264\3\2\2\2\u008a\u026b\3\2\2\2")
        buf.write("\u008c\u026d\3\2\2\2\u008e\u026f\3\2\2\2\u0090\u0271\3")
        buf.write("\2\2\2\u0092\u0273\3\2\2\2\u0094\u027e\3\2\2\2\u0096\u0289")
        buf.write("\3\2\2\2\u0098\u0295\3\2\2\2\u009a\u02a1\3\2\2\2\u009c")
        buf.write("\u02b1\3\2\2\2\u009e\u02b3\3\2\2\2\u00a0\u02ca\3\2\2\2")
        buf.write("\u00a2\u02d3\3\2\2\2\u00a4\u02d5\3\2\2\2\u00a6\u02da\3")
        buf.write("\2\2\2\u00a8\u02dc\3\2\2\2\u00aa\u02e9\3\2\2\2\u00ac\u02eb")
        buf.write("\3\2\2\2\u00ae\u02f5\3\2\2\2\u00b0\u00b1\t\2\2\2\u00b1")
        buf.write("\3\3\2\2\2\u00b2\u00b3\t\3\2\2\u00b3\5\3\2\2\2\u00b4\u00b5")
        buf.write("\5\b\5\2\u00b5\u00b6\7\2\2\3\u00b6\7\3\2\2\2\u00b7\u00b8")
        buf.write("\5\16\b\2\u00b8\u00b9\5\b\5\2\u00b9\u00bc\3\2\2\2\u00ba")
        buf.write("\u00bc\5\16\b\2\u00bb\u00b7\3\2\2\2\u00bb\u00ba\3\2\2")
        buf.write("\2\u00bc\t\3\2\2\2\u00bd\u00c7\5\20\t\2\u00be\u00c7\5")
        buf.write("\26\f\2\u00bf\u00c7\5f\64\2\u00c0\u00c7\5.\30\2\u00c1")
        buf.write("\u00c7\5j\66\2\u00c2\u00c7\5p9\2\u00c3\u00c7\5\u0084C")
        buf.write("\2\u00c4\u00c7\5\u0086D\2\u00c5\u00c7\5\u0088E\2\u00c6")
        buf.write("\u00bd\3\2\2\2\u00c6\u00be\3\2\2\2\u00c6\u00bf\3\2\2\2")
        buf.write("\u00c6\u00c0\3\2\2\2\u00c6\u00c1\3\2\2\2\u00c6\u00c2\3")
        buf.write("\2\2\2\u00c6\u00c3\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\13\3\2\2\2\u00c8\u00c9\5\n\6\2\u00c9\u00ca")
        buf.write("\5\f\7\2\u00ca\u00cd\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc")
        buf.write("\u00c8\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\r\3\2\2\2\u00ce")
        buf.write("\u00d4\5\20\t\2\u00cf\u00d4\5\26\f\2\u00d0\u00d4\5\30")
        buf.write("\r\2\u00d1\u00d4\5H%\2\u00d2\u00d4\5Z.\2\u00d3\u00ce\3")
        buf.write("\2\2\2\u00d3\u00cf\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\17\3\2\2\2\u00d5\u00d8")
        buf.write("\5\22\n\2\u00d6\u00d8\5\24\13\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d6\3\2\2\2\u00d8\21\3\2\2\2\u00d9\u00da\7\24\2\2\u00da")
        buf.write("\u00dd\7:\2\2\u00db\u00de\5\u00a6T\2\u00dc\u00de\3\2\2")
        buf.write("\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df\u00e0\7/\2\2\u00e0\u00e1\5\u0092J\2\u00e1")
        buf.write("\u00e2\78\2\2\u00e2\23\3\2\2\2\u00e3\u00e4\7\24\2\2\u00e4")
        buf.write("\u00e5\7:\2\2\u00e5\u00e6\5\u00a6T\2\u00e6\u00e7\78\2")
        buf.write("\2\u00e7\25\3\2\2\2\u00e8\u00e9\7\23\2\2\u00e9\u00ea\7")
        buf.write(":\2\2\u00ea\u00eb\7/\2\2\u00eb\u00ec\5\u0092J\2\u00ec")
        buf.write("\u00ed\78\2\2\u00ed\27\3\2\2\2\u00ee\u00f1\5\32\16\2\u00ef")
        buf.write("\u00f1\5\34\17\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2")
        buf.write("\2\u00f1\31\3\2\2\2\u00f2\u00f3\7\13\2\2\u00f3\u00f4\7")
        buf.write(":\2\2\u00f4\u00f7\7\61\2\2\u00f5\u00f8\5*\26\2\u00f6\u00f8")
        buf.write("\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\u00fc\7\62\2\2\u00fa\u00fd\5\u00a6")
        buf.write("T\2\u00fb\u00fd\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fb")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\7\63\2\2\u00ff")
        buf.write("\u0100\5\f\7\2\u0100\u0101\7\64\2\2\u0101\u0102\78\2\2")
        buf.write("\u0102\33\3\2\2\2\u0103\u0104\7\13\2\2\u0104\u0105\7\61")
        buf.write("\2\2\u0105\u0106\5\36\20\2\u0106\u0107\5 \21\2\u0107\u0108")
        buf.write("\7\62\2\2\u0108\u0109\7:\2\2\u0109\u010c\7\61\2\2\u010a")
        buf.write("\u010d\5*\26\2\u010b\u010d\3\2\2\2\u010c\u010a\3\2\2\2")
        buf.write("\u010c\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0111\7")
        buf.write("\62\2\2\u010f\u0112\5\u00a6T\2\u0110\u0112\3\2\2\2\u0111")
        buf.write("\u010f\3\2\2\2\u0111\u0110\3\2\2\2\u0112\u0113\3\2\2\2")
        buf.write("\u0113\u0114\7\63\2\2\u0114\u0115\5\f\7\2\u0115\u0116")
        buf.write("\7\64\2\2\u0116\u0117\78\2\2\u0117\35\3\2\2\2\u0118\u0119")
        buf.write("\7:\2\2\u0119\37\3\2\2\2\u011a\u011b\7:\2\2\u011b!\3\2")
        buf.write("\2\2\u011c\u011d\5&\24\2\u011d\u011e\5$\23\2\u011e#\3")
        buf.write("\2\2\2\u011f\u0120\7\67\2\2\u0120\u0121\5&\24\2\u0121")
        buf.write("\u0122\5$\23\2\u0122\u0125\3\2\2\2\u0123\u0125\3\2\2\2")
        buf.write("\u0124\u011f\3\2\2\2\u0124\u0123\3\2\2\2\u0125%\3\2\2")
        buf.write("\2\u0126\u0127\7:\2\2\u0127\u012a\5\u00a6T\2\u0128\u012a")
        buf.write("\7:\2\2\u0129\u0126\3\2\2\2\u0129\u0128\3\2\2\2\u012a")
        buf.write("\'\3\2\2\2\u012b\u012c\7:\2\2\u012c\u012d\5\u00a6T\2\u012d")
        buf.write(")\3\2\2\2\u012e\u012f\5\"\22\2\u012f\u0130\7\67\2\2\u0130")
        buf.write("\u0131\5(\25\2\u0131\u0134\3\2\2\2\u0132\u0134\5(\25\2")
        buf.write("\u0133\u012e\3\2\2\2\u0133\u0132\3\2\2\2\u0134+\3\2\2")
        buf.write("\2\u0135\u013c\b\27\1\2\u0136\u0137\f\4\2\2\u0137\u0138")
        buf.write("\5\60\31\2\u0138\u0139\7\60\2\2\u0139\u013b\3\2\2\2\u013a")
        buf.write("\u0136\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d-\3\2\2\2\u013e\u013c\3\2\2")
        buf.write("\2\u013f\u0140\5,\27\2\u0140\u0141\5\60\31\2\u0141\u0142")
        buf.write("\78\2\2\u0142/\3\2\2\2\u0143\u0146\5\62\32\2\u0144\u0146")
        buf.write("\5\64\33\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u0146")
        buf.write("\61\3\2\2\2\u0147\u0148\7:\2\2\u0148\u014b\7\61\2\2\u0149")
        buf.write("\u014c\5\66\34\2\u014a\u014c\3\2\2\2\u014b\u0149\3\2\2")
        buf.write("\2\u014b\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e")
        buf.write("\7\62\2\2\u014e\63\3\2\2\2\u014f\u0150\5\u00a8U\2\u0150")
        buf.write("\u0151\7\60\2\2\u0151\u0152\7:\2\2\u0152\u0155\7\61\2")
        buf.write("\2\u0153\u0156\5\66\34\2\u0154\u0156\3\2\2\2\u0155\u0153")
        buf.write("\3\2\2\2\u0155\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("\u0158\7\62\2\2\u0158\65\3\2\2\2\u0159\u015a\5:\36\2\u015a")
        buf.write("\u015b\58\35\2\u015b\u015e\3\2\2\2\u015c\u015e\5:\36\2")
        buf.write("\u015d\u0159\3\2\2\2\u015d\u015c\3\2\2\2\u015e\67\3\2")
        buf.write("\2\2\u015f\u0160\7\67\2\2\u0160\u0161\5:\36\2\u0161\u0162")
        buf.write("\58\35\2\u0162\u0165\3\2\2\2\u0163\u0165\3\2\2\2\u0164")
        buf.write("\u015f\3\2\2\2\u0164\u0163\3\2\2\2\u01659\3\2\2\2\u0166")
        buf.write("\u0167\5\u0092J\2\u0167;\3\2\2\2\u0168\u0169\b\37\1\2")
        buf.write("\u0169\u016c\7\65\2\2\u016a\u016d\5\2\2\2\u016b\u016d")
        buf.write("\7:\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016e\u016f\7\66\2\2\u016f\u0179\3\2\2")
        buf.write("\2\u0170\u0171\f\4\2\2\u0171\u0174\7\65\2\2\u0172\u0175")
        buf.write("\5\2\2\2\u0173\u0175\7:\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178\7\66\2")
        buf.write("\2\u0177\u0170\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u0179\u017a\3\2\2\2\u017a=\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017c\u017d\5<\37\2\u017d\u017e\5\u00a4S\2\u017e")
        buf.write("\u0183\3\2\2\2\u017f\u0180\5<\37\2\u0180\u0181\7:\2\2")
        buf.write("\u0181\u0183\3\2\2\2\u0182\u017c\3\2\2\2\u0182\u017f\3")
        buf.write("\2\2\2\u0183?\3\2\2\2\u0184\u0187\5<\37\2\u0185\u0188")
        buf.write("\5\u00a4S\2\u0186\u0188\7:\2\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\7\63\2")
        buf.write("\2\u018a\u018b\5B\"\2\u018b\u018c\7\64\2\2\u018cA\3\2")
        buf.write("\2\2\u018d\u018e\5F$\2\u018e\u018f\5D#\2\u018f\u0192\3")
        buf.write("\2\2\2\u0190\u0192\5F$\2\u0191\u018d\3\2\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192C\3\2\2\2\u0193\u0194\7\67\2\2\u0194\u0195")
        buf.write("\5F$\2\u0195\u0196\5D#\2\u0196\u0199\3\2\2\2\u0197\u0199")
        buf.write("\3\2\2\2\u0198\u0193\3\2\2\2\u0198\u0197\3\2\2\2\u0199")
        buf.write("E\3\2\2\2\u019a\u01a6\5\2\2\2\u019b\u01a6\7?\2\2\u019c")
        buf.write("\u01a6\7@\2\2\u019d\u01a6\5\4\3\2\u019e\u01a6\7\30\2\2")
        buf.write("\u019f\u01a6\5N(\2\u01a0\u01a6\7:\2\2\u01a1\u01a2\7\63")
        buf.write("\2\2\u01a2\u01a3\5B\"\2\u01a3\u01a4\7\64\2\2\u01a4\u01a6")
        buf.write("\3\2\2\2\u01a5\u019a\3\2\2\2\u01a5\u019b\3\2\2\2\u01a5")
        buf.write("\u019c\3\2\2\2\u01a5\u019d\3\2\2\2\u01a5\u019e\3\2\2\2")
        buf.write("\u01a5\u019f\3\2\2\2\u01a5\u01a0\3\2\2\2\u01a5\u01a1\3")
        buf.write("\2\2\2\u01a6G\3\2\2\2\u01a7\u01a8\7\f\2\2\u01a8\u01a9")
        buf.write("\7:\2\2\u01a9\u01aa\7\r\2\2\u01aa\u01ab\7\63\2\2\u01ab")
        buf.write("\u01ac\5J&\2\u01ac\u01ad\7\64\2\2\u01ad\u01ae\78\2\2\u01ae")
        buf.write("I\3\2\2\2\u01af\u01b0\5L\'\2\u01b0\u01b1\5J&\2\u01b1\u01b4")
        buf.write("\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01af\3\2\2\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4K\3\2\2\2\u01b5\u01b6\7:\2\2\u01b6")
        buf.write("\u01b7\5\u00a6T\2\u01b7\u01b8\78\2\2\u01b8M\3\2\2\2\u01b9")
        buf.write("\u01ba\7:\2\2\u01ba\u01bd\7\63\2\2\u01bb\u01be\5P)\2\u01bc")
        buf.write("\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c0\7\64\2\2\u01c0O\3\2\2")
        buf.write("\2\u01c1\u01c2\5T+\2\u01c2\u01c3\5R*\2\u01c3\u01c6\3\2")
        buf.write("\2\2\u01c4\u01c6\5T+\2\u01c5\u01c1\3\2\2\2\u01c5\u01c4")
        buf.write("\3\2\2\2\u01c6Q\3\2\2\2\u01c7\u01c8\7\67\2\2\u01c8\u01c9")
        buf.write("\5T+\2\u01c9\u01ca\5R*\2\u01ca\u01cd\3\2\2\2\u01cb\u01cd")
        buf.write("\3\2\2\2\u01cc\u01c7\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cd")
        buf.write("S\3\2\2\2\u01ce\u01cf\7:\2\2\u01cf\u01d0\79\2\2\u01d0")
        buf.write("\u01d1\5\u0092J\2\u01d1U\3\2\2\2\u01d2\u01d3\7:\2\2\u01d3")
        buf.write("\u01d6\7\61\2\2\u01d4\u01d7\5d\63\2\u01d5\u01d7\3\2\2")
        buf.write("\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01d8")
        buf.write("\3\2\2\2\u01d8\u01db\7\62\2\2\u01d9\u01dc\5\u00a6T\2\u01da")
        buf.write("\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01da\3\2\2\2")
        buf.write("\u01dc\u01dd\3\2\2\2\u01dd\u01de\78\2\2\u01deW\3\2\2\2")
        buf.write("\u01df\u01e0\5V,\2\u01e0\u01e1\5X-\2\u01e1\u01e4\3\2\2")
        buf.write("\2\u01e2\u01e4\3\2\2\2\u01e3\u01df\3\2\2\2\u01e3\u01e2")
        buf.write("\3\2\2\2\u01e4Y\3\2\2\2\u01e5\u01e6\7\f\2\2\u01e6\u01e7")
        buf.write("\7:\2\2\u01e7\u01e8\7\16\2\2\u01e8\u01e9\7\63\2\2\u01e9")
        buf.write("\u01ea\5X-\2\u01ea\u01eb\7\64\2\2\u01eb\u01ec\78\2\2\u01ec")
        buf.write("[\3\2\2\2\u01ed\u01ee\5`\61\2\u01ee\u01ef\5^\60\2\u01ef")
        buf.write("]\3\2\2\2\u01f0\u01f1\7\67\2\2\u01f1\u01f2\5`\61\2\u01f2")
        buf.write("\u01f3\5^\60\2\u01f3\u01f6\3\2\2\2\u01f4\u01f6\3\2\2\2")
        buf.write("\u01f5\u01f0\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6_\3\2\2")
        buf.write("\2\u01f7\u01f8\7:\2\2\u01f8\u01fb\5\u00a6T\2\u01f9\u01fb")
        buf.write("\7:\2\2\u01fa\u01f7\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fb")
        buf.write("a\3\2\2\2\u01fc\u01fd\7:\2\2\u01fd\u01fe\5\u00a6T\2\u01fe")
        buf.write("c\3\2\2\2\u01ff\u0200\5\\/\2\u0200\u0201\7\67\2\2\u0201")
        buf.write("\u0202\5b\62\2\u0202\u0205\3\2\2\2\u0203\u0205\5b\62\2")
        buf.write("\u0204\u01ff\3\2\2\2\u0204\u0203\3\2\2\2\u0205e\3\2\2")
        buf.write("\2\u0206\u0207\5\u00a8U\2\u0207\u0208\5h\65\2\u0208\u0209")
        buf.write("\5\u0092J\2\u0209\u020a\78\2\2\u020ag\3\2\2\2\u020b\u020c")
        buf.write("\t\4\2\2\u020ci\3\2\2\2\u020d\u020e\7\7\2\2\u020e\u020f")
        buf.write("\7\61\2\2\u020f\u0210\5x=\2\u0210\u0211\7\62\2\2\u0211")
        buf.write("\u0212\7\63\2\2\u0212\u0213\5\f\7\2\u0213\u0214\7\64\2")
        buf.write("\2\u0214\u0215\5l\67\2\u0215\u0216\78\2\2\u0216k\3\2\2")
        buf.write("\2\u0217\u0218\7\b\2\2\u0218\u0219\7\7\2\2\u0219\u021a")
        buf.write("\7\61\2\2\u021a\u021b\5x=\2\u021b\u021c\7\62\2\2\u021c")
        buf.write("\u021d\7\63\2\2\u021d\u021e\5\f\7\2\u021e\u021f\7\64\2")
        buf.write("\2\u021f\u0220\5l\67\2\u0220\u0223\3\2\2\2\u0221\u0223")
        buf.write("\5n8\2\u0222\u0217\3\2\2\2\u0222\u0221\3\2\2\2\u0223m")
        buf.write("\3\2\2\2\u0224\u0225\7\b\2\2\u0225\u0226\7\63\2\2\u0226")
        buf.write("\u0227\5\f\7\2\u0227\u0228\7\64\2\2\u0228\u022b\3\2\2")
        buf.write("\2\u0229\u022b\3\2\2\2\u022a\u0224\3\2\2\2\u022a\u0229")
        buf.write("\3\2\2\2\u022bo\3\2\2\2\u022c\u0230\5r:\2\u022d\u0230")
        buf.write("\5t;\2\u022e\u0230\5|?\2\u022f\u022c\3\2\2\2\u022f\u022d")
        buf.write("\3\2\2\2\u022f\u022e\3\2\2\2\u0230q\3\2\2\2\u0231\u0232")
        buf.write("\7\t\2\2\u0232\u0233\5x=\2\u0233\u0234\7\63\2\2\u0234")
        buf.write("\u0235\5\f\7\2\u0235\u0236\7\64\2\2\u0236\u0237\78\2\2")
        buf.write("\u0237s\3\2\2\2\u0238\u0239\7\t\2\2\u0239\u023a\5v<\2")
        buf.write("\u023a\u023b\5x=\2\u023b\u023c\78\2\2\u023c\u023d\5z>")
        buf.write("\2\u023d\u023e\7\63\2\2\u023e\u023f\5\f\7\2\u023f\u0240")
        buf.write("\7\64\2\2\u0240\u0241\78\2\2\u0241u\3\2\2\2\u0242\u0245")
        buf.write("\5f\64\2\u0243\u0245\5\22\n\2\u0244\u0242\3\2\2\2\u0244")
        buf.write("\u0243\3\2\2\2\u0245w\3\2\2\2\u0246\u0247\5\u0092J\2\u0247")
        buf.write("y\3\2\2\2\u0248\u0249\5\u00a8U\2\u0249\u024a\5h\65\2\u024a")
        buf.write("\u024b\5\u0092J\2\u024b{\3\2\2\2\u024c\u024d\7\t\2\2\u024d")
        buf.write("\u024e\5~@\2\u024e\u024f\7\67\2\2\u024f\u0250\5\u0080")
        buf.write("A\2\u0250\u0251\7)\2\2\u0251\u0252\7\27\2\2\u0252\u0253")
        buf.write("\5\u0082B\2\u0253\u0254\7\63\2\2\u0254\u0255\5\f\7\2\u0255")
        buf.write("\u0256\7\64\2\2\u0256\u0257\78\2\2\u0257}\3\2\2\2\u0258")
        buf.write("\u0259\7:\2\2\u0259\177\3\2\2\2\u025a\u025b\7:\2\2\u025b")
        buf.write("\u0081\3\2\2\2\u025c\u025d\5\u0092J\2\u025d\u0083\3\2")
        buf.write("\2\2\u025e\u025f\7\26\2\2\u025f\u0260\78\2\2\u0260\u0085")
        buf.write("\3\2\2\2\u0261\u0262\7\25\2\2\u0262\u0263\78\2\2\u0263")
        buf.write("\u0087\3\2\2\2\u0264\u0267\7\n\2\2\u0265\u0268\5\u0092")
        buf.write("J\2\u0266\u0268\3\2\2\2\u0267\u0265\3\2\2\2\u0267\u0266")
        buf.write("\3\2\2\2\u0268\u0269\3\2\2\2\u0269\u026a\78\2\2\u026a")
        buf.write("\u0089\3\2\2\2\u026b\u026c\t\5\2\2\u026c\u008b\3\2\2\2")
        buf.write("\u026d\u026e\t\6\2\2\u026e\u008d\3\2\2\2\u026f\u0270\t")
        buf.write("\7\2\2\u0270\u008f\3\2\2\2\u0271\u0272\t\b\2\2\u0272\u0091")
        buf.write("\3\2\2\2\u0273\u0274\bJ\1\2\u0274\u0275\5\u0094K\2\u0275")
        buf.write("\u027b\3\2\2\2\u0276\u0277\f\4\2\2\u0277\u0278\7\'\2\2")
        buf.write("\u0278\u027a\5\u0094K\2\u0279\u0276\3\2\2\2\u027a\u027d")
        buf.write("\3\2\2\2\u027b\u0279\3\2\2\2\u027b\u027c\3\2\2\2\u027c")
        buf.write("\u0093\3\2\2\2\u027d\u027b\3\2\2\2\u027e\u027f\bK\1\2")
        buf.write("\u027f\u0280\5\u0096L\2\u0280\u0286\3\2\2\2\u0281\u0282")
        buf.write("\f\4\2\2\u0282\u0283\7&\2\2\u0283\u0285\5\u0096L\2\u0284")
        buf.write("\u0281\3\2\2\2\u0285\u0288\3\2\2\2\u0286\u0284\3\2\2\2")
        buf.write("\u0286\u0287\3\2\2\2\u0287\u0095\3\2\2\2\u0288\u0286\3")
        buf.write("\2\2\2\u0289\u028a\bL\1\2\u028a\u028b\5\u0098M\2\u028b")
        buf.write("\u0292\3\2\2\2\u028c\u028d\f\4\2\2\u028d\u028e\5\u008a")
        buf.write("F\2\u028e\u028f\5\u0098M\2\u028f\u0291\3\2\2\2\u0290\u028c")
        buf.write("\3\2\2\2\u0291\u0294\3\2\2\2\u0292\u0290\3\2\2\2\u0292")
        buf.write("\u0293\3\2\2\2\u0293\u0097\3\2\2\2\u0294\u0292\3\2\2\2")
        buf.write("\u0295\u0296\bM\1\2\u0296\u0297\5\u009aN\2\u0297\u029e")
        buf.write("\3\2\2\2\u0298\u0299\f\4\2\2\u0299\u029a\5\u008cG\2\u029a")
        buf.write("\u029b\5\u009aN\2\u029b\u029d\3\2\2\2\u029c\u0298\3\2")
        buf.write("\2\2\u029d\u02a0\3\2\2\2\u029e\u029c\3\2\2\2\u029e\u029f")
        buf.write("\3\2\2\2\u029f\u0099\3\2\2\2\u02a0\u029e\3\2\2\2\u02a1")
        buf.write("\u02a2\bN\1\2\u02a2\u02a3\5\u009cO\2\u02a3\u02aa\3\2\2")
        buf.write("\2\u02a4\u02a5\f\4\2\2\u02a5\u02a6\5\u008eH\2\u02a6\u02a7")
        buf.write("\5\u009cO\2\u02a7\u02a9\3\2\2\2\u02a8\u02a4\3\2\2\2\u02a9")
        buf.write("\u02ac\3\2\2\2\u02aa\u02a8\3\2\2\2\u02aa\u02ab\3\2\2\2")
        buf.write("\u02ab\u009b\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ad\u02ae\5")
        buf.write("\u0090I\2\u02ae\u02af\5\u009cO\2\u02af\u02b2\3\2\2\2\u02b0")
        buf.write("\u02b2\5\u009eP\2\u02b1\u02ad\3\2\2\2\u02b1\u02b0\3\2")
        buf.write("\2\2\u02b2\u009d\3\2\2\2\u02b3\u02b4\bP\1\2\u02b4\u02b5")
        buf.write("\5\u00a0Q\2\u02b5\u02c0\3\2\2\2\u02b6\u02b7\f\6\2\2\u02b7")
        buf.write("\u02b8\7\60\2\2\u02b8\u02bf\5\u00aaV\2\u02b9\u02ba\f\5")
        buf.write("\2\2\u02ba\u02bb\7\60\2\2\u02bb\u02bf\5\62\32\2\u02bc")
        buf.write("\u02bd\f\4\2\2\u02bd\u02bf\5\u00acW\2\u02be\u02b6\3\2")
        buf.write("\2\2\u02be\u02b9\3\2\2\2\u02be\u02bc\3\2\2\2\u02bf\u02c2")
        buf.write("\3\2\2\2\u02c0\u02be\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1")
        buf.write("\u009f\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c3\u02cb\5\u00a2")
        buf.write("R\2\u02c4\u02cb\7:\2\2\u02c5\u02cb\5\62\32\2\u02c6\u02c7")
        buf.write("\7\61\2\2\u02c7\u02c8\5\u0092J\2\u02c8\u02c9\7\62\2\2")
        buf.write("\u02c9\u02cb\3\2\2\2\u02ca\u02c3\3\2\2\2\u02ca\u02c4\3")
        buf.write("\2\2\2\u02ca\u02c5\3\2\2\2\u02ca\u02c6\3\2\2\2\u02cb\u00a1")
        buf.write("\3\2\2\2\u02cc\u02d4\5\2\2\2\u02cd\u02d4\7?\2\2\u02ce")
        buf.write("\u02d4\7@\2\2\u02cf\u02d4\5\4\3\2\u02d0\u02d4\7\30\2\2")
        buf.write("\u02d1\u02d4\5N(\2\u02d2\u02d4\5@!\2\u02d3\u02cc\3\2\2")
        buf.write("\2\u02d3\u02cd\3\2\2\2\u02d3\u02ce\3\2\2\2\u02d3\u02cf")
        buf.write("\3\2\2\2\u02d3\u02d0\3\2\2\2\u02d3\u02d1\3\2\2\2\u02d3")
        buf.write("\u02d2\3\2\2\2\u02d4\u00a3\3\2\2\2\u02d5\u02d6\t\t\2\2")
        buf.write("\u02d6\u00a5\3\2\2\2\u02d7\u02db\7:\2\2\u02d8\u02db\5")
        buf.write("\u00a4S\2\u02d9\u02db\5> \2\u02da\u02d7\3\2\2\2\u02da")
        buf.write("\u02d8\3\2\2\2\u02da\u02d9\3\2\2\2\u02db\u00a7\3\2\2\2")
        buf.write("\u02dc\u02dd\bU\1\2\u02dd\u02de\7:\2\2\u02de\u02e6\3\2")
        buf.write("\2\2\u02df\u02e0\f\5\2\2\u02e0\u02e1\7\60\2\2\u02e1\u02e5")
        buf.write("\5\u00aaV\2\u02e2\u02e3\f\4\2\2\u02e3\u02e5\5\u00acW\2")
        buf.write("\u02e4\u02df\3\2\2\2\u02e4\u02e2\3\2\2\2\u02e5\u02e8\3")
        buf.write("\2\2\2\u02e6\u02e4\3\2\2\2\u02e6\u02e7\3\2\2\2\u02e7\u00a9")
        buf.write("\3\2\2\2\u02e8\u02e6\3\2\2\2\u02e9\u02ea\7:\2\2\u02ea")
        buf.write("\u00ab\3\2\2\2\u02eb\u02ec\bW\1\2\u02ec\u02ed\5\u00ae")
        buf.write("X\2\u02ed\u02f2\3\2\2\2\u02ee\u02ef\f\4\2\2\u02ef\u02f1")
        buf.write("\5\u00aeX\2\u02f0\u02ee\3\2\2\2\u02f1\u02f4\3\2\2\2\u02f2")
        buf.write("\u02f0\3\2\2\2\u02f2\u02f3\3\2\2\2\u02f3\u00ad\3\2\2\2")
        buf.write("\u02f4\u02f2\3\2\2\2\u02f5\u02f6\7\65\2\2\u02f6\u02f7")
        buf.write("\5\u0092J\2\u02f7\u02f8\7\66\2\2\u02f8\u00af\3\2\2\2;")
        buf.write("\u00bb\u00c6\u00cc\u00d3\u00d7\u00dd\u00f0\u00f7\u00fc")
        buf.write("\u010c\u0111\u0124\u0129\u0133\u013c\u0145\u014b\u0155")
        buf.write("\u015d\u0164\u016c\u0174\u0179\u0182\u0187\u0191\u0198")
        buf.write("\u01a5\u01b3\u01bd\u01c5\u01cc\u01d6\u01db\u01e3\u01f5")
        buf.write("\u01fa\u0204\u0222\u022a\u022f\u0244\u0267\u027b\u0286")
        buf.write("\u0292\u029e\u02aa\u02b1\u02be\u02c0\u02ca\u02d3\u02da")
        buf.write("\u02e4\u02e6\u02f2")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "NL", "WS", "SG_CMT", "MUL_CMT", "IF", 
                      "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
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
    RULE_function_decl = 12
    RULE_method_decl = 13
    RULE_rec = 14
    RULE_rec_type = 15
    RULE_not_last_para_func = 16
    RULE_tail_para_func = 17
    RULE_para_func = 18
    RULE_last_para_func = 19
    RULE_list_para_func = 20
    RULE_star_func_call_dot = 21
    RULE_func_call_stmt = 22
    RULE_func_call = 23
    RULE_function_call = 24
    RULE_method_call = 25
    RULE_list_arg = 26
    RULE_tail_arg = 27
    RULE_arg = 28
    RULE_arr_dim_decl = 29
    RULE_arr_type = 30
    RULE_arr_lit = 31
    RULE_list_ele_arr = 32
    RULE_tail_ele_arr = 33
    RULE_ele_arr = 34
    RULE_struct_decl = 35
    RULE_star_struct_ele_decl = 36
    RULE_attr_decl = 37
    RULE_struct_lit = 38
    RULE_list_ele_struct = 39
    RULE_tail_ele_struct = 40
    RULE_ele_struct = 41
    RULE_method_interface = 42
    RULE_star_interface_method_decl = 43
    RULE_interface_decl = 44
    RULE_not_last_para = 45
    RULE_tail_para = 46
    RULE_para = 47
    RULE_last_para = 48
    RULE_list_para = 49
    RULE_assign_stmt = 50
    RULE_assign_op = 51
    RULE_if_stmt = 52
    RULE_else_if = 53
    RULE_else_stmt = 54
    RULE_for_stmt = 55
    RULE_basic_for = 56
    RULE_init_for = 57
    RULE_init = 58
    RULE_condit = 59
    RULE_update = 60
    RULE_range_for = 61
    RULE_index = 62
    RULE_value = 63
    RULE_array_id = 64
    RULE_break_stmt = 65
    RULE_continue_stmt = 66
    RULE_return_stmt = 67
    RULE_rela_op = 68
    RULE_addsub = 69
    RULE_mudimo = 70
    RULE_unary = 71
    RULE_expr1 = 72
    RULE_expr2 = 73
    RULE_expr3 = 74
    RULE_expr4 = 75
    RULE_expr5 = 76
    RULE_expr6 = 77
    RULE_expr7 = 78
    RULE_operand = 79
    RULE_lit = 80
    RULE_primi = 81
    RULE_all_type = 82
    RULE_lhs = 83
    RULE_field = 84
    RULE_dims = 85
    RULE_dim = 86

    ruleNames =  [ "int_lit", "bool_lit", "program", "manydecl", "stmt", 
                   "stmt_block", "decl", "var_decl", "var_decl_init", "var_decl_uninit", 
                   "const_decl", "func_decl", "function_decl", "method_decl", 
                   "rec", "rec_type", "not_last_para_func", "tail_para_func", 
                   "para_func", "last_para_func", "list_para_func", "star_func_call_dot", 
                   "func_call_stmt", "func_call", "function_call", "method_call", 
                   "list_arg", "tail_arg", "arg", "arr_dim_decl", "arr_type", 
                   "arr_lit", "list_ele_arr", "tail_ele_arr", "ele_arr", 
                   "struct_decl", "star_struct_ele_decl", "attr_decl", "struct_lit", 
                   "list_ele_struct", "tail_ele_struct", "ele_struct", "method_interface", 
                   "star_interface_method_decl", "interface_decl", "not_last_para", 
                   "tail_para", "para", "last_para", "list_para", "assign_stmt", 
                   "assign_op", "if_stmt", "else_if", "else_stmt", "for_stmt", 
                   "basic_for", "init_for", "init", "condit", "update", 
                   "range_for", "index", "value", "array_id", "break_stmt", 
                   "continue_stmt", "return_stmt", "rela_op", "addsub", 
                   "mudimo", "unary", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "operand", "lit", "primi", 
                   "all_type", "lhs", "field", "dims", "dim" ]

    EOF = Token.EOF
    NL=1
    WS=2
    SG_CMT=3
    MUL_CMT=4
    IF=5
    ELSE=6
    FOR=7
    RETURN=8
    FUNC=9
    TYPE=10
    STRUCT=11
    INTERFACE=12
    STRING=13
    INT=14
    FLOAT=15
    BOOLEAN=16
    CONST=17
    VAR=18
    CONTINUE=19
    BREAK=20
    RANGE=21
    NIL=22
    TRUE=23
    FALSE=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    DBL_EQ=30
    NOT_EQ=31
    LT=32
    LE=33
    GT=34
    GE=35
    AND=36
    OR=37
    NOT=38
    AS_EQ=39
    ADD_EQ=40
    SUB_EQ=41
    MUL_EQ=42
    DIV_EQ=43
    MOD_EQ=44
    EQ=45
    DOT=46
    LCIB=47
    RCIB=48
    LCUB=49
    RCUB=50
    LSQB=51
    RSQB=52
    COMMA=53
    SECO=54
    COLON=55
    ID=56
    DEC=57
    BIN=58
    OCT=59
    HEX=60
    FLOAT_LIT=61
    STRING_LIT=62
    ERROR_CHAR=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65

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
            self.state = 174
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
            self.state = 176
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
            self.state = 178
            self.manydecl()
            self.state = 179
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
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.decl()
                self.state = 182
                self.manydecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
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
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 190
                self.func_call_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 191
                self.if_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 192
                self.for_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 193
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 194
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 195
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
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.stmt()
                self.state = 199
                self.stmt_block()
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
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 207
                self.struct_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 208
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
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.var_decl_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
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
            self.state = 215
            self.match(MiniGoParser.VAR)
            self.state = 216
            self.match(MiniGoParser.ID)
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSQB, MiniGoParser.ID]:
                self.state = 217
                self.all_type()
                pass
            elif token in [MiniGoParser.EQ]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 221
            self.match(MiniGoParser.EQ)
            self.state = 222
            self.expr1(0)
            self.state = 223
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
            self.state = 225
            self.match(MiniGoParser.VAR)
            self.state = 226
            self.match(MiniGoParser.ID)
            self.state = 227
            self.all_type()
            self.state = 228
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
            self.state = 230
            self.match(MiniGoParser.CONST)
            self.state = 231
            self.match(MiniGoParser.ID)
            self.state = 232
            self.match(MiniGoParser.EQ)
            self.state = 233
            self.expr1(0)
            self.state = 234
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

        def function_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


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
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.function_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCIB(self):
            return self.getToken(MiniGoParser.LCIB, 0)

        def RCIB(self):
            return self.getToken(MiniGoParser.RCIB, 0)

        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def list_para_func(self):
            return self.getTypedRuleContext(MiniGoParser.List_para_funcContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_decl" ):
                return visitor.visitFunction_decl(self)
            else:
                return visitor.visitChildren(self)




    def function_decl(self):

        localctx = MiniGoParser.Function_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(MiniGoParser.FUNC)
            self.state = 241
            self.match(MiniGoParser.ID)
            self.state = 242
            self.match(MiniGoParser.LCIB)
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 243
                self.list_para_func()
                pass
            elif token in [MiniGoParser.RCIB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 247
            self.match(MiniGoParser.RCIB)
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSQB, MiniGoParser.ID]:
                self.state = 248
                self.all_type()
                pass
            elif token in [MiniGoParser.LCUB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 252
            self.match(MiniGoParser.LCUB)
            self.state = 253
            self.stmt_block()
            self.state = 254
            self.match(MiniGoParser.RCUB)
            self.state = 255
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LCIB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LCIB)
            else:
                return self.getToken(MiniGoParser.LCIB, i)

        def rec(self):
            return self.getTypedRuleContext(MiniGoParser.RecContext,0)


        def rec_type(self):
            return self.getTypedRuleContext(MiniGoParser.Rec_typeContext,0)


        def RCIB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RCIB)
            else:
                return self.getToken(MiniGoParser.RCIB, i)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def list_para_func(self):
            return self.getTypedRuleContext(MiniGoParser.List_para_funcContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(MiniGoParser.FUNC)
            self.state = 258
            self.match(MiniGoParser.LCIB)
            self.state = 259
            self.rec()
            self.state = 260
            self.rec_type()
            self.state = 261
            self.match(MiniGoParser.RCIB)
            self.state = 262
            self.match(MiniGoParser.ID)
            self.state = 263
            self.match(MiniGoParser.LCIB)
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 264
                self.list_para_func()
                pass
            elif token in [MiniGoParser.RCIB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 268
            self.match(MiniGoParser.RCIB)
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSQB, MiniGoParser.ID]:
                self.state = 269
                self.all_type()
                pass
            elif token in [MiniGoParser.LCUB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 273
            self.match(MiniGoParser.LCUB)
            self.state = 274
            self.stmt_block()
            self.state = 275
            self.match(MiniGoParser.RCUB)
            self.state = 276
            self.match(MiniGoParser.SECO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_rec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRec" ):
                return visitor.visitRec(self)
            else:
                return visitor.visitChildren(self)




    def rec(self):

        localctx = MiniGoParser.RecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_rec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rec_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_rec_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRec_type" ):
                return visitor.visitRec_type(self)
            else:
                return visitor.visitChildren(self)




    def rec_type(self):

        localctx = MiniGoParser.Rec_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_rec_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_last_para_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_func(self):
            return self.getTypedRuleContext(MiniGoParser.Para_funcContext,0)


        def tail_para_func(self):
            return self.getTypedRuleContext(MiniGoParser.Tail_para_funcContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_not_last_para_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_last_para_func" ):
                return visitor.visitNot_last_para_func(self)
            else:
                return visitor.visitChildren(self)




    def not_last_para_func(self):

        localctx = MiniGoParser.Not_last_para_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_not_last_para_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.para_func()
            self.state = 283
            self.tail_para_func()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tail_para_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def para_func(self):
            return self.getTypedRuleContext(MiniGoParser.Para_funcContext,0)


        def tail_para_func(self):
            return self.getTypedRuleContext(MiniGoParser.Tail_para_funcContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_tail_para_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail_para_func" ):
                return visitor.visitTail_para_func(self)
            else:
                return visitor.visitChildren(self)




    def tail_para_func(self):

        localctx = MiniGoParser.Tail_para_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_tail_para_func)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(MiniGoParser.COMMA)
                self.state = 286
                self.para_func()
                self.state = 287
                self.tail_para_func()
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


    class Para_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_para_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_func" ):
                return visitor.visitPara_func(self)
            else:
                return visitor.visitChildren(self)




    def para_func(self):

        localctx = MiniGoParser.Para_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_para_func)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(MiniGoParser.ID)
                self.state = 293
                self.all_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Last_para_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_last_para_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLast_para_func" ):
                return visitor.visitLast_para_func(self)
            else:
                return visitor.visitChildren(self)




    def last_para_func(self):

        localctx = MiniGoParser.Last_para_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_last_para_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MiniGoParser.ID)
            self.state = 298
            self.all_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_para_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_last_para_func(self):
            return self.getTypedRuleContext(MiniGoParser.Not_last_para_funcContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def last_para_func(self):
            return self.getTypedRuleContext(MiniGoParser.Last_para_funcContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_para_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_para_func" ):
                return visitor.visitList_para_func(self)
            else:
                return visitor.visitChildren(self)




    def list_para_func(self):

        localctx = MiniGoParser.List_para_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_para_func)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.not_last_para_func()
                self.state = 301
                self.match(MiniGoParser.COMMA)
                self.state = 302
                self.last_para_func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.last_para_func()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Star_func_call_dotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_func_call_dot(self):
            return self.getTypedRuleContext(MiniGoParser.Star_func_call_dotContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_star_func_call_dot

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar_func_call_dot" ):
                return visitor.visitStar_func_call_dot(self)
            else:
                return visitor.visitChildren(self)



    def star_func_call_dot(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Star_func_call_dotContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_star_func_call_dot, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Star_func_call_dotContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_star_func_call_dot)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    self.func_call()
                    self.state = 310
                    self.match(MiniGoParser.DOT) 
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_func_call_dot(self):
            return self.getTypedRuleContext(MiniGoParser.Star_func_call_dotContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


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
        self.enterRule(localctx, 44, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.star_func_call_dot(0)
            self.state = 318
            self.func_call()
            self.state = 319
            self.match(MiniGoParser.SECO)
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

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_func_call)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.method_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
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

        def list_arg(self):
            return self.getTypedRuleContext(MiniGoParser.List_argContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MiniGoParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MiniGoParser.ID)
            self.state = 326
            self.match(MiniGoParser.LCIB)
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LCIB, MiniGoParser.LSQB, MiniGoParser.ID, MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 327
                self.list_arg()
                pass
            elif token in [MiniGoParser.RCIB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 331
            self.match(MiniGoParser.RCIB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCIB(self):
            return self.getToken(MiniGoParser.LCIB, 0)

        def RCIB(self):
            return self.getToken(MiniGoParser.RCIB, 0)

        def list_arg(self):
            return self.getTypedRuleContext(MiniGoParser.List_argContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.lhs(0)
            self.state = 334
            self.match(MiniGoParser.DOT)
            self.state = 335
            self.match(MiniGoParser.ID)
            self.state = 336
            self.match(MiniGoParser.LCIB)
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LCIB, MiniGoParser.LSQB, MiniGoParser.ID, MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 337
                self.list_arg()
                pass
            elif token in [MiniGoParser.RCIB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 341
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
        self.enterRule(localctx, 52, self.RULE_list_arg)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.arg()
                self.state = 344
                self.tail_arg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
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
        self.enterRule(localctx, 54, self.RULE_tail_arg)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(MiniGoParser.COMMA)
                self.state = 350
                self.arg()
                self.state = 351
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
        self.enterRule(localctx, 56, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
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

        def LSQB(self):
            return self.getToken(MiniGoParser.LSQB, 0)

        def RSQB(self):
            return self.getToken(MiniGoParser.RSQB, 0)

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arr_dim_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_dim_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_dim_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_dim_decl" ):
                return visitor.visitArr_dim_decl(self)
            else:
                return visitor.visitChildren(self)



    def arr_dim_decl(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Arr_dim_declContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_arr_dim_decl, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(MiniGoParser.LSQB)
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX]:
                self.state = 360
                self.int_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 361
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 364
            self.match(MiniGoParser.RSQB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 375
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Arr_dim_declContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arr_dim_decl)
                    self.state = 366
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 367
                    self.match(MiniGoParser.LSQB)
                    self.state = 370
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX]:
                        self.state = 368
                        self.int_lit()
                        pass
                    elif token in [MiniGoParser.ID]:
                        self.state = 369
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 372
                    self.match(MiniGoParser.RSQB) 
                self.state = 377
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_dim_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_dim_declContext,0)


        def primi(self):
            return self.getTypedRuleContext(MiniGoParser.PrimiContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = MiniGoParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arr_type)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.arr_dim_decl(0)
                self.state = 379
                self.primi()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.arr_dim_decl(0)
                self.state = 382
                self.match(MiniGoParser.ID)
                pass


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

        def arr_dim_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_dim_declContext,0)


        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def list_ele_arr(self):
            return self.getTypedRuleContext(MiniGoParser.List_ele_arrContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def primi(self):
            return self.getTypedRuleContext(MiniGoParser.PrimiContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = MiniGoParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.arr_dim_decl(0)
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 387
                self.primi()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 388
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 391
            self.match(MiniGoParser.LCUB)
            self.state = 392
            self.list_ele_arr()
            self.state = 393
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
        self.enterRule(localctx, 64, self.RULE_list_ele_arr)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.ele_arr()
                self.state = 396
                self.tail_ele_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
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
        self.enterRule(localctx, 66, self.RULE_tail_ele_arr)
        try:
            self.state = 406
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(MiniGoParser.COMMA)
                self.state = 402
                self.ele_arr()
                self.state = 403
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
        self.enterRule(localctx, 68, self.RULE_ele_arr)
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.int_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 410
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 411
                self.bool_lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 412
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 413
                self.struct_lit()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 414
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 415
                self.match(MiniGoParser.LCUB)
                self.state = 416
                self.list_ele_arr()
                self.state = 417
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
        self.enterRule(localctx, 70, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(MiniGoParser.TYPE)
            self.state = 422
            self.match(MiniGoParser.ID)
            self.state = 423
            self.match(MiniGoParser.STRUCT)
            self.state = 424
            self.match(MiniGoParser.LCUB)
            self.state = 425
            self.star_struct_ele_decl()
            self.state = 426
            self.match(MiniGoParser.RCUB)
            self.state = 427
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
        self.enterRule(localctx, 72, self.RULE_star_struct_ele_decl)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.attr_decl()
                self.state = 430
                self.star_struct_ele_decl()
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
        self.enterRule(localctx, 74, self.RULE_attr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(MiniGoParser.ID)
            self.state = 436
            self.all_type()
            self.state = 437
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
        self.enterRule(localctx, 76, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(MiniGoParser.ID)
            self.state = 440
            self.match(MiniGoParser.LCUB)
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 441
                self.list_ele_struct()
                pass
            elif token in [MiniGoParser.RCUB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 445
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
        self.enterRule(localctx, 78, self.RULE_list_ele_struct)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.ele_struct()
                self.state = 448
                self.tail_ele_struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
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
        self.enterRule(localctx, 80, self.RULE_tail_ele_struct)
        try:
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(MiniGoParser.COMMA)
                self.state = 454
                self.ele_struct()
                self.state = 455
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
        self.enterRule(localctx, 82, self.RULE_ele_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(MiniGoParser.ID)
            self.state = 461
            self.match(MiniGoParser.COLON)
            self.state = 462
            self.expr1(0)
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
        self.enterRule(localctx, 84, self.RULE_method_interface)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(MiniGoParser.ID)
            self.state = 465
            self.match(MiniGoParser.LCIB)
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 466
                self.list_para()
                pass
            elif token in [MiniGoParser.RCIB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 470
            self.match(MiniGoParser.RCIB)
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSQB, MiniGoParser.ID]:
                self.state = 471
                self.all_type()
                pass
            elif token in [MiniGoParser.SECO]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 475
            self.match(MiniGoParser.SECO)
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
        self.enterRule(localctx, 86, self.RULE_star_interface_method_decl)
        try:
            self.state = 481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.method_interface()
                self.state = 478
                self.star_interface_method_decl()
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
        self.enterRule(localctx, 88, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(MiniGoParser.TYPE)
            self.state = 484
            self.match(MiniGoParser.ID)
            self.state = 485
            self.match(MiniGoParser.INTERFACE)
            self.state = 486
            self.match(MiniGoParser.LCUB)
            self.state = 487
            self.star_interface_method_decl()
            self.state = 488
            self.match(MiniGoParser.RCUB)
            self.state = 489
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
        self.enterRule(localctx, 90, self.RULE_not_last_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.para()
            self.state = 492
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
        self.enterRule(localctx, 92, self.RULE_tail_para)
        try:
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.match(MiniGoParser.COMMA)
                self.state = 495
                self.para()
                self.state = 496
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
        self.enterRule(localctx, 94, self.RULE_para)
        try:
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.match(MiniGoParser.ID)
                self.state = 502
                self.all_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.match(MiniGoParser.ID)
                pass


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
        self.enterRule(localctx, 96, self.RULE_last_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(MiniGoParser.ID)
            self.state = 507
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

        def not_last_para(self):
            return self.getTypedRuleContext(MiniGoParser.Not_last_paraContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def last_para(self):
            return self.getTypedRuleContext(MiniGoParser.Last_paraContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_para" ):
                return visitor.visitList_para(self)
            else:
                return visitor.visitChildren(self)




    def list_para(self):

        localctx = MiniGoParser.List_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_list_para)
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.not_last_para()
                self.state = 510
                self.match(MiniGoParser.COMMA)
                self.state = 511
                self.last_para()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.last_para()
                pass


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
        self.enterRule(localctx, 100, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.lhs(0)
            self.state = 517
            self.assign_op()
            self.state = 518
            self.expr1(0)
            self.state = 519
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
        self.enterRule(localctx, 102, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
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

        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def SECO(self):
            return self.getToken(MiniGoParser.SECO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(MiniGoParser.IF)
            self.state = 524
            self.match(MiniGoParser.LCIB)
            self.state = 525
            self.condit()
            self.state = 526
            self.match(MiniGoParser.RCIB)
            self.state = 527
            self.match(MiniGoParser.LCUB)
            self.state = 528
            self.stmt_block()
            self.state = 529
            self.match(MiniGoParser.RCUB)
            self.state = 530
            self.else_if()
            self.state = 531
            self.match(MiniGoParser.SECO)
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

        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = MiniGoParser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_else_if)
        try:
            self.state = 544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.match(MiniGoParser.ELSE)
                self.state = 534
                self.match(MiniGoParser.IF)
                self.state = 535
                self.match(MiniGoParser.LCIB)
                self.state = 536
                self.condit()
                self.state = 537
                self.match(MiniGoParser.RCIB)
                self.state = 538
                self.match(MiniGoParser.LCUB)
                self.state = 539
                self.stmt_block()
                self.state = 540
                self.match(MiniGoParser.RCUB)
                self.state = 541
                self.else_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 543
                self.else_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LCUB(self):
            return self.getToken(MiniGoParser.LCUB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def RCUB(self):
            return self.getToken(MiniGoParser.RCUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = MiniGoParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_else_stmt)
        try:
            self.state = 552
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.match(MiniGoParser.ELSE)
                self.state = 547
                self.match(MiniGoParser.LCUB)
                self.state = 548
                self.stmt_block()
                self.state = 549
                self.match(MiniGoParser.RCUB)
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
        self.enterRule(localctx, 110, self.RULE_for_stmt)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.basic_for()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
                self.init_for()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
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
        self.enterRule(localctx, 112, self.RULE_basic_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(MiniGoParser.FOR)
            self.state = 560
            self.condit()
            self.state = 561
            self.match(MiniGoParser.LCUB)
            self.state = 562
            self.stmt_block()
            self.state = 563
            self.match(MiniGoParser.RCUB)
            self.state = 564
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
        self.enterRule(localctx, 114, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(MiniGoParser.FOR)
            self.state = 567
            self.init()
            self.state = 568
            self.condit()
            self.state = 569
            self.match(MiniGoParser.SECO)
            self.state = 570
            self.update()
            self.state = 571
            self.match(MiniGoParser.LCUB)
            self.state = 572
            self.stmt_block()
            self.state = 573
            self.match(MiniGoParser.RCUB)
            self.state = 574
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
        self.enterRule(localctx, 116, self.RULE_init)
        try:
            self.state = 578
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.assign_stmt()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 577
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
        self.enterRule(localctx, 118, self.RULE_condit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
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
        self.enterRule(localctx, 120, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self.lhs(0)
            self.state = 583
            self.assign_op()
            self.state = 584
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

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


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

        def getRuleIndex(self):
            return MiniGoParser.RULE_range_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_for" ):
                return visitor.visitRange_for(self)
            else:
                return visitor.visitChildren(self)




    def range_for(self):

        localctx = MiniGoParser.Range_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_range_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(MiniGoParser.FOR)
            self.state = 587
            self.index()
            self.state = 588
            self.match(MiniGoParser.COMMA)
            self.state = 589
            self.value()
            self.state = 590
            self.match(MiniGoParser.AS_EQ)
            self.state = 591
            self.match(MiniGoParser.RANGE)
            self.state = 592
            self.array_id()
            self.state = 593
            self.match(MiniGoParser.LCUB)
            self.state = 594
            self.stmt_block()
            self.state = 595
            self.match(MiniGoParser.RCUB)
            self.state = 596
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
        self.enterRule(localctx, 124, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(MiniGoParser.ID)
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
        self.enterRule(localctx, 126, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
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
        self.enterRule(localctx, 128, self.RULE_array_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
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
        self.enterRule(localctx, 130, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(MiniGoParser.BREAK)
            self.state = 605
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
        self.enterRule(localctx, 132, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.match(MiniGoParser.CONTINUE)
            self.state = 608
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
        self.enterRule(localctx, 134, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610
            self.match(MiniGoParser.RETURN)
            self.state = 613
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LCIB, MiniGoParser.LSQB, MiniGoParser.ID, MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 611
                self.expr1(0)
                pass
            elif token in [MiniGoParser.SECO]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 615
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
        self.enterRule(localctx, 136, self.RULE_rela_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
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


    class AddsubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_addsub

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddsub" ):
                return visitor.visitAddsub(self)
            else:
                return visitor.visitChildren(self)




    def addsub(self):

        localctx = MiniGoParser.AddsubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_addsub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
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


    class MudimoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mudimo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMudimo" ):
                return visitor.visitMudimo(self)
            else:
                return visitor.visitChildren(self)




    def mudimo(self):

        localctx = MiniGoParser.MudimoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_mudimo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
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


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_unary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = MiniGoParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
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
        _startState = 144
        self.enterRecursionRule(localctx, 144, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 633
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 628
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 629
                    self.match(MiniGoParser.OR)
                    self.state = 630
                    self.expr2(0) 
                self.state = 635
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        _startState = 146
        self.enterRecursionRule(localctx, 146, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 644
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 639
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 640
                    self.match(MiniGoParser.AND)
                    self.state = 641
                    self.expr3(0) 
                self.state = 646
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        _startState = 148
        self.enterRecursionRule(localctx, 148, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 656
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 650
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 651
                    self.rela_op()
                    self.state = 652
                    self.expr4(0) 
                self.state = 658
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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


        def addsub(self):
            return self.getTypedRuleContext(MiniGoParser.AddsubContext,0)


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
        _startState = 150
        self.enterRecursionRule(localctx, 150, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 668
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 662
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 663
                    self.addsub()
                    self.state = 664
                    self.expr5(0) 
                self.state = 670
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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


        def mudimo(self):
            return self.getTypedRuleContext(MiniGoParser.MudimoContext,0)


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
        _startState = 152
        self.enterRecursionRule(localctx, 152, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 680
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 674
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 675
                    self.mudimo()
                    self.state = 676
                    self.expr6() 
                self.state = 682
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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

        def unary(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryContext,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


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
        self.enterRule(localctx, 154, self.RULE_expr6)
        try:
            self.state = 687
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 683
                self.unary()
                self.state = 684
                self.expr6()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LCIB, MiniGoParser.LSQB, MiniGoParser.ID, MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 686
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

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def dims(self):
            return self.getTypedRuleContext(MiniGoParser.DimsContext,0)


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
        _startState = 156
        self.enterRecursionRule(localctx, 156, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 690
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 702
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 700
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 692
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 693
                        self.match(MiniGoParser.DOT)
                        self.state = 694
                        self.field()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 695
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 696
                        self.match(MiniGoParser.DOT)
                        self.state = 697
                        self.function_call()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 698
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 699
                        self.dims(0)
                        pass

             
                self.state = 704
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


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
        self.enterRule(localctx, 158, self.RULE_operand)
        try:
            self.state = 712
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 705
                self.lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 706
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 707
                self.function_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 708
                self.match(MiniGoParser.LCIB)
                self.state = 709
                self.expr1(0)
                self.state = 710
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
        self.enterRule(localctx, 160, self.RULE_lit)
        try:
            self.state = 721
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 714
                self.int_lit()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 715
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 716
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 717
                self.bool_lit()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 718
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 719
                self.struct_lit()
                pass
            elif token in [MiniGoParser.LSQB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 720
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
        self.enterRule(localctx, 162, self.RULE_primi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 723
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
        self.enterRule(localctx, 164, self.RULE_all_type)
        try:
            self.state = 728
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 725
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 726
                self.primi()
                pass
            elif token in [MiniGoParser.LSQB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 727
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


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def dims(self):
            return self.getTypedRuleContext(MiniGoParser.DimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 166
        self.enterRecursionRule(localctx, 166, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 731
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 740
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 738
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 733
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 734
                        self.match(MiniGoParser.DOT)
                        self.state = 735
                        self.field()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 736
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 737
                        self.dims(0)
                        pass

             
                self.state = 742
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 743
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dim(self):
            return self.getTypedRuleContext(MiniGoParser.DimContext,0)


        def dims(self):
            return self.getTypedRuleContext(MiniGoParser.DimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dims

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDims" ):
                return visitor.visitDims(self)
            else:
                return visitor.visitChildren(self)



    def dims(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.DimsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 170
        self.enterRecursionRule(localctx, 170, self.RULE_dims, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 746
            self.dim()
            self._ctx.stop = self._input.LT(-1)
            self.state = 752
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.DimsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dims)
                    self.state = 748
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 749
                    self.dim() 
                self.state = 754
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 172, self.RULE_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self.match(MiniGoParser.LSQB)
            self.state = 756
            self.expr1(0)
            self.state = 757
            self.match(MiniGoParser.RSQB)
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
        self._predicates[21] = self.star_func_call_dot_sempred
        self._predicates[29] = self.arr_dim_decl_sempred
        self._predicates[72] = self.expr1_sempred
        self._predicates[73] = self.expr2_sempred
        self._predicates[74] = self.expr3_sempred
        self._predicates[75] = self.expr4_sempred
        self._predicates[76] = self.expr5_sempred
        self._predicates[78] = self.expr7_sempred
        self._predicates[83] = self.lhs_sempred
        self._predicates[85] = self.dims_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def star_func_call_dot_sempred(self, localctx:Star_func_call_dotContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def arr_dim_decl_sempred(self, localctx:Arr_dim_declContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

    def dims_sempred(self, localctx:DimsContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         




