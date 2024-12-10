#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:56:17 2024

@author: pauline
"""

from collections import defaultdict

puzzle = ["............",
"........0...",
".....0......",
".......0....",
"....0.......",
"......A.....",
"............",
"............",
"........A...",
".........A..",
"............",
"............"]


def import_puzzle(path="./d8_input.txt")->list[str]:
    with open(path, "r", encoding="UTF8") as file :
        puzzle = file.read().strip().split("\n")
        return puzzle


def get_antennes(puzzle:list[str])-> dict:
    antennes = defaultdict(list)
    for x, ligne in enumerate(puzzle):
        for y, char in enumerate(ligne):
            if char != ".":
                antennes[char].append(tuple((x,y)))
    return antennes


def get_vector(antenne1:tuple, antenne2:tuple)->tuple:
    return tuple([antenne2[0] - antenne1[0], antenne2[1] - antenne1[1]])


def is_in_map(antinode:tuple, puzzle_size:tuple)->bool:
    return ((puzzle_size[0] - antinode[0]) >= 0
            and (puzzle_size[0] - antinode[0]) <= puzzle_size[0]
            and (puzzle_size[1] - antinode[1]) >= 0
            and (puzzle_size[1] - antinode[1]) <= puzzle_size[1])


def antinode_possible_loc(antenne1:tuple, antenne2:tuple, puzzle_size:tuple):
    vecteur = get_vector(antenne1, antenne2)

    possible_loc = set()
    possible_loc.add(antenne1)
    possible_loc.add(antenne2)
    while is_in_map(antenne1, puzzle_size) or is_in_map(antenne2, puzzle_size):
        antenne1 = (antenne1[0] - vecteur[0], antenne1[1] - vecteur[1])
        antenne2 = (antenne2[0] + vecteur[0], antenne2[1] + vecteur[1])
        for posloc in [antenne1, antenne2]:
            if is_in_map(posloc, puzzle_size):
                possible_loc.add(posloc)
                
    return possible_loc

         
def get_all_antinodes(antennes:dict, puzzle:list[str])->int:
    antinodes = set()
    puzzle_size = tuple((len(puzzle)-1, len(puzzle[0])-1))
    for reseau in antennes.keys():
        for n, antenne1 in enumerate(antennes[reseau][:-1]):
            for antenne2 in antennes[reseau][n+1:]:
                possible_loc = antinode_possible_loc(
                    antenne1, antenne2, puzzle_size)
                for loc in possible_loc:
                    antinodes.add(loc)
    return antinodes
            

        
def get_nb_antinodes():
    puzzle = import_puzzle()
    antennes = get_antennes(puzzle)
    nb = get_all_antinodes(antennes, puzzle)
    return (print(f"Nb antinodes : {len(nb)}"))


if __name__ == "__main__":
    get_nb_antinodes()