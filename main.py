# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
#
# file_one = open("my_file_task_1.txt", 'w')
#
# print("enter strings")
#
#
# while True:
#     user_input = input()
#     if r' ' in user_input:
#         exit(0)
#     else:
#         print(user_input)
#         file_one.writelines(user_input+'\n')
#
# file_one.close()

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

# file_two = open('file_for_task_two.txt','r')
# string_counnt=1
# for line in file_two:
#     word_arr = line.split(' ')
#     print(word_arr)
#     print('words count in line is ' + str(len(word_arr)))
#     if '\n' in line:
#         string_counnt += 1
#
# print("\n" +" total strings in file is: " + str(string_counnt))
# file_two.close()

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32
#
# file_three = open('file_task_three.txt','r')
# total_ammount = 0
# string_count=1
# for line in file_three:
#     line_comb =line.split(' ')
#     if '\n'in line:
#         string_count +=1
#     if int(line_comb[1]) < 20000:
#         print(line_comb[0])
#     total_ammount += int(line_comb[1])
#
# #print(string_count)
# #print(total_ammount)
# print("averege salalry is: " + str(total_ammount/string_count))
# file_three.close()

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
#
# file_four_read = open('file_for_task_four.txt','r')
# file_four_write = open('file_for_task_four_write.txt','w')
# for line in file_four_read:
#     if "One" in line:
#         sp_line = line.split(' ')
#         sp_line[0] = 'один'
#         new_line = ' '.join(sp_line)
#         file_four_write.write(new_line)
#         print(new_line)
#     if "Two" in line:
#         sp_line = line.split(' ')
#         sp_line[0] = 'два'
#         new_line = ' '.join(sp_line)
#         file_four_write.write(new_line)
#         print(new_line)
#     if "Three" in line:
#         sp_line = line.split(' ')
#         sp_line[0] = 'три'
#         new_line = ' '.join(sp_line)
#         file_four_write.write(new_line)
#         print(new_line)
#     if "Four" in line:
#         sp_line = line.split(' ')
#         sp_line[0] = 'тимми!'
#         new_line = ' '.join(sp_line)
#         file_four_write.write(new_line)
#         print(new_line)
#
# file_four_write.close()
# file_four_read.close()


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
# import random
# file_five = open('task_five_file.txt','w')
# line_to_write = ''
# numbers_ammount = random.randint(1, 10)
# numbers_arr = []
# counter = 1
# while counter <= numbers_ammount:
#     randomint = random.randint(0, 999)
#     numbers_arr.append(str(randomint))
#     counter += 1
# print(numbers_arr)
# line_to_write = str(" ".join(numbers_arr))
# file_five.write(line_to_write)
# file_five.close()
# print(line_to_write)
# with open("task_five_file.txt", "r+") as f_obj:
#     summ_of_numbers = 0
#     for linne in f_obj:
#         sp_ln = linne.split()
#         for inttosum in sp_ln:
#             summ_of_numbers += int(inttosum)
#
#         print(summ_of_numbers)

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
# task_six_dict = {}
# with open('six_task.txt','r',encoding="utf-8") as file6_obj:
#     for line in file6_obj:
#         hours_summ = 0
#         repl_line = line.replace('(', ' ')
#         sp_line = repl_line.split(' ')
#         for searching_int in sp_line:
#             try:
#                 trytoint = int(searching_int)
#                 hours_summ += trytoint
#             except ValueError:
#                 pass
#         task_six_dict[sp_line[0]] = hours_summ
#         #print(hours_summ)
#
# print(task_six_dict)


#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.