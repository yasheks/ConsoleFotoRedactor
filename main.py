GeekPaste
 
from PIL import Image
from Filters import grey, noisily, two_colors, hype, four_colors, mirror_image, pasta, rectangle, curtains
while True:
    print("Добро пожаловать в консольный фоторедактор.")

    # путь к файлу
    path = input("Введите путь к картинке, которую хотите изменить: ")

    # открываем изображение и на всякий случай преобразуем его в RGB - чтобы работало с png и gif
    img = Image.open(path).convert("RGB")

    print("Какой фильтр вы хотите применить?")
    print("1 - градации серого")
    print("2 - цветовой шум")
    print("3 - яркостный шум")
    print("4 - использование всего двух цветов")
    print("5 - разделение фотографии на 4 части, где в каждой части свой цвет")
    print("6 - отзеркаленное изображение по вертикали")
    print("7- разрезанное изображение на вертикальные полоски, ширину которуых выбирает пользователь")
    print("8 - разделение картинки на прямоугольники, котоые будут идти к центру переворачиваясь, кол-во которых выбирает пользователь")
    print("9 - шторы из одного пикселя в высоту, которое будет закрывать столько процентов картинки снизу которое выберит пользователь")
    # запрашиваем номер фильтра
    choice = input("Выберите фильтр: ")

    # если нажали 1 - применяем градации серого
    if choice == "1":
        grey(img)

    # если нажали 2 - шум
    if choice == "2":
        hype(img)

    if choice == "3":
        noisily(img)

    if choice == "4":
        two_colors(img)

    if choice == "5":
        four_colors(img)
    if choice == "6":
        mirror_image(img)
    if choice == "7":
        pasta(img)
        continue
    if choice ==  "8":
        rectangle(img)
    if choice == "9":
        curtains(img)

    


    # спрашиваем куда сохранить результат
    save_path = input("Куда сохранить: ")
    print("загрузка")

    # сохраняем
    img.show()
    img.save(save_path)
