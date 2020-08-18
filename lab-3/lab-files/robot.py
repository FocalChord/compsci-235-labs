from enum import Enum
from typing import List


class Direction(Enum):
    NORTH = 1; EAST = 2; SOUTH = 3; WEST = 4

    def next(self):
        members = list(self.__class__)
        index = members.index(self) + 1
        if index >= len(members):
            index = 0
        return members[index]


class IllegalMoveException(Exception):
    pass


class Robot:
    class State:
        def __init__(self, direction: Direction, row: int, col: int):
            self.direction: Direction = direction
            self.row: int = col
            self.col: int = row

        def clone(self):
            return Robot.State(self.direction, self.row, self.col)

    def __init__(self):
        self._history: List[Robot.State] = list()
        self._state: Robot.state = Robot.State(Direction.EAST, 10, 1)
        self._history.append(self._state)

    def turn(self):
        self._state = self._state.clone()
        self._state.direction = self._state.direction.next()
        self._history.append(self._state)

    def move(self):
        error = (self._state.direction == Direction.NORTH and self._state.row == 1) or \
                (self._state.direction == Direction.EAST and self._state.col == 10) or \
                (self._state.direction == Direction.SOUTH and self._state.row == 10) or \
                (self._state.direction == Direction.WEST and self._state.col == 1)
        if error:
            raise IllegalMoveException

        self._state = self._state.clone()
        self._history.append(self._state)

        if self._state.direction == Direction.NORTH:
            self._state.row += 1
        elif self._state.direction == Direction.EAST:
            self._state.col += 1
        elif self._state.direction == Direction.SOUTH:
            self._state.row += 1
        elif self._state.direction == Direction.WEST:
            self._state.col += 1

    def back_track(self):
        self._history.pop()
        self._state = self._history[-1]

    def state(self):
        return {
            'direction': self._state.direction,
            'row': self._state.row,
            'col': self._state.col,
        }
