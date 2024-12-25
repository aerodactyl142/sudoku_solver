# Sudoku Solver
#### Description:

This sudoku solver solves sudoku based on how a human (me) would do it. It is able to take in sudokus of multiple sizes (e.g. 4x4, 9x9, 16x16), although sizes other than 9x9 have not been iteratively tested.
Because this program solves it in the exact steps that the human would, it is able to grade sudokus according to the skills required, instead of arbitrarily based on the emptiness of the sudoku grid, as many sudoku books like to do.
This would ensure the "fun level" of the sudoku before a player attempts it.

Input sudoku blanks are represented by zeros in this case. Any other numbers can be used as inputs (e.g. 1 to 16). The top of this file contains a few example sudokus.
Firstly, the check_valid() function checks if there are any contradictions in the sudoku which would deem the sudoku invalid. There is also a function, check_solved(), which checks that the sudoku is valid AND have no more blanks AND is not empty.

basic_solve() traverses the grid and looks for any row, column or tiny grid (called a box) that has only one possible number. basic_solve() fills that in and recursively runs itself as long as any new number is filled in. Note that the size of the tiny grid (box) is sqrt(sudoku_size). Sudokus solvable by this are grade 1.

get_possible() runs through each row/col/box and lists out all the possibilities. When there is only one possibility left for an entry, it fills that in and is once again recursive, running basic_solve() before itself. Sudokus solvable by this method are grade 2.

remove_twins() is slightly more advanced. It makes use of the fact that if a row has two boxes with the same two possibilities, the rest of the same row cannot have those two numbers. This set is called a twin/ triplet/ quadruplet and so on, depending on how many are in the set. remove_twin() turns each row/col/box into a single row and passes a row of possibilities to twin_check() to narrow down the possibilities. This is recursive and runs until no changes are made to the sudoku (and not the possibilities list as that ultimately does not change the solve).
twin_check() takes in each row and based on the number of non-zeros, churns out all combinations of twins/triplets/quadruplets and so on. It creates and returns a new row of possibilities, with the twins removed.

The last method is guess_solve(), which takes the possibilities list and iterates through it to find a possible solution. This functions returns the first viable solution starting from the top of the possibilities list, which may not be the only solution. First, a copy of the original sudoku is made. Then, each member from the list of possibilities is used to propagate through the sudoku until a solution is obtained or the sudoku becomes invalid. We know that if there are, e.g. 3 possible entries in a blank, if two of them result in invalid solutions, the last one would be the correct number for that entry. This logic is handled by poss_check variable in this function. This function is also recursive and uses all 3 previous method in attempt_solve() for each member in the possibilities list.
attempt_solve() uses techniques 1 to 3 and returns an empty list when unsolvable. This is used in guess_solve(), where is the result is empty, that possibility is invalid and the next possibility is used.

The function solve() merely combines all the previous techniques and prints the level that the sudoku is on.

In conclusion, use this sudoku solver and you never have to play with a boring sudoku again!
