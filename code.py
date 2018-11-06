#!/usr/bin/env python

import web
from urls import urls
import config


render = web.template.render("templates/")

app = web.application(urls, globals())

class index:
    def GET(self):
        return render.base()

    def POST(self):
        data = web.input()
        name, age = data.name, data.age
        pass

class about:
    def GET(self):
        return "About me"

if __name__ == "__main__":
    app.run()
