#!/usr/bin/env python
from pyglet.gl import *
import pyglet
from pyglet.window import *

window = pyglet.window.Window(width=640, height=480, resizable=True)

zoom=-12
xrot=yrot=zrot=0.0      
xrotspeed = 1.0
yrotspeed = 0.0

botom = None # display list storage
top = None #display list storage
right = None
left = None
front = None
back = None
def build_lists():
	global botom, top, front, right,left,back
	
	botom = glGenLists(4)
 	glNewList(botom, GL_COMPILE)    # new compiled box display list
  	glBegin(GL_QUADS)
  	glVertex3f(0.0, 0.0, 0.0)       
  	glVertex3f(4.0, 0.0, 0.0)   
  	glVertex3f(4.0, 0.0, 4.0)       
  	glVertex3f(0.0, 0.0, 4.0)
  	glEnd()
  	glEndList()
  	 
  	front = glGenLists(4)
 	glNewList(front, GL_COMPILE)    # new compiled box display list
  	glBegin(GL_QUADS)      
  	glVertex3f(0.0, 0.0, 4.0)       
  	glVertex3f(4.0, 0.0, 4.0)       
  	glVertex3f(4.0, 4.0, 4.0)       
  	glVertex3f(0.0, 4.0, 4.0)
  	glEnd()
  	glEndList()
  	
  	back = glGenLists(4)
 	glNewList(back, GL_COMPILE)    # new compiled box display list
  	glBegin(GL_QUADS)    
  	glVertex3f(0.0, 0.0, 0.0)       
  	glVertex3f(0.0, 4.0, 0.0)   
  	glVertex3f(4.0, 4.0, 0.0)    
  	glVertex3f(4.0, 0.0, 0.0)
  	glEnd()
  	glEndList()
  	
  	right = glGenLists(4)
 	glNewList(right, GL_COMPILE)    # new compiled box display list
  	glBegin(GL_QUADS)
  	glVertex3f(4.0, 0.0, 0.0)
  	glVertex3f(4.0, 4.0, 0.0)
  	glVertex3f(4.0, 4.0, 4.0)
  	glVertex3f(4.0, 0.0, 4.0)
  	glEnd()
  	glEndList()
  	
  	left = glGenLists(4)
 	glNewList(left, GL_COMPILE)    # new compiled box display list
  	glBegin(GL_QUADS)
  	glVertex3f(0.0, 0.0, 0.0)
  	glVertex3f(0.0, 0.0, 4.0)
  	glVertex3f(0.0, 4.0, 4.0)
  	glVertex3f(0.0, 4.0, 0.0)
  	glEnd()
  	glEndList()   # Done building the list

  	top=glGenLists(4)
  	glNewList(top, GL_COMPILE)    # new compiled top display list
  	glBegin(GL_QUADS)
  	glVertex3f(0.0, 4.0, 0.0)
  	glVertex3f(0.0, 4.0, 4.0)
  	glVertex3f(4.0, 4.0, 4.0)
  	glVertex3f(4.0, 4.0, 0.0)
  	glEnd()
  	glEndList()

def init():
        """
        Pyglet oftentimes calls this setup()    
        """
        build_lists()
        glShadeModel(GL_SMOOTH) # Enables smooth shading GL_SMOOTH or GL_FLAT
        glClearColor(0.0, 0.0, 0.0, 0.0) #Black background red, blue, green, alpha
        glClearDepth(1.0)               # Depth buffer setup
        glEnable(GL_DEPTH_TEST)         # Enables depth testing
        glDepthFunc(GL_LEQUAL)          # The type of depth test to do
        glEnable(GL_LIGHT0) # quick and dirty lighting 
        glEnable(GL_COLOR_MATERIAL)     # enable coloring
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)       # Really nice perspective calculations


@window.event
def on_draw():
        # Here we do all the drawing
        global xrot,yrot,zoom
        glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()        # load identity matrix and make the 3D objects to get 2D points
        glTranslatef( 0.5,0.5,zoom)
        glRotatef(0.0 + xrot, 1.0, 0.0, 0.0) # tilt up/down
        glRotatef(0.0 + yrot, 0.0, 1.0, 0.0)   # spin left/right
        glColor3f(1.0, 0.0, 0.0) # select a botom color
        glCallList(botom) # draw the botom
	glColor3f(0.5, 0.0, 0.0)
        glCallList(top)  
        glColor3f(0.0,1.0,0.0)
        glCallList(front)
        glColor3f(0.0,0.5,0.0)
        glCallList(back)
        glColor3f(0.0,0.0,1.0)
        glCallList(right)
        glColor3f(0.0,0.0,0.5)
        glCallList(left)
	return pyglet.event.EVENT_HANDLED
        
@window.event
def on_mouse_scroll(x,y,scroll_x,scroll_y):
	global zoom
	if scroll_y > 0:
		zoom +=0.1
	elif scroll_y < 0:
		zoom -=0.1
	return pyglet.event.EVENT_HANDLED
	
@window.event
def on_key_press(symbol, modifiers):
        global xrot, yrot, xrotspeed, yrotspeed,zoom
        if symbol == key.RETURN or symbol == key.ESCAPE:
                  exit()
        elif symbol == key.LEFT:
                if key.Q == modifiers:
                        yrotspeed-=0.2
                else:
                        yrotspeed-=1.2
        elif symbol == key.RIGHT:
                yrotspeed+=1.2
        elif symbol == key.UP:
                xrotspeed -= 1.2
        elif symbol == key.DOWN:
                xrotspeed += 1.2
        elif symbol == key.SPACE:
                xrotspeed = yrotspeed = 0
        elif symbol == key.F:
        	window.set_fullscreen(fullscreen=True)
        elif symbol == key.M:
        	window.set_fullscreen(fullscreen=False)
        return pyglet.event.EVENT_HANDLED


def update(dt):
        global xrot, yrot, zrot
        xrot += xrotspeed
        yrot += yrotspeed

@window.event
def on_resize(width, height):
        if height==0:
                height = 1
        glViewport(0, 0, width, height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # Calculate the aspect ratio of the window
        gluPerspective(45.0, 1.0*width/height, 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        return pyglet.event.EVENT_HANDLED

pyglet.clock.schedule(update)
init()
pyglet.app.run()
