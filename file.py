# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}
# ]

numbers = [2, 4, 28, 77, 60, 55, 21, 33, 44, 100]
# print(len(numbers))
# a = len(numbers)
# print (a +1)
numbers[3] = 28
for number in numbers:
    if number > 28:
        print(number)

    else :
        print("Hello")