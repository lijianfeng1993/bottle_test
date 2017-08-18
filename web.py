#!/usr/bin/env python

import bottle

DEFAULT_HOST = '0.0.0.0'
DEFAULT_PORT = 4501

app = bottle.Bottle()

@app.route('/hello')
def hello():
    hello = 'helloworld!Welcom to cmcc.'
    return hello

if __name__ == '__main__':
    app.run(host = DEFAULT_HOST, port = DEFAULT_PORT)
