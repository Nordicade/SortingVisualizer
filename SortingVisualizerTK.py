#SortingVisualizerTK
import turtle
import pandas as pd
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill = BOTH, expand = 1)
        insertion_button = Button(self, text = "Insertion", command = self.run_insertion_sort)
        insertion_button.place(x = 0, y = 0)
        insertion_button.config(height = 4, width = 24)
        quick_button = Button(self, text = "Quick", command = self.run_insertion_sort)
        quick_button.config(height = 4, width = 24)
        quick_button.place(x = 240, y = 0)
        merge_button = Button(self, text = "Merge", command = self.run_insertion_sort)
        merge_button.place(x = 580, y = 0)
        merge_button.config(height = 4, width = 24)
    def run_insertion_sort(self):
        print("hi")

root = Tk()
root.geometry("1200x800")
canvas = tk.Canvas(master = root, width = 1200, height = 800)
#canvas.pack()
canva = tk.Canvas(root)
line = canva.create_line(0, 0, 150, 150)
app = Window(root)
root.mainloop()
