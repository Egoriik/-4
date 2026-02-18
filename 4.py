# В целом все утраивает, но хочется добавить повторный ввод пароля(passA)
# Но не совсем понимаю куда его тыкать и через что, была мысль прописать через
# wlile not az and not AZ and num < 2
# после первого else, но код вовсе полетел...

"commit2"
#добавил строку с while как и хотел, проверяю первое условие,
#но как только условие 6 и более выполняется он идет дальше
#не до конца понимаю почему так

passA = input("Введите пароль: ")
az = False
AZ = False
num = 0
cntSim = False
if len(passA) >= 6:
    cntSim = True
    for i in passA:
        if "a" <= i <= "z":
            az = True
        elif "A" <= i <= "Z":
            AZ = True
        elif "0" <= i <= "9":
            num += 2
    if az and AZ and num >= 2 and cntSim:
        print("Пароль принят")
else:
    while not az and not AZ and num < 2 and not cntSim:
        if not cntSim:
            print("В пароле должно быть шесть и более символов")
        if not az:
            print("В пароле должны быть строчные буквы")
        if not AZ:
            print("В пароле должны быть заглавыне буквы")
        if num < 2:
            print("В пароле должно быть больше двух цифр")
            break
    passA = input("Введите измененный пароль: ")


passB = input("Введите пароль еще раз: ")
if passA == passB:
    print("Пароль верный!")
else:
    while passA != passB:
        passB = input("Повторите попытку: ")
    print("Пароль верный!")
