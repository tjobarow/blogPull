from blogPost import blogPost
from csvStorer import csvStorer

# collection of post objects
blogPosts = {blogPost("jelloisgood.wordpress.com"),blogPost("adonisabdullahitscblog.wordpress.com")}

# iterating over these objects, printing name and text (post parsing)
newCSV = csvStorer(blogPosts)
