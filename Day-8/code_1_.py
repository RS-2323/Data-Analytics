import json

my_json="""
	{
		"emp no": 180612017,
		"Name": {
			"first": "Dr. Sylvester",
			"last": "Fernandes"
		},
		"age": 34,
		"mobile": [6376604301, 6378787310],
		"department": "data analytics",
		"email": ["SylvesterFernandes.ind@gmail.com", "Sylvester@gmail.com", "180612S017@ruj-bsdu.in"],
        "salary":50000
	}

"""
new_json= json.dumps(my_json)
new_json= json.loads(my_json)

print (type(new_json) )
print (new_json) 

new_json = json.dumps(my_json, indent=2 )
print (new_json) 

new_json= json.dumps(my_json, indent=2, sort_keys=True)
print (new_json)



# Writing/Storing the JSON data in a File 

with open("faculty.json", "w") as write_file:
    json.dump(my_json, write_file)
    # json.dump(json_string, write_file, indent=2   )


# Reading from a JSON file

with open("faculty.json", "r") as read_file:
    jsondata=json.load(read_file)
    print(jsondata)
 
    # JSON in python data structure 
    my_json1 = json.loads(jsondata)
    print ( my_json1)