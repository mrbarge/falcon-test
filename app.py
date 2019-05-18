#!/bin/env python
import falcon
import falcon_jsonify
from wsgiref import simple_server


class HelloResource(object):
	def on_post(self, req, resp):
		try:
			name = req.get_json('name')
			msg = "Hello " + name
			resp.json = {"message": msg }
			resp.status = falcon.HTTP_200
		except Exception:
			raise falcon.HTTPError(falcon.HTTP_501)
		

app = application = falcon.API(middleware=[
	falcon_jsonify.Middleware(help_messages=True),
])

hello = HelloResource()

app.add_route('/hello', hello)

if __name__ == '__main__':
	http = simple_server.make_server('0.0.0.0', 8080, app)
	http.serve_forever()
