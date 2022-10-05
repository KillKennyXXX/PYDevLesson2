answer = None
answer2 = None


try:
    answer = int(input('Год рождения А.С. Пушкина?'))
except ValueError:
    print("Это не правильный ввод, введена строка, попробуйте еще раз.")

if answer == 1799:
    print("Верно!")

    try:
        answer2 = int(input('День рождения А.С. Пушкина?'))
    except ValueError:
        print("Это не правильный ввод, введена строка, попробуйте еще раз.")

    if answer2 == 6:
        print("Верно!")
    else:
        print("Неверный день рождения")

else:
    print("Неверный год")





