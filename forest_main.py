import sys
from time import time
from forest_print import (print_forest, pretty_print_forest)
from forest_randomizer import (randomize_forest_1, randomize_forest_2)
from forest_generator import generate_forest


def main(rows_num=20, cols_num=20, leafy_to_coniferous_proportion=0.2):
    forest = generate_forest(
        rows_num, cols_num, leafy_to_coniferous_proportion)
    t1 = time()
    forest1 = randomize_forest_1(forest)
    t2 = time()
    forest2 = randomize_forest_2(forest)
    t3 = time()
    diff1 = t2 - t1
    diff2 = t3 - t2
    print('orig forest')
    print_forest(forest)
    print('forest 1')
    print_forest(forest1)
    print('execution time: ', diff1)
    print('forest 2')
    print_forest(forest2)
    print('execution time: ', diff2)
    print('execution time ratio: ', diff1 / diff2)

    if rows_num <= 20 and cols_num <= 20:
        pretty_print_forest(forest2)

    if diff1 > diff2:
        print(
            f'randomize_forest_2 is faster by {(diff1 - diff2)} seconds, it\'s {(diff1 / diff2):.3f} times faster'
        )
    else:
        print(
            f'randomize_forest_1 is faster by {diff2 - diff1} seconds, it\'s {(diff2 / diff1):.3f} times faster'
        )


if __name__ == '__main__':
    rows_num = 10
    cols_num = 10
    leafy_to_coniferous_proportion = 0.33
    try:
        rows_num = int(sys.argv[1])
        cols_num = int(sys.argv[2])
        leafy_to_coniferous_proportion = float(sys.argv[3])
    except IndexError:
        print('default params used: rows:', rows_num, 'cols:', cols_num,
              'tree type ratio:', leafy_to_coniferous_proportion)
    main(rows_num, cols_num, leafy_to_coniferous_proportion)
