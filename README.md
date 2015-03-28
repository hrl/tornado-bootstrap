# tornado-bootstrap
A simple template to create a Tornado project with:
- SQLAlchemy
- WTForms (and i18n)
- Sub Apps

### Getting started
Clone this repo:
```
git clone https://github.com/hrl/tornado-bootstrap.git
cd tornado-bootstrap
pip install -r requirements.txt
```
Run demo:
```
python ./main.py 8000
```
Then visit http://localhost:8000/app?n=a

### i18n
####Translating WTForms' built-in messages:
Copy [WTForms' translation files](https://github.com/wtforms/wtforms/tree/master/wtforms/locale) into your locale directory.

####Translating your own messages:
In your RequestHandler:
```
_ = self.locale.translate
```
In your form's validator:
```
_ = field.gettext
```
Then follow [Tornado's documentation](http://www.tornadoweb.org/en/stable/locale.html#tornado.locale.load_gettext_translations) to generate a translation file.
