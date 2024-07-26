import turtle as t
import random
import time

def find_card(x, y):
  min_idx = 0
  min_dis = 100

  for i in range(16):
    distance = turtle[i].distance(x, y)
    if distance < min_dis:
      min_dis = distance
      min_idx = i
  return min_idx


def draw_text(message, size):
  t.write(message, False, "center", ("", size))

def result(m):
  t.goto(9, -60)
  draw_text(m, 30)

def score_update(m):
  score_pen.clear()
  score_pen.write(f"{m} {score}점/{attempt}번 시도", False,"center", ("", 15))

def play(x, y):
  global click_num
  global first_pick
  global second_pick
  global attempt
  global score

  if attempt == 12:
    result(("Game Over"))
  else:
    click_num += 1
    # 클릭한 이미지 찾기
    card_idx = find_card(x, y)
    turtle[card_idx].shape(img_list[card_idx])

    # 매 2회 클릭 시 마다 정답 check

    if click_num == 1: # 첫번째 이미지 클릭
      first_pick = card_idx
    elif click_num == 2: # 두번째 이미지 클릭
      second_pick = card_idx
      click_num = 0 # 두번 클릭했기 때문에 0으로 초기화
      attempt += 1

      # 정답 체크
      if img_list[first_pick] == img_list[second_pick]:
        # 정답
        score += 1
        score_update("정답")
        if score == 8:
          result("성공")
      else:
        # 오답
        score_update("오답")
        turtle[first_pick].shape(default_img)
        turtle[second_pick].shape(default_img)


t.bgcolor("pink")
t.setup(700, 700)
t.up()
t.hideturtle()
t.goto(0, 280)
draw_text("카드 매칭 게임", 30)

#점수 펜 객체 생성
score_pen = t.Turtle()
score_pen.up()
score_pen.ht()
score_pen.goto(9, 230)

# 터틀 객체 생성

turtle = []
pos_x = [-210, -70, 70, 210]
pos_y = [-250, -110, 30, 170]

for x in range(4):
  for y in range(4):
    new_turtle = t.Turtle()
    new_turtle.up()
    new_turtle.color("pink")
    new_turtle.speed(0)
    new_turtle.goto(pos_x[x], pos_y[y])
    turtle.append(new_turtle)

default_img ="images/default_img.gif"
t.addshape(default_img)

img_list = []
for i in range(8):
  img = f"images/img{i}.gif"
  t.addshape(img)
  img_list.append(img)
  img_list.append(img)

random.shuffle(img_list)
for i in range(16):
  turtle[i].shape(img_list[i])

time.sleep(3)

for i in range(16):
  turtle[i].shape(default_img)

click_num = 0 # 클릭 횟수 (매 2회 클릭마다 정답 체크)
score = 0 # 점수
attempt = 0 # 시도한 횟수
first_pick = "" # 첫번째 이미지 클릭
second_pick = "" # 두번째 이미지 클릭

t.onscreenclick(play)




t.mainloop()