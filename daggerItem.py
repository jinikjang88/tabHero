from tkinter import *
import random
import math
import item

class DaggerItem(item.Item):
    def __init__(self, root, level, type, name, count, price, equipment, damage, attackSpeed):
        self.root = root
        self.level = level ## 레벨
        self.type = type
        self.name = name
        self.count = count
        self.price = price * count ## 가격
        self.equiqment = equipment ## 장비여부
        self.damage = damage
        self.attackSpeed = attackSpeed

    def work(self):
        print('단검 아이템임')