print("Введите один из цветов:")

while True:
    print("1 - Красный")
    print("2 - Синий")
    print("3 - Желтый")
    color = input("Впишите название или цифру выбранного цвета: ")
    SecondColor = input("Впишите название или цифру вторичного цвета: ")
    if color == "Красный" or "1" and SecondColor == "Синий" or "2":
        print("В результате смешивания получится фиолетовый")
        break
    elif color == "Красный" or "1" and SecondColor == "Желтый" or "3":
        print("В результате смешивания получится оранжевый")
        break
    elif color == "Синий" or "2" and SecondColor == "Желтый" or "3":
        print("В результате смешивания получится зеленый")
        break
    else:
        print("Вы ввели некорректное название цвета!")