from Clases.NM import NM

class HashMap :
    def __init__(self): # Constructor
        self.conteo_buckets = 10
        self.conteo = 0
        self.buckets = [None] * self.conteo_buckets

    def obtener(self,llave): # Busca el elemento con la llave y lo retorna
        hash_reducido = self.__obtener_hash_reducido(llave)
        iterador = self.buckets[hash_reducido]
        while iterador is not None and llave != iterador.retornaLlave():
            iterador = iterador.retornaLiga()
        if iterador is None:
            raise Exception(f"No se encontró la llave {llave}")
        return iterador
    
    def contiene(self, llave): # Retorna true si el elemento con la llave especificada existe, False de lo contrario
        try:
            self.obtener(llave)
        except:
            return False
        return True
    def poner(self, llave, valor): # Asocia el valor ingresado a la llave especificada.
        nodo_nuevo = NM(llave,valor)
        hash_reducido = self.__obtener_hash_reducido(llave)
        if self.buckets[hash_reducido] is None:
            self.buckets[hash_reducido] = nodo_nuevo
            self.conteo += 1
            return
        
        iterador = self.buckets[hash_reducido]
        anterior = None

        while iterador is not None and llave != iterador.retornaLlave():
            anterior = iterador
            iterador = iterador.retornaLiga()
        
        if iterador is None:
            anterior.asignaLiga(nodo_nuevo)
            self.conteo += 1
        else:
            iterador.asignaValor(valor)

    def __obtener_hash_reducido(self, llave): # Calcula el HashReducido a partir de una función hash que usted elija (no tiene que implementarla)
        valor_hash = hash(llave)
        hash_reducido = valor_hash % self.conteo_buckets
        return hash_reducido
    
    def conteo(self): ## Retorna el número de elementos del HashMap
        return len(self.buckets)

""" Simon Alejandro """