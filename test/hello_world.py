# coding: utf-8

import sys
from bottle.bottle import run, route

@route('/')
def hello():
    return 'hello, world'


def main():
    run(host='localhost', port=9001)

if __name__ == "__main__":
    sys.exit(main())