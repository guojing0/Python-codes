import web
from web import form

urls = (
    '/(.*)', 'form'
)

app_form = web.application(urls, locals())

my_form = form.Form(
    form.Textbox('Name'),
    form.Password('Password'),
    form.Button('Login'),
    form.Dropdown('Language',
		[('value0', 'Latin'),
		 ('value1', 'Common Lisp'), 
	         ('value2', 'Python')]))

class form:
    def GET(self):
        form = my_form()
	return my_form.render()
