#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:53:16 2024

@author: pauline
"""


def get_data(path="./d9_input.txt")->str:
    with open(path, "r", encoding="UTF8") as file:
        input_str = file.read().strip("\n")
        return input_str

    
def modify(input_str:str)->list:
    file_blocks = []

    n = 0
    i = 0
    while n < (len(input_str)-2):
        blocks_vides = ["." for _ in range(int(input_str[n+1]))]
        indices_fichiers = [i for _ in range(int(input_str[n]))]
        file_blocks = file_blocks + indices_fichiers + blocks_vides
        n += 2
        i += 1
    file_blocks = file_blocks + [i for _  in range(int(input_str[-1]))]
    return file_blocks


def get_chuncks(file_blocks:list)->list:
    sp = 0
    chuncks = []
    val = file_blocks[0]
    for i, n in enumerate(file_blocks[1:]):
        if file_blocks[i] != val:
            cle = (val, i-sp, sp)
            chuncks.append(cle)
            val = file_blocks[i]
            sp = i
    
    cle = (val, len(file_blocks)-i, sp)
    chuncks.append(cle)
    return chuncks
        

def sort_this_shit(chuncks:list, residuals:list):

    while residuals != []:
        need_sort = residuals[0]
        for i, chunck in enumerate(chuncks):
            sous = chunck[1] - need_sort[1]
            if chunck[0] == "." and sous >= 0:
                if sous > 0:
                    dot = ["." for _ in range(sous)]
                    cle_dot = (".", len(dot), "?")
                    chuncks = chuncks[:i] + [need_sort] + [cle_dot] + chuncks[i+1:]
                else:
                    chuncks = chuncks[:i] + [need_sort] + chuncks[i+1:]
                
                break
        residuals.pop(0)
    
    return chuncks


def return_to_list(sorted_chunks:list[tuple])->list:
    
    output_list = []
    for chunck in sorted_chunks:
        output_list = output_list + [chunck[0] for _ in range(chunck[1])]
    return output_list


def compress_2(file_blocks:list)-> list:
    chuncks = get_chuncks(file_blocks)
    residuals = [x for x in chuncks if x[0] != "."][::-1]
    
    output = sort_this_shit(chuncks, residuals)
    
    seen = []
    new_output = output
    for i, element in enumerate(output):
        if element in seen :
            new_output[i] = (".", element[1], "?")
        else :
            seen.append(element)

    return new_output
            

def compress(file_blocks:list)-> list:
    vides = ["." for x in file_blocks if x =="."]
    lego = [c for c in file_blocks if c != "."][::-1]
    l = len(vides)

    compressed = file_blocks
    for i, n in enumerate(file_blocks[:-(l)]):
        if n == ".":
            compressed[i] = lego[0]
            lego.pop(0)
    
    compressed = compressed[:i+1]
    return compressed


def check_sum(compressed:list)->int:
    res = 0
    for i, n in enumerate(compressed):
        if n != ".":
            res += (i*n)
        
    return res


def day9():
    data = get_data()
    file_blocks = modify(data)
    #compressed = compress(file_blocks)
    compressed = compress_2(file_blocks)
    nb = check_sum(compressed)
    return print(f"The filesystem checksum is {nb}")

if __name__ == "__main__":
    day9()