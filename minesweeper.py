def count_adjacent_mines(mine):

    length = len(mine)
    width = len(mine[0])

    # pad the mine
    padded_mine = [["-"] * (width + 2)]

    for row in mine:
        padded_mine.append(["-"] + row + ["-"])

    padded_mine.append(["-"] * (width + 2))

    for i in range(1, length + 1):
        for j in range(1, width + 1):

            # if the cell itself is a mine, keep it
            if padded_mine[i][j] == "#":
                continue

            count = 0

            for x, y in [(-1,-1),(-1,0),(-1,1),
                         (0,-1),       (0,1),
                         (1,-1),(1,0),(1,1)]:

                if padded_mine[i + x][j + y] == "#":
                    count += 1

            padded_mine[i][j] = count

    return [row[1:-1] for row in padded_mine[1:-1]]


def main():

    mine = [["-", "-", "-", "#", "#"],
            ["-", "#", "-", "-", "-"],
            ["-", "-", "#", "-", "-"],
            ["-", "#", "#", "-", "-"],
            ["-", "-", "-", "-", "-"]]

    for row in count_adjacent_mines(mine):
        print(" ".join(str(x) for x in row))


if __name__ == "__main__":
    main()