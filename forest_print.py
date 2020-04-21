from forest_calculations import get_tree_counts
from forest_constants import (LEAFY, CONIFEROUS)


def print_forest(forest, print_tree_counts=True):
    print('*' * 20)
    for forest_row in forest:
        print(' '.join(
            list(
                map(str, forest_row)
            )
        )
        )
    if print_tree_counts:
        print('-' * 5)
        print(get_tree_counts(forest))
    print('*' * 20)


def pretty_print_forest(forest):
    print('*' * 20)
    for forest_row in forest:
        print(' '.join(list(map(get_tree_stage_1, forest_row))))
        print(' '.join(list(map(get_tree_stage_2, forest_row))))
        print(' '.join(list(map(get_tree_stage_3, forest_row))))
        print()

    print('*' * 20)


def get_tree_stage_1(tree_type):
    return get_tree_str(tree_type, 0)


def get_tree_stage_2(tree_type):
    return get_tree_str(tree_type, 1)


def get_tree_stage_3(tree_type):
    return get_tree_str(tree_type, 2)


def get_tree_str(tree_type, stage):
    leafy_stages = [
        ' /\\ ',
        '(  )',
        ' || ',
    ]
    coniferous_stages = [
        ' /\\ ',
        '/  \\',
        ' || ',
    ]

    if tree_type == LEAFY:
        return leafy_stages[stage]
    else:
        return coniferous_stages[stage]
