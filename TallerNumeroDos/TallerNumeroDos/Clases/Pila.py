class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.es_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def es_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)
    
    def tope(self): 
        return self.items[-1]
    def sort(self): # Ordena los elementos de la pila
        return self.items.sort() #se realizo con el apoyo de chatgpt
    
""" Juan fernando """
