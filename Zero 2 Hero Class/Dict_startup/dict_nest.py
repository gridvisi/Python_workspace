

presidents ={
	"obama": {
		"firstname" : "barak",
		"lastname" : "obama"
		},
	"trump": {
		"firstname" : "donald",
		"lastname" : "trump"
		}
	}
for name, nameplus in presidents.items():
	print(name.title() + "'s full name is ")
	fullname = nameplus['firstname'] + " " + nameplus['lastname']
	print(fullname.title())