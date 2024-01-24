import os

import tornado.web
import random
import csv

quotes = [
    "The only thing we have to fear is fear itself.",
    "Fourscore and seven years ago...",
    "We the People of the United States..."
]

class User:
    def __init__(self, realname, dob, username, email):
        self.name = realname
        self.dob = dob
        self.username = username
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_dob(self):
        return self.dob

    def get_username(self):
        return self.username
class Handler(tornado.web.RequestHandler):
    def get(self):
        user_dict = None
        url = self.request.path
        username = url.split("/profile/")[1]
        with open(f'temp/{username}temp', 'r') as newcsv:
            reader = csv.DictReader(newcsv)
            for row in reader:
                user_dict = row
        self.render("../html/TemplateTest.html", username=user_dict["username"], dob=user_dict["birthday"], email=user_dict["email"], realname=user_dict["name"])
