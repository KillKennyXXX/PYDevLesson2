answer = None
answer2 = None

while answer != 1799:
    try:
        answer = int(input('Год рождения А.С. Пушкина?'))
    except ValueError:
        print("Это не правильный ввод, введена строка, попробуйте еще раз.")
        continue
    if answer == 1799:
        print("Верно!")
        while answer2 != 6:
            try:
                answer2 = int(input('День рождения А.С. Пушкина?'))
            except ValueError:
                print("Это не правильный ввод, введена строка, попробуйте еще раз.")
                continue
            if answer2 == 6:
                print("Верно!")
                break

            else:
                print("Неверный день рождения")
        break
    else:
        print("Неверный год")



