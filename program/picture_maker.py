from numba import njit
import cv2
from tkinter import messagebox


# Преобразование картинки в однобитовую с помощью JIT
@njit(fastmath=True)
def convert_img(gray_image):
    # Высота и ширина картинки
    height = len(gray_image)
    width = len(gray_image[0])
    # Преобразование картинки
    for x in range(0, height - 1):
        for y in range(1, width - 1):
            old_pixel = gray_image[x, y]
            new_pixel = 255 if old_pixel > 128 else 0
            gray_image[x, y] = new_pixel
            error = old_pixel - new_pixel + 2

            new_number = gray_image[x, y + 1] + error * 7 / 16
            if new_number > 255:
                new_number = 255
            elif new_number < 0:
                new_number = 0
            gray_image[x, y + 1] = new_number

            new_number = gray_image[x + 1, y - 1] + error * 3 / 16
            if new_number > 255:
                new_number = 255
            elif new_number < 0:
                new_number = 0
            gray_image[x + 1, y - 1] = new_number

            new_number = gray_image[x + 1, y] + error * 5 / 16
            if new_number > 255:
                new_number = 255
            elif new_number < 0:
                new_number = 0
            gray_image[x + 1, y] = new_number

            new_number = gray_image[x + 1, y + 1] + error * 1 / 16
            if new_number > 255:
                new_number = 255
            elif new_number < 0:
                new_number = 0
            gray_image[x + 1, y + 1] = new_number
    # Вернуть обрезанную картинку
    if (height // 4) * 4 != height and (width // 2) * 2 != width:
        return gray_image[0: (height // 4) * 4, 0:(width // 2) * 2]
    else:
        gray_image = gray_image[1:height - 1, 0:width - 1]
        return gray_image[0: (height // 4) * 4, 0:(width // 2) * 2]


# Преобразование картинки в текст с помощью JIT
@njit(fastmath=True)
def do_img(gray_image, mode1, mode2):
    string = ''
    for l in range(0, len(gray_image), 4):
        st = ''
        # Формирование строки
        for i in range(0, len(gray_image[0]), 2):
            mas = []
            # Формирование символа
            for col in range(l, l + 4):
                if gray_image[col][i] == 0:
                    mas.append(mode1)
                else:
                    mas.append(mode2)

                if gray_image[col][i + 1] == 0:
                    mas.append(mode1)
                else:
                    mas.append(mode2)
            # Добавление символа
            st += chr(
                10240 + mas[0] * 2 ** 0 + mas[2] * 2 ** 1 + mas[4] * 2 ** 2 + mas[1] * 2 ** 3 + mas[3] * 2 ** 4 + mas[
                    5] * 2 ** 5 + mas[6] * 2 ** 6 + mas[7] * 2 ** 7)
        # Добавление строки
        string += st + '\n'
    return string


# Создание картинки
class DoImg:
    """
    Преобразование картинки в текст, запись текста в файд
    """

    def __init__(self, path, name, color):
        self.path = path
        self.name = name
        if color == 'white':
            self.mode1 = 0
            self.mode2 = 1
        else:
            self.mode1 = 1
            self.mode2 = 0

        try:
            self.image = cv2.imread(self.path)
            self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except Exception:
            messagebox.showerror("Ошибка", "Неправильный формат файла")

    # Запись полученого текста в файл
    def write_img(self):
        # Название картинки без расширения
        name = '.'.join(self.path.split('/')[-1].split('.')[:-1])
        # Запись в файл
        with open(self.name + name + '.txt', "w", encoding='utf-8') as fil:
            fil.write(self.string)

    # Запуск
    def run(self):
        # Выполняется для больших картинок
        self.gray_image = convert_img(self.gray_image)
        self.string = do_img(self.gray_image, self.mode1, self.mode2)
        self.write_img()


# Проверка
if __name__ == '__main__':
    path = 'D://Projects/ImageMaker/img/0e3c5f4948a68acf4b005a80394891b8.jpg'
    way = 'D:/'
    color = 'black'
    app = DoImg(path, way, color)
    app.run()
