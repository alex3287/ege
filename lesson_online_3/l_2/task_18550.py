print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((y <= z) or ((not x) and w)) == (w == z):
                    print(x, y, z, w)
