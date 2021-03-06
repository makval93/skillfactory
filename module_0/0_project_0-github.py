#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число.'''
    
    count_ls = []
    random.seed(1)
    random_array = np.random.randint(1,101, size=1000)
    
    for number in random_array:
        count_ls.append(game_core(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)



def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного. Функция принимает загаданное число и возвращает число попыток.
    '''
    
    count = 1
    left = 1
    right = 101
    
    predict = (left + right) // 2
    
    while number != predict:
        '''Задается цикл с условием. Пока загадываемое число не совпадёт с predict.'''
        
        count+=1
        
        if predict < number:
            left = predict
            '''Если predict меньше загадываемого числа, тогда суммируется predict с правой стороной массива и делится попалам.
            '''
            
        else:
            right = predict
            '''Если predict меньше загадываемого числа, тогда суммируется predict с левой стороной массива и делится попалам.
            '''
            
        predict = (left + right) // 2
        
    return(count)

score_game(game_core_v2)

