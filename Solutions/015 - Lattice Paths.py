from math import factorial


def binomial_coefficient(total_items, items_chosen):
    return (factorial(total_items) // (factorial(items_chosen)
            * factorial(total_items - items_chosen)))


def count_routes_in_grid(grid_size):
    return binomial_coefficient(2 * grid_size, grid_size)


grid_size = 20

print(count_routes_in_grid(grid_size))
