import turtle as t

t.bgcolor("black")
t.color("pink")
t.speed(0)

for i in range(200):
  # pen 사이즈를 점점 굵게 : 200이 됐을 때 4
  t.pensize(i/50)
  t.forward(i)
  t.left(65)

# 마지막 펜이 끝나는 지점에서 줄기 그리기

t.color("lightblue")
t.setheading(270)

for i in range(50):
  t.pensize(25-i/2)
  t.forward(i/4)

# 잎 그리기

t.color("yellowgreen")
t.setheading(60)
for x in range(100):
  t.pensize(100 - x)
  t.forward(x/10)

# 터틀 숨기기

t.hideturtle()

t.mainloop()