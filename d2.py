#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:35:39 2024

@author: pauline
"""


def extract_input(path:str)->list[list]:
    """récupérer les rapports depuis un fichier texte
    vers une liste de liste"""
    
    rapports = []
    with open(path, "r", encoding="UTF8") as file:
        lines = file.readlines()
        
    for line in lines :
        rapport = [int(x.strip()) for x in line.split()]
        rapports.append(rapport)
        
    return rapports


def try_tol(rapport:list)->bool:
    """Appliquer une tolerance d'un level."""
    
    for i in range(len(rapport)):
        new_rapport = rapport[:i] + rapport[i+1:]
        if step_is_safe(new_rapport) and prog_is_safe(new_rapport):
            return True
    
    return False


def step_is_safe(rapport:list)->bool:
    """Vérifie si l'écart entre deux levels est compris entre 1 et 3 inclus"""
    
    for i in range(len(rapport[:-1])):
        if abs(rapport[i]-rapport[i+1]) not in [1, 2, 3]:
            return False
        
    return True


def prog_is_safe(rapport:list)->bool:
    """Vérifie si le rapport est bien strictement croissant ou décroissant"""
    
    if rapport == sorted(rapport):
        return True
    if rapport == sorted(rapport)[::-1]:
        return True
    else:
        return False
    

def nb_safe_tol(rapports:list)->int:
    """Compte le nombre de rapport safe"""
    nb = 0
    for rapport in rapports :
        if step_is_safe(rapport) and prog_is_safe(rapport):
            nb += 1
        else :
            if try_tol(rapport):
                nb+=1
                
    return nb

def main():
    """Renvoie le nombre de rapport safe depuis des data txt."""
    rapports = extract_input("./d2_input.txt")
    nb= nb_safe_tol(rapports)
    return print(f"Nombre de rapports safe : {nb}")


if __name__ == "__main__":
    main()