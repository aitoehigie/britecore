#!/usr/bin/env python

from app import app

wsgiapp = app.wsgifunc()
