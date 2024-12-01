from blog import Blog
from unittest import TestCase

class Blog_Test(TestCase):
    def test_create_post_in_blog(self):
        blog = Blog("Test Blog", "Test Author")
        blog.create_post("Test Post", "Test Content")
        
        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, "Test Post")
        self.assertEqual(blog.posts[0].content, "Test Content")
        
    def test_json_no_posts(self):
        blog = Blog("Test Blog", "Test Author")
        
        expected = {"title": "Test Blog", "author": "Test Author", "posts": []}
        
        self.assertDictEqual(expected, blog.json())
        
        
    def test_json_one_post(self):
        blog = Blog("Test Blog", "Test Author")
        blog.create_post("Test Post", "Test Content")
        
        expected = {
            "title": "Test Blog",
            "author": "Test Author",
            "posts": [
                {
                    "title": "Test Post", 
                    "content": "Test Content"
                }
            ]
        }
        
        self.assertDictEqual(expected, blog.json())
        
    def test_json_multiple_posts(self):
        blog = Blog("Test Blog", "Test Author")
        blog.create_post("Test Post 1", "Test Content 1")
        blog.create_post("Test Post 2", "Test Content 2")
        
        expected = {
            "title": "Test Blog",
            "author": "Test Author",
            "posts": [
                {
                    "title": "Test Post 1", 
                    "content": "Test Content 1"
                },
                {
                    "title": "Test Post 2", 
                    "content": "Test Content 2"
                }
            ]
        }
        
        self.assertDictEqual(expected, blog.json())