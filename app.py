from flask import Flask
from views import views
#import requests
#from bs4 import BeautifuSoup as bs
#import json
#import random
#import os.paths


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
''''''

#app.register_blueprint(blueprint)

#def grab_igpfp():



if __name__=='__main__':
    app.run(debug=True, port=8000)