import web
from web import form

urls = ('/', 'index',
        '/result', 'result')

app = web.application(urls, globals())

my_form = form.Form(
    form.Textbox('Number: '),
    form.Button('Get in')
)


class index:


    def GET(self):
        form = my_form()
	return form.render()


class result:

    def GET(self):
        return '<h1>How you doing~</h1>'

if __name__ == '__main__': app.run()
