from flask_restful import Resource,Api
from flask import Flask,request,session
app=Flask(__name__)
api=Api(app)
class Login(Resource):
    def post(self):
        user=User.query.filter(User.username=request.get_json()["user_name"]).first()
        session["user_id"]=user.id
        return user.to_dict()
class CheckSession(Resource):   
    def get(self):
        user=User.query.filter(User.id==session.get("user_id"))
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401

class Logout(Resource):
    def delete():
        session["user_id"]=None
        return {"Message","204 ,not found"},204

api.add_resource(Login,"/login")
api.add_resource(CheckSession,"/checksession")
api.add_resource(Logout,"/logout")
        
# class CheckSeesion(Resource):
#     def get(self):
#         user=Login.query.filter(Login.id==session.get("user_id")).first()

# class Logout(Resource):
#     def delete(self):
#         session["user_id"]=None
#         return {
#             "Message":"204:no current"
#         },204
# api.add_resource(Logout,"/logout")
# @app.before_request()
# def check_if_logged_in():
#     if not session["user_id"]:
#         return {"error":"unauthorized"}
# class Document(Resource):
#     def get(self,id):
#         document=Document.query.filter(Document.id==id).first()
#         return document.to_dict()
    
#     # Password protection
# class Login(Resource):
#     def post(self):
#         username=request.get_json()["username"]
#         user=
@app.before_request()
def check_if_logged_in():
    if not session["user_id"] and request.endpoint!="document_list":
        return {"Error":"Unauthorized user"},401
class Document(Resource):
    def get(self,id):
        if not session["user_id"]:
            return {"Error":"unauthorized"},401
        document=Document.query.filter(Document.id==id).first()
        return document.to_dict()
    def patch(self, id):

        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401

        # patch code

    def delete(self, id):

        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401

class DocumentList(Resource):
    def get(self):
        documents=Document.query.all()
        return [document.to_dict() for document in documents ]    

api.add_resource(Document,"/documents/<int:id>",endpoint="document")
api.add_resource(DocumentList,"/documents",endpoint="document_list")
