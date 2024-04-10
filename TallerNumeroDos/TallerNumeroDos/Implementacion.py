from Clases.Pila import Pila
from Clases.HashMap import HashMap
from Constantes.constantesemojis import constantesEmojis
from Constantes.constantesOperadores import constantesOperadores

class ValoresEmojisMap(HashMap):
    def __init__(self):
        super().__init__()
        self.asignar_valores()

    def asignar_valores(self):
        # Asignar valores numéricos a los emojis
        self.poner(constantesEmojis.SOL, 1)
        self.poner(constantesEmojis.NUBE, 2)
        self.poner(constantesEmojis.LLUVIA, 3)
        self.poner(constantesEmojis.NIEVE, 4)
        self.poner(constantesEmojis.METEORO, 5)
        self.poner(constantesEmojis.MARCA, 6)
        self.poner(constantesEmojis.FLOR, 7)
        self.poner(constantesEmojis.AS, 8)
        self.poner(constantesEmojis.TREBOL, 9)
        self.poner(constantesEmojis.CORAZON, 10)
        self.poner(constantesEmojis.DIAMANTE, 11)
        self.poner(constantesEmojis.DADO1, 12)
        self.poner(constantesEmojis.ADVERTENCIA, 13)
        self.poner(constantesEmojis.AJUSTES, 14)
        self.poner(constantesEmojis.DADO2, 15)
        self.poner(constantesEmojis.DADO3, 16)
        self.poner(constantesEmojis.DADO4, 17)
        self.poner(constantesEmojis.DADO5, 18)
        self.poner(constantesEmojis.DADO6, 19)
        self.poner(constantesEmojis.ALAMBIQUE, 20)
        self.poner(constantesEmojis.ATOMO, 21)
        self.poner(constantesEmojis.WHITEFLAG, 22)
        self.poner(constantesEmojis.ANCLA, 23)
        self.poner(constantesEmojis.ESPADAS, 24)
        self.poner(constantesEmojis.BALANZAS, 25)
        self.poner(constantesEmojis.FLORDELIS, 26)

def evaluar_expresion_postfija(expresion):
    pila = Pila()
    hashmap = ValoresEmojisMap()  # Usamos nuestra clase especializada
    for token in expresion:
        if token in constantesEmojis.__dict__.values():
            # Es un glifo, obtenemos su valor numérico
            valor = hashmap.obtener(token).retornaValor()
            pila.apilar(valor)
        elif token in constantesOperadores.__dict__.values():
            # Es un operador, realizamos la operación correspondiente
            if pila.es_vacia() or pila.tamanio() < 2:
                raise ValueError("Expresión inválida: faltan operandos")
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if token == constantesOperadores.SUMA:
                pila.apilar(operando1 + operando2)
            elif token == constantesOperadores.RESTA:
                pila.apilar(operando1 - operando2)
            elif token == constantesOperadores.MULTIPLICACION:
                pila.apilar(operando1 * operando2)
            elif token == constantesOperadores.DIVISION:
                if operando2 == 0:
                    raise ValueError("División por cero")
                pila.apilar(operando1 / operando2)
        else:
            raise ValueError(f"Token no reconocido: {token}")

    if pila.es_vacia() or pila.tamanio() != 1:
        raise ValueError("Expresión inválida: demasiados operadores")

    resultado = pila.desapilar()
    return resultado

def procesar_archivo_emojis(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as f_in, open(archivo_salida, 'w') as f_out:
        for linea in f_in:
            expresion = linea.strip().split()
            try:
                resultado = evaluar_expresion_postfija(expresion)
                f_out.write(f"{resultado}\n")
            except (ValueError, KeyError) as e:
                f_out.write(f"Error: {str(e)}\n")

if __name__ == "__main__":
    archivo_entrada = r"D:\TallerNumeroDosAlex+\ArchivosTxt\entrada.txt"
    archivo_salida = r"D:\TallerNumeroDosAlex+\ArchivosTxt\salida.txt"
    procesar_archivo_emojis(archivo_entrada, archivo_salida)
