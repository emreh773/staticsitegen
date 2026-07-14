import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="div", value="This is a div", children=[], props={"href": "http://example.com", "target": "_blank"})
        node2 = HTMLNode(tag="div", value="This is a div", children=[], props={"href": "http://example.com", "target": "_blank"})
        node3 = HTMLNode(tag="span", value="This is a span", children=[], props={"href": "http://example.com", "target": "_blank"})
        node4 = HTMLNode(tag="div", value="This is a div", children=[], props={"href": "http://example.org", "target": "_blank"})
        node5 = HTMLNode(tag="div", value="This is a div", children=[], props={"href": "http://example.com", "target": "_self"})
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)

if __name__ == "__main__":
    unittest.main()
