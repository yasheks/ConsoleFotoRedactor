from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import random
def grey(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))

            average = (r + g + b) // 3

            img.putpixel((i, j), (average, average, average))

def two_colors(img):
    threshold = 127  # ставим порог для бинаризации(подсмотрел эту функцию в инете)



    for i in range(img.width):
        for j in range(img.height):
            # получаем интенсивность серого (grayscale)
            r, g, b = img.getpixel((i, j))

            if (r + g + b)/3 >= threshold:
                img.putpixel((i, j), 255)  # условие для белого цвета
            else:
                img.putpixel((i, j), 0)  # условие для черного цвета

def noisily(img):
    enhancer = ImageEnhance.Brightness(img)

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))

            # Случайно уменьшаем или увеличиваем яркость
            diaposon = random.uniform(0.5, 1.5)  # можно изменить диапазон яркостей
            r, g, b = int(r * diaposon), int(g * diaposon), int(b * diaposon)

            img.putpixel((i, j), (r, g, b))

def hype(img):
    def RandomColor():
        return [random.randint(0, 150), random.randint(0, 150), random.randint(0, 150)]

    # Проходим по каждому пикселю и меняем его цвет
    for i in range(img.width):
        for j in range(img.height):
            # Получаем текущий цвет пикселя
            r, g, b = img.getpixel((i, j))

            # Получаем случайные числа для каждого компонента цвета
            random_pixel = RandomColor()

            # Вычисляем новые значения цветов с добавлением случайных чисел
            new_r = r + random_pixel[0]
            new_g = g + random_pixel[1]
            new_b = b + random_pixel[2]

            # Устанавливаем новый цвет пикселя в новом изображении
            img.putpixel((i, j), (new_r, new_g, new_b))

def four_colors(img):
    part_width = img.width // 2
    part_height = img.height // 2

    # Изменяем оттенок только в одной из частей
    for i in range(2):
        for j in range(2):
            # Выделяем область и получаем ее данные
            left = part_width * i
            upper = part_height * j
            right = left + part_width
            lower = upper + part_height
            part = img.crop((left, upper, right, lower))

            # Изменяем оттенок в соответствии с требованиями
            if i == 1 and j == 0:
                pixels = part.load()

                for x in range(part_width):
                    for y in range(part_height):
                        r, g, b = pixels[x, y]
                        # Изменяем оттенок на красный
                        pixels[x, y] = (255, g, b)

            elif i == 0 and j == 1:
                pixels = part.load()

                for x in range(part_width):
                    for y in range(part_height):
                        r, g, b = pixels[x, y]
                        # Изменяем оттенок на синий
                        pixels[x, y] = (r, g, 255)

            elif i == 1 and j == 1:
                pixels = part.load()

                for x in range(part_width):
                    for y in range(part_height):
                        r, g, b = pixels[x, y]
                        # Изменяем оттенок на зеленый
                        pixels[x, y] = (r, 255, b)

            elif i == 0 and j == 0:
                pixels = part.load()

                for x in range(part_width):
                    for y in range(part_height):
                        r, g, b = pixels[x, y]
                        # Изменяем оттенок на розовый
                        pixels[x, y] = (255, g, 255)
            # Заменяем область на измененную
            img.paste(part, (left, upper, right, lower))

def mirror_image(img):
    flipped_image = img.transpose(Image.FLIP_LEFT_RIGHT)
    # обрезаем отзеркаленную фотографию
    LastPart = flipped_image.crop((400, 0, 800, 800))
    # накладываем отзеркаленное изображение во второй половине фотографии
    img.paste(LastPart, (img.width // 2, 0))

def pasta(img):
    strip_width = int(input("Введите ширину полосы в пикселях: "))

    n = 0
    # Определить кол-во повторений выделений полос
    for x in range(0, img.width, strip_width):
        # Извлечь полосу изображения
        strip = img.crop((n, 0, n + strip_width, img.height))

        # Повернуть полосу на 180 градусов
        rotated_strip = strip.rotate(180)
        # вставить полосу
        img.paste(rotated_strip, (x, 0, x + strip_width, img.height))
        n += strip_width

    rotated_img = img.rotate(180)
    rotated_img.show()

def rectangle(img):
    numrectangles = int(input("Введите количество прямоугольников: "))

    x = 0
    y = 0

    # Цикл по количеству прямоугольников
    for i in range(numrectangles):
        # Вырезаем прямоугольник из исходного изображения
        croppedimage = img.crop((int(x), int(y), int(img.width - x), int(img.height - y)))

        # Поворачиваем вырезанный прямоугольник на 180 градусов
        rotatedimage = croppedimage.rotate(180)

        # Вставляем повернутый прямоугольник на исходные координаты
        img.paste(rotatedimage, (int(x), int(y)))

        # Обновляем координаты прямоугольника и уменьшаем размеры
        x += int((1 / (numrectangles * 2)) * img.width)
        y += int((1 / (numrectangles * 2)) * img.height)

def curtains(img):
    dola = int(input("Какую долю картинки вы хотите закрасить? (напишите в процентах): "))

    # расчитвыем нужный процент заполнения
    part = 100 - dola

    # создаем новое изображение с высотой в один пиксель
    one_pixel = img.crop((0, img.height - 1, img.width, img.height))

    # создаем новую ширину и высоту для нового изображения
    new_width = img.width
    new_height = int(img.height - (img.height * part / 100))  # Приводим к целочисленному типу

    # изменяем изображение

    one_pixel = one_pixel.resize((new_width, new_height))

    # накладываем новое изображение снизу вверх, до нужного значения
    img.paste(one_pixel, (0, img.height - new_height))
