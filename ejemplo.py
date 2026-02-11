# Importación de módulos del sistema y utilidades

import sys # Permite acceder a argumentos de línea de comandos
from pprint import pprint # Impresión formateada de estructuras de datos
from src.fuentes.fuente_excel_class import FuenteExcel  # Clase personalizada para manejo de Excel

def read_excel():
    """
    Carga y procesa datos desde un archivo Excel.

    Returns:
        dict: Datos del archivo Excel convertidos a formato de diccionario (simulado como DataFrame).
    """
    # Instancia de la clase FuenteExcel con parámetros específicos
    ventas_excel = FuenteExcel(ruta="ventas_2026.xlsx", hoja="Hoja2026")
    # Convierte los datos cargados a un formato tipo DataFrame
    return ventas_excel.to_dataframe()

def saludar():
    print("La función saludar() te saluda")


def main():
    """
    Función principal que maneja el flujo del programa.
    Procesa argumentos de línea de comandos y ejecuta la operación correspondiente.
    """
    print("--- Inicio del proceso de automatización ---")
    # Muestra todos los argumentos recibidos (sys.argv[0] es el nombre del script)
    print(sys.argv )

    # Validación: verifica que se haya proporcionado al menos un argumento
    if len(sys.argv) < 2:
        print("el uso de este programa incluye un argumento <DatosExcel | Saludar>")
        return

    # Captura el primer argumento (la opción seleccionada por el usuario)
    opcion = sys.argv[1]

    # Control de flujo basado en la opción proporcionada
    if opcion == "DatosExcel":
        # Ejecuta la función de lectura de Excel y muestra los datos formateados
        excel = read_excel()
        pprint(excel)
    elif opcion == "Saludar":
        # Ejecuta la función de saludo
        saludar()
    else:
        # Manejo de opciones no válidas
       print(f"Opción {opcion} argumentos validos <DatosExcel | Saludar>")


# Punto de entrada del programa
# Se ejecuta solo si el script es llamado directamente (no importado como módulo)
if __name__ == '__main__':
    main()