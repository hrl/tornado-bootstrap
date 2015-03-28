import util
from . import urls


__all__ = [
    'mapping',
]


mapping = util.generate_url(urls.urls, urls.apps, __name__)
