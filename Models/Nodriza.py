from Models.Materiales import *


class Nodriza():
    def __init__(self, nombre, img, rect):
        self.nombre = nombre
        self.img = img
        self.rect = rect
        self.almacen = []
        self.materiales = Materiales(None)
        self.cantidad = 0
        

    def set_almacen(self):
        cantidad = 0
        for material in self.almacen:
            cantidad += material["cantidad"]
        self.cantidad = cantidad
        return cantidad

    def agregar_materiales(self, materiales):
            for i in materiales:
                self.materiales.add(i)
            #print(self.materiales.inorder(self.materiales))
    
        