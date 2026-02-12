

from pathlib import Path
from typing import Union

import pandas as pd
from src.fuentes.fuente_base_class import FuenteDatos

class FuenteCSV(FuenteDatos):
    def __init__(self, ruta: Path, sep: str = ","):
        super().__init__(ruta)
        self.sep = sep

    def cargar(self):
        return pd.read_csv(self.ruta, sep=self._sep)