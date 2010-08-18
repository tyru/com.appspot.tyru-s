#!/usr/bin/env python
# coding: utf-8


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
  def get(self, path):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write("""
Hello, webapp World!
{outlist}
path = {path}
    """.format(
            outlist="\n".join(["    " + e for e in dir(self.response)]),
            path=repr(path),
        )
    )

application = webapp.WSGIApplication(
                                     [('/(.*)', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
