from tkinter import *
import random
import time
import math

class Player:
    def __init__(self, root, inventory):
        self.root = root
        self.inventory = inventory
        self.level = 1
        self.exp = 0
        self.max_exp = self.calculate_max_exp(self.level)
        self.health = 100
        self.mana = 50
        self.gold = 0
        self.attack_speed = 1

        self.weapons = []
        for v in inventory.itemList:
            if (v.type == 'WEAPON'):
                self.weapons.append(v)
            elif (v.type == 'GOLD'):
                self.gold = v.price

        print(self.weapons[0].damage)

        # self.weapons = [{"name": "dagger", "damage": range(1, 4), "attack_speed": 0.2  * self.attack_speed},
        #                 {"name": "one-handed sword", "damage": range(4, 7), "attack_speed": 0.35  * self.attack_speed},
        #                 {"name": "two-handed sword", "damage": range(7, 11), "attack_speed": 0.8  * self.attack_speed}
        #                 ]
        self.current_weapon = self.weapons[0]

        print(self.current_weapon.name)
    
        self.level_label = Label(root, text=f"Level: {self.level} (exp: {self.exp} max: {self.max_exp}), Weapon: +{self.current_weapon.level} {self.current_weapon.name}", font=("Arial", 10))
        self.level_label.place(x=10, y=310)

        self.gold_label = Label(root, text=f"Gold: {self.gold}", font=("Arial", 10))
        self.gold_label.place(x=10, y=295)

        self.health_bar = Canvas(root, width=100, height=15, bg="#CB4335")
        self.health_bar.place(x=10, y=330)
        self.health_bar_text = self.health_bar.create_text(55, 10, text=f'{self.health}', fill='white', font=("Arial", 10))

        self.mana_bar = Canvas(root, width=100, height=15, bg="#2E86C1")
        self.mana_bar.place(x=10, y=350)
        self.mana_bar_text = self.mana_bar.create_text(55, 10, text=f'{self.mana}', fill='white', font=("Arial", 10))

        self.last_click_time = time.time() - 1.0

        # self.weapon_upgrade_boxes = []
        # for i, weapon in enumerate(self.weapons):
        #     upgrade_box = Button(root, text=f"U {weapon['name']} ({self.weapon_upgrades[i]})", command=lambda i=i: self.upgrade_weapon(i))
        #     upgrade_box.place(x=10, y = 10 + i * 30)
        #     self.weapon_upgrade_boxes.append(upgrade_box)

        # root.bind("<Key>", self.change_weapon)

    # def change_weapon(self, event):
    #     self.health_bar.itemconfigure(self.health_bar_text, text = f'{self.health}')
    #     self.mana_bar.itemconfigure(self.mana_bar_text, text = f'{self.mana}')
    #     if event.char == '1':
    #         self.current_weapon = self.weapons[0]
    #     elif event.char == '2':
    #         self.current_weapon = self.weapons[1]
    #     elif event.char == '3':
    #         self.current_weapon = self.weapons[2]
    #     self.level_label.config(text=f"Level: {self.level} (exp: {self.exp} max: {self.max_exp}), Weapon: {self.current_weapon['name']}")

    def item_click(self, event, t):
        print(t.name)

    def attack(self):
        delay = self.current_weapon.attackSpeed * self.attack_speed
        if time.time() - self.last_click_time >= delay:
            self.last_click_time = time.time()
            damage = random.choice(self.current_weapon.damage)
            maxDamage = max(self.current_weapon.damage)
            doubleHit = random.randint(0, 5) > 3 and damage == maxDamage
            if doubleHit:
                damage = damage * 2
            return damage, doubleHit
        else:
            return 0, 0
     
    def calculate_max_exp(self, level):
        return 10 * math.factorial(level)

    def gain_exp(self, amount):
        self.health_bar.itemconfigure(self.health_bar_text, text = f'{self.health}')
        self.mana_bar.itemconfigure(self.mana_bar_text, text = f'{self.mana}')
        self.exp += amount
        self.level_label.config(text=f"Level: {self.level} (exp: {self.exp} max: {self.max_exp}), Weapon: +{self.current_weapon.level} {self.current_weapon.name}")
        while self.exp >= self.max_exp:
            self.level_up()

    def gain_damage(self, amout):
        self.health -= amout
        if (self.health < 0):
            print("DIE")
        else:
            print("AAA")

    def level_up(self):
        self.level += 1
        self.exp -= self.max_exp
        self.max_exp = self.calculate_max_exp(self.level)
        self.level_label.config(text=f"Level: {self.level} (exp: {self.exp} max: {self.max_exp}), Weapon: +{self.current_weapon.level} {self.current_weapon.name}")
        self.health += self.level * 10
        self.mana += self.level * 5
        self.health_bar.itemconfigure(self.health_bar_text, text = f'{self.health}')
        self.mana_bar.itemconfigure(self.mana_bar_text, text = f'{self.mana}')

    def gain_gold(self, amount):
        self.health_bar.itemconfigure(self.health_bar_text, text = f'{self.health}')
        self.mana_bar.itemconfigure(self.mana_bar_text, text = f'{self.mana}')
        self.gold += amount
        self.gold_label.config(text=f"Gold: {self.gold}")

    def upgrade_weapon(self, weapon_index):
        upgrade_cost = 100
        if self.gold >= upgrade_cost:
            self.gold -= upgrade_cost
            self.weapon_upgrades[weapon_index] += 1
            self.weapons[weapon_index]['damage'] = range(
            self.weapons[weapon_index]['damage'].start + 1,
            self.weapons[weapon_index]['damage'].stop + 1)
            self.weapon_upgrade_boxes[weapon_index].configure(
                text=f"U {self.weapons[weapon_index]['name']} ({self.weapon_upgrades[weapon_index]})"
            )
            self.gold_label.config(text=f"Gold : {self.gold}")