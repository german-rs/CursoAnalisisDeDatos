class FuenteDatos:
  """
  Esto es docsstring
  Define la documentación
  """

  # Constructor de la clase __init__
  def __init__(self, ruta : str) -> None:
    # Encapsulación: protegemos el acceso a la ruta
    self._ruta = ruta

  @property
  def ruta(self) -> str:
    return self._ruta


  def cargar(self):
    # Polimorfismo: El código que implementa esta clase será definido en la clase hija
    raise NotImplementedError("Implementar en la clase hija")

  def to_dataframe(self):
    datos = self.cargar()
    return datos


