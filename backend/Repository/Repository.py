import helpers

csv_path_user='test_user.csv'
csv_path_producer='test_producer.csv'
# take an username ( string ) and return a json corresponding of the information of the user
def read_user_data(username):
    json = helpers.make_json(csv_path_user)
    print(json)
    data = json[username]
    return data if data else json.dumps('"error":"404 not found"')

#write the corresponding json into the csv file
def write_user_data(json):
    helpers.write_json_in_csv(csv_path_user,json)

#get all the producer
def fetch_producer():
    json=helpers.make_json(csv_path_producer)
    print(json)
    return json if json else json.dumps('"error":"404 not found"')

