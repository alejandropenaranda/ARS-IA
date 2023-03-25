import pygame , sys
import random

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
            if i == mouse.get('y') and h == mouse.get('x'):
                matriz[i].append(1) 
            elif i == queso.get('y') and h == queso.get('x'):
                matriz[i].append(1) 
            else:
                matriz[i].append(wall_generator())
    return matriz

#funcion retorna 1 o 0 dependiendo del valor que se genere automaticamente
#se le da mas posibillidad de devolver 1 para que no hayan muchas paredes
#1 es un espacio libre para avanzar
#0 no es un espacio libre
def wall_generator():
    numero = random.randint(0,10)
    if numero == 0 or numero == 8:
        return 0
    else:
        return 1

#solo funciona para matrices nxn

#se crea el tablero, nota si se actualiza el tablero se debe de referenciar otra vez ya que no esta en el while del refresco
def create_board (matriz,size):
    i = -1 #desplazamiento en las columnas
    j = 0  #desplazamiento en las filas
    tamanho = len(matriz) #tamanho de la matriz
    aux = 0 #corrimiento de los cuadrados
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
#-----------------

# tamaño de las filas y columnas
n = 5
m = 5

#-----------------
def generate_rata():
    mouse = {'x':0, 'y':0}
    mouse.update({'x':random.randint(0,n-1), 'y':random.randint(0,m-1)})
    return  mouse
mouse = generate_rata()

def generate_queso():
    queso = {'x':0, 'y':0}
    queso.update({'x':random.randint(0,n-1), 'y':random.randint(0,m-1)})
    if(queso == mouse):
        generate_queso()
    return queso
    
queso = generate_queso()

#se inicia la aplicacion
pygame.init()

#se carga la imagen del raton y demas
mouseImage = pygame.image.load('imagenes/rata2.png')
cheeseImage = pygame.image.load('imagenes/queso.png')
roadImage = pygame.image.load('imagenes/road1.png')
wallImage = pygame.image.load('imagenes/wall.jpg')
imgsize = 90

#Definir colores
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)

#tamanho de la GUI
aux1 = n*imgsize
aux2 = m*imgsize
size = (aux1,aux2)

#definicion de la GUI
screen = pygame.display.set_mode(size)

#fondo blanco
screen.fill(white)

#llamado de la funcion tablero
#create_board(matriz)
create_board(generate_matrix(n,m),imgsize)
screen.blit(mouseImage, ((mouse.get('x')*imgsize),(mouse.get('y')*imgsize)))
screen.blit(cheeseImage, ((queso.get('x')*imgsize),(queso.get('y')*imgsize)))

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