import tkinter as tk
import random
import time

# 게임 변수 초기화
player_level = 1
player_health = 100
player_mana = 100
player_attack_power = 5

monster_level = 1
monster_health = random.randint(10, 20) * 100
monster_color = "ivory"

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("게임")
window.geometry("400x400")

# 플레이어 UI 구성
player_level_label = tk.Label(window, text=f"레벨: {player_level}", font=("Arial", 10))
player_level_label.place(x=10, y=350, anchor="w")

player_health_bar = tk.Canvas(window, width=100, height=10, bg="red")
player_health_bar.place(x=10, y=370, anchor="w")
player_health_bar.create_rectangle(0, 0, 100, 10, fill="red")

player_mana_bar = tk.Canvas(window, width=100, height=10, bg="blue")
player_mana_bar.place(x=10, y=380, anchor="w")
player_mana_bar.create_rectangle(0, 0, 100, 10, fill="blue")

player_width = 30
player_height = 60
player_x = 200 - player_width/2
player_y = 200 - player_height/2
player = tk.Canvas(window, width=player_width, height=player_height, bg="blue")
player.place(x=player_x, y=player_y)

# 몬스터 생성 함수
def create_monster():
    global monster_level, monster_health, monster_color

    monster_level = random.randint(1, 10)
    if monster_level <= 3:
        monster_health = random.randint(10, 20) * 100
        monster_color = "ivory"
    elif monster_level <= 6:
        monster_health = random.randint(30, 50) * 100
        monster_color = "green"
    else:
        monster_health = random.randint(60, 100) * 100
        monster_color = "purple"

    monster_width = 30
    monster_height = 60
    monster_x = 200 + player_width/2
    monster_y = 200 - monster_height/2
    monster = tk.Canvas(window, width=monster_width, height=monster_height, bg=monster_color)
    monster.place(x=monster_x, y=monster_y)

    monster_health_bar = tk.Canvas(window, width=monster_width, height=10, bg="red")
    monster_health_bar.place(x=monster_x, y=monster_y - 13)

    return monster, monster_health_bar, monster_width

# 몬스터 클릭 이벤트 핸들러
def handle_monster_click(event, monster_width):
    global monster_health

    monster.config(bg="red")
    window.after(500, lambda: monster.config(bg=monster_color))

    player_attack = random.randint(1, 7)
    monster_health -= player_attack

    if monster_health <= 0:
        monster.destroy()
        monster_health_bar.destroy()
        window.after(1000, create_monster)
    else:
        monster_health_bar_width = monster_width * (monster_health / (monster_level * 10))  # 체력바 너비 계산
        monster_health_bar.coords(1, 0, 0, monster_health_bar_width, 10)

# 몬스터 생성
monster, monster_health_bar, monster_width = create_monster()

# 몬스터 클릭 이벤트 바인딩
monster.bind("<Button-1>", lambda event: handle_monster_click(event, monster_width))

window.mainloop()
