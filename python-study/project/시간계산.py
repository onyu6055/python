print("초를 입력하면, 시간과 분으로 변화합니다.")

sec = int(input("초를 입력하세요 : "))

h = sec // (60 * 60)
r = sec % (60 * 60)
m = r // 60
s = sec % 60

print(f"입력하신 {sec}초는 {h}시 {m}분 {s}초 입니다.")