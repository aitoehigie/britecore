import web
DB = web.database(dbn='postgres', db='appname', user='username', pw='')
cache = False
render = web.template.render("templates/", base="base")
