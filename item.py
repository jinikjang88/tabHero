from tkinter import *

class Item:
    def __init__(self, root, level, type, name, count, price, equipment, damage):
        self.root = root
        self.level = level ## 레벨
        self.type = type
        self.name = name
        self.count = count
        self.price = price * count ## 가격
        self.equiqment = equipment ## 장비여부
        self.damage = damage
    
    def work(self):
        print('그냥 아이템임')