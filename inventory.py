from tkinter import *

class Invetory:
    def __init__(self, root, itemList):
        self.root = root
        self.itemList = itemList
    
    def getItemList(self):
        print('그냥 아이템임' + self.itemList)