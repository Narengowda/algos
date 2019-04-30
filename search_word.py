
def read():
    grid = []
    words = []
    stop = 0

    try:
        while True:
            print('reading')
            if stop == 0:
                data = raw_input()
                grid.append(list(data))

            if stop == 1:
                data = raw_input()
                words.append(data)

            if not data:
                stop += 1
    except EOFError:
        return grid, words

# READ the data

# grid, words = read()

raw_grid = """ELEKTRAHTHORGV
SILVERAORWTNSH
AUAUAWREHSINUP
HNERKCTNWHAMRR
AFTEHSIITMASFA
ICYMILDRRNCAEA
IEIMAOIEEAERRL
WWYTWNDVRMGEIO
INVIDIBLEGAGRO
TDHSPAEOHDCNOP
CIOSKTTZTGEAND
HFKOKPRNNLKRMA
EBWOMANPAEUTAE
UOFALCONPFLSND"""

raw_words = """ANTMAN
DAREDEVIL
DEADPOOL
ELEKTRA
HAWKEYE
PUNISHER
THING
WITCH"""

out = {}
grid = [list(x) for x in raw_grid.split()]
words = [x for x in raw_words.split()]

words_map = {w: w for w in words}
max_word_len = max([len(w) for w in words])

def _children(r, c):
    return [[r+1, c], [r+1, c], [r-1, c], [r, c-1], [r+1, c+1], [r+1, c-1], [r-1, c-1], [r-1, c+1]]

def get_children(r, c):
    # out = []
    # Can use filter and lambda

    return filter(lambda child: child[0] >=0  and child[0] < len(grid) and child[1] >= 0 and child[1] < len(grid[0]), _children(r,c))

    # for child in _children(r,c):
    #     if child[0] >=0  and child[0] < len(grid) and child[1] >= 0 and child[1] < len(grid[0]):
    #         out.append(child)
    # return out


def dfs(r, c, string, visited, source):
    letter = grid[r][c]

    if string + letter in words_map:
        if string + letter not in out:
            out[string + letter] = source
        return

    if not any([s.startswith(string + letter) for s in words_map.keys()]):
        return

    if len(string + letter) > max_word_len:
        return

    childrens = get_children(r, c)
    for rc, cc in childrens:
        if (rc, cc) not in visited:
            dfs(rc, cc, string + letter, visited[::] + [(rc, cc)], source)


# Search
for r in range(len(grid)):
    for c in range(len(grid[0])):
        dfs(r, c, "", [], (r, c))


for k, v in sorted(out.items(), key=lambda x: x[0]):
    print k, v[0], v[1]


