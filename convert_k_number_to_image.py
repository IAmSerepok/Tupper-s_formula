import pygame as pg

class App:
    """Класс для визуализации числа с помощью формулы Таппера.
    
    Приложение отображает бинарное представление числа (0 и 1) из файла 'k_number.txt'
    в виде черно-белой сетки, где каждый бит представлен квадратом заданного размера.

    Attributes:
        columns (int): Количество столбцов в сетке.
        rows (int): Количество строк в сетке.
        scale (int): Размер стороны квадрата (в пикселях) для отображения одного бита.
        screen_size (tuple): Размеры окна (ширина, высота) в пикселях.
        image (str): Бинарная строка для визуализации.
        surface (pg.Surface): Основная поверхность для отрисовки.
        clock (pg.time.Clock): Таймер для контроля частоты кадров.
    """

    def __init__(self, columns: int = 106, rows: int = 17, scale: int = 10) -> None:
        """Инициализирует приложение с заданными параметрами отображения.
        
        Args:
            columns (int): Количество столбцов в сетке (рекомендуется 106 для стандартного файла).
            rows (int): Количество строк в сетке (рекомендуется 17 для стандартного файла).
            scale (int): Масштаб отрисовки одного бита в пикселях.
        """
        pg.init()
        self.columns, self.rows = columns, rows
        self.scale = scale
        self.screen_size = self.screen_width, self.screen_height = self.scale * self.columns, self.scale * self.rows
        self.image = self.__convert()
        self.surface = pg.display.set_mode(self.screen_size)
        self.clock = pg.time.Clock()

    @staticmethod
    def __convert() -> str:
        """Конвертирует число из файла в бинарную строку фиксированной длины.
        
        Returns:
            binary_string (str): Бинарная строка длиной 1802 символа (106*17), дополненную ведущими нулями при необходимости.
        """
        with open('k_number.txt', 'r') as f:
            k = int(f.read())
            k //= 17
            binary = bin(k)[2:]
            binary = ("0" * (1802 - len(binary))) + binary
        return binary

    def __draw(self) -> None:
        """Отрисовывает бинарную сетку на экране.
        
        Каждый бит представляется квадратом:
        - '1' -> черный квадрат
        - '0' -> белый квадрат
        """
        self.surface.fill('white')
        for x in range(self.columns):
            for y in range(self.rows):
                numb = int(self.image[len(self.image) - x*17 - y - 1])
                col = 'white'
                if numb:
                    col = 'black'
                size = self.scale
                pg.draw.rect(self.surface, col, (x * size, (self.rows - y - 1) * size, size, size))

    def run(self) -> None:
        """Запускает основной цикл приложения."""
        self.__draw()
        pg.display.flip()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            self.clock.tick()


if __name__ == "__main__":  # Пример использования
    app = App()
    app.run()
