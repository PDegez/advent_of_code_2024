#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:52:58 2024

@author: pauline
"""

import re

def get_patterns(path:str)-> list:
    with open(path, "r", encoding="UTF8") as file:
        content = file.read()
    
    raw_patterns = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", content)
    return raw_patterns


def get_enabled_data(raw_patterns:list):
    clean =[]
    
    index_first_op = 0
    while True :
        if raw_patterns[index_first_op] in ["do()", "don't()"]:
            break
        else:
            clean.append(raw_patterns[index_first_op])
            index_first_op += 1
    
    raw_pat_sec = raw_patterns[index_first_op:]
    
    for index_pat, pattern in enumerate(raw_pat_sec):
        if pattern == "do()":
            pattern_a_check = raw_pat_sec[index_pat+1:]
            index_a_check = 0
            while True :
                if index_a_check > (len(pattern_a_check)-1):
                    break
                if pattern_a_check[index_a_check] in ["do()", "don't()"]:
                    break
                if pattern_a_check[index_a_check] not in ["do()", "don't()"]:
                    clean.append(pattern_a_check[index_a_check])
                    index_a_check += 1

    return clean
                

def get_numbers(patterns:list)-> list:
    paires = []
    for pattern in patterns :
        paire = re.findall(r"\d{1,3}", pattern)
        paire_int = [int(x) for x in paire]
        paires.append(paire_int)
    return paires
 
       
def mul(a:int, b:int)->int:
    return a*b


def calcul(paires:list)->int:
    res = 0
    for paire in paires :
        if paire != []:
            res += mul(paire[0], paire[1])
    return res
    
    
def main():
    patterns = get_patterns("./d3_input.txt")
    clean_patterns = get_enabled_data(patterns)
    paires = get_numbers(clean_patterns)
    res = calcul(paires)
    return print(f"resultat = {res}")

if __name__ == "__main__":
    main()