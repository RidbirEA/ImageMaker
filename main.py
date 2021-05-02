from program.graphical_interface import *
from program.picture_maker import *
from tkinter import messagebox
import os
import json

# Открытике файла с данными
try:
    # Если файл есть
    with open('data.json', 'r') as file:
        data_file = json.load(file)
except FileNotFoundError:
    # Если файла нет
    with open('data.json', 'w') as file:
        data_file = {"img": "", "way": "", "color": "black"}
        json.dump(data_file, file, indent=3)


# Запуск
class Main(MainWindow):
    # Создание картинки
    def do_img(self):
        self.data_file['img'] = self.ent.get(1.0, END).rstrip()
        if os.path.exists(self.data_file['way']):
            if os.path.isfile(self.data_file['img']):
                img = DoImg(self.data_file['img'], self.data_file['way'], self.data_file['color'])
                img.run()
                del img
            else:
                messagebox.showerror("Ошибка", "Не правильный путь к картинке")
        else:
            messagebox.showerror("Ошибка", "Не правильный путь сохранения")


# Открытике окна
root = Tk()
app = Main(root, data_file)
root.iconbitmap('icon.ico')
root.mainloop()

# Запись в файл всех настроек
with open('data.json', 'w') as file:
    json.dump(data_file, file, indent=3)
