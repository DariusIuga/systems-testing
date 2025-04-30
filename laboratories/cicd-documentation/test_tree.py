import unittest

from tree import Node, Tree


class TestTreeFind(unittest.TestCase):

    def setUp(self):
        """Set up a sample tree for testing."""
        self.tree = Tree()
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(12)
        self.tree.add(18)
        # Tree structure:
        #      10
        #     /  \
        #    5    15
        #   / \  /  \
        #  3   7 12  18

    def test_find_existing_node_left_subtree(self):
        """Test finding a node that exists in the left subtree."""
        found_node = self.tree.find(7)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 7)

    def test_find_existing_node_right_subtree(self):
        """Test finding a node that exists in the right subtree."""
        found_node = self.tree.find(12)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 12)

    def test_find_root_node(self):
        """Test finding the root node."""
        found_node = self.tree.find(10)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 10)
        self.assertIs(found_node, self.tree.getRoot())

    def test_find_non_existent_node(self):
        """Test finding a node that does not exist in the tree."""
        found_node = self.tree.find(99)
        self.assertIsNone(found_node)

    def test_find_in_empty_tree(self):
        """Test finding in an empty tree."""
        empty_tree = Tree()
        found_node = empty_tree.find(10)
        self.assertIsNone(found_node)


if __name__ == "__main__":
    unittest.main()
