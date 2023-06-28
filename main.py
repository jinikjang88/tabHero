from tkinter import *
import player
import monster
import item
import daggerItem
import inventory

def main():
    root = Tk()
    root.geometry("400x400")

    ## 최초 시작 시 단검과, 돈 1000원을 준다.
    firstDagger = daggerItem.DaggerItem(root, 0, "WEAPON", "단검", 1, 100, True, range(1, 4), 0.2)
    secondDagger = daggerItem.DaggerItem(root, 0, "WEAPON", "단검1", 1, 100, FALSE, range(1, 4), 0.2)
    firstMoney = item.Item(root, 0, "GOLD", "GOLD", 1_000, 1, False, range(0))
    ## 인벤토리에 담고
    initItemList = [firstMoney, firstDagger, secondDagger]
    myInventory = inventory.Invetory(root, initItemList)
  
    ## 플레이어에게 넘겨준다
    p = player.Player(root, myInventory)

    ## 최초 시작 시 몬스터 레벨
    ## TODO 레벨별 던전을 선택할 수 있게 한다. 
    level = 1
    color = "ivory"

    m = monster.Monster(root, p, level, color)

    root.mainloop()

if __name__ == "__main__":
    main()
