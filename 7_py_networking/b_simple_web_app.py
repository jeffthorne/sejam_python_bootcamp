from flask import Flask, request

# Flask is a web microframework for Python based on Werkzeug, Jinja 2 and good intentions.
# http://flask.pocoo.org/

app = Flask(__name__)            #The first argument is the name of the application’s module or package. 
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def hello_world():
	print(request.args)
	return 'Hello, World!'



if __name__ == '__main__':
    app.run()


# kill with crtl-C. If not use lsof -i :5000 | grep LISTEN on mac to find process


# we use this for quick DS SQL injection demos
# Show baker login demo

