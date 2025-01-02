'''
/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
 '''

# Funciones simples
def greet():
    print("Funciones simples: ")
    print("Hola, Python!")
greet()


# Funciones con retorno
def return_greet():
    print("Funciones con retorno: ")
    return("Hola, Python retornado!")
greet = return_greet()
print(greet)

# Funciones con argumento
def arg_greet(name):
    print("Funciones con argumento: ")
    print(f"Hola, {name}!")
arg_greet("Luis")

def args_greet(greet, name):
    print("Funciones con argumentos sin ordenar: ")
    print(f"{greet}, {name}!")
args_greet(name="Luis", greet="Hi!")

# Funciones con argumento predeterminado
def default_arg_greet(name="Brais default"):
    print("Funciones con argumento predeterminado: ")
    print(f"Hola, {name}!")
default_arg_greet()
default_arg_greet("Luis")