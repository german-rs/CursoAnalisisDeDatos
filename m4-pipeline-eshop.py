from pathlib import Path
from src.fuentes.fuente_csv_class import FuenteCSV

def main():
    print('[INICIO] Pipeline de E-ShopNow')
    # 1. Cargar E-Shop
    r = Path("data/raw/E-ShopNow (Proyecto ABP M2).csv")
    raw_eshop = FuenteCSV(ruta=r, sep=";")
    df_eshop = raw_eshop.to_dataframe()
    print(df_eshop.info())

    # 2. Validar esquemas (Schema)
    # 3. QA de datos
    #

    print('[FIN] Pipeline de E-ShopNow')

if __name__ == '__main__':
    main()