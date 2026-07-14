import unittest
from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag="a", value="This is a link", props={"href": "http://example.com", "target": "_blank"})
        node2 = LeafNode(tag="a", value="This is a link", props={"href": "http://example.com", "target": "_blank"})
        node3 = LeafNode(tag="a", value="This is a different link", props={"href": "http://example.com", "target": "_blank"})
        node4 = LeafNode(tag="a", value="This is a link", props={"href": "http://example.org", "target": "_blank"})
        node5 = LeafNode(tag="a", value="This is a link", props={"href": "http://example.com", "target": "_self"})
        node6 = LeafNode("p", "Hello, world!")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)
        self.assertEqual(node6.to_html(), "<p>Hello, world!</p>")