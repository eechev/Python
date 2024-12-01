from unittest import TestCase
from blog import Blog


class Blog_Test(TestCase):
    def test_create_blog(self):
        blog = Blog("Test Blog", "Test Author")
        
        self.assertEqual(blog.title, "Test Blog")
        self.assertEqual(blog.author, "Test Author")
        self.assertListEqual([], blog.posts)
       
    def test_repr(self):
        blog = Blog("Test Blog", "Test Author")
        self.assertEqual(blog.__repr__(), "{} by {} ({} post)".format(blog.title, blog.author, 0))
        
        anotherBlog = Blog("Test Blog 2", "Test Author 2")
        self.assertEqual(anotherBlog.__repr__(), "{} by {} ({} post)".format(anotherBlog.title, anotherBlog.author, 0))
        
    def test_repr_with_multiple_posts(self):
        blog = Blog("Test Blog", "Test Author")
        blog.posts = ["Test Post 1"]
        self.assertEqual(blog.__repr__(), "{} by {} ({} post)".format(blog.title, blog.author, 1))
        
        blog.posts.append("Test Post 2")
        self.assertEqual(blog.__repr__(), "{} by {} ({} posts)".format(blog.title, blog.author, 2))
        
    def test_create_post_in_blog(self):
        blog = Blog("Test Blog", "Test Author")
        blog.create_post("Test Post", "Test Content")
        
        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, "Test Post")
        self.assertEqual(blog.posts[0].content, "Test Content")