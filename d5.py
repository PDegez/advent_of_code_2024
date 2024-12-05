#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:42:50 2024

@author: pauline
"""

class Update:
    def __init__(self, rules, update):
        self.rules = rules
        self.update = update

    def correct_order(self):
        """retourne l'update dans l'ordre défini par les règles"""
        dico = {}
        for nb in self.rules:
            dico[nb[0]] = dico.get(nb[0],0) + 1
        sorted_rules = sorted(dico.items(),key = lambda x : x[1], reverse=True)
        correct_order_beta = [x[0] for x in sorted_rules]
        orphan_nb = [nb for nb in self.update if nb not in correct_order_beta]
        return tuple(correct_order_beta + orphan_nb)

    def is_correct(self):
        """vérifie que l'update respecte l'ordre imposé"""
        return self.correct_order() == self.update

    def middle(self):
        """renvoie la valeur du milieu"""
        return self.update[(len(self.update)//2)]
    

def get_relevant_rules(rules:list, update:tuple)->list[tuple]:
    
    relevant_rules = [
        rule for rule in rules if rule[0] in update and rule[1] in update
        ]
    return relevant_rules
            

def get_data(path="./d5_input.txt")->tuple[list,list]:
    with open(path, "r", encoding="UTF8") as file:
        content = file.read().strip().split("\n\n")
        rules_r, updates_r = [content[x].split("\n") for x in range(len(content))]
        rules = [tuple(int(x) for x in pair.split("|")) for pair in rules_r]
        updates = [tuple(int(x) for x in update.split(",")) for update in updates_r]
        return rules, updates

def check_updates_n_sum_middles():
    get_data()
    rules, updates = get_data()
    res_nat = 0
    res_cor = 0
    for occurrence in updates:
        relevant_rules = get_relevant_rules(rules, occurrence)
        update = Update(relevant_rules, occurrence)
        if update.is_correct():
            res_nat += update.middle()
        else :
            corrected_update = Update(relevant_rules, update.correct_order())
            res_cor += corrected_update.middle()
    
    
    return print(
        f"la somme des milieux des updates correctes est : {res_nat}",
        f"la somme des milieux des updates incorrectes est : {res_cor}",
        sep = "\n")

if __name__ == "__main__":
    check_updates_n_sum_middles()
        