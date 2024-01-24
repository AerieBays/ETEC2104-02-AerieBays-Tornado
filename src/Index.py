import tornado.web
import csv

class Handler(tornado.web.RequestHandler):
    def get(self):
        with open('src/users.csv', 'r') as newcsv:
            reader = csv.DictReader(newcsv)
            for row in reader:
                self.write(f'<a href="/profile/{row['username']}">User: {row['name']}<br></a>')
            newcsv.close()