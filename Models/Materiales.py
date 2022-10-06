class Materiales:
    def __init__(self, material):
        self.left = None
        self.right = None
        self.material = material

    def add(self, material):
        if self.material:
            if material["codigo"] < self.material["codigo"]:
                if self.left is None:
                    self.left = Materiales(material)
                else:
                    self.left.add(material)
            elif material["codigo"] > self.material["codigo"]:
                if self.right is None:
                    self.right = Materiales(material)
                else:
                    self.right.add(material)

            elif material["fecha"] < self.material["fecha"]:
                if self.left is None:
                    self.left = Materiales(material)
                else:
                    self.left.add(material)
            elif material["fecha"] > self.material["fecha"]:
                if self.right is None:
                    self.right = Materiales(material)
                else:
                    self.right.add(material)
            
        else:
            #print("Nodo nulo creado")
            self.material = material

    def mostrar(self):
        if self.material is None:
            return print("None")
        if self.left:
            self.left.mostrar()
        print(f"{self.material}"),
        if self.right:
            self.right.mostrar()

    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.material)
            res = res + self.inorder(root.right)
        return res

    def preorder(self, root):
        res = []
        if root:
            res.append(root.material)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res

    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.material)
        return res

    def sumar(self, root):
        if root is None:
            return 0
        if root.material == None:
            return 0
        return self.sumar(root.left) + self.sumar(root.right) + root.material["cantidad"]

    def total_nodos(self, root):
        if root is None:
            return 0
        return 1 + self.total_nodos(root.left) + self.total_nodos(root.right)

    def buscar(self, root, codigo, fecha):
        if root is None or root.planeta.codigo == codigo and root.planeta.fecha == fecha:
            return root
        if root.planeta.codigo < codigo :
            return self.buscar(root.right, codigo, fecha)
        elif root.planeta.codigo > codigo:
            return self.buscar(root.left, codigo, fecha)
        if root.planeta.fecha < fecha :
            return self.buscar(root.right, codigo, fecha)
        elif root.planeta.fecha > fecha:
            return self.buscar(root.left, codigo, fecha)
