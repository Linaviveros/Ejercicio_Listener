from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser
from CSVListener import CSVListener  
from csv_loader import CSVLoader

def main():
    archivo_csv = "data.csv"  

    # Leer el archivo .csv
    input_stream = FileStream(archivo_csv, encoding='utf-8')
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    tree = parser.csvFile()

    # Instanciar nuestro loader personalizado
    loader = CSVLoader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)

    # Mostrar estadísticas y otras funcionalidades
    print(f"\n Total de campos vacíos: {loader.emptyFieldCount}")
    loader.limpiar_montos()
    loader.print_column_stats("Cantidad")
    loader.contar_por_mes()
    loader.sumar_por_mes()
    loader.mostrar_filas_duplicadas()
    loader.exportar_a_json("salida.json")
    print("\n Datos exportados exitosamente a 'salida.json'")

if __name__ == '__main__':
    main()
