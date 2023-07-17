from math import factorial


def binomial_coefficient(total_items, items_chosen):
    """Calculates the binomial coefficient."""
    # Formula -> b! / (a! * (b - a)!)
    return (factorial(total_items) // (factorial(items_chosen)
            * factorial(total_items - items_chosen)))


def count_routes_in_grid(grid_size):
    """Calculates the number of routes through a grid using combinatorics."""
    return binomial_coefficient(2 * grid_size, grid_size)


grid_size = 20

print(count_routes_in_grid(grid_size))
