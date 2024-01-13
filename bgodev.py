import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time

class cubeClass:

    def __init__(self):
        #açı tanımlamaları
        cos45=0.707
        sin45=-0.707
        cos35=0.816
        sin35=0.577
        #-----------------------------------
        #matris tanımlamaları
        donY =[[cos45,0,-sin45,0],[0,1,0,0],[sin45,0,cos45,0],[0,0,0,1]]
        donX =[[1,0,0,0],[0,cos35,sin35,0],[0,-sin35,cos35,0],[0,0,0,1]]
        tiz=[[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,1]]
        x=[[0,0,0,1],[1,0,0,1],[1,0,1,1],[0,0,1,1],[0,1,1,1],[0,1,0,1],[1,1,0,1],[1,0.5,1,1],[0.5,1,1,1],[1,1,0.5,1]]
        #-----------------------------------
        #matris çarpımı için gerekli döngüler
        result = []
        for i in range(len(donY)):

            row = [] 
            for j in range(len(donX[0])):
        
                product = 0
                for v in range(len(donY[i])):
                    product += donY[i][v] * donX[v][j]
                row.append(product)
        
            result.append(row) 
        #-----------------------------------
        result1 = []
        for i in range(len(result)):

            row1 = [] 
            for j in range(len(tiz[0])):
        
                product1 = 0
                for v in range(len(result[i])):
                    product1 += result[i][v] * tiz[v][j]
                row1.append(product1)
        
            result1.append(row1) 
        #-----------------------------------
        global sonuc 

        sonuc=[]

        for i in range(len(x)):

            row2 = [] 
            for j in range(len(result1[0])):
        
                product1 = 0
                for v in range(len(x[i])):
                    product1 += x[i][v] * result1[v][j]
                row2.append(product1)
        
            sonuc.append(row2) 
        #-----------------------------------

        self.rotation = [0,0,0,0]
        #köşe noktaları
        self.verticies =[
            ( sonuc[0][0], sonuc[0][1], sonuc[0][2]), # 0 A

            ( sonuc[1][0], sonuc[1][1], sonuc[1][2]), # 1 B

            (sonuc[2][0], sonuc[2][1], sonuc[2][2]), # 2 C

            (sonuc[3][0], sonuc[3][1], sonuc[3][2]), # 3 D

            ( sonuc[4][0], sonuc[4][1], sonuc[4][2]), # 4 E

            ( sonuc[5][0], sonuc[5][1], sonuc[5][2]), # 5 F

            (sonuc[6][0], sonuc[6][1], sonuc[6][2]), # 6 G

            (sonuc[7][0], sonuc[7][1], sonuc[7][2]), # 7 H

            (sonuc[8][0], sonuc[8][1], sonuc[8][2]), #8 J
             
            (sonuc[9][0], sonuc[9][1], sonuc[9][2]) #9 K
            ]
        #kenar noktaları
        self.edges = (
            (0,1),#a-b
            (1,2),#b-c
            (2,3),#c-d
            (3,4),#d-e
            (4,5),#e-f
            (5,6),#f-g
            (6,9),#g-k
            (8,9),#j-k
            (8,2),#j-h
            (9,2),#k-h
            (3,0),#d-a
            (4,8),#e-j
            (7,2),#h-c
            (6,1),#g-b
            (0,5)#a-f
            )

        # Küpü 1.5 birim x ekseni boyunca öteleme
        self.otele_x = 1.5
        for i in range(len(self.verticies)):
            self.verticies[i] = (self.verticies[i][0] + self.otele_x, self.verticies[i][1], self.verticies[i][2])

    def cube(self):
        glBegin(GL_LINES)
        for self.edge in self.edges:
            for self.vertex in self.edge:
                glVertex3fv(self.verticies[self.vertex])
        glEnd()

    # eksen çizimi
    def systems(self):
      glBegin(GL_LINES)
      glVertex3f(0,0,0)
      glVertex3f(0,100,0)#y
      glEnd()
      # -----------------------------------
      glBegin(GL_LINES)
      glVertex3f(0,0,0)
      glVertex3f(70,-40,0)#x
      glEnd()
      # -----------------------------------
      glBegin(GL_LINES)
      glVertex3f(0,0,0)
      glVertex3f(-70,-40,0)#z
      glEnd()

# -----------------------------------
# çalıştırılacak main fonk
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    cube1 = cubeClass()

    glTranslatef(0.0, 0.0 , -5)  # Kamerayı daha geriye taşıdık

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        cube1.cube()
        cube1.systems()
        pygame.display.flip()
        pygame.time.wait(10)

main()