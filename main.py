from flask import Flask, Blueprint
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app = app)
# описание главного блока нашего api http://127.0.0.1:5000/main/.
name_space = api.namespace('main', description='Main APIs')

@name_space.route("/")
class MainClass(Resource):
  def get(self):
    return {"status": "Got new data"}
  def post(self):
    return {"status": "Posted new data"}
  
# подключение api из другого файла
from part.part import api as partns1
api.add_namespace(partns1)

from part.parttmpl import api as partns2
from part.parttmpl import templ as templ
api.add_namespace(partns2)
app.register_blueprint(templ,url_prefix='/templ')
app.run(debug=True,host='127.0.0.1',port=5000)
