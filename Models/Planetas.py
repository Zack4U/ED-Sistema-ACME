class Planetas():
    def __init__(self, codigo, nombre, recurso, cantidad, rect):
        self.codigo = codigo
        self.nombre = nombre
        self.recurso = recurso
        self.cantidad = cantidad
        self.rect = rect
        self.visitas = 0
        self.explotado = False

    def toString(self):
        data = {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'recurso': self.recurso,
            'cantidad': self.cantidad,
            'Ubicacion': (self.rect.centerx, self.rect.centery)}
        return data

    def get_material(self, cantidad):
        if self.cantidad == 0:
            print(f"{self.nombre}: Material insuficiente")
        if self.cantidad <= cantidad:
            cantidad = self.cantidad
        material = {
            'codigo': self.codigo,
            'cantidad': cantidad,
            'fecha' : 0
        }
        #print(f"Sacando: {cantidad}")
        self.cantidad -= cantidad
        return material
