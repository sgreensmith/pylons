import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/hello.mako')
        # or, return a string
        return 'Hello World from the index() action'

    def environment(self):
        result = '<HTML><BODY><h1>Environment variables</h1>'
        for key, value in request.environ.items():
            result += '%s: %r <br />' %(key, value)
        result += '</BODY></HTML>'
        return result