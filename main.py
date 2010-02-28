#!/usr/bin/python
# -*- coding: utf-8 -*-
# by Artemy M.
# http://artemy.mp
from sets import Set
a = []
rho = []
arr1 = []
arr2 = []
tau = [] 

for x in range(1,6): #запиливаем массив А, из которого будем брать значения
    for y in range(1,6):
        a.append([x,y])
print 'A array:'
print a

def create_arrays(): # функция создания массивов. сделал, потому что глюк и массивы сами меняются по ходу дела. а функцию можно вызывать много раз.
    for x in range(1,6):
        for y in range(1,6):
            if (abs(int((3-x)*(3-y))) <= 1): #здесь условие для ро. abs() - модуль
                rho.append([x,y]) #приделываем к массиву ро подходящие элементы
    for x in range(1,6):
        for y in range(1,6):
            if int(x+y) < 5: #условие для тау
                tau.append([x,y]) #запиливаем тау


def sort(List): #сортируем массивы и удаляем дубликаты элементов
    if List:
        List.sort()
        last = List[-1]
        for i in range(len(List)-2, -1, -1):
            if last == List[i]:
                del List[i]
            else:
                last = List[i]
    create_arrays()
    return List

def compose(arr1,arr2): #композиция элементов - принимает два массива/множества как аргументы
    result = []
    for x in arr1:
        for y in arr2:
            if x[1] == y[0]:
                result.append([x[0],y[1]])
                #print result
    create_arrays()
    return sort(result)

def reverse(set): #обратное отношение
    for x in set:
        set[len(set)-1] =[x[1],x[0]]
    create_arrays()
    return sort(set)
        

def square(array): #квадрат отношения
    create_arrays()
    return compose(array,array)

def print_matrix(array): #печать матрицы. делаем матрицу 5х5, заполненную нулями, а потом точечно меняем нужные места на единицы
    matrix = ""
    row = ""
    dummy1 = []
    dummy2 = []
    for x in range(1,6):
        for y in range(1,6):
           dummy2.append('0')
        dummy1.append(dummy2)
        dummy2 = []
    
    for x in array:
           dummy1[x[0]-1][x[1]-1]= '1'
  #  return dummy1
    dummy2=""
    for x in range(0,5):
        for y in range(0,5):
            dummy2+=str(dummy1[x][y])
        dummy2+="\n"
        dummy2 = str(dummy2)
    create_arrays()
    return dummy2


create_arrays()

print "Array Rho" #множество ро
print rho
print 'Matrix of Rho' #матрица множества
print print_matrix(rho) 



 
print "Array Tau" #тау
print tau
print 'Matrix of Tau'
print print_matrix(tau)




print 'composition of Rho and Tau' # композиция ро и тау
print compose(rho,tau)
print print_matrix(compose(rho,tau))



print 'Reversal relation of Rho' # обратное отношение ро
print reverse(rho)
print print_matrix(reverse(rho))

print 'Reversal relation of Tau' # то же самое для тау
print reverse(tau)
print print_matrix(reverse(tau))


# Оказывается не нужно
#print 'composition of both reversal Rho and Tau' 
#print compose(reverse(rho), reverse(tau))



print 'Square of Rho' # квадрат ро
print square(rho)
print print_matrix(square(rho))


print 'Square of Tau' # квадрат тау
print square(tau)
print print_matrix(square(tau))


print 'Square composition of Rho and Tau' # квадратная композиция ро и тау
print square(compose(rho,tau))
print print_matrix(square(compose(rho,tau)))
