#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:54:49 2024

@author: pauline
"""

def get_puzzle(path="d4_input.txt"):
    """Extrait le puzzle du fichier et renvoie une liste de string"""
    with open (path, "r", encoding="UTF8") as file :
        puzzle = file.readlines()
        return puzzle
    

def find_crossmas(puzzle:list)->int:
    """Compte le nombre de patterns cross-mass dans le puzzle.
    Renvoie un int"""
    
    def get_cadre(ind_c, ind_l, puzzle):
        """Construit une liste de liste. Dans les faits, il s'agit d'un
        cadre de dimension (3,3)"""
        cadre = []
        for i_l in range(ind_l,ind_l+3):
            cadre.append(puzzle[i_l][ind_c:ind_c+3])
        return cadre
        
    def is_crossmas(cadre:list)->bool:
        """Vérifie si le cadre fourni contient un pattern cross-mas"""
        if cadre[1][1] == "A":
            c1 = cadre[0][0]
            c2 = cadre[0][2]
            c3 = cadre[2][0]
            c4 = cadre[2][2]
            cond1 = sorted([c1, c2, c3, c4]) == ["M", "M", "S", "S"]
            cond2 = c1 != c4
            if cond1 and cond2:
                return True
            return False
        
    
    cropped_puzzle = puzzle[:-2]
    len_cropped_line = len(puzzle[0][:-2])
    nb = 0
    
    for ind_l, l in enumerate(cropped_puzzle):
        for ind_c in range(len_cropped_line):
            cadre = get_cadre(ind_c, ind_l, puzzle)
            if is_crossmas(cadre):
                nb+= 1
    
    return nb
            
     


def find_xmas(puzzle:list):
    
    def find_horizontal(puzzle:list, patterns:list)->int:
    
        def get_nb_pat_line(ligne:str, patterns):
                nb = 0
                for pattern in patterns:
                    start = 0
                    while True:
                        index = ligne.find(pattern, start)
                        if index == -1:
                            break
                        
                        nb += 1
                        start = index + 1
                        
                return nb
    
        nb = 0
    
        for ligne in puzzle:
            nb += get_nb_pat_line(ligne, patterns)
    
        return nb


    def find_vertical(puzzle:str, patterns:list)->int:
        
        new_puzzle = []
        for i in range(len(puzzle[0])):
            new_line = ""
            for line in puzzle:
                new_line = new_line + line[i]
            new_puzzle.append(new_line)
        
        nb = find_horizontal(new_puzzle, patterns)
                
        return nb
    
    
    def find_diagonales(puzzle:str, patterns:list)->int:
        l_new_line = len(puzzle) + len(puzzle[0]) -1
        
        nb = 0
        new_puzzle1 = [] 
        for id_l, line in enumerate(puzzle) :
            b = "."*id_l
            a = "."*(l_new_line-len(line)-id_l)
            new_line = b + line + a
            new_puzzle1.append(new_line)
        
        new_puzzle2 = []
        for id_l, line in enumerate(puzzle) :
            b = "."*(l_new_line-len(line)-id_l)
            a = "."*id_l
            new_line = b + line + a
            new_puzzle2.append(new_line)
        
        for puzzle_v in [new_puzzle1, new_puzzle2]:
            nb += find_vertical(puzzle_v, patterns)
        
        return nb
    
    patterns = ["XMAS", "SAMX"]
    v = find_vertical(puzzle, patterns)
    h = find_horizontal(puzzle, patterns)
    d = find_diagonales(puzzle, patterns)
    nb = v + h + d
    
    return nb


puzzle = get_puzzle()
print(f"Nombre de patterns XMAS et SAMX : {find_xmas(puzzle)}")
print(f"Nombre de cross-mas : {find_crossmas(puzzle)}")
