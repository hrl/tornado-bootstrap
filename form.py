import re

import tornado.locale

from tornado.escape import _unicode
from tornado.util import unicode_type

import wtforms.form


class WTFormsTornadoTranslationWarpper(object):
    def __init__(self, locale_code):
        self.locale = tornado.locale.get(locale_code)

    def gettext(self, string):
        return self.locale.translate(string)

    def ngettext(self, singular, plural, n):
        return self.locale.translate(singular, plural, n)


class WTFormsTornadoArgumentsWarpper(dict):
    def getlist(self, key):
        """
        tornado.web.RequestHandler._get_arguments
        """
        try:
            _remove_control_chars_regex = re.compile(r"[\x00-\x08\x0e-\x1f]")
            values = []
            for v in self.get(key, []):
                if isinstance(v, bytes):
                    v = _unicode(v)
                if isinstance(v, unicode_type):
                    v = _remove_control_chars_regex.sub(" ", v)
                values.append(v)
            return values
        except UnicodeDecodeError:
            return []


class Form(wtforms.form.Form):
    class Meta:
        def get_translations(self, form):
            if not hasattr(form, '_locale_code'):
                form._locale_code = "en_US"
            return WTFormsTornadoTranslationWarpper(form._locale_code)

    def __init__(self, formdata=None, obj=None, prefix='', data=None, meta=None,
                 locale_code="en_US", **kwargs):
        self._locale_code = locale_code
        self.kwargs = kwargs
        super(Form, self).__init__(formdata, obj, prefix, data, meta, **kwargs)

    def process(self, formdata=None, obj=None, data=None, **kwargs):
        if formdata is not None \
                and not hasattr(formdata, 'getlist') \
                and not hasattr(formdata, 'getall'):
            formdata = WTFormsTornadoArgumentsWarpper(formdata)
        super(Form, self).process(formdata, obj, data, **kwargs)
