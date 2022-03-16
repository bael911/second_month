import turtle

trt = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor('black')
trt.speed(0)
scr.title('corona virus structure')
trt.color('red')

for x in range(210):
    if x in range(50):
        trt.hideturtle()
    else:
        trt.forward(10 + x)
        trt.left(x)

turtle.done()
