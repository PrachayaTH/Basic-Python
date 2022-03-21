Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen() #P ตัวใหญ่
tao.shape('turtle')

for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.penup()
tao.goto(50,50)
tao.pendown()

for i in range(4):
    tao.forward(100)
    tao.right(90)

    
def Move(x,y):
    '''เอาไว้ย้ายตัวเต่า'''
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

    
def Rec():
    for i in range(4):
        tao.forward(100)
        tao.left(90)

        
def Circle():
    '''เอาไว้สร้างวงกลม'''
    for i in range(4)
    
SyntaxError: expected ':'
def Circle():
    '''เอาไว้สร้างวงกลม'''
    for i in range(4):
        tao.circle(50)

        
Move(-100,-100)
Rec()
Move(-100,-100)
Move(-200,-200)
Circle()
Move(25,25)
Move(-100,100)
Circle()
