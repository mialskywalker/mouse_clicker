import mouse
import time
import tkinter as tk
from tkinter import *
import keyboard


class Window:
    def __init__(self, master):
        self.panel = tk.Frame(master)
        self.panel.grid()
        self.label1 = Label(self.panel)
        self.label1.place(x=0, y=0)
        self.button_quit = tk.Button(self.panel, text="Quit", command=self.panel.quit)
        self.button_quit.grid()
        vcmd = (master.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # x1 data
        self.label_x1 = Label(self.panel, text="Position X1:")
        self.label_x1.grid()
        self.coordinate_x1 = tk.Entry(self.panel, validate='key', validatecommand=vcmd)
        self.coordinate_x1.grid()
        self.coordinate_x1.focus()

        # y1 data
        self.label_y1 = Label(self.panel, text="Position Y1:")
        self.label_y1.grid()
        self.coordinate_y1 = tk.Entry(self.panel, validate='key', validatecommand=vcmd)
        self.coordinate_y1.grid()

        # x2 data
        self.label_x2 = Label(self.panel, text="Position X2:")
        self.label_x2.grid()
        self.coordinate_x2 = tk.Entry(self.panel, validate='key', validatecommand=vcmd)
        self.coordinate_x2.grid()

        # y2 data
        self.label_y2 = Label(self.panel, text="Position X1:")
        self.label_y2.grid()
        self.coordinate_y2 = tk.Entry(self.panel, validate='key', validatecommand=vcmd)
        self.coordinate_y2.grid()

        # sleep
        self.sleep = Label(self.panel, text="Sleep:")
        self.sleep.grid()
        self.sleep = tk.Entry(self.panel, validate='key', validatecommand=vcmd)
        self.sleep.grid()

        self.button_start = tk.Button(self.panel, text="Start", command=self.mouse_click)
        self.button_start.grid()

    def get_text(self):
        return [
            self.coordinate_x1.get(),
            self.coordinate_y1.get(),
            self.coordinate_x2.get(),
            self.coordinate_y2.get(),
            self.sleep.get()
        ]

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def mouse_click(self):
        count = 0
        coordinate_a, coordinate_b, coordinate_c, coordinate_d, sleep = self.get_text()
        while True:
            try:
                mouse.move(coordinate_a, coordinate_b)
                mouse.click('left')
                mouse.move(coordinate_c, coordinate_d)
                mouse.click('left')
                count += 2
                time.sleep(float(sleep))
                if keyboard.is_pressed('`'):
                    print(count)
                    break
            except EnvironmentError:
                break


root = tk.Tk()
Window(root)
root.mainloop()
