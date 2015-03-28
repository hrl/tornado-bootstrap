import util
from . import urls


__all__ = [
    'mapping',
]


mapping = util.generate_url(urls.default_urls, urls.apps, __name__)
