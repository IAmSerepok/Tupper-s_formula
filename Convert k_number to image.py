import pygame as pg


class App:
    def __init__(self):
        pg.init()
        self.columns, self.rows = 106, 17
        self.scale = 10
        self.screen_size = self.screen_width, self.screen_height = self.scale*self.columns, self.scale*self.rows
        self.image = self.convert()
        self.surface = pg.display.set_mode(self.screen_size)
        self.clock = pg.time.Clock()

        self.speed = 10
        self.time = 0
        self.running = True

    @staticmethod
    def convert():
        with open('k_number', 'r') as f:
            k = int(f.read())
            k //= 17
            binary = bin(k)[2:]
            binary = ("0" * (1802 - len(binary))) + binary

        return binary

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

    def run(self):
        self.draw()
        pg.display.flip()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            self.clock.tick()


app = App()
app.run()
