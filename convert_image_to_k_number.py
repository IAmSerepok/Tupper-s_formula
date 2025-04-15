import pygame as pg
from math import floor


class App:
    """Конвертатор изображений в сид для формулы Таппера.

    Attributes:
        columns (int): Количество столбцов в сетке.
        rows (int): Количество строк в сетке.
        scale (int): Размер одного элемента сетки в пикселях.
        screen_size (tuple): Размеры окна (ширина, высота) в пикселях.
        image (list[int]): Массив бинарных значений (0 или 1) для отображения.
        surface (pg.Surface): Основная поверхность для отрисовки.
        clock (pg.time.Clock): Таймер для контроля частоты кадров.
    """

    def __init__(self, columns: int = 106, rows: int = 17, scale: int = 10) -> None:
        """Инициализирует редактор с заданными параметрами сетки.

        Args:
            columns (int): Количество столбцов.
            rows (int): Количество строк.
            scale (int): Размер элемента сетки в пикселях.
        """
        pg.init()
        self.columns, self.rows = columns, rows
        self.scale = scale
        self.screen_size = self.screen_width, self.screen_height = self.scale * self.columns, self.scale * self.rows
        self.image = [0 for _ in range(self.columns) for _ in range(self.rows)]
        self.surface = pg.display.set_mode(self.screen_size)
        self.clock = pg.time.Clock()

    def __convert(self) -> int:
        """Конвертирует бинарную сетку в числовое значение.

        Returns:
            seed (int): Числовой сид изображения для формулы Таппера
        """
        binary = ""
        for x in range(self.columns):
            for y in range(self.rows):
                binary += str(self.image[x * 17 + y])
        return int(binary, 2) * 17

    def __write(self) -> None:
        """Сохраняет текущее состояние сетки в файл 'k_number.txt'."""
        with open('k_number.txt', 'w') as f:
            f.write(str(self.__convert()))

    def __draw(self) -> None:
        """Отрисовывает текущее состояние сетки на экране."""
        self.surface.fill('white')
        for x in range(self.columns):
            for y in range(self.rows):
                numb = self.image[len(self.image) - x * 17 - y - 1]
                col = 'black' if numb else 'white'
                pg.draw.rect(
                    self.surface, 
                    col, 
                    (x * self.scale, (self.rows - y - 1) * self.scale, 
                    self.scale, self.scale)
                )
    
    def __get_cords(self, pos: tuple[int, int]) -> tuple[int, int]:
        """Конвертирует экранные координаты в координаты сетки.

        Args:
            pos (Typle[int, int]): Координаты мыши (x, y) в пикселях.

        Returns:
            new_cords (Typle[int, int]): Координаты (column, row) в сетке.
        """
        x, y = pos
        return floor(x / self.screen_width * self.columns), floor(y / self.screen_height * self.rows)

    def run(self) -> None:
        """Запускает основной цикл приложения с обработкой событий."""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = self.__get_cords(event.pos)
                    if event.button == 1:  # ЛКМ
                        idx = (self.columns - x - 1) * 17 + y
                        self.image[idx] = int(not self.image[idx])
                    elif event.button == 2:  # СКМ
                        self.__write()

            self.__draw()
            pg.display.flip()
            self.clock.tick()


if __name__ == "__main__":  # Пример использования
    app = App()
    app.run()
