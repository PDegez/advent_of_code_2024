# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:45:36 2024

@author: pauli
"""
from collections import Counter


def main():
    """Advent of code day 1 : Extrait la distance et la similarité entre
    deux listes extraites depuis un fichier txt"""

    def get_lists(path="./d1_input.txt")->tuple:
        """Récupère deux listes depuis un fichier txt"""
        with open("./d1_input.txt", "r", encoding="UTF8") as file:
            l1 = []
            l2 = []
            for line in file.readlines():
                pair = line.split("   ")
                l1.append(int(pair[0].strip()))
                l2.append(int(pair[1].strip()))
    
        l1s = sorted(l1)
        l2s = sorted(l2)
        return l1s, l2s
    
    
    def get_distance(l1:list, l2:list)->int:
        """Compare 2 à 2 les éléments de deux listes triées et renvoie
        la somme des écarts"""
        distance = 0
        for i in range(len(l1)):
            distance += abs(l1[i]-l2[i])
        return distance
    
    
    def get_similarity(l1:list, l2:list)->int:
        """Compare 2 liste en fonction de la fréquence des valeurs qu'elles 
        ont en commun."""
        similarity = 0
        countl1 = Counter(l1)
        countl2 = Counter(l2)
        
        for key, value in countl1.items():
            similarity += countl2.get(key, 0)*key
        
        return similarity

    l1, l2 = get_lists()
    d = get_distance(l1, l2)
    s = get_similarity(l1, l2)
    
    return print(f"Distance = {d}\nSimilarity = {s}")

if __name__ == "__main__":
    main()