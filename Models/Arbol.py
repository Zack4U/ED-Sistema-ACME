class Arbol:
    def __init__(self, planeta):
        self.left = None
        self.right = None
        self.planeta = planeta

    def add(self, planeta):
        if self.planeta:
            if planeta.codigo < self.planeta.codigo:
                if self.left is None:
                    self.left = Arbol(planeta)
                else:
                    self.left.add(planeta)
            elif planeta.codigo > self.planeta.codigo:
                if self.right is None:
                    self.right = Arbol(planeta)
                else:
                    self.right.add(planeta)
        else:
            print("Nodo Nulo creado")
            self.planeta = planeta

    def mostrar(self):
        if self.left:
            self.left.mostrar()
        print(self.planeta.nombre),
        if self.right:
            self.right.mostrar()

    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.planeta)
            res = res + self.inorder(root.right)
        return res

    def inorderR(self, root):
        res = []
        if root:
            res = self.inorder(root.right)
            res.append(root.planeta)
            res = res + self.inorder(root.left)
        return res

    def preorder(self, root):
        res = []
        if root:
            res.append(root.planeta)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res

    def preorderR(self, root):
        res = []
        if root:
            res.append(root.planeta)
            res = res + self.preorder(root.right)
            res = res + self.preorder(root.left)
        return res

    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.planeta)
        return res

    def postorderR(self, root):
        res = []
        if root:
            res = self.postorder(root.right)
            res = res + self.postorder(root.left)
            res.append(root.planeta)
        return res

    # def delete(self, planeta):
    #    response = self
    #    if (planeta.codigo < self.planeta.codigo):
    #        self.left = self.left.delete(planeta)
    #    elif (planeta.codigo > self.planeta.codigo):
    #        self.right = self.right.delete(planeta)
    #    else:
    #        if (self.left != None and self.right != None):
    #            temp = self
    #            maxOfTheLeft = self.left.findPredecessor()
    #            self.planeta = maxOfTheLeft.planeta
    #            temp.left = temp.left.delete(maxOfTheLeft.planeta)
    #        elif (self.left != None):
    #            response = self.left
    #        elif (self.right != None):
    #            response = self.right
    #        else:
    #            response = None
    #    return None

    def delete(self, root, planeta):
        if root is None:
            return root
        
        if planeta.codigo < root.planeta.codigo:
            root.left = self.delete(root.left, planeta)
            
        elif (planeta.codigo > root.planeta.codigo):
            root.right = self.delete(root.right, planeta)
            
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.minValueNode(root.right)
            root.planeta = temp.planeta
            root.right = self.delete(root.right, temp.planeta)

        return root

    def minValueNode(self, planeta):
        current = planeta

        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current
