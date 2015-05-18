import cherrypy

class HelloWorld(object):
	
	@cherrypy.expose
	def index(self):
		return "<a href=\"http://www.google.com\">Hello World!</a>"

	@cherrypy.expose
	def bark(self):
		return 'woof woof'

	@cherrypy.expose
	def sayhi(self, name='Yaser'):
		return 'Carolyn says hi to %s' % name
		
if __name__ == '__main__':
	some_object = HelloWorld()
	cherrypy.quickstart(some_object)