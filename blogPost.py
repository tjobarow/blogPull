import requests
from htmlParser import MyHTMLParser
# Use '$pip install --user requests'

'''

    In the future, we can use this but loop through
    all of the students' blog urls.
    URL = https://public-api.wordpress.com/rest/v1/sites/
          $site/posts/

'''
class blogPost:

    site = ""
    url = ""
    posts = {}
    content = ""

    def __init__(self, urlStudent):
        self.site = urlStudent
        self.url = ('https://public-api.wordpress.com/rest/v1/sites/' + self.site + '/posts/')
        self.pullPost()

    def pullPost(self):

        # Retrieve info from the given URL
        r = requests.get(self.url)
        print("Success!" if r.status_code == 200 else "Failed")

        # Convert from json to dictionary
        response_dict = r.json()

        # Display the keys
        #print(response_dict.keys())

        # Using the key, display # of Found posts
        #print("Found posts:", response_dict['found'])

        # Explore information about the posts
        self.posts = response_dict['posts']
        #print("Number of posts: ", len(posts))

        # parse the posts html content for plaintext only
        htmlParser = MyHTMLParser()
        htmlParser.feed(self.posts[0]['content'])
        #print("Author login: "+posts[0]['author']['login'])
        #print(htmlParser.content)
        self.content = htmlParser.content

    def getName(self):
        return self.posts[0]['author']['nice_name']

    def getText(self):
        return self.content




