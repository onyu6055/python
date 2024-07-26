art = """
            S     S
        S        S
       S    S      S
        S     S  S
  **********************  **
   **                **  ***
     **   Coffee   ** ****
       **        ** ***
          ******
"""

menu = """
      커피 자판기 메뉴

  1. 아메리카노     1,800원
  2. 카페라떼       2,700원
  3. 핫초코         2,300원
"""

print(art)
print(menu)
print("=" * 50)

coffee_price = 0

order = int(input("커피 종류를 선택하세요. (1, 2, 3) : "))

if 1 <= order <=3:
  if order == 1:
   coffee_price = 1800
  elif order == 2:
    coffee_price = 2700
  elif order == 3:
    coffee_price = 2300

  cups = int(input("몇 잔을 드릴까요? : "))

  total_price = coffee_price * cups

  received = int(input(f"총 금액은 {total_price}원입니다. 돈을 투입해주세요 : "))

  if received >= total_price:
    change = received - total_price
    print(f"{received}원을 받았습니다. 거슴름돈은 {change}원 입니다")

    change_1000 = change // 1000
    remain_1000 = change % 1000
    change_500 = remain_1000 // 500
    remain_500 = remain_1000 % 500
    change_100 = remain_500 // 100

    print(f"(1000원 지폐 {change_1000}장, 500원 동전 {change_500}개, 100원 동전 {change_100}개)")
    print()
    print("맛있게 드세요~~")
  else:
    print("금액이 부족합니다. 주분이 취소되었습니다.")

else:
  print("잘못된 주문입니다. 다시 확인해 주세요.")