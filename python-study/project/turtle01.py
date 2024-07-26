import turtle as t

t.speed(0)

t.bgcolor("white")

for _ in range(36):
  t.pencolor("blue")
  t.forward(100)
  t.right(45)
  t.pencolor("red")
  t.forward(50)
  t.right(45)
  t.pencolor("yellow")
  t.forward(25)
  t.right(45)
  t.backward(25)
  t.left(90)
  t.backward(50)
  t.left(90)
  t.backward(100)
  t.right(10)

t.mainloop()