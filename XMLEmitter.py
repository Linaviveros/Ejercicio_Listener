from JSONParserListener import JSONParserListener

class XMLEmitter(JSONParserListener):
    def __init__(self):
        self.xml_map = {}
        self.indent_level = {}

    def getXML(self, ctx):
        return self.xml_map.get(ctx, '')

    def setXML(self, ctx, value):
        self.xml_map[ctx] = value

    def indent(self, level):
        return '  ' * level

    def exitAtom(self, ctx):
        self.setXML(ctx, ctx.getText())

    def exitString(self, ctx):
        self.setXML(ctx, ctx.getText().strip('"'))

    def exitObjectValue(self, ctx):
        self.setXML(ctx, self.getXML(ctx.jsonObject()))

    def exitPair(self, ctx):
        tag = ctx.STRING().getText().strip('"')
        val = self.getXML(ctx.value())
        level = self.indent_level.get(ctx, 0)
        ind = self.indent(level + 1)
        xml = f"{ind}<{tag}>{val}</{tag}>\n"
        self.setXML(ctx, xml)

    def exitAnObject(self, ctx):
        level = self.indent_level.get(ctx, 0)
        seen_keys = set()
        for p in ctx.pair():
            key = p.STRING().getText().strip('"')
            if key in seen_keys:
                print(f" Advertencia: clave duplicada '{key}' detectada.")
            seen_keys.add(key)
            self.indent_level[p] = level + 1
        body = ''.join(self.getXML(p) for p in ctx.pair())
        self.setXML(ctx, body)

    def exitEmptyObject(self, ctx):
        self.setXML(ctx, '')

    def exitArrayOfValues(self, ctx):
        level = self.indent_level.get(ctx, 0)
        elements = []
        for v in ctx.value():
            self.indent_level[v] = level + 1
            elements.append(f"{self.indent(level + 1)}<element>{self.getXML(v)}</element>\n")
        self.setXML(ctx, ''.join(elements))

    def exitEmptyArray(self, ctx):
        self.setXML(ctx, '')

    def exitJson(self, ctx):
        self.setXML(ctx, self.getXML(ctx.getChild(0)))
