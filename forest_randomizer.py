from random import (randrange, shuffle)
from copy import deepcopy
from forest_calculations import (get_forest_dimensions, get_tree_counts)
from forest_transpormations import (flatten_forest, deflatten_forest)
from forest_constants import (LEAFY, CONIFEROUS)


def get_random_position(rows, cols):
    return randrange(rows), randrange(cols)


def randomize_forest_1(forest):
    forest_cpy = deepcopy(forest)
    rows_num, cols_num = get_forest_dimensions(forest_cpy)
    leafy_count, coniferous_count = get_tree_counts(forest_cpy)

    if leafy_count > coniferous_count:
        more_trees = LEAFY
        less_trees = CONIFEROUS
        less_trees_count = coniferous_count

    else:
        more_trees = CONIFEROUS
        less_trees = LEAFY
        less_trees_count = leafy_count

    for row_index, row in enumerate(forest_cpy):
        for col_index, _ in enumerate(row):
            forest_cpy[row_index][col_index] = more_trees

    for _ in range(less_trees_count):
        while True:
            random_row, random_col = get_random_position(rows_num, cols_num)
            if forest_cpy[random_row][random_col] != less_trees:
                forest_cpy[random_row][random_col] = less_trees
                break
    return forest_cpy


def randomize_forest_2(forest):
    rows, _ = get_forest_dimensions(forest)
    flat_forest = flatten_forest(forest)
    shuffle(flat_forest)
    return deflatten_forest(flat_forest, rows)
