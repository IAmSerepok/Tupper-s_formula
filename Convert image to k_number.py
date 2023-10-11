import pygame as pg
from math import floor


class App:
    def __init__(self):
        pg.init()
        self.columns, self.rows = 106, 17
        self.scale = 10
        self.screen_size = self.screen_width, self.screen_height = self.scale*self.columns, self.scale*self.rows
        self.image = [0 for i in range(self.columns) for j in range(self.rows)]
        self.surface = pg.display.set_mode(self.screen_size)
        self.clock = pg.time.Clock()

    def convert(self): #correct
        binary = ""
        for x in range(self.columns):
            for y in range(self.rows):
                binary += str(self.image[x*17 + y])
        height = int(binary, 2) * 17
        print(height)
        return height

    def write(self):
        with open('k_number', 'w') as f:
            f.write(str(self.convert()))

    def draw(self):
        self.surface.fill('white')
        for x in range(self.columns):
            for y in range(self.rows):
                numb = int(self.image[len(self.image) - x*17 - y - 1])
                col = 'white'
                if numb:
                    col = 'black'
                size = self.scale
                pg.draw.rect(self.surface, col, (x * size, (self.rows - y - 1) * size, size, size))

    def get_cords(self, pos):
        x, y = pos
        x = floor(x/self.screen_width*self.columns)
        y = floor(y/self.screen_height*self.rows)
        return x, y

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = self.get_cords(event.pos)
                    if event.button == 1:
                        self.image[(self.columns - x - 1)*17 + y] = int(not self.image[(self.columns - x - 1)*17 + y])
                    elif event.button == 2:
                        self.write()

            self.draw()
            pg.display.flip()
            self.clock.tick()


app = App()
app.run()
