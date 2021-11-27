from flask import Flask, json
#
companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
api = Flask(__name__)
mock_response=[{"name":"max","meals":"yeah"}]
@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)
@api.route('/login', methods=['GET'])
def get_login():
    return json.dumps(mock_response)

if __name__ == '__main__':
    api.run()



