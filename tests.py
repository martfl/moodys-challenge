import sys
import time
import random
import unittest
from io import StringIO
from main import process_rover, main, Rover, parse_input

class TestRover(unittest.TestCase):
    def setUp(self):
        self.rover1 = Rover(1, 2, 'N', (5, 5))
        self.rover2 = Rover(3, 3, 'E', (5, 5))

    def test_turn_left(self):
        self.rover1._turn('L')
        self.assertEqual(self.rover1.direction, 'W')

    def test_turn_right(self):
        self.rover2._turn('R')
        self.assertEqual(self.rover2.direction, 'S')

    def test_move_north(self):
        self.rover1._move()
        self.assertEqual(self.rover1.x, 1)
        self.assertEqual(self.rover1.y, 3)

    def test_move_east(self):
        self.rover2._move()
        self.assertEqual(self.rover2.x, 4)
        self.assertEqual(self.rover2.y, 3)

    def test_move_out_of_bounds(self):
        rover3 = Rover(5, 5, 'N', (5, 5))
        rover3._move()
        self.assertEqual(rover3.x, 5)
        self.assertEqual(rover3.y, 5)

    def test_process_rover(self):
        result = process_rover('1 2 N', 'LMLMLMLMM', (5, 5))
        self.assertEqual(result, '1 3 N')

class TestParseInput(unittest.TestCase):
    def test_invalid_plateau_size(self):
        with self.assertRaises(ValueError):
            parse_input('5 -5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM\n')

    def test_invalid_rover_position(self):
        with self.assertRaises(ValueError):
            parse_input('5 5\n1 2 X\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM\n')

    def test_invalid_rover_instructions(self):
        with self.assertRaises(ValueError):
            parse_input('5 5\n1 2 N\nLMLMLMLMX\n3 3 E\nMMRMMRMRRM\n')

    def test_missing_rover_instructions(self):
        with self.assertRaises(ValueError):
            parse_input('5 5\n1 2 N\nLMLMLMLMM\n3 3 E\n')

    def test_whitespace_instructions(self):
        plateau_size, rover_data = parse_input('5 5\n1 2 N\nL M L M L M L M M\n3 3 E\nM M R M M R M R R M\n')
        self.assertEqual(plateau_size, (5, 5))
        self.assertEqual(rover_data, [('1 2 N', 'L M L M L M L M M'), ('3 3 E', 'M M R M M R M R R M')])

class TestMain(unittest.TestCase):
    def test_main(self):
        input_str = '5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM\n'
        expected_output = '1 3 N\n5 1 E\n'
        output = StringIO()
        sys.stdin = StringIO(input_str)
        sys.stdout = output
        main()
        self.assertEqual(output.getvalue(), expected_output)

class TestPerformance(unittest.TestCase):
    def test_large_input(self):
        plateau_size = (1000, 1000)
        num_rovers = 100

        # Generate random rover positions and instructions
        input_str = f"{plateau_size[0]} {plateau_size[1]}\n"
        for _ in range(num_rovers):
            x = random.randint(0, plateau_size[0])
            y = random.randint(0, plateau_size[1])
            d = random.choice(['N', 'E', 'S', 'W'])
            instructions = ' '.join(random.choices(['L', 'R', 'M'], k=200))
            input_str += f"{x} {y} {d}\n{instructions}\n"

        start_time = time.time()
        sys.stdin = StringIO(input_str)
        sys.stdout = StringIO()
        main()
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        self.assertLess(elapsed_time, 10)


if __name__ == '__main__':
    unittest.main()

