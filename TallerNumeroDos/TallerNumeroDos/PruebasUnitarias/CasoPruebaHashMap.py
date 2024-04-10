# Importar las clases necesarias
import sys
sys.path.append(r'D:\TallerNumeroDos')  # Agrega la ruta del directorio principal de tu proyecto

from Clases.HashMap import HashMap

# Crear un objeto de la clase HashMap
mi_mapa = HashMap()

# Caso de prueba para el método poner
mi_mapa.poner("clave1", 10)
mi_mapa.poner("clave2", 20)
mi_mapa.poner("clave3", 30)

# Caso de prueba para el método obtener
print(mi_mapa.obtener("clave1").retornaValor())  # Debería imprimir 10
print(mi_mapa.obtener("clave2").retornaValor())  # Debería imprimir 20
print(mi_mapa.obtener("clave3").retornaValor())  # Debería imprimir 30

# Caso de prueba para el método contiene
print(mi_mapa.contiene("clave1"))  # Debería imprimir True
print(mi_mapa.contiene("clave4"))  # Debería imprimir False

# Caso de prueba para el método poner (actualización de valor)
mi_mapa.poner("clave1", 100)

print(mi_mapa.obtener("clave1").retornaValor())  # Debería imprimir 100

print("Cantidad de objetos en el mapa:", mi_mapa.conteo)

print("__obtener_hash_reducido('clave1'):", mi_mapa._HashMap__obtener_hash_reducido('clave1'))


