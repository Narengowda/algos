import random
import copy
import pprint

pp = pprint.PrettyPrinter(indent=4)

LEN_X = LEN_Y = 10


colors = range(0, 4)

colors_map = {c: None for c in colors}


def generate_box():
    x = []
    for i in range(10):
        x.append([random.randint(0, 3) for j in range(10)])
    return x


def get_siblings(x, y):
    siblings = []

    if y + 1 < LEN_Y:
        siblings.append((x, y + 1))
    if x + 1 < LEN_X:
        siblings.append((x + 1, y))

    return siblings


def flood(box_copy, ref_color, color, x, y):
    box_copy[x][y] = color

    sibs = get_siblings(x, y)
    # print(sibs)
    for sib in sibs:
        if sib and box_copy[sib[0]][sib[1]] == ref_color:
            flood(box_copy, ref_color, color, sib[0], sib[1])


def box_score(box_copy, ref_color, color, x, y, visited):
    score = 0
    sibs = get_siblings(x, y)
    for sib in sibs:
        if sib and box_copy[sib[0]][sib[1]] == ref_color and (sib not in visited):
            visited.append(sib)
            score += box_score(box_copy, ref_color, color, sib[0], sib[1], visited)

    return score + 1


def main():
    # box = generate_box()
    box = [
        [2, 3, 2, 0, 3, 0, 0, 1, 0, 0],
        [2, 2, 0, 2, 0, 1, 1, 1, 3, 0],
        [0, 3, 0, 3, 3, 1, 3, 3, 3, 1],
        [0, 1, 2, 0, 2, 3, 3, 2, 2, 0],
        [3, 1, 2, 2, 1, 0, 0, 3, 3, 2],
        [0, 2, 2, 2, 0, 2, 0, 1, 2, 1],
        [1, 2, 1, 1, 3, 0, 2, 0, 2, 0],
        [3, 0, 3, 0, 1, 0, 2, 3, 1, 3],
        [3, 1, 3, 0, 1, 1, 2, 3, 0, 3],
        [2, 2, 1, 3, 2, 0, 2, 2, 2, 0],
    ]

    # pp.pprint(box)
    # pp.pprint(flood(box, box[0][0], 0, 0, 0))
    # pp.pprint(box)
    # print(box_score(box, box[0][0], 0, 0, 0))

    # exit()

    for i in range(16):

        color_score = []

        for c in colors_map:
            temp_box = copy.deepcopy(box)
            flood(temp_box, temp_box[0][0], c, 0, 0)
            score = box_score(temp_box, temp_box[0][0], c, 0, 0, [])
            print(">>>>>>>>lcal score>>>", c, score)
            color_score.append((score, c, temp_box))

        selected = max(color_score)
        print("MAx=======", selected[0])
        box = selected[2]
        pp.pprint(box)
        if selected[0] == (LEN_X * LEN_Y):
            print("Done")
            pp.pprint(box)

            return


main()
