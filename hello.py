#!/usr/bin/env python
# coding: utf-8


from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write(
            template.render(
                'template/index.html',
                {'title': "ohayo-", 'name': "tyru"}
            )
        )

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
