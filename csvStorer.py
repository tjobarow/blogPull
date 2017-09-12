import csv
import datetime

class csvStorer:
    def __init__(self,posts):
        self.curDate = datetime.date.today()
        print("Please enter your filename: ")
        self.fileName = input() + str(self.curDate) + ".csv"
        self.posts=posts
        print(len(posts))
        self.newCSV()

    def newCSV(self):
        try:
            with open(self.fileName,'xt',encoding='utf-8',newline='') as csvfile:
                filewriter = csv.writer(csvfile, dialect='excel')
                for post in self.posts:
                    filewriter.writerow([post.getName(), post.getText()])
        except FileNotFoundError:
            print("An issue occurred while creating the CSV file!")


