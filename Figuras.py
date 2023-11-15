import turtle

# Ventana
window = turtle.Screen()
window.title("Automata Figura")
window.bgcolor("yellow")

# Crear una tortuga
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("green")
tortuga.shapesize(2)

# Definir coordenadas 
coordenadas_destino = [(0, 0), (100, 0), (100, 100), (0, 100)]  # Define las coordenadas de forma [x, y]

# Funciones girar izquierda y derecha
def girar_Izq(grados):
    tortuga.left(grados)

def girar_Der(grados):
    tortuga.right(grados)

# Función para avanzar a una coordenada específica
def avanzar_a_coordenada(x, y):
    tortuga.goto(x, y)

# Función para ejecutar una cadena de comandos
def ejecutar_comandos(cadena_comandos):
    comandos = cadena_comandos.split()

    i = 0
    while i < len(comandos):
        comando = comandos[i]

        if comando == "AV":
            i += 1
            distancia = float(comandos[i])
            tortuga.forward(distancia)
        elif comando == "DE":
            i += 1
            distancia = float(comandos[i])
            tortuga.right(90)
            tortuga.forward(distancia)
        elif comando == "IZ":
            tortuga.left(90)
        elif comando == "GI":
            i += 1
            grados = int(comandos[i])
            girar_Izq(grados)
        elif comando == "GD":
            i += 1
            grados = int(comandos[i])
            girar_Der(grados)
        else:
            print("Cadena incorrecta:", comando)

        i += 1

# Usuario
print("Alfabeto:")
print("- 'AV' Para avanzar")
print("- 'DE' Para avanzar a la derecha")
print("- 'IZ' Para avanzar a la izquierda")
print("- 'GI' Para girar a la izquierda X grados")
print("- 'GD' Para girar a la derecha X grados")

cadena_comandos = input("Ingrese una cadena: ")
ejecutar_comandos(cadena_comandos)

# Verificar si cumple con la cadena
if (round(tortuga.xcor()), round(tortuga.ycor())) in coordenadas_destino:
    print("Es un autómata finito con estado de aceptación.")
else:
    print("No es un autómata finito con estado de aceptación.")

# Esperar a que el usuario presione Enter antes de cerrar la ventana
input("Presione Enter para cerrar la ventana...")
turtle.bye()  # Cerrar la ventana





