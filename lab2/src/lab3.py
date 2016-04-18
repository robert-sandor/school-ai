from random import randint, random


def bintournir(population, x=None, y=None):
    if len(population) <= 0:
        return None

    if len(population) == 1:
        return population[0]

    if x is None:
        x = randint(0, len(population) - 1)
    if y is None:
        y = x
        while y == x:
            y = randint(0, len(population) - 1)

    if population[x] < population[y]:
        return population[x]
    else:
        return population[y]


def cross(crom1, crom2, prob, x=None):
    a = random()
    if a > prob:
        return crom1, crom2

    if len(crom1) == 0 or len(crom2) == 0 or len(crom1) != len(crom2):
        return None

    if x is None:
        x = randint(0, len(crom1))

    x += 1
    return crom1[:x] + crom2[x:], crom2[:x] + crom1[x:]


def hardmutation(crom, pm):
    for i in range(0, len(crom)):
        a = random()
        if a < pm:
            crom[i] = (crom[i] + 1) % 2
    return crom


if __name__ == '__main__':
    assert bintournir([]) is None
    assert bintournir([1]) == 1
    assert bintournir([1, 2], 0, 1) == 1
    assert bintournir([1, 2, 3, 4, 5, 6], 4, 5) == 5
    assert bintournir([1, 2]) == 1

    assert cross([], [], 1) is None
    assert cross([1, 1, 1], [1, 1], 1) is None
    assert cross([], [], 0, 1) == ([], [])
    assert cross([1, 1, 0], [1, 0, 0], 1, 2) == ([1, 1, 0], [1, 0, 0])
    assert cross([1, 0, 1, 1, 0], [1, 1, 0, 0, 0], 1, 2) == ([1, 0, 1, 0, 0], [1, 1, 0, 1, 0])

    assert hardmutation([1, 0, 1, 1, 0], 1) == [0, 1, 0, 0, 1]
    assert hardmutation([], 1) == []
    assert hardmutation([1, 1, 1], 1) == [0, 0, 0]
    assert hardmutation([0, 0, 0], 1) == [1, 1, 1]
    assert hardmutation([1, 1, 1], 0) == [1, 1, 1]
