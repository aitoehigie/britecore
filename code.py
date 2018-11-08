#!/usr/bin/env python

import web
from urls import urls
import config
from config import render

app = web.application(urls, globals())

class Index:
    def GET(self):
        name = "ehigie aito"
        return render.index(name)

    def POST(self):
        data = web.input()
        name, age = data.name, data.age
        pass

class About:
    def GET(self):
        context = {}
        context["string"] = "About me"
        return render.about(context)

if __name__ == "__main__":
    app.run()
