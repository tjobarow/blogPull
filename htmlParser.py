from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    content=""
    def handle_data(self, data):
        self.content += data+" "
