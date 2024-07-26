import turtle as t
import random

def turn_left():
  player.left(30)
def turn_right():
  player.right(30)

def rand_pos():
  x_cor = random.randint(-350, 350)
  y_cor = random.randint(-350, 350)
  return x_cor, y_cor

def end():
  global game_over
  game_over = True

# 초기 화면 크기 설정
t.setup(800, 800)
t.bgcolor("skyblue")
t.up()
t.ht()

player_speed = 5
score = 0
game_over = False

t.goto(0, 350)
t.write(f"score: {score}", False, "center", ("", 20))

# player 터틀 객체를 새로 생성

player = t.Turtle()
player.shape("turtle")
player.shapesize(2)
player.up()
player.color("lavender")
player.speed(0)

# 먹이 객체 생성

food = t.Turtle()
food.ht()
food.shape("triangle")
food.up()
food.color("darkgreen")
food.speed(0)
food.setheading(90)
food.goto(rand_pos())
food.st()

# 독초 객체 생성

p_herbs = t.Turtle()
p_herbs.ht()
p_herbs.shape("triangle")
p_herbs.up()
p_herbs.color("red")
p_herbs.speed(0)
p_herbs.setheading(90)
p_herbs.goto(rand_pos())
p_herbs.st()

# 이벤트 설정

t.onkeypress(turn_left, "Left")
t.onkeypress(turn_right, "Right")
t.listen()

t.ontimer(end, 60*1000)

while not game_over:
  player.forward(player_speed)

# 거북이가 벽에 부딪혔을때 각도를 180 회전
  if player.xcor() > 380 or player.xcor() < -380 or player.ycor() > 380 or player.ycor() < -380:
    player.right(180)

  # 거북이가 먹이를 먹었는지 판단
  if player.distance(food) < 20:
   food.goto(rand_pos())
   p_herbs.goto(rand_pos())
   player_speed += 1
   score += 1
   t.clear()
   t.write(f"score: {score}", False, "center", ("", 20))
  
  # 거북이가 독초를 먹으면, game_over
  if player.distance(p_herbs) < 20:
    game_over = True

t.goto(0, 0)
t.write(f"Game Over", False, "center", ("", 50))
  

t.mainloop()