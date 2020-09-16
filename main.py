import turtle
import time
import random

posponer = 0.1

#Crear ventana del juego
ventana = turtle.Screen()
ventana.title("SNAKE GAME")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0)

#Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup() # Método para quitar rastro de la tortuga
cabeza.goto(0, 0)
cabeza.direction = "stop"

#Comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("yellow")
comida.penup()
comida.goto(79, 100)

# Cola de la serpiente
cola = []

#Funciones de movimiento
def arriba():
    cabeza.direction = "arriba"

def abajo():
    cabeza.direction = "abajo"

def derecha():
    cabeza.direction = "derecha"

def izquierda():
    cabeza.direction = "izquierda"


# Función para mover a la serpierte 
def movimiento():
    if cabeza.direction == "arriba":
        y = cabeza.ycor() # Método que brinda la cordenada "Y"
        cabeza.sety(y + 20)
    if cabeza.direction == "abajo":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "derecha":
        x = cabeza.xcor() # Método que brinda la cordenada "X"
        cabeza.setx(x + 20)
    if cabeza.direction == "izquierda":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#Función para conectar moviento con teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(izquierda, "Left")
        
while True:
    ventana.update()

    # Tocar borde de pantanlla y detener desplezamieto de la serpiente
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 280 or cabeza.ycor() < -290:
        time.sleep(1) # Para dar pausa
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        # Limpiar listas de segmentos
        for esconder in cola:
            #Conservar código
            #1 esconder.goto(1000, 1000)
            #esconder.hideturtle()
        #2 cola.clear()
            esconder.hideturtle()
        cola.clear()


    # Comparar la distancia entre los 2 objetos (cabeza y comida)
    # Tanto la cabeza de la serpiente como la comida tiene 20x20 pixeles
    # Si la distancia es menor entre ambos objetos, significa que se han tocado
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280) # Método que crea enteros, desde que número incia y termina
        y = random.randint(-280, 280)
        comida.goto(x, y)
        
        # Cada vez que la serpiente come se agrega un segmento a tu cola
        # Código que se agregará elementos a la lista "cola"
        nueva_cola = turtle.Turtle()
        nueva_cola.speed(0)
        nueva_cola.shape("square")
        nueva_cola.color("grey")
        nueva_cola.penup()
        cola.append(nueva_cola)
    
    # Agregar cola al cuerpo de la serpiente
    total_cola = len(cola)
    for i in range(total_cola-1, 0, -1):
        x = cola[i - 1].xcor()
        y = cola[i - 1].ycor()
        cola[i].goto(x, y)
    if total_cola > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cola[0].goto(x, y)

    movimiento()
    time.sleep(posponer)