from antlr4 import *
from JSONLexer import JSONLexer
from JSONParser import JSONParser
from JSONVisitor import JSONVisitor
import sys


class XMLVisitor(JSONVisitor):
    def visitJson(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitAnObject(self, ctx):
        pairs = ctx.pair()
        xml = ""
        for p in pairs:
            xml += self.visit(p)
        return xml

    def visitEmptyObject(self, ctx):
        return ""

    def visitPair(self, ctx):
        key = ctx.STRING().getText().strip('"')
        value = self.visit(ctx.value())
        return f"<{key}>{value}</{key}>\n"

    def visitArrayOfValues(self, ctx):
        values = ctx.value()
        return "".join(f"<element>{self.visit(v)}</element>\n" for v in values)

    def visitEmptyArray(self, ctx):
        return ""

    def visitString(self, ctx):
        return ctx.getText().strip('"')

    def visitAtom(self, ctx):
        return ctx.getText()

    def visitObjectValue(self, ctx):
        return self.visit(ctx.jsonObject())

    def visitArrayValue(self, ctx):
        return self.visit(ctx.array())


def main():
    if len(sys.argv) != 2:
        print("Uso: python json_to_xml.py archivo.json")
        return

    input_file = sys.argv[1]
    output_file = input_file.replace(".json", ".xml")

    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = JSONLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = JSONParser(tokens)
    tree = parser.json()

    visitor = XMLVisitor()
    xml_output = visitor.visit(tree)

    with open(output_file, "w", encoding='utf-8') as f:
        f.write(xml_output)

    print(f"Archivo convertido y guardado en: {output_file}")


if __name__ == "__main__":
    main()
