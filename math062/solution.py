"""
Cubic Permutations
"""


def answer():
    """
    answer function
    """
    cubes = {}
    n = 345
    while True:
        cube = n**3
        cube_str = "".join(sorted(str(cube)))
        if cube_str not in cubes:
            cubes[cube_str] = []
        cubes[cube_str].append(cube)
        if len(cubes[cube_str]) == 5:
            return cubes[cube_str][0]
        n += 1


if __name__ == "__main__":
    print("Math062")
    print("answer() =", answer(), "\n")
