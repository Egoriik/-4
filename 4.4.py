print("Введите один из цветов:")

while True:
    print("-- Красный")
    print("-- Синий")
    print("-- Желтый")
    color = input("Впишите название выбранного цвета: ")
    SecondColor = input("Впинишите название вторичного цвета: ")
    if color == "Красный" and SecondColor == "Синий":
        print("В результате смешивания получится фиолетовый")
        break
    elif color == "Красный" and SecondColor == "Желтый":
        print("В результате смешивания получится оранжевый")
        break
    elif color == "Синий" and SecondColor == "Желтый":
        print("В результате смешивания получится зеленый")
        break
    else:
        print("Вы ввели неккоректное название цвета!")