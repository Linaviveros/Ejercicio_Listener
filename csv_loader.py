from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser
from CSVListener import CSVListener  # Este es el listener correcto, no CSVParserListener
import json
from collections import Counter, defaultdict

class CSVLoader(CSVListener):
    EMPTY = "␀"  # Valor especial para campos vacíos

    def __init__(self):
        self.rows = []
        self.header = []
        self.currentRowFieldValues = []
        self.emptyFieldCount = 0
        self.filas_repetidas = set()
        self.filas_duplicadas = []

    def exitText(self, ctx):
        self.currentRowFieldValues.append(ctx.getText())

    def exitString(self, ctx):
        self.currentRowFieldValues.append(ctx.getText().strip('"'))

    def exitEmpty(self, ctx):
        self.currentRowFieldValues.append(self.EMPTY)
        self.emptyFieldCount += 1

    def exitRow(self, ctx):
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            self.header = self.currentRowFieldValues
            self.currentRowFieldValues = []
            return

        if len(self.currentRowFieldValues) != len(self.header):
            print(f"  Fila inválida: {self.currentRowFieldValues}")
        else:
            row_dict = {
                self.header[i]: self.currentRowFieldValues[i]
                for i in range(len(self.currentRowFieldValues))
            }
            row_tuple = tuple(row_dict.items())
            if row_tuple in self.filas_repetidas:
                self.filas_duplicadas.append(row_dict)
            else:
                self.filas_repetidas.add(row_tuple)
                self.rows.append(row_dict)

        self.currentRowFieldValues = []

    def limpiar_montos(self):
        for fila in self.rows:
            if "Cantidad" in fila:
                monto = fila["Cantidad"]
                if monto != self.EMPTY:
                    fila["Cantidad"] = monto.replace('"', '').replace('$', '').replace(',', '').strip()

    def print_column_stats(self, column_name="Cantidad"):
        valores = [fila[column_name] for fila in self.rows if column_name in fila and fila[column_name] != self.EMPTY]
        print(f"\n Estadísticas para columna '{column_name}':")
        for valor in valores:
            print(f"• {valor}")

    def contar_por_mes(self, columna="Mes"):
        conteo = Counter()
        for fila in self.rows:
            mes = fila.get(columna, None)
            if mes:
                conteo[mes] += 1
        print("\n Conteo por mes:")
        for mes, cantidad in conteo.items():
            print(f"{mes}: {cantidad} veces")

    def sumar_por_mes(self, columna_mes="Mes", columna_cantidad="Cantidad"):
        totales = defaultdict(float)
        for fila in self.rows:
            mes = fila.get(columna_mes)
            monto = fila.get(columna_cantidad)
            if mes and monto and monto != self.EMPTY:
                try:
                    totales[mes] += float(monto)
                except ValueError:
                    print(f"  Monto mal formateado: '{monto}' en fila: {fila}")

        print("\n Total de montos por mes:")
        for mes, total in totales.items():
            print(f"{mes}: ${total:,.2f}")

    def exportar_a_json(self, filename="output.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.rows, f, indent=2, ensure_ascii=False)

    def mostrar_filas_duplicadas(self):
        if self.filas_duplicadas:
            print("\n  Filas duplicadas detectadas:")
            for fila in self.filas_duplicadas:
                print(fila)
        else:
            print("\n No hay filas duplicadas.")
