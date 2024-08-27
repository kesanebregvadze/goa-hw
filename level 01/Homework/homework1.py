from turtle import *

#we want to paint a hous
#stpe 1:  draw a squaare 

width(7)
speed(30)

color("pink")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of  squrae
 
#drawing door

forward(70)
left(90)
forward(120)
right(90)
forward(60)   
right(90)
forward(120)
penup()
goto(200,200)
pendown()

begin_fill()
right(150)
forward(200) 
left(120)
forward(200)
end_fill()


#drawing windous
left(30)
forward(100)
left(90)
color("blue")
forward(60)
left(90)

forward(60)
left(90)
forward(60)
left(90)
color("pink")
forward(160)
left(90)
forward(200)
left(90)
forward(160)



exitonclick()