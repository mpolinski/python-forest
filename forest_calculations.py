from forest_constants import (LEAFY, CONIFEROUS)


def get_forest_dimensions(forest):
    rows_num = len(forest)
    cols_num = 0
    if rows_num:
        cols_num = len(forest[0])
    return rows_num, cols_num


def get_tree_counts(forest):
    leafy_count = 0
    coniferous_count = 0

    for row in forest:
        leafy_count += row.count(LEAFY)
        coniferous_count += row.count(CONIFEROUS)

    return leafy_count, coniferous_count
