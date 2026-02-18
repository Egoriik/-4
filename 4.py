#В целом все утраивает, но хочется добавить повторный ввод пароля(passA)
#Но не совсем понимаю куда его тыкать и через что, была мысль прописать через
#wlile not az and not AZ and num < 2
#после первого else, но код вовсе полетел...

passA = input("Введите пароль: ")
cnt = 0
az = False
AZ = False
num = 0
if len(passA)>=6:
    for i in passA:
        if "a" <= i <= "z":
            az = True
        elif "A" <= i <= "Z":
            AZ = True
        elif "0" <= i <= "9":
            num += 2
    if az and AZ and num >= 2:
        print("Пароль принят")
    else:
        if not az:
            print("В пароле должны быть строчные буквы")
        if not AZ:
            print("В пароле должны быть заглавыне буквы")
        if num < 2:
            print("В пароле должно быть больше двух цифр")
passB = input("Введите пароль еще раз: ")
if passA == passB:
    print("Пароль верный!")
else:
    while passA != passB:
        passB = input("Повторите попытку: ")
    print("Пароль верный!")





