from pathlib import Path

# --- Extraccion
from src.fuentes.fuente_csv_class import FuenteCSV
# -- models
from src.models.eshop_models import EShopSchema
# --- QA
from src.qa.qa_eshop_schema import validar_schema

def main():
    print('[INICIO] Pipeline de E-ShopNow')
    # 1. Cargar E-Shop
    r = Path("data/raw/E-ShopNow (Proyecto ABP M2).csv")
    raw_eshop = FuenteCSV(ruta=r, sep=";")
    df_eshop = raw_eshop.to_dataframe()
    #print(df_eshop.info())

    # 2. Validar esquemas (Schema)
    # 2.1. ¿Existen todas las columas esperadas?
    # 2.2. ¿Hay cambios en las columnas?
    # class -> dataclass
    validar_schema(df_eshop, EShopSchema)


    # 3. QA de datos


    print('[FIN] Pipeline de E-ShopNow')

if __name__ == '__main__':
    main()