import unittest
import cnwgl

class TestToroidalNCount(unittest.TestCase):
    """ Test related to cell neighbours counting """

    def setUp(self):
        self.field = [
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        ]

    def test_inbound_empty(self):
        self.assertEqual(0, cnwgl.countN(2, 1, self.field))
    
    def test_inbound_with_n(self):
        self.assertEqual(1, cnwgl.countN(2, 6, self.field))

    def test_inbound_on_alive_with_empty(self):
        self.assertEqual(0, cnwgl.countN(3, 6, self.field))
    
    def test_inbound_on_dead_with_8_n(self):
        self.assertEqual(8, cnwgl.countN(2, 9, self.field))
    
    def test_inbound_on_alive_with_8_n(self):
        self.assertEqual(8, cnwgl.countN(2, 12, self.field))
    
    def test_outbound_on_dead_with_2_n(self):
        self.assertEqual(2, cnwgl.countN(0, 15, self.field))
    
    def test_outbound_on_alive_with_1_n(self):
        self.assertEqual(2, cnwgl.countN(3, 17, self.field))

class TestGenerateNext(unittest.TestCase):
    """ Test conway's generator rules validity """

    def test_check_generations(self):
        field = [
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        cnwgl.generateNext(field)
        self.assertEqual([
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
        ], field)

        cnwgl.generateNext(field)
        self.assertEqual([
            [1, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ], field)

if __name__ == '__main__':
    unittest.main()