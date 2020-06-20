#Pregunta 4
#Parte a
#Autor: William Guadalupe
#Descripcion: Eje x(color rojo), Eje y(color verde), Eje z(color azul)
#-------------------------------------------------------------------------------
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


#Funcion que Grafica el Cubo por vertices
def cubo():
    glBegin(GL_QUADS)
                    
    #Contruccion de Cara ABCD
    glColor3f(1.0,0.0,0.0)#color rojo            
    glVertex3f( 0.0, 0.0, 0.0)#VERTICE_A        
    glVertex3f( 0.0, 1.0, 0.0)#VERTICE_B 
    glVertex3f( 1.0, 1.0, 0.0)#VERTICE_C
    glVertex3f( 1.0, 0.0, 0.0)#VERTICE_D                 
    
    ##Contruccion de Cara BCGF
    glColor3f(0.0,0.0,1.0)#color azul          
    glVertex3f( 0.0, 1.0, 0.0)#VERTICE_B                
    glVertex3f( 1.0, 1.0, 0.0)#VERTICE_C                
    glVertex3f( 1.0, 1.0, 1.0)#VERTICE_G                
    glVertex3f( 0.0, 1.0, 1.0)#VERTICE_F                
    
    ##Contruccion de Cara CDGH
    glColor3f(0.0,1.0,0.0)#color verde         
    glVertex3f( 1.0, 1.0, 0.0)#VERTICE_C        
    glVertex3f( 1.0, 0.0, 0.0)#VERTICE_D
    glVertex3f( 1.0, 0.0, 1.0)#VERTICE_H        
    glVertex3f( 1.0, 1.0, 1.0)#VERTICE_G       
           
    #Contruccion de Cara ADHE
    glColor3f(0.0,0.0,1.0)#color azul            
    glVertex3f( 0.0, 0.0, 0.0)#VERTICE_A        
    glVertex3f( 1.0, 0.0, 0.0)#VERTICE_D
    glVertex3f( 1.0, 0.0, 1.0)#VERTICE_H       
    glVertex3f( 0.0, 0.0, 1.0)#VERTICE_E        
           
    ##Contruccion de Cara ABFE
    glColor3f(0.0,1.0,0.0)#color verde           
    glVertex3f( 0.0, 0.0, 0.0)#VERTICE_A       
    glVertex3f( 0.0, 1.0, 0.0)#VERTICE_B
    glVertex3f( 0.0, 1.0, 1.0)#VERTICE_F         
    glVertex3f( 0.0, 0.0, 1.0)#VERTICE_E       

    ##Contruccion de Cara EFGH
    glColor3f(1.0,0.0,0.0)#color rojo             
    glVertex3f( 0.0, 0.0, 1.0)#VERTICE_E       
    glVertex3f( 0.0, 1.0, 1.0)#VERTICE_F        
    glVertex3f( 1.0, 1.0, 1.0)#VERTICE_G        
    glVertex3f( 1.0, 0.0, 1.0)#VERTICE_H       

    glEnd() 

#Funcion que Grafica los ejes X,Y,Z
def ejes():
    #EJE X-Color rojo
    glBegin(GL_LINES)
    glColor3f(1.0,0.0,0.0)#color rojo            
    glVertex3f( 0.0, 0.0, 0.0)#origen        
    glVertex3f( 2.5, 0.0, 0.0)# X+
    glEnd()
    
    #EJE Y-Color verde
    glBegin(GL_LINES) 
    glColor3f(0.0,1.0,0.0)#color verde            
    glVertex3f( 0.0, 0.0, 0.0)#Origen        
    glVertex3f( 0.0, 2.5, 0.0)# Y+
    glEnd()
    
    #EJE Z-Color azul
    glBegin(GL_LINES)
    glColor3f(0.0,0.0,1.0)#color azul            
    glVertex3f( 0.0, 0.0, 0.0)#Origen        
    glVertex3f( 0.0, 0.0, 2.5)# Z+
    glEnd()

#Funcion para el grafico del cubo y ejes
def grafico():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()
    glTranslatef(0.0,0.0,-6.0)
#Giraremos la vista en el eje Y, X para apreciar el cubo 3D
    glRotatef(-25.0,0.0,1.0,0.0)#eje y
    glRotatef(15.0,1.0,0.0,0.0)#eje x
#Llamada a los metodos cubo y ejes
    cubo()
    ejes()
    glutSwapBuffers()

#Funcion arranque
def inicia(Width, Height):                
    glClearColor(0.3, 0.3, 0.3, 0.0)    
    glClearDepth(1.0)                   
    glDepthFunc(GL_LESS)                
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT, GL_LINE)    
    glPolygonMode(GL_BACK, GL_LINE)     
    glShadeModel(GL_SMOOTH)                
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                                                        
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("CUBO UNITARIO")
    glutDisplayFunc(grafico) #llama al metodo grafico
    inicia(640, 480)
    glutMainLoop()
main()