from functools import lru_cache

# +1 *2 или *3 (2)
# >= 69
# 10  1 <= s <= 58


def move(pos):
    h1, h2 = pos
    return (h1+1, h2), (h1*2, h2), (h1, h2+1), (h1, h2*3)


@lru_cache(None)
def game(pos):
    if sum(pos) >= 69:
        return 'W'
    if any(game(i) == 'W' for i in move(pos)):
        return 'P1'
    if all(game(i) == 'P1' for i in move(pos)):
        return 'B1'
    if any(game(i) == 'B1' for i in move(pos)):
        return 'P2'
    if all(game(i) == 'P2' or game(i) == 'P1' for i in move(pos)):
        return 'B2'


# p = (9, 21)
# print(game(p))
for i in range(1, 59):
    pos = (10, i)
    if game(pos) is not None:
        print(i, game(pos))