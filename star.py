from turtle import Turtle

def draw_star(t, size):
    t.down()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(75)
    t.forward(size)
    for _ in range(4):
        t.left(144)
        t.forward(size)
    t.end_fill()

def draw_pattern(t, size, star_func, count):  
    angle = 360 / count
    for i in range(count):
        t.up()
        cur_angle = i * angle
        t.right(cur_angle)
        t.forward(size * 2)  
        t.left(cur_angle)
        star_func(t, size)
        t.up()
        t.home()

count = int(input("Enter the number of stars: "))
size = int(input("Enter the size: "))
t = Turtle()
draw_pattern(t, size, draw_star, count)
