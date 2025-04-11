# Generated from JSON.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\5\2")
        buf.write("\17\n\2\3\3\3\3\3\3\3\3\7\3\25\n\3\f\3\16\3\30\13\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\7\4$\n\4\f\4")
        buf.write("\16\4\'\13\4\3\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6:\n\6\3\6\2\2\7\2\4\6")
        buf.write("\b\n\2\2\2A\2\16\3\2\2\2\4\35\3\2\2\2\6,\3\2\2\2\b.\3")
        buf.write("\2\2\2\n9\3\2\2\2\f\17\5\4\3\2\r\17\5\6\4\2\16\f\3\2\2")
        buf.write("\2\16\r\3\2\2\2\17\3\3\2\2\2\20\21\7\3\2\2\21\26\5\b\5")
        buf.write("\2\22\23\7\4\2\2\23\25\5\b\5\2\24\22\3\2\2\2\25\30\3\2")
        buf.write("\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\31\3\2\2\2\30\26\3")
        buf.write("\2\2\2\31\32\7\5\2\2\32\36\3\2\2\2\33\34\7\3\2\2\34\36")
        buf.write("\7\5\2\2\35\20\3\2\2\2\35\33\3\2\2\2\36\5\3\2\2\2\37 ")
        buf.write("\7\6\2\2 %\5\n\6\2!\"\7\4\2\2\"$\5\n\6\2#!\3\2\2\2$\'")
        buf.write("\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\7")
        buf.write("\7\2\2)-\3\2\2\2*+\7\6\2\2+-\7\7\2\2,\37\3\2\2\2,*\3\2")
        buf.write("\2\2-\7\3\2\2\2./\7\f\2\2/\60\7\b\2\2\60\61\5\n\6\2\61")
        buf.write("\t\3\2\2\2\62:\7\f\2\2\63:\7\r\2\2\64:\5\4\3\2\65:\5\6")
        buf.write("\4\2\66:\7\t\2\2\67:\7\n\2\28:\7\13\2\29\62\3\2\2\29\63")
        buf.write("\3\2\2\29\64\3\2\2\29\65\3\2\2\29\66\3\2\2\29\67\3\2\2")
        buf.write("\298\3\2\2\2:\13\3\2\2\2\b\16\26\35%,9")
        return buf.getvalue()


class JSONParser ( Parser ):

    grammarFileName = "JSON.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "'['", "']'", "':'", 
                     "'true'", "'false'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NUMBER", "WS" ]

    RULE_json = 0
    RULE_jsonObject = 1
    RULE_array = 2
    RULE_pair = 3
    RULE_value = 4

    ruleNames =  [ "json", "jsonObject", "array", "pair", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    STRING=10
    NUMBER=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class JsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def jsonObject(self):
            return self.getTypedRuleContext(JSONParser.JsonObjectContext,0)


        def array(self):
            return self.getTypedRuleContext(JSONParser.ArrayContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJson" ):
                return visitor.visitJson(self)
            else:
                return visitor.visitChildren(self)




    def json(self):

        localctx = JSONParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.jsonObject()
                pass
            elif token in [JSONParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.array()
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


    class JsonObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_jsonObject

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AnObjectContext(JsonObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.JsonObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.PairContext)
            else:
                return self.getTypedRuleContext(JSONParser.PairContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnObject" ):
                listener.enterAnObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnObject" ):
                listener.exitAnObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnObject" ):
                return visitor.visitAnObject(self)
            else:
                return visitor.visitChildren(self)


    class EmptyObjectContext(JsonObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.JsonObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyObject" ):
                listener.enterEmptyObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyObject" ):
                listener.exitEmptyObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyObject" ):
                return visitor.visitEmptyObject(self)
            else:
                return visitor.visitChildren(self)



    def jsonObject(self):

        localctx = JSONParser.JsonObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_jsonObject)
        self._la = 0 # Token type
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = JSONParser.AnObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(JSONParser.T__0)
                self.state = 15
                self.pair()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 16
                    self.match(JSONParser.T__1)
                    self.state = 17
                    self.pair()
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 23
                self.match(JSONParser.T__2)
                pass

            elif la_ == 2:
                localctx = JSONParser.EmptyObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(JSONParser.T__0)
                self.state = 26
                self.match(JSONParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayOfValuesContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.ValueContext)
            else:
                return self.getTypedRuleContext(JSONParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayOfValues" ):
                listener.enterArrayOfValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayOfValues" ):
                listener.exitArrayOfValues(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayOfValues" ):
                return visitor.visitArrayOfValues(self)
            else:
                return visitor.visitChildren(self)


    class EmptyArrayContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyArray" ):
                listener.enterEmptyArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyArray" ):
                listener.exitEmptyArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyArray" ):
                return visitor.visitEmptyArray(self)
            else:
                return visitor.visitChildren(self)



    def array(self):

        localctx = JSONParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = JSONParser.ArrayOfValuesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(JSONParser.T__3)
                self.state = 30
                self.value()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 31
                    self.match(JSONParser.T__1)
                    self.state = 32
                    self.value()
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self.match(JSONParser.T__4)
                pass

            elif la_ == 2:
                localctx = JSONParser.EmptyArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(JSONParser.T__3)
                self.state = 41
                self.match(JSONParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = JSONParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(JSONParser.STRING)
            self.state = 45
            self.match(JSONParser.T__5)
            self.state = 46
            self.value()
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


        def getRuleIndex(self):
            return JSONParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ObjectValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def jsonObject(self):
            return self.getTypedRuleContext(JSONParser.JsonObjectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectValue" ):
                listener.enterObjectValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectValue" ):
                listener.exitObjectValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectValue" ):
                return visitor.visitObjectValue(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class ArrayValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(JSONParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayValue" ):
                listener.enterArrayValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayValue" ):
                listener.exitArrayValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayValue" ):
                return visitor.visitArrayValue(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(JSONParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = JSONParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.STRING]:
                localctx = JSONParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(JSONParser.STRING)
                pass
            elif token in [JSONParser.NUMBER]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(JSONParser.NUMBER)
                pass
            elif token in [JSONParser.T__0]:
                localctx = JSONParser.ObjectValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.jsonObject()
                pass
            elif token in [JSONParser.T__3]:
                localctx = JSONParser.ArrayValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.array()
                pass
            elif token in [JSONParser.T__6]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.match(JSONParser.T__6)
                pass
            elif token in [JSONParser.T__7]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 53
                self.match(JSONParser.T__7)
                pass
            elif token in [JSONParser.T__8]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 54
                self.match(JSONParser.T__8)
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





