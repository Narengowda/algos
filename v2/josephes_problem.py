def joseph(start, soldiers):

    qqq = 1 if start else 0
    alive = [s for i, s in enumerate(soldiers) if (i+1) % 2 == qqq]

    if len(alive) == 1:
        print alive, " Found pos"
        return

    end = soldiers[-1] == alive[-1]
    joseph(not end, alive)

joseph(True, range(1, 13))
