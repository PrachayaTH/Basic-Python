Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen() #P ตัวใหญ่
tao.shape('turtle')
tao.forward(80)
tao.left(225)
tao.forward(160)
tao.left(45)
tao.forward(200)
tao.right(90)
tao.forward(250)
tao.right(90)
tao.forward(500)
tao.right(90)
tao.forward(250)
tao.right(90)
tao.forward(160)
tao.left(45)
tao.forward(50)
tao.left(135)
tao.forward(100)
tao.right(90)

tao.penup()
tao.forward(150)
tao.pendown()
tao.forward(100)
tao.lefr(90)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tao.lefr(90)
AttributeError: 'Turtle' object has no attribute 'lefr'. Did you mean: 'left'?
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
