"""
sampleTest.py should be test cases where important functions/algorithms are to be tested against.
"""

import unittest
import Othello
import Algorithms


class OthelloTest(unittest.TestCase):

    def setUp(self):
        self.game = Othello.Othello([
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, 1, 0, None, None, None],
            [None, None, None, 0, 1, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ])

    def tearDown(self):
        self.game = None

    def testGameOver(self):
        self.failUnless(not self.game.is_game_over())

    def testValidPosition(self):
        self.failUnless(self.game.valid_position((2, 4))
                        and self.game.valid_position((3, 5))
                        and self.game.valid_position((5, 3))
                        and self.game.valid_position((4, 2)))

    def testSuccessors(self):
        self.assertEqual(len(self.game.successors()), 4)
        self.assertEqual(self.game.successors()[0].current_player, 0)  # assert that successors have opponent to play next turn.

    def testCountDisk(self):
        self.assertEqual(self.game.count_disks(1), 2)
        self.assertEqual(self.game.count_disks(0), 2)

    def TestPlacePiece(self):
        self.game.place_piece((2, 4))
        self.assertEqual(self.game.count_disks(1), 4)  # White will have 4 disks
        self.assertEqual(self.game.count_disks(0), 1)  # Black should have 1
        self.failUnless(self.game.current_player == 0)  # Should be Black's turn next

# class AlgorithmsTest(unittest.TestCase):
#
#     # def setUp(self):
#     # def tearDown(self):
#     # def tearDown(self):


def main():
    unittest.main()

if __name__ == '__main__':
    main()
