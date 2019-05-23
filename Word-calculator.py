def calc_str():
    try:
        expression = input('Введите выражение словами через пробел на английском:')
        div_input = expression.split(" ")
        while 'multiply' in div_input or 'divide' in div_input:
            # print('TEST')
            if 'multiply' in div_input:
                targ_ind = (div_input.index('multiply'))
                result = int(div_input[targ_ind - 1]) * int(div_input[targ_ind + 1])
                del div_input[targ_ind - 1:targ_ind + 2]
                div_input.insert(targ_ind - 1, result)
            if 'divide' in div_input:
                targ_ind = (div_input.index('divide'))
                result = int(div_input[targ_ind - 1]) / int(div_input[targ_ind + 1])
                del div_input[targ_ind - 1:targ_ind + 2]
                div_input.insert(targ_ind - 1, result)
        while 'plus' in div_input or 'minus' in div_input:
            if 'plus' in div_input:
                targ_ind = (div_input.index('plus'))
                result = int(div_input[targ_ind - 1]) + int(div_input[targ_ind + 1])
                del div_input[targ_ind - 1:targ_ind + 2]
                div_input.insert(targ_ind - 1, result)
            if 'minus' in div_input:
                targ_ind = (div_input.index('minus'))
                result = int(div_input[targ_ind - 1]) - int(div_input[targ_ind + 1])
                del div_input[targ_ind - 1:targ_ind + 2]
                div_input.insert(targ_ind - 1, result)

    except:
        print('Ошибка: нарушен синтаксис или присутсвует деление на 0.')

    else:

        div_input_str = ''.join(str(e) for e in div_input)
        print('\nРезультат выражения равен', div_input_str)
    finally:
        print('Функция завершила работу. \n\nHave a nice day!')


calc_str()




# Это все можно было сделать проще поменяв слова на математические знаки  str.replace(old, new [, count]) ,
# Потом посчитать выражение с помощью eval(string)
#ОТВЕТ: eval может выполнить небезопасный код. Стараются не использовать. Не принятло.




2+3*5-2/2