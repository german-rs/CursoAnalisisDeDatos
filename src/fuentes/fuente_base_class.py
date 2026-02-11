class FuenteDatos:
  """
    Clase base abstracta para manejo de fuentes de datos.

    Implementa el patrón de diseño Template Method, donde la clase base
    define la estructura y las clases hijas implementan los detalles específicos.
  """

  # Constructor de la clase __init__
  def __init__(self, ruta : str) -> None:
    """
       Getter property para acceder al nombre de la hoja.

        Returns:
            str: Nombre de la hoja de Excel.
    """

      # Atributo protegido (convención con _) para encapsulación
      # Almacena la ubicación de la fuente de datos
    self._ruta = ruta

  @property
  def ruta(self) -> str:
    return self._ruta


  def cargar(self):
    """
    Metodo abstracto para cargar datos.

        Implementa polimorfismo: cada clase hija debe proporcionar
        su propia implementación según el tipo de fuente de datos
        (Excel, CSV, JSON, base de datos, etc.).

        Raises:
            NotImplementedError: Si la clase hija no implementa este metodo.
    """
    raise NotImplementedError("Implementar en la clase hija")

  def to_dataframe(self):
        """
          Convierte los datos cargados a formato DataFrame.

            Utiliza el metodo cargar() implementado en las clases hijas
            para obtener los datos y retornarlos en formato estructurado.

            Returns:
                dict/DataFrame: Datos estructurados listos para procesamiento.
          """

        # Invoca el metodo polimórfico cargar()
        datos = self.cargar()
        return datos
