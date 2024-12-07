#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:26:59 2024

@author: pauline
"""

import numpy as np

class Position:
    def __init__(self, x, y, direction, puzzle_mat, puzzle_dim):
        self.x = x
        self.y = y
        self.direction = direction
        self.puzzle_mat = puzzle_mat
        self.puzzle_dim = puzzle_dim
        
    def step(self):
        x_step = self.x + self.direction[0]
        y_step = self.y + self.direction[1]
        return Position(
            x_step,
            y_step,
            self.direction,
            self.puzzle_mat,
            self.puzzle_dim
            )
    
    
    def is_step_in_map(self):
        x_step = self.x + self.direction[0]
        y_step = self.y + self.direction[1]
        return (x_step in range(self.puzzle_dim[0]) 
                and y_step in range(self.puzzle_dim[1]))
        
    
    def step_is_legal(self):
        x_try, y_try = self.step().x, self.step().y
        return self.puzzle_mat[x_try][y_try] != "#"

    
    def take_turn(self):
        change_dir = {
            (-1,0):(0,1),
            (0,1):(1,0),
            (1,0):(0,-1),
            (0,-1):(-1,0)
            }
        
        try_pos = Position(
                self.x,
                self.y,
                change_dir[self.direction],
                self.puzzle_mat,
                self.puzzle_dim
                )
        
        if try_pos.step_is_legal():
            return Position(
                    self.x + change_dir[self.direction][0],
                    self.y + change_dir[self.direction][1],
                    change_dir[self.direction],
                    self.puzzle_mat,
                    self.puzzle_dim)


def get_puzzle(path="./d6_input.txt")->list[str]:
    with open(path, "r", encoding="UTF8") as file:
        puzzle = file.read().strip().split("\n")
        return puzzle


def puzzle_to_array(puzzle:list[str])->np.array:
    pzl = []
    for line in puzzle :
        line_l = [line[x] for x in range(len(line))]
        pzl.append(line_l)
        
    puzzle_mat = np.array(pzl)
    puzzle_dim = puzzle_mat.shape
    return puzzle_mat, puzzle_dim


def get_starting_point(puzzle_mat:np.array)->tuple:
    for id_line, line in enumerate(puzzle_mat):
        for id_char, char in enumerate(line):
            if char == "^":
                return id_line, id_char


def get_path_surface():
    puzzle = get_puzzle()
    puzzle_mat, puzzle_dim = puzzle_to_array(puzzle)
    x_start, y_start = get_starting_point(puzzle_mat)
    pos = Position(x_start, y_start, (-1,0), puzzle_mat, puzzle_dim)
    surface = [(pos.x, pos.y)]
    while pos.is_step_in_map():
        if pos.step_is_legal():
            pos = pos.step()
        else:
            pos = pos.take_turn()
        
        surface.append((pos.x, pos.y))
        
    return print(f"Nombre de cases visitées : {len(set(surface))}")
    
if __name__ == "__main__":
    get_path_surface()
