class Cola: 
    def __init__(self,max_size):
        self.datos = [None]*max_size
        self.primero = None
        self.ultimo = None
        self.size = 0
        self.max_size = max_size
        

    def esVacia(self): 
        return self.size == 0  
    def esLleno(self): 
        return self.size == self.max_size
 
    
    def encolar(self, dato):  
        if self.esVacia():
            self.primero = self.ultimo  = 0
            self.datos[self.ultimo] = dato
        elif not self.esLleno() : 
            self.datos[(self.ultimo+1) % self.max_size ] = dato
            self.ultimo=(self.ultimo+1) % self.max_size 
            self.size +=1

            
    def desencolar(self):   
        if self.esVacia() :
            raise Exception("La lista esta vacia")
        des=self.datos[self.primero] 
        self.primero = (self.primero+1) % self.max_size
        self.size -= 1
        print(des)
          
        
    def pistear(self): 
        if self.esVacia():
            #raise Exception("La lista esta vacia") 
            return self.datos[self.primero] 

    def rotar(self, pos): # Rota los elementos de la cola el número de posiciones especificado
        if  self.esVacia():
            raise Exception("No hay Elementos en la cola") 
        rotar = self.primero = (self.primero+1) % pos
        self.primero = rotar 
       # se le dio una base a chatgpt para que realizara la correcion la base que se le dio fue la siguinte def rotar(self, pos): # Rota los elementos de la cola el número de posiciones especificado
       #  self.datos[self.primero] 
       # self.primero = (self.primero+1) % pos 
       
    def desencolar_n(self,n): # Desencola los siguientes n elementos, debe retornar una lista
        des=[] 
        des.append(self.datos[self.primero] )
        self.primero = (self.primero+1) % n
        self.size -= 1
        return (des)
    """ Alex Giraldo"""