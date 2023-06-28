from tkinter import *
import random
from player import Player

class Monster:
  def __init__(self, root, player: Player, level, color):
    self.root = root
    self.level = level
    self.color = color
    self.max_hp = random.randint(level*10, level*10 + 10)
    self.hp = self.max_hp


    self.hp_bar = Canvas(root, width=40, height=10, bg="red")
    self.hp_bar.place(x=195, y=160)


    self.monster_box = Canvas(root, width=90, height=60, bg=self.color)
    self.monster_box.place(x=180, y=170)

    self.damage_label = Label(root, text="")
    self.damage_label.place(x=195, y=130)

    self.doutbleHit_label = Label(root, text="")
    self.doutbleHit_label.place(x=195, y=100)

    self.player = player
    self.monster_box.bind("<Button-1>", self.monster_click)

  def monster_click(self, event):
    damageValue = self.player.attack()
    damage = damageValue[0];
    doubleHit = damageValue[1];
    if damage > 0:
      dLablex = random.randint(195, 240)
      if dLablex > 235:
        dLabley = random.randint(130, 230)
      else:
        dLabley = random.randint(130, 135)
      self.damage_label.place(x=dLablex, y=dLabley)

      if doubleHit:
        self.doutbleHit_label.config(text="doubleHit")
        self.root.after(300, lambda: self.doutbleHit_label.config(text="") if self.doutbleHit_label.winfo_exists() else None)

      self.hp -= damage
      if self.hp < 0:
        self.hp = 0
      self.hp_bar.config(width=40 * (self.hp / self.max_hp))

      self.damage_label.config(text=f"-{damage}")
      self.root.after(300, lambda: self.damage_label.config(text="") if self.damage_label.winfo_exists() else None)

      if self.hp <= 0:
        self.monster_box.destroy()
        self.hp_bar.destroy()
        self.damage_label.destroy()

        gold_earned = random.randint(10, 100)  # Random gold amount earned
        self.player.gain_gold(gold_earned)  # Gain gold

        self.player.gain_exp(self.level * 10)
        # When the monster is defeated, spawn a new one with a random level.
        level = random.randint(1, 10)
        color = ""
        if level <= 3:
          color = "ivory"
        elif level <= 6:
          color = "green"
        else:
          color = "purple"

        Monster(self.root, self.player, level, color)
