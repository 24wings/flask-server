from flask import Flask, Response, jsonify
from flask_cors import *
import model.index
class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        #response = make_response(jsonify(response=get_articles(ARTICLES_NAME)))  
        #response.headers['Access-Control-Allow-Origin'] = '*'  
        #response.headers['Access-Control-Allow-Methods'] = 'POST'  
        #response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)

class MyFlask(Flask):
    response_class = MyResponse

app = MyFlask(__name__)
# cross domain
CORS(app, supports_credentials=True)

@app.route('/')
def root():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return t

    
if __name__ == '__main__':
    app.debug = True
    app.run()
    
