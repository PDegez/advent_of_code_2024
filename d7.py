#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 07:58:26 2024

@author: pauline
"""
import time
import math

class Equation:
    def __init__(self, resultat, nombres):
        self.resultat = resultat
        self.nombres = nombres

start_time = time.time()

    
def get_input(path="./d7_input.txt")->list[Equation]:
    equations = []
    with open(path, "r", encoding="UTF8") as file:
        brut = file.read().strip().split("\n")
    for ligne in brut:
            res = int(ligne.split(":")[0])
            numbers = [int(x) for x in ligne.split(":")[1].split()]
            equations.append(Equation(res,numbers))
    return equations


def try_operateur(a:int, b:int, l:list, res:int, lenl:int, n:int):
    if a>res:
        return False
    res1 = a + b
    res2 = a * b
    res3 = a*(10)**(math.floor(math.log10(b))+1) + b
    if n == lenl:
        return res == res1 or res == res2 or res == res3
    n +=1
    return (try_operateur(res1,l[n], l, res, lenl, n) 
            or try_operateur(res2, l[n],l, res,lenl, n) 
            or try_operateur(res3,l[n],l, res,lenl, n))


# def try_operateur(a:int, l:list, res:int):
#     if a>res:
#         return False
#     if not l:
#         return a == res
#     res1 = a + l[0]
#     res2 = a * l[0]
#     res3 = a*(10)**(math.floor(math.log10(l[0]))+1) + l[0]
#     return (try_operateur(res1, l[1:], res) 
#             or try_operateur(res2, l[1:], res) 
#             or try_operateur(res3, l[1:], res))

def sum_test_values_when_correct():
    equations = get_input()
    res = 0
    for equation in equations:
        if try_operateur(equation.nombres[0],
                          equation.nombres[1],
                          equation.nombres,
                          equation.resultat,
                          len(equation.nombres)-1,
                          1):
        # if try_operateur(equation.nombres[0],
        #                  equation.nombres[1:],
        #                  equation.resultat):
            res += equation.resultat
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return (print(f"Somme des résultats de calibrations correctes : {res}",
                  f"Durée d'exécution : {execution_time}",
                  sep="\n"))

if __name__ == "__main__":
    sum_test_values_when_correct()
            