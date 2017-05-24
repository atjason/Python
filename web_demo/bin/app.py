import web

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

render = web.template.render("templates/")

class index:
    def GET(self):
        #form = web.input(name="Nobody")
        #greeting = "Hello, %s" % form.name
        #return render.index(greeting = greeting)
	return render.hello_form()

    def POST(self):
	form = web.input(name="Nobody", greeting="Hello")
	greeting = "%s, %s" % (form.greeting, form.name)
	return render.index(greeting = greeting)        

if __name__ == "__main__":
    app.run()
