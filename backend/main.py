import flask
from flask import Flask, json, redirect, url_for, render_template, request, session, app

#
companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
api = Flask(__name__)
mock_response=[{"name":"max","meals":"yeah"}]
"""
Enable CORS. Disable it if you don't need CORS
https://parzibyte.me/blog
"""

@api.route('/companies', methods=['GET'])
def get_companies():
  rresponse  = flask.Response(json.dumps("{<\"code\":200}"))
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response
@api.route('/login', methods=['GET'])
def get_login():
    response=json.dumps(mock_response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
@api.route('/taste',methods=['POST','OPTION'])
def post_taste():
    print(request.json)


    response  = flask.Response(json.dumps("{<\"code\":200}"))
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers[
        "Access-Control-Allow-Origin"] = "*"  # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers[
        "Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response
@api.route('/localisation',methods=['POST','OPTION'])
def post_localistaion():
    print(request.json)
    response  = flask.Response(json.dumps("{<\"code\":200}"))
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers[
        "Access-Control-Allow-Origin"] = "*"  # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers[
        "Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response
@api.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == '__main__':
    api.run()



