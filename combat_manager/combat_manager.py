import tkinter as tk
import numpy as np
import battleMap


class CombatManager(object):
    def __init__(self, battle_map=None):
        self.battle_map = battle_map
        # self.zoom = ((0, 0, 0), (-1, -1, -1))

        self.root = tk.Tk()
        self.root.title("D&D 5e Combat Manager")
        self.root.configure(background='red')

        # Create menubar
        menubar = tk.Menu(self.root)

        submenu_file = tk.Menu(menubar)
        submenu_file.add_command(label='New')
        submenu_file.add_command(label='Open')
        submenu_file.add_command(label='Save')
        submenu_file.add_command(label='Exit')

        menubar.add_cascade(label='File', menu=submenu_file)
        self.root.configure(menu=menubar)

        self.canvas = tk.Canvas(self.root, height=1000, width=1000, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.draw_grid)
        self.canvas.bind('<Key>', self.keypress)
        self.canvas.bind('<Button-1>', self.mouse1Press)
        self.canvas.focus_set()

    def draw_grid(self, event=None):
        c = self.canvas
        w = c.winfo_width()  # Get current width of canvas
        h = c.winfo_height()  # Get current height of canvas
        c.delete('grid_line')  # Will only remove the grid_line

        bm = self.battle_map
        space = min(w//bm.width, h//bm.height) - 2
        x_0 = w//2-space*bm.width//2
        y_0 = h//2-space*bm.height//2
        # Creates all vertical lines
        for i in range(x_0, w-x_0+2, space):
            c.create_line([(i, y_0), (i, h-y_0)], tag='grid_line')

        # Creates all horizontal lines
        for i in range(y_0, h-y_0+2, space):
            c.create_line([(x_0, i), (w-x_0, i)], tag='grid_line')

    def keypress(self, event=None):
        print(event.char)

    def mouse1Press(self, event=None):
        print(event.x, event.y)

    def load_map(self):
        pass

    def create_map(self, width, height, depth):
        self.battle_map = battleMap.BattleMap(
            width=width, height=height, depth=depth)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    bm = battleMap.BattleMap(15, 3, 5)
    main = CombatManager(battle_map=bm)
    main.run()
