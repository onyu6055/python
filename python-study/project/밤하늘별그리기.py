import turtle as t
import random

def draw_star():
  t.up()
  t.goto(random.randint(-300, 300), random.randint(-300, 300))
  t.down

  for i in range (5):
    t.forward(star_size)
    t.left(72)
    t.forward(star_size)
    t.right(144)

color = ("red","orange", "blue", "green", "white", "yellow", "indigo", "pink")

t.bgcolor("black")
t.speed(0)

for x in range(20):
  
  # t.dot(5, random.choice(color))

  t.color(random.choice(color))
  t.begin_fill()
  star_size = random.randint(3, 15)

  draw_star()

  t.end_fill()

# draw_star()
# draw_star()
# draw_star()
# draw_star()
# draw_star()
# draw_star()
# draw_star()

t.hideturtle()

t.mainloop()