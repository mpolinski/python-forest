from forest_constants import (CONIFEROUS, LEAFY)


def generate_forest(rows_num, cols_num, leafy_to_coniferous_proportion=0.2):
    trees_num = rows_num * cols_num
    leafy_num = trees_num * leafy_to_coniferous_proportion
    forest = [[] for _ in range(rows_num)]

    counter = 0
    for row in forest:
        for _ in range(cols_num):
            counter += 1
            if counter <= leafy_num:
                row.append(LEAFY)
            else:
                row.append(CONIFEROUS)

    return forest
