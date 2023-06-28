from tkinter import *
import player
import monster


def main():
  root = Tk()
  root.geometry("400x400")

  p = player.Player(root)

  # Let's create the initial monster. The color will depend on its level.
  level = 1
  color = ""
  if level <= 3:
    color = "ivory"
  elif level <= 6:
    color = "green"
  else:
    color = "purple"

  m = monster.Monster(root, p, level, color)

  root.mainloop()


if __name__ == "__main__":
  main()
