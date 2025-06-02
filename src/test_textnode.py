import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", "bold")
        node4 = TextNode("This is a text node", "link")
        node5 = TextNode("This is a node", "bold")
        node6 = TextNode("This is a text node", "bold", None)
        node7 = TextNode("This is a text node", "bold", "boot.dev")
        self.assertEqual(node, node2)
        self.assertEqual(node, node3)
        self.assertEqual(node, node6)

    def test_ne(self):
        node3 = TextNode("This is a text node", "bold")
        node4 = TextNode("This is a text node", "link")
        node5 = TextNode("This is a node", "bold")
        node7 = TextNode("This is a text node", "bold", "boot.dev")
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node3, node5)
        self.assertNotEqual(node3, node7)


if __name__ == "__main__":
    unittest.main()