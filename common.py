import time
from collections.abc import Callable
from enum import Enum


class State(Enum):
    ALIVE = "*"
    DEAD = "-"

    def __str__(self) -> str:
        return self.value


class Grid:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.rows = [[State.DEAD for _ in range(width)] for _ in range(height)]

    def get(self, x: int, y: int) -> State:
        return self.rows[y % self.height][x % self.width]

    def set(self, x: int, y: int, state: State) -> None:
        self.rows[y % self.height][x % self.width] = state

    def __str__(self) -> str:
        return "\n".join("".join(str(cell) for cell in row) for row in self.rows)


def count_neighbors(y: int, x: int, get: Callable[[int, int], State]) -> int:
    n_ = get(y - 1, x + 0)  # North
    ne = get(y - 1, x + 1)  # Northeast
    e_ = get(y + 0, x + 1)  # East
    se = get(y + 1, x + 1)  # Southeast
    s_ = get(y + 1, x + 0)  # South
    sw = get(y + 1, x - 1)  # Southwest
    w_ = get(y + 0, x - 1)  # West
    nw = get(y - 1, x - 1)  # Northwest
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    return neighbor_states.count(State.ALIVE)


def game_logic(state: State, neighbors: int) -> State:
    if state == State.ALIVE:
        if neighbors < 2:
            return State.DEAD  # Die: Too few
        elif neighbors > 3:
            return State.DEAD  # Die: Too many
    else:
        if neighbors == 3:
            return State.ALIVE  # Regenerate
    return state


def step_cell(y: int, x: int, get: Callable[[int, int], State], set: Callable[[int, int, State], None]) -> None:
    current_state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_state = game_logic(current_state, neighbors)
    set(y, x, next_state)


def simulate(grid: Grid) -> Grid:
    new_grid = Grid(grid.height, grid.width)
    for y in range(grid.height):
        for x in range(grid.width):
            step_cell(y, x, grid.get, new_grid.set)
    return new_grid


if __name__ == "__main__":
    grid = Grid(5, 9)
    grid.set(0, 3, State.ALIVE)
    grid.set(1, 4, State.ALIVE)
    grid.set(2, 2, State.ALIVE)
    grid.set(2, 3, State.ALIVE)
    grid.set(2, 4, State.ALIVE)
    for _ in range(50):
        print(grid)
        time.sleep(0.5)
        grid = simulate(grid)
