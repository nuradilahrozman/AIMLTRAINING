print("Dictionary Example")
our_dictionary=[
    {"id":"1", "name": "lala", "age":"45"},
    {"id":"2", "name": "dila", "age":"56"},
    {"id":"3", "name": "tod", "age":"30"},
    {"id":"4", "name": "nur", "age":"27"}
    ]
#key is the id/name/age
for key in our_dictionary:
    print(key["id"]+"->"+key["name"]+"->"+key["age"])
