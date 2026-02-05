from src.fuentes.fuente_base_class import FuenteDatos

class FuenteExcel(FuenteDatos):
  """
  Hereda de FuenteDatos
  """
  def __init__(self, ruta: str, hoja: str):
    super().__init__(ruta)
    self._hoja = hoja

  @property
  def hoja(self) -> str:
    return self._hoja

  def cargar(self):
      # Simular que cargamos datos de una hoja
      data = {
          "fechas": ["2026-02-01", "2026-02-02"],
          "productos": ["C", "A"],
          "ventas": [1000, 2000],
          "ruta": [self.ruta, self.hoja],
      }
      return data