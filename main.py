import re
import sys
from typing import List, Tuple


class Rover:
    """
    Represents a Mars rover with a position (x, y) and a direction (N, E, S, W).
    The rover can process instructions to move or turn on a plateau of given size.
    """

    DIRECTIONS = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}

    TURNS = {
        ("N", "L"): "W",
        ("N", "R"): "E",
        ("E", "L"): "N",
        ("E", "R"): "S",
        ("S", "L"): "E",
        ("S", "R"): "W",
        ("W", "L"): "S",
        ("W", "R"): "N",
    }

    def __init__(self, x: int, y: int, d: str, plateau_size: Tuple[int, int]):
        self.x = x
        self.y = y
        self.direction = d
        self.max_x, self.max_y = plateau_size

    def process_instruction(self, instruction: str) -> None:
        """
        Process a single instruction to either move the rover or change its direction.

        :param instruction: A single-character string representing the instruction ('L', 'R', or 'M').
        """
        if instruction in ("L", "R"):
            self._turn(instruction)
        elif instruction == "M":
            self._move()

    def _turn(self, direction: str) -> None:
        """
        Update the rover's direction based on the given turn instruction ('L' or 'R').

        :param direction: A single-character string representing the turn instruction ('L' for left or 'R' for right).
        """
        self.direction = self.TURNS[(self.direction, direction)]

    def _move(self) -> None:
        """
        Move the rover one grid point forward in its current direction, if the new position is within the plateau boundaries.
        """
        dx, dy = self.DIRECTIONS[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x <= self.max_x and 0 <= new_y <= self.max_y:
            self.x = new_x
            self.y = new_y

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.direction}"


# process final rover position from instruction list
def process_rover(pos: str, instructions: str, plateau_size: Tuple[int, int]) -> str:
    """
    Process rover's position and instructions to determine its final position on the plateau.

    :param pos: A string representing the rover's initial position (e.g., '1 2 N').
    :param instructions: A string containing space-separated instructions for the rover (e.g., 'L M L M L M L M M').
    :param plateau_size: A tuple containing the plateau size (max_x, max_y).
    :return: A string representing the rover's final position (e.g., '1 3 N').
    """
    x, y, d = pos.split()
    rover = Rover(int(x), int(y), d, plateau_size)
    for instruction in instructions:
        rover.process_instruction(instruction)
    return str(rover)


def parse_input(input_str: str) -> Tuple[Tuple[int, int], List[Tuple[str, str]]]:
    """
    Parse the input string and extract plateau size and rover information.

    :param input_str: A string containing the formatted input data to validate
    :return: A tuple containing the plateau size as a tuple of integers (max_x, max_y) and a list of rover information.
    """
    input_list = input_str.strip().split("\n")

    # validate and extract plateau size
    plateau_size = tuple(map(int, input_list[0].split()))
    if len(plateau_size) != 2 or not all(x >= 0 for x in plateau_size):
        raise ValueError("invalid plateau size")

    rover_data = []
    rover_input_list = input_list[1:]

    if len(rover_input_list) % 2 != 0:
        raise ValueError("missing rover instructions")

    position_pattern = re.compile(r"^\d+ \d+ [NESW]$")
    instruction_pattern = re.compile(r"^([LRM]\s*)+$")

    for i in range(0, len(rover_input_list), 2):
        rover_position = rover_input_list[i]
        rover_instructions = rover_input_list[i + 1]

        if not position_pattern.match(rover_position) or not instruction_pattern.match(
            rover_instructions
        ):
            raise ValueError("invalid rover position or instructions")
        rover_data.append((rover_position, rover_instructions))

    return plateau_size, rover_data


def main():
    """
    Main function to read input data, process rover instructions, and output the final positions of all rovers.
    """
    # input format: upper-right coordinates of the plateau, followed by rover positions and instructions
    try:
        plateau_size, rover_data = parse_input(sys.stdin.read())
    except ValueError as e:
        print(e)
        return

    # process each rover and print final position
    for rover_position, rover_instructions in rover_data:
        final_position = process_rover(rover_position, rover_instructions, plateau_size)
        print(final_position)


if __name__ == "__main__":
    main()
