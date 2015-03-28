import os

__all__ = [
    "site_settings",
    "database_settings",
]

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates/').replace('\\', '/')
STATIC_DIR = os.path.join(BASE_DIR, 'static/').replace('\\', '/')
LOCALE_DIR = os.path.join(BASE_DIR, 'locale/').replace('\\', '/')

site_settings = {
    "debug": False,
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "xsrf_cookies": True,
    "login_url": "/login",
    "autoescape": None,
    "port": 8000,
    "base_path": BASE_DIR,
    "template_path": TEMPLATE_DIR,
    "static_path": STATIC_DIR,
    "locale_path": LOCALE_DIR,
    "locale_domain": "wtforms",
}

database_settings = {
    "default": "sqlite:///databse.db",
}
