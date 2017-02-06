#!/usr/bin/env python

import os
from bottle import route, run, static_file, template, view

# ***************** #
# Helpers           #
# ***************** #


# ***************** #
# Views             #
# ***************** #

@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./static/js')


@route('/img/<filename>')
def img_static(filename):
    return static_file(filename, root='./static/img')


@route('/css/<filename>')
def img_static(filename):
    return static_file(filename, root='./static/css')


@route("/")
@view("main")
def hello():
    return dict(title="Hello", content="Hello from Python!")

# ***************** #
# MAIN              #
# ***************** #

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    run(
        host='localhost',
        port=port,
        debug=True,
    )
