# Используемые библиотеки
from tkinter import *
from tkinter import filedialog

# Параметры
color_back = '#4c5eaa'
color_front = '#ffffff'
color_text_label = '#ffffff'
color_text_button = '#000000'
color_text_entry = '#000000'
text_label = 'Comic Sans MS'
text_button = 'Comic Sans MS'
text_entry = 'Verdana'


# Главное окно
class MainWindow:
    """
    Создание гравного окна графического интерфейса
    """

    # Графический интерфейс
    def __init__(self, root, data_file):
        # Настройки окна
        self.data_file = data_file
        self.root = root
        self.root.title("ImageMaker")
        self.root.geometry('300x450+200+180')
        self.root.configure(background='#b8b8b8')
        self.root.resizable(False, False)
        self.frame = Frame(root, bg=color_back)
        self.frame.place(width=300, height=450)
        self.data_file['img'] = ''

        # Кнопка переключения на настройки
        Button(self.frame,
               text='⚙',
               fg=color_text_button,
               relief=SUNKEN,
               bg=color_front,
               bd=0, borderwidth=0,
               highlightthickness=0,
               highlightcolor="#aaaaaa",
               highlightbackground="#009588",
               activebackground='#6777ca',
               command=self.go_customization,
               font=(text_button, 10),
               ).place(x=240, y=250, width=25, height=25)

        # Строка для ввода
        self.ent = Text(self.frame,
                        bg=color_front,
                        fg=color_text_entry,
                        bd=0,
                        font=(text_entry, 12),
                        highlightthickness=0,
                        selectbackground='#b4b6e2',
                        padx=10,
                        pady=5,
                        )
        self.ent.place(x=30, y=30, width=240, height=200)

        # Кнопка для указания расположения картики
        Button(self.frame,
               text='Обзор',
               fg=color_text_button,
               relief=SUNKEN,
               bg=color_front,
               bd=0, borderwidth=0,
               activebackground='#6777ca',
               command=self.get_loc,
               font=(text_button, 11),
               ).place(x=30, y=250, width=110)

        # Кнопка создания картинки из текста
        self.but = Button(self.frame,
                          text='СОЗДАТЬ',
                          fg=color_text_button,
                          font=(text_button, 15),
                          relief=SUNKEN,
                          bg=color_front,
                          bd=0, borderwidth=0,
                          activebackground='#6777ca',
                          command=self.do_img,
                          )
        self.but.place(x=50, y=375, width=200, height=50)

        self.customization = Customization(master=self.root, app=self, data_file=self.data_file)

    # Получение расположения картинки
    def get_loc(self):
        f = filedialog.askopenfilename()
        if f != '':
            self.ent.delete(1.0, END)
            self.ent.insert(1.0, f)

    # Вызывавется при нажатии на кнопку СОЗДАТЬ
    def do_img(self):
        pass

    # Вызывается при нажатии кнопки сохранить
    def go_maimwindow(self):
        self.frame.place(width=300, height=450)

    # Переключение на настройки
    def go_customization(self):
        self.frame.place_forget()
        self.customization.go_customization()


# Окно настроек
class Customization:
    """
    Создание окна настроек граффического интерфейса
    """

    # Графический интерфейс
    def __init__(self, master, app, data_file):
        self.data_file = data_file
        self.master = master
        self.app = app
        self.frame = Frame(self.master, bg=color_back)

        # Надпись ПУТЬ СОХРАНЕНИЯ
        Label(self.frame,
              text='ПУТЬ СОХРАНЕНИЯ',
              bg=color_back,
              fg=color_text_label,
              font=(text_label, 11),
              ).place(x=25, y=25)

        # Строка для ввода пути сохранения
        self.locEntry = Text(self.frame,
                             bg=color_front,
                             fg=color_text_entry,
                             bd=0,
                             font=(text_entry, 10),
                             highlightthickness=0,
                             padx=10,
                             pady=5,
                             selectbackground='#b4b6e2'
                             )
        self.locEntry.place(x=25, y=55, width=250, height=58)

        # Кнопка для указания пути сохранения
        Button(self.frame,
               text='Обзор',
               fg=color_text_button,
               relief=SUNKEN,
               bg=color_front,
               bd=0, borderwidth=0,
               activebackground='#6777ca',
               command=self.get_loc,
               font=(text_button, 10),
               ).place(x=25, y=125, width=110, height=25)

        # Надпись ИНВЕРСИЯ ЦВЕТА
        Label(self.frame,
              text='ИНВЕРСИЯ ЦВЕТА',
              bg=color_back,
              fg=color_text_label,
              font=(text_label, 11),
              ).place(x=25, y=170)

        # Надпись БЕЛЫЙ НА ЧЕРНОМ и ЧЕРНЫЙ НА БЕЛОМ
        self.white_and_black = Label(self.frame,
                                     font=(text_label, 11),
                                     )
        self.white_and_black.place(x=25, y=200, width=190, height=40)

        # Кнопка для смены цвета
        Button(self.frame,
               text='Изменить',
               command=self.impl_1,
               font=(text_button, 10),
               fg=color_text_button,
               relief=SUNKEN,
               bg=color_front,
               bd=0, borderwidth=0,
               activebackground='#6777ca',
               ).place(x=25, y=250, width=110, height=25)

        # Надпись О ПРОЕКТЕ
        Label(self.frame,
              text='О ПРОЕКТЕ',
              bg=color_back,
              fg=color_text_label,
              font=(text_label, 11),
              ).place(x=25, y=300)

        # Кнопка для просмотра инструкций
        Button(self.frame,
               text='Посмотреть',
               font=(text_button, 10),
               fg=color_text_button,
               relief=SUNKEN,
               bg=color_front,
               bd=0, borderwidth=0,
               activebackground='#6777ca',
               command=self.go_about,
               ).place(x=25, y=330, width=110, height=25)

        # Кнопка сохранения настроек и перехода на главное окно
        Button(self.frame,
               text='СОХРАНИТЬ',
               command=self.go_mainwindow,
               font=(text_button, 14),
               fg=color_text_button,
               relief=SUNKEN,
               bg=color_front,
               bd=0, borderwidth=0,
               activebackground='#6777ca',
               ).place(x=50, y=375, width=200, height=50)

        # Добавление в строку ввода пути сохранения путь, который был указан при закрытии программы
        try:
            self.locEntry.insert(1.0, self.data_file['way'])
        except Exception:
            pass

        # Добавление цвета, который был указан при закрытии программы
        if not ('color' in self.data_file):  # Если цвета нету
            self.white_and_black['text'] = 'Черный на белом'
            self.white_and_black['bg'] = '#ffffff'
            self.white_and_black['fg'] = '#000000'
            self.data_file['color'] = 'black'
        elif self.data_file['color'] == 'black':  # Если черный на белом
            self.white_and_black['text'] = 'Черный на белом'
            self.white_and_black['bg'] = '#ffffff'
            self.white_and_black['fg'] = '#000000'
        elif self.data_file['color'] == 'white':  # Если белый на черном
            self.white_and_black['text'] = 'Белый на черном'
            self.white_and_black['bg'] = '#000000'
            self.white_and_black['fg'] = '#ffffff'

    # Получение пути сохранения
    def get_loc(self):
        f = filedialog.askdirectory()
        if f != "":
            self.locEntry.delete(1.0, END)
            self.locEntry.insert(1.0, f)

    # Переключение с черного на белый и с белого на черный
    def impl_1(self):
        if self.data_file['color'] == 'white':
            self.white_and_black['text'] = 'Черный на белом'
            self.white_and_black['bg'] = '#ffffff'
            self.white_and_black['fg'] = '#000000'
            self.data_file['color'] = 'black'
        elif self.data_file['color'] == 'black':
            self.white_and_black['text'] = 'Белый на черном'
            self.white_and_black['bg'] = '#000000'
            self.white_and_black['fg'] = '#ffffff'
            self.data_file['color'] = 'white'

    # Сохранение настроек и переход на главное окно
    def go_mainwindow(self):
        way = self.locEntry.get(1.0, END).rstrip().rstrip('/') + '/'
        if way != '/':
            self.data_file['way'] = way
        else:
            self.data_file['way'] = ''
        self.frame.place_forget()
        self.app.go_maimwindow()

    # Вызывается при нажатии кнопки настроек
    def go_customization(self):
        self.frame.place(width=300, height=450)

    # Переход в инструкцию
    def go_about(self):
        self.frame.place_forget()
        About(master=self.master, app=self).go_about()


# Окно с инструкцией
class About:
    """
    Создание окна с инструкцией
    """

    # Графический интерфейс
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.frame = Frame(self.master, bg=color_back)
        # Текст
        instruction = """
Это приложение создано для того, чтобы переводить изображение в текст. 
Для начала пользования нужно зайти в настройки, указать путь сохранения и задать инверсию цвета. 
После этого нужно нажать на кноку СОХРАНИТЬ. 
После перехода на главное окно приложения необходимо указать путь к картинке, которую вы хотите перевести в текст, и нажать на кнопку СОЗДАТЬ.
        """

        # Текст инструкции
        Label(self.frame,
              text=instruction,
              bg=color_back,
              fg=color_text_label,
              font=(text_label, 10),
              justify=LEFT,
              wraplength=250,
              ).place(x=25, y=0, width=250)

        # Переход в настройки
        Button(self.frame,
               text='НАЗАД',
               command=self.go_customization,
               font=(text_button, 15),
               fg=color_text_button,
               relief=SUNKEN,
               bg=color_front,
               bd=0, borderwidth=0,
               activebackground='#b4b6e2',
               ).place(x=50, y=380, width=200, height=40)

    # Переход в настройки
    def go_customization(self):
        self.frame.place_forget()
        self.app.go_customization()

    # Вызывается при нажатии кнопки О ПРОЕКТЕ
    def go_about(self):
        self.frame.place(x=0, y=0, width=300, height=450)


# Проверка
if __name__ == '__main__':
    data_file = {"img": "", "color": "black", "way": "C:/Users/R/Desktop/"}
    root = Tk()
    app = MainWindow(root, data_file)
    root.mainloop()
