menu = ["사과", "당근", "망고"]

while True:
  func = """
  ========== 관리자 모드 ==========
    1. 메뉴 출력하기
    2. 신메뉴 추가하기
    3. 메뉴 삭제하기
    4. 메뉴 이름 변경하기
    5. 관리자 모드 종료하기
  """

  print(func)

  user_input = input("원하는 기능을 선택하세요. : ")

  if user_input == "1": 
    print()
    for i in menu:
      print(f"  {i} 쥬스")
  elif user_input == "2":
    print()
    new_menu = input("새로운 메뉴를 추가하세요. : ")
    menu.append(new_menu)
  elif user_input == "3":
    print()
    remove_menu = input("삭제할 메뉴를 입력하세요. : ")
    menu.remove(remove_menu)
  elif user_input == "4":
    print()
    for i in range(len(menu)):
      print(f"{i}. {menu[i]}")
    print()
    index = int(input("몇번 메뉴를 변경하시겠습니까? : "))
    print()
    new_name = input("변경할 이름을 입력하세요 : ")
    print()
    print(f"{menu[index]} 메뉴를 {new_name}(으)로 변경합니다")

    menu[index] = new_name 
  elif user_input == "5":
    break