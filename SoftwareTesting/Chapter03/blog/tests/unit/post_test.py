from unittest import TestCase
from post import Post

class Post_Test(TestCase):
    def test_create_post(self):
        post = Post("Test Title", "Test Content")
        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.content, "Test Content")
        
    def test_json(self):
        post = Post("Test Title", "Test Content")
        expected = {"title": "Test Title", "content": "Test Content"}
        self.assertDictEqual(expected, post.json())