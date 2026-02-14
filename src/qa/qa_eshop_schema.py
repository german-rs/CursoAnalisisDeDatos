from src.models.eshop_models import EShopSchema


def validar_schema(df, schema):
    print('[QA] Validando schema de E-ShopNow CSV')

    col_esperada = set(schema.__annotations__.keys())
    col_actual = set(df.columns)
    print(df.columns)

    #print()
    #print(schema.__annotations__.keys())
    #print(col_esperada)

    col_faltan = col_esperada -col_actual
    col_nuevas = col_actual - col_esperada

    if not col_faltan:
        print("[QA] No hay columnas faltantes")
    else:
        print(f"[ERROR] faltan las siguientes columnas: {col_faltan}")
    if not col_nuevas:
        print("[QA] No hay columnas nuevas")
    else:
        print(f"[ERROR] Las siguientes columnas no ha sido agregadas: {col_nuevas}")



