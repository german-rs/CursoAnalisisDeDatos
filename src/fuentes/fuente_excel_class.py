from src.fuentes.fuente_base_class import FuenteDatos

class FuenteExcel(FuenteDatos):
  """
   Clase especializada para manejo de archivos Excel.

    Hereda de FuenteDatos e implementa la funcionalidad específica
    para trabajar con hojas de cálculo Excel.
  """
  def __init__(self, ruta: str, hoja: str):
    """
    Constructor de la clase FuenteExcel.

    Args:
        ruta (str): Ruta al archivo Excel.
        hoja (str): Nombre de la hoja específica a leer.
    """
    # Llama al constructor de la clase padre para inicializar _ruta
    super().__init__(ruta)
    # Atributo adicional específico de Excel: nombre de la hoja
    self._hoja = hoja

  @property
  def hoja(self) -> str:
    """
    Getter property para acceder al nombre de la hoja.

    Returns:
        str: Nombre de la hoja de Excel.
    """
    return self._hoja

  def cargar(self):
      """
      Implementación concreta del metodo abstracto cargar().

        Sobrescribe el metodo de la clase padre para proporcionar
        funcionalidad específica de carga de datos de Excel.

        Nota: Esta es una simulación. En producción, usaría pandas
        o librerías similares para leer archivos Excel reales.

        Returns:
            dict: Diccionario con datos simulados de ventas.
      """

      # Simula la carga de datos de un archivo Excel
      # En un caso real, aquí se usaría pandas.read_excel()
      data = {
          "fechas": ["2026-02-01", "2026-02-02"],
          "productos": ["C", "A"],
          "ventas": [1000, 2000],
          "ruta": [self.ruta, self.hoja], # Incluye metadatos de la fuente
      }
      return data