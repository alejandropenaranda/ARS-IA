import pygame , sys
import random

#-----------------
mouse = {'x':0, 'y':0}


#-----------------

def movements_table (left_sen, up_sen, right_sen,down_sen, hq):
    # the movements will be represented by numbers  1 = up, 2 = left, 3 = down, 4 = right
    # when the mouse found the cheese, this will be represented by the number 5 = found cheese
    # when any sensor is true, it means that the mouse can go in that direction, otherwise he cant (false)
    action = 0
    if hq:
        action = 5
        return action
    elif (left_sen and up_sen and right_sen and down_sen and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen and right_sen and down_sen == False and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen and right_sen == False and down_sen and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen and right_sen == False and down_sen == False and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen == False  and right_sen and down_sen and hq == False): 
        action = 2
        return action
    
    elif (left_sen and up_sen == False and right_sen and down_sen == False and hq == False): 
        action = 4
        return action
    
    elif (left_sen and up_sen == False and right_sen == False and down_sen and hq == False): 
        action = 2
        return action
    
    elif (left_sen and up_sen == False and right_sen == False and down_sen == False and hq == False): 
        action = 2
        return action
    
    elif (left_sen == False and up_sen and right_sen and down_sen and hq == False): 
        action = 1
        return action
    
    elif (left_sen == False and up_sen and right_sen and down_sen == False and hq == False): 
        action = 4
        return action

    elif (left_sen == False and up_sen and right_sen == False and down_sen and hq == False): 
        action = 3
        return action
    
    elif (left_sen == False and up_sen and right_sen == False and down_sen == False and hq == False): 
        action = 1
        return action

    elif (left_sen == False and up_sen == False and right_sen and down_sen and hq == False): 
        action = 4
        return action
    
    elif (left_sen == False and up_sen == False and right_sen and down_sen == False and hq == False): 
        action = 4
        return action
    
    elif (left_sen == False and up_sen == False and right_sen == False and down_sen and hq == False): 
        action = 3
        return action
    
#print(movements_table(True,True,True,False,False))

def generate_matrix(n,m):
    matriz = []
    for i in range(n):
        matriz.append([])
        for h in range(m):
            matriz[i].append(wall_generator())
    return matriz

#funcion retorna 1 o 0 dependiendo del valor que se genere automaticamente
# se le da mas posibillidad de devolver 0 para que no hayan muchas paredes
def wall_generator():
    numero = random.randint(0,8)
    if numero == 0:
        return 0
    else:
        return 1

#solo funciona para matrices nxn

#se crea el tablero, nota si se actualiza el tablero se debe de referenciar otra vez ya que no esta en el while del refresco
def create_board (matriz):
    i = -1 #desplazamiento en las columnas
    j = 0  #desplazamiento en las filas
    size = 90 #tamanho del cuadrado
    tamanho = len(matriz) #tamanho de la matriz
    aux = 25 #corrimiento de los cuadrados
    for rows in matriz:
        i = i+1
        for cells in rows:
            if (cells == 1):
                #pygame.draw.rect(screen,blue,((j*size)+aux,(i*size)+aux,size,size))
                screen.blit(roadImage, ((j*size)+aux,(i*size)+aux))
            elif(cells ==0):
                #pygame.draw.rect(screen,black,((j*size)+aux,(i*size)+aux,size,size))
                screen.blit(wallImage, ((j*size)+aux,(i*size)+aux))
            j = j+1
            if (j==tamanho):
                j = 0
                break
            if (i==tamanho):
                break
    return True
            
#1 es un espacio libre para avanzar
#0 no es un espacio libre
#2 es la rata
matriz =[[1,1,0,1,1],
         [0,1,1,1,0],
         [1,1,0,1,1],
         [1,1,1,1,1],
         [0,1,0,2,0]]

# tamaño de las filas y columnas
n = 5
m = 5

#se inicia la aplicacion
pygame.init()


#se carga la imagen del raton y demas
mouseImage = pygame.image.load('imagenes/prueba1.png')
roadImage = pygame.image.load('imagenes/road.jpg')
wallImage = pygame.image.load('imagenes/wall.jpg')

#Definir colores
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)

#tamanho de la GUI
size= (500,500)

#definicion de la GUI
screen = pygame.display.set_mode(size)

#fondo blanco
screen.fill(white)

#llamado de la funcion tablero
#create_board(matriz)
create_board(generate_matrix(n,m))
screen.blit(mouseImage, ((mouse.get('x')*90)+25,(mouse.get('y')*90)+25))

#while para la logica o los eventos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #zona de dibujo
    #pygame.draw.line(screen, green, [0,100], [100,100], 5)
    #pygame.draw.rect(screen,blue,(0,0,50,50)),

    # actualiza la pantalla
    pygame.display.flip()

#definition of code
#cambio de commit