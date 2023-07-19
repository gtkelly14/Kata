def path_finder(maze):
    return


if __name__ == "__main__":

    TARGET_MAZE = "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...W.",
        "...W."])
    # test.assert_equals(path_finder(a), True)

    TARGET_MAZE = "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...WW",
        "...W."])
    # test.assert_equals(path_finder(a), False)

    TARGET_MAZE = "\n".join([
        "..W",
        ".W.",
        "W.."])
    # test.assert_equals(path_finder(a), False)

    TARGET_MAZE = "\n".join([
        ".WWWW",
        ".W...",
        ".W.W.",
        ".W.W.",
        "...W."])
    # test.assert_equals(path_finder(a), True)

    TARGET_MAZE = "\n".join([
        ".W...",
        "W....",
        ".....",
        ".....",
        "....."])
    # test.assert_equals(path_finder(a), False)

    TARGET_MAZE = "\n".join([
        ".W",
        "W."])
    # test.assert_equals(path_finder(a), False)
