import tornado.web

from . import forms


__all__ = [
    'ExampleHandler',
]


class ExampleHandler(tornado.web.RequestHandler):
    def get(self):
        form = forms.ExampleForm(self.request.arguments,
                                 locale_code=self.locale.code)
        if form.validate():
            if form.n.data is None:
                self.finish("n is None")
            else:
                self.finish("n == %d" % form.n.data)
        else:
            self.set_status(400)
            self.finish(repr(form.errors))
