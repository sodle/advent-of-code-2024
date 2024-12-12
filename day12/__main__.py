import sys

Garden = list[list[str]]
Inventory = set[str]
Coordinate = tuple[int, int]
Plot = set[Coordinate]


def read_input() -> tuple[Garden, Inventory]:
    garden = []
    inventory = set()
    for line in sys.stdin.readlines():
        if len(line) > 0:
            row = [c for c in line if c.isalpha()]
            garden.append(row)
            inventory = inventory.union(row)
    return garden, inventory


def part1(garden: Garden, inventory: Inventory) -> int:
    plots: dict[str, list[Plot]] = {s: [] for s in inventory}

    height = range(len(garden))
    width = range(len(garden[0]))

    for y, row in enumerate(garden):
        for x, crop in enumerate(row):
            matching_plots = plots[crop]

            # check if we can join the plot to our left side
            left = x - 1
            left_plot = None
            if left in width:
                if garden[y][left] == crop:
                    for plot in matching_plots:
                        if (y, left) in plot:
                            plot.add((y, x))
                            left_plot = plot

            # check if we can join the plot above us
            up = y - 1
            up_plot = None
            if up in height:
                if garden[up][x] == crop:
                    for plot in matching_plots:
                        if (up, x) in plot:
                            plot.add((y, x))
                            up_plot = plot

            if not (left_plot or up_plot):
                matching_plots.append({(y, x)})

            # if we joined two different plots, merge them
            if left_plot is not None and up_plot is not None and up_plot != left_plot:
                matching_plots.remove(left_plot)
                matching_plots.remove(up_plot)
                matching_plots.append(left_plot.union(up_plot))

    acc = 0
    for crop, crop_plots in plots.items():
        for plot in crop_plots:
            area = len(plot)
            perimeter = 0
            for y, x in plot:
                point_perimeter = 4
                if (y - 1, x) in plot:
                    point_perimeter -= 1
                if (y + 1, x) in plot:
                    point_perimeter -= 1
                if (y, x - 1) in plot:
                    point_perimeter -= 1
                if (y, x + 1) in plot:
                    point_perimeter -= 1
                perimeter += point_perimeter
            acc += area * perimeter

    return acc


if __name__ == "__main__":
    garden, inventory = read_input()
    print(f"Part 1:\t{part1(garden, inventory)}")
