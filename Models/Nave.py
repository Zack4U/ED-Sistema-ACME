class Nave():
    def __init__(self, nombre, img, rect, disponible=True):
        self.nombre = nombre
        self.almacen = []
        self.img = img
        self.rect = rect
        self.disponible = True
        self.cantidad = 0

    def set_cantidad(self):
        cantidad = 0
        for material in self.almacen:
            cantidad += material["cantidad"]
        self.cantidad = cantidad
        return cantidad

    def get_material(self):
        data = self.almacen
        self.almacen = []
        #print(f"Guardando: {self.cantidad}")
        self.cantidad = 0
        return data
    
    def get_nodos(self):
        total = 0
        for i in self.almacen:
            total += 1
        return total