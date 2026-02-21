while True:
    pass1 = input("Введите пароль: ")

    az = False
    AZ = False
    num = 0
    cnt = len(pass1)

    for i in pass1:
        if "0" <= i <= "9":
            num += 1
        elif "a" <= i <= "z":
            az = True
        elif "A" <= i <= "Z":
            AZ = True

    if az and AZ and num >= 2 and cnt >= 6:
        print("Пароль принят")
        break
    else:
        if cnt < 6:
            print("В пароле должно быть шесть и более символов!")
        if not az:
            print("В пароле должны быть прописные буквы!")
        if not AZ:
            print("В пароле должны быть заглавные буквы!")
        if num < 2:
            print("В пароле должно быть дые и более цифр!")
        print("")
        print("Измените свой пароль соблюдая все замечания")
        print("")

while True:
    pass2 = input("Напишите свой пароль еще раз: ")
    if pass1 == pass2:
        print("Пароли совпадают!")
        break
    else:
        print("Пароли не совпадают!")