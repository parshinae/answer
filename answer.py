#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import pandas as pd
import glob
import messagebox
# from var_dump import var_dump


dataf = pd.DataFrame()


def main():
    data_f = []
    data_f = pd.DataFrame(data_f)
    files = glob.glob('**/*.ans', recursive=True)
    for path in range(0, len(files)):
        with open(files[path], 'r', encoding='CP1251') as file:
            text = file.read()
            answer = re.findall(r'\d+', text)
            if (len(answer)) > 0:
                del answer[0:13]
                numbers = answer[4]+answer[0]+answer[1]+answer[2]+answer[3]
                answer_list = list(numbers)
                fil = str(files[path])
                fil1 = fil[4:9]
                answer_list.append(fil1)
                file.close()

                data_f = data_f.append([answer_list])

    return data_f


if __name__ == '__main__':
    dataf = main()
    dataf.to_excel('Ответы.xlsx', sheet_name='Ответы', index=False)
    messagebox.showinfo('Completed', 'Выполнено! Файл с ответами создан в текущей директории.')
