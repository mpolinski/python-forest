def flatten_forest(forest):
    flat_forest = []
    for row in forest:
        flat_forest += row
    return flat_forest


def deflatten_forest(forest_1d, rows):
    cols = len(forest_1d) // rows
    forest_2d = []
    for i in range(cols):
        forest_slice = forest_1d[i*cols: (i+1)*cols]
        forest_2d.append(forest_slice)
    return forest_2d
