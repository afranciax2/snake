import turtle
import time

posponer = 0.1

#Crear ventana del juego
ventana = turtle.Screen()
ventana.title("SNAKE")
ventana.bgcolor("blue")
ventana.setup(width=600, height=600)
ventana.tracer(0)

#Crear cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup() #quitar rastra de la tortuga
cabeza.goto(0, 0)
cabeza.direction = "stop"

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
        y = cabeza.ycor() # Te brinda la corrdena "Y"
        cabeza.sety(y + 20)
    if cabeza.direction == "abajo":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "derecha":
        x = cabeza.xcor() # Te brinda la corrdena "X"
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

    movimiento()
    time.sleep(posponer)