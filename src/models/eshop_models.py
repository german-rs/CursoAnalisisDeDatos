from dataclasses import dataclass

#class EshopSchema:
#    def __init__(self, id_venta):
#        self.id_venta = id_venta

@dataclass
class EShopSchema:
    id_venta : str
    fecha_venta  : str
    id_empleado : int
    antiguedad_vendedor : int
    id_cliente : int
    nombre_cliente : str
    email_cliente : str
    genero_cliente : str
    edad_cliente : float
    ciudad_cliente : str
    region_cliente : str
    canal_venta : str
    producto : str
    categoria_producto : str
    precio_unitario : int
    cantidad : int
    descuento_pct : float



