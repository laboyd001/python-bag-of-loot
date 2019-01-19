# ==================================================
# TESTING FILE
# python test_lootbag.py -v
# ==================================================
# Each feature of the app must be tested. Use Python's unittest module to create test coverage for the following app requirements

import unittest
import sys
sys.path.append('../')
from lootbag import Lootbag


def setUpModule():
      print('set up module')

def tearDownModule():
  print('tear down module')

class TestLootbag(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setup class')
        cls.lootbag = Lootbag('../lootbag.db')

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

# ==================================================
# 1. Items can be added to bag, and assigned to a child.
# ==================================================

    def test_add_gift(self):
        result = self.lootbag.addGift({
            "name": "ball",
            "child_name": "bob"
        })
        expected = ({
            "name": "ball",
            "child_name": "bob"
        })
        print("result", result)
        print("expected",expected)
        self.assertEqual(result, expected)
        self.assertNotEqual(self.lootbag.addGift({
            "name":"boat",
            "child_name":"timmy"
        }), ({
            "name":"racecar",
            "child_name":"timmy"
        }))


# ==================================================
# 2. Items can be removed from bag, per child. Removing ball from the bag should not be allowed. A child's name must be specified.
# ==================================================

# ==================================================
# # 3. Must be able to list all children who are getting a toy.
# ===================================================

# ==================================================
# 4. Must be able to list all toys for a given child's name.
# ===================================================

# ===================================================
# # 5. Must be able to set the delivered property of a child's toys -- which defaults to false-- to true.
# ==================================================

if __name__ == '__main__':
    unittest.main()
