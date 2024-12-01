from blog import Blog

MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to create a post, or 'q' to quit."

blogs = dict()


def menu():
    #show the user the avialable blogs
    #let the user make a choice
    #Do something with that choice
    #exit
    print_blogs()
    selection = input(MENU_PROMPT)
    
    while selection != 'q':
        
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print("- {}".format(blog));
        
def ask_create_blog():
    #ask user for the blog title and their name
    blogTitle = input("Enter blog title: ")
    blogAuthor = input("Enter your name: ")
    blogs[blogTitle] = Blog(blogTitle, blogAuthor)

def ask_read_blog():
    #ask for a blog title and print the posts
    blogTitle = input("Enter blog title: ")
    blog = blogs[blogTitle]
    print(blog)

def ask_create_post():
    #ask for a blog title and post title and content and add it to the blog
    blogTitle = input("Enter blog title: ")
    blog = blogs[blogTitle]
    postTitle = input("Enter post title: ")
    postContent = input("Enter post content: ")
    blog.create_post(postTitle, postContent)