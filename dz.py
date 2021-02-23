
# 1)Дан
# лист:
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]



# - найти min число влисте

# minNumberFromList = list[0]
# for i in list:
#     if minNumberFromList > i:
#         minNumberFromList=i
# print(minNumberFromList)


# - удалить все одинаковые значения
# for i in range(len(list) -1, -1, -1):
#     if list.count(list[i]) > 1:
#         del list[i]
#     print(list.count(i), end=" ")
# print(list)



# - заменить каждое четвертое значение на"Х"



# k = 0
# while k<len(list):
#     list[k] ="X"
#     k +=4
# print(list)


# - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа пример:
# [1, 2, 3, 4, 5, 56, 7, 8, 9] = > 5
# [-1, -2, 3, 4, 555] = > 4
# [5, 5, 5, 5] = > 5
# [-10, 5, 5] = > 5
# a = 0
# for i in list:
#     a += i
# avg = a//len(list)
#
# array = []
#
# for k in list:
#     if k == avg:
#         v = 0
#         array.append(v)
#
#     elif k < avg:
#         v = 0
#         while k < avg:
#             v += 1
#             k += 1
#             if k == avg:
#                 array.append(v)
#     elif k > avg:
#         v = 0
#         while k > avg:
#             v += 1
#             k -= 1
#             if k == avg:
#                 array.append(v)
#
# print(avg)
# minNumberFromArray = array[0]
# for i in array:
#     if minNumberFromArray > i:
#         minNumberFromArray = i
# indexAvg = array.index(minNumberFromArray)
# print(list[indexAvg])


# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# f = 0
# while f <= 5:
#     k = 0
#     while k <= 5:
#         if f == 0 or f == 5 or k == 0 or k == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         k += 1
#     print('')
#     f += 1



# 3) переделать первое задание под меню с помощью цикла
#
while True:
    print(list)
    print("1 - найти min число влисте")
    print("2 - удалить все одинаковые значения")
    print("3 - заменить каждое четвертое значение на 'Х'")
    print("4 - - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа пример:")
    print("0 - вихід")
    n = int(input("Зробіть ваш вибір:"))
    minNumberFromList = list[0]
    if n == 1:
        for i in list:
          if minNumberFromList > i:
              minNumberFromList = i
          print("min number:", minNumberFromList)

    elif n == 2:
        for i in range(len(list) - 1, -1, -1):
            if list.count(list[i]) > 1:
               del list[i]
        print(list)

    elif n == 3:
        k = 0
        while k < len(list):
            list[k] = "X"
            k += 4
        print(list)

    elif n == 4:
        a = 0
        for i in list:
            a += i
        avg = a // len(list)

        array = []

        for k in list:
            if k == avg:
                v = 0
                array.append(v)

            elif k < avg:
                v = 0
                while k < avg:
                    v += 1
                    k += 1
                    if k == avg:
                        array.append(v)
            elif k > avg:
                v = 0
                while k > avg:
                    v += 1
                    k -= 1
                    if k == avg:
                        array.append(v)

        print("середнє арифметичне:",avg)
        minNumberFromArray = array[0]
        for i in array:
            if minNumberFromArray > i:
                minNumberFromArray = i
        indexAvg = array.index(minNumberFromArray)
        print("найблтжче до середнього арифметичного:", list[indexAvg])

    elif n == 0:
        break

    else:
        print("числа не знайдено")

# 4) вывести табличку умножения с помощью цикла whileу
# a = 1
#
# while a < b:
#     c = 1
#     while c < b:
#         print(a*c, end=' ')
#         c += 1
#     print('')
#     a += 1


