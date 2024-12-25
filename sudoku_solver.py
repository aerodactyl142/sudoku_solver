# -*- coding: utf-8 -*-
"""
'''
Step 0: check that input is valid
Step 1: basic solve (recursive)
# Simple solve (recursive)
Step 2: Write possible numbers and see if solvable
Step 3: If any change, repeat basic solve and simple solve
##
# Intermediate solve: Triplet logic
Step 4: Find triplets/twins/quadruplets and eliminate them from others in the same row/col/box
Step 5: If any change, repeat basic solve, simple solve and intermediate solve

# Advanced solve: propagation
Step 6: Guess one number and iterate through. Recursively using previous techniques.
'''

"""

import numpy as np
# import sys
# import copy

# try a 4x4 sudoku first
# the correct solution
ans4 = np.array([[1,3,2,4],
                 [2,4,1,3],
                 [3,1,4,2],
                 [4,2,3,1]])

# use zero to represent empty
arr4 = np.array([[1,0,0,4],
                 [0,4,0,3],
                 [0,1,0,2],
                 [4,0,3,0]])

arrinvalid = np.array([[1,0,1,4],
                     [0,4,0,3],
                     [0,1,2,2],
                     [4,3,3,0]])

#9x9 easy, correct
ans_easy = np.array([[5,3,2,4,8,1,7,9,6],
                     [1,7,4,6,9,3,8,2,5],
                     [9,6,8,2,7,5,1,4,3],
                     [3,1,6,7,2,8,4,5,9],
                     [2,9,7,5,6,4,3,8,1],
                     [4,8,5,3,1,9,6,7,2],
                     [6,4,3,9,5,7,2,1,8],
                     [7,5,1,8,3,2,9,6,4],
                     [8,2,9,1,4,6,5,3,7]])

arr_easy = np.array([[5,0,2,0,8,1,7,0,6],
                     [1,0,4,6,9,3,0,0,0],
                     [0,0,8,0,7,5,1,4,3],
                     [3,1,0,0,2,0,0,5,9],
                     [0,9,0,5,0,4,0,8,0],
                     [4,8,0,0,1,0,0,7,2],
                     [6,4,3,9,5,0,2,0,0],
                     [0,0,0,8,3,2,9,0,4],
                     [8,0,9,1,4,0,5,0,7]])

#9x9 medium, correct
ans_medi = np.array([[4,1,8,6,7,9,5,2,3],
                     [2,3,7,5,8,1,4,6,9],
                     [6,9,5,2,3,4,7,8,1],
                     [7,5,1,4,9,6,2,3,8],
                     [8,4,2,7,1,3,9,5,6],
                     [9,6,3,8,2,5,1,7,4],
                     [3,7,4,9,5,8,6,1,2],
                     [1,2,9,3,6,7,8,4,5],
                     [5,8,6,1,4,2,3,9,7]])

arr_medi = np.array([[4,1,0,6,7,0,0,0,3],
                     [0,0,0,0,8,1,0,6,9],
                     [0,9,5,0,3,4,0,0,1],
                     [0,0,1,0,9,0,2,0,8],
                     [0,4,0,0,0,3,0,0,0],
                     [0,0,3,8,0,5,0,0,4],
                     [0,7,0,9,0,0,6,0,2],
                     [0,0,0,0,6,0,0,0,5],
                     [0,0,0,0,0,0,0,0,0]])

#9x9 hard
ans9 = np.array([[2,1,3,6,5,8,7,4,9],
                 [4,6,5,7,1,9,2,3,8],
                 [9,7,8,4,2,3,6,5,1],
                 [7,4,6,1,3,5,9,8,2],
                 [5,8,9,2,7,4,1,6,3],
                 [3,2,1,9,8,6,5,7,4],
                 [1,3,7,8,6,2,4,9,5],
                 [8,9,2,5,4,7,3,1,6],
                 [6,5,4,3,9,1,8,2,7]])

arr9 = np.array([[0,0,0,0,5,8,0,0,0],
                 [0,0,0,7,0,9,0,0,0],
                 [9,0,8,0,0,0,6,0,1],
                 [7,0,0,0,3,0,0,0,2],
                 [5,0,0,2,0,4,0,0,3],
                 [3,0,1,0,0,0,5,0,4],
                 [1,0,0,0,6,0,0,0,5],
                 [0,0,0,5,0,7,0,0,0],
                 [0,0,4,0,0,0,8,0,0]])

num_57 = np.array([[0,0,8,0,0,0,6,0,0],
                   [0,6,0,0,2,0,0,5,0],
                   [5,0,1,0,0,9,4,0,7],
                   [0,0,0,0,0,6,3,0,0],
                   [0,2,0,0,1,0,0,9,0],
                   [0,0,3,4,0,0,0,0,0],
                   [3,0,6,5,0,0,2,0,4],
                   [0,8,0,0,4,0,0,3,0],
                   [0,0,5,0,0,0,7,0,0]])

num_252 = np.array([[0,0,0,0,3,0,0,0,0],
                    [0,0,2,5,0,6,9,0,0],
                    [0,6,0,1,0,2,0,8,0],
                    [0,3,1,0,0,0,7,9,0],
                    [4,0,0,0,0,0,0,0,8],
                    [0,9,7,0,0,0,2,3,0],
                    [0,5,0,7,0,4,0,6,0],
                    [0,0,8,2,0,5,1,0,0],
                    [0,0,0,0,9,0,0,0,0]])

# basic solve
def basic_solve(sudoku):
    '''
    Solve if each row, col and box result in only one number left
    '''
    # automatically get the size of sudoku puzzle
    sudoku_size = len(sudoku)
    filled = False
    to_fill = np.copy(sudoku)

    # traverse the whole grid
    for i in range(sudoku_size):
        for j in range(sudoku_size):
            if sudoku[i][j] == 0:
                # check row, col and box
                box = sudoku[i - i%(np.sqrt(sudoku_size)).astype(int) : i + (np.sqrt(sudoku_size) - i%(np.sqrt(sudoku_size))).astype(int), 
                           j - j%(np.sqrt(sudoku_size)).astype(int) : j + (np.sqrt(sudoku_size) - j%(np.sqrt(sudoku_size))).astype(int)]
                unq_list = np.unique([sudoku[i], sudoku[:,j], box.reshape(-1)])
                unq_list = unq_list[unq_list!=0] # this is sorted
                if len(unq_list) == (sudoku_size - 1):
                    idx = np.where(unq_list - np.arange(sudoku_size-1) != 1)
                    idx = idx[0]
                    if len(idx) == 0:
                        idx = sudoku_size
                    else:
                        idx = idx[0] + 1
                    to_fill[i][j] = idx
                    filled = True
    if filled == True:
        return basic_solve(to_fill)
    else:
        return(to_fill)

def check_ans(solved, ans):
    print("Attempt:")
    print(solved)
    if np.unique(solved)[0] == 0:
        print("There are still some blanks!")
    elif ans.all() == solved.all():
        print("Yay correct!")
    elif check_valid(solved):
        print("Solution is valid but wrong! Multiple answers?")
    else:
        print("Solution is invalid")

def check_valid(sudoku):
    # check that the sudoku given is valid, no repeated numbers
    # zeros are allowed as blanks
    su_num = len(sudoku)
    sqrt_num = int(np.sqrt(su_num))
    for i in range(su_num):
        # if any row or col has more than one of each number, invalid
        # check row
        unq_num = np.unique(sudoku[i,:][sudoku[i,:]!=0],return_counts=True)[1]
        if any(unq_num > 1):
            return False
        # check col
        unq_num = np.unique(sudoku[:,i][sudoku[:,i]!=0],return_counts=True)[1]
        if any(unq_num > 1):
            return False
        box_i = i//sqrt_num
        box_j = i%sqrt_num
        # print(box_i, box_j)
        box = sudoku[box_i*sqrt_num:(box_i+1)*sqrt_num,box_j*sqrt_num:(box_j+1)*sqrt_num]
        unq_num = np.unique(box[box!=0], return_counts=True)[1]
        if any(unq_num > 1):
            return False
    return True

def check_solved(sudoku):
    # if sudoku is valid and have no more blanks, it is solved
    return check_valid(sudoku) and not any(np.unique(sudoku) == 0) and len(sudoku) > 0

def get_possible(sudoku):
    '''
    Get a list of all possible numbers. Does not remove twins yet.
    If only one possibility in an entry, fill that in and rerun solves.
    '''
    possibilities = []
    # get possible solutions
    sudoku_size = len(sudoku)
    sqrt_size = int(np.sqrt(sudoku_size))
    for i in range(sudoku_size): # row
        possibilities.append([])
        for j in range(sudoku_size): #col
            
            if sudoku[i][j] != 0: # if already filled in
                possibilities[i].append([]) # no other possibilities
            else: # if blank
                poss = []
                # get box for i and j
                box = sudoku[i//sqrt_size*sqrt_size:i//sqrt_size*sqrt_size+sqrt_size, j//sqrt_size*sqrt_size:j//sqrt_size*sqrt_size+sqrt_size]
                # get unique list from each box, row and col
                unq_list = np.unique([sudoku[i], sudoku[:,j], box.reshape(-1)])
                # check against possible numbers and list all possibilities for each entry
                for num in range(1,sudoku_size+1):
                    if num not in unq_list:
                        poss.append(num)
                if len(poss) == 1: # if only one possibility
                    sudoku[i][j] = poss[0]
                    # if any new number filled in, re-run basic solve
                    sudoku = basic_solve(sudoku)
                    if check_solved(sudoku):
                        # print("Solved!")
                        return sudoku, []
                    else:
                        # if any new number filled in, re-run get_possible
                        return get_possible(sudoku)
                possibilities[i].append(poss)
    # make into np ragged array of lists before returning
    possibilities = np.array(possibilities, dtype=object)
    return sudoku, possibilities


#%% twin check
from itertools import combinations
from itertools import chain

# Step 5: Find twins/triplets/quadruplets
def remove_twins(sudoku, possibilities):
    changed = False
    # sudoku, possibilities = get_possible(sudoku)
    if len(possibilities) == 0:
        # print("Solved!")
        return sudoku, []
    sudoku_size = len(sudoku)
    sqrt_size = int(np.sqrt(sudoku_size))
    
    for i in range(sudoku_size):
        # check for twins in each row, col and box
        possibilities[i] = twin_check(possibilities[i])
        possibilities[:,i] = twin_check(possibilities[:,i])
        box = possibilities[i//sqrt_size*sqrt_size:i//sqrt_size*sqrt_size+sqrt_size, i%sqrt_size*sqrt_size:i%sqrt_size*sqrt_size+sqrt_size]
        box_out = twin_check(box.reshape(-1)).reshape(sqrt_size, sqrt_size)
        possibilities[i//sqrt_size*sqrt_size:i//sqrt_size*sqrt_size+sqrt_size, i%sqrt_size*sqrt_size:i%sqrt_size*sqrt_size+sqrt_size] = box_out
    for i in range(sudoku_size):
        for j in range(sudoku_size):
            # check each possibility for only one possible number
            # if found, fill in the sudoku
            if len(possibilities[i][j]) == 1:
                sudoku[i][j] = possibilities[i][j][0]
                possibilities[i][j] = []
                changed = True
    # if any new number filled in the sudoku, re-run the solves
    if changed:
        sudoku, possibilities = get_possible(np.copy(sudoku))
        return remove_twins(sudoku, possibilities)
    else:
        return sudoku, possibilities
    
def twin_check(row):
    # checks one row for each possible combination of twins, triplet, etc.
    # up to the length of non-empty possibilities in the row
    poss_list = []
    for j in range(len(row)):
        if len(row[j]) != 0:
            poss_list.append(row[j])
    # p = 2 checks for twins, p = 3 checks for triplets and so on
    for p in range(2, len(poss_list)):
        # combis give all combinations of twins
        combis = list(combinations(poss_list,p))
        for c in combis:
            possible_twin = np.unique(list(chain.from_iterable(c)))
            if len(possible_twin) == len(c):
                # print(possible_twin)
                for j in range(len(row)):
                    if row[j] != []:
                        # if not all items in row[j] are inside possible_twin
                        if not all([x in possible_twin for x in row[j]]):
                            # remove possible twin from row[j]
                            new_row_j = []
                            for num in row[j]:
                                if num not in possible_twin:
                                    new_row_j.append(num)
                            # print("twin found!")
                            row[j] = new_row_j # update new row
    return row

def guess_solve(sudoku, possibilities):
    '''
    Uses one of the possibilities to propagate through the sudoku.
    Recursive until solution is found
    '''
    sudoku_orig = np.copy(sudoku) # keep a copy of original
    for i in range(len(possibilities)):
        for j in range(len(possibilities[0])):
            # for entries with possibilities
            if len(possibilities[i][j]) != 0:
                poss_check = np.zeros(len(possibilities[i][j]), dtype=bool)
                # iterate through each possiblity
                for p in range(len(possibilities[i][j])):
                    sudoku[i][j] = possibilities[i][j][p]
                    result = attempt_solve(sudoku)
                    if len(result) != 0:
                        return result
                    else:
                        poss_check[p] = False
                        # if last possibility in list
                        if p == len(possibilities[i][j]) - 1:
                            if np.count_nonzero(poss_check) == 1:
                                # if only one is possible, fill that in
                                idx = np.argwhere(poss_check==True)[0][0]
                                sudoku_orig[i][j] = possibilities[i][j][idx]
                        # reset the original
                        sudoku = np.copy(sudoku_orig)
    # if not solved, continue rerunning the loop
    return guess_solve(sudoku, possibilities)

def attempt_solve(sudoku):
    '''
    Used for level 4: guess solve. Makes use of techniques from previous 
    3 levels to attempt solution of the sudoku, while guessing each number
    '''
    sudoku = basic_solve(sudoku)
    if check_solved(sudoku):
        return sudoku
    else:
        sudoku, poss = get_possible(sudoku)
        # print(sudoku, poss)
        if check_solved(sudoku):
            return sudoku
        # check if possibilities is empty. If empty, sudoku is invalid
        elif poss.any():
            sudoku, poss = remove_twins(sudoku, poss)
            if check_solved(sudoku):
                return sudoku
    # cannot be solved
    return []

def solve(sudoku):
    if not check_valid(sudoku):
        print("Sudoku is invalid! Exiting...")
        return
    sudoku = basic_solve(sudoku)
    if check_solved(sudoku):
        print("Level one: basic solve")
        return(sudoku)
    sudoku, poss = get_possible(np.copy(sudoku))
    if check_solved(sudoku):
        print("Level Two: simple solve")
        return(sudoku)
    sudoku, possibilities = remove_twins(np.copy(sudoku), poss)
    if check_solved(sudoku):
        print("Level three: intermediate solve -- twins!")
        return(sudoku)
    sudoku = guess_solve(sudoku, possibilities)
    if check_solved(sudoku):
        print("Level four: advanced solve -- propagation!")
        return(sudoku)
    else:
        print("Unsolvable??? =(")

sudoku = num_252
solution = solve(sudoku)
print(solution)

