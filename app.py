#!/usr/bin/env python

import web
from urls import urls

app = web.application(urls, globals())

class index:
    def GET(self):
        return "Hello world!"


class about:
    def GET(self):
        return "About me"

if __name__ == "__main__":
    app.run()
