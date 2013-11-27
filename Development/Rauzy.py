import json
from Object import *
from Relation import *

#define a "parse" function to parse a rau file for a model and create all Objects and Relations
def parse(file):
	#open and then read the file
	f=open(file,'r')        #open a file for reading
	s=f.read()              #read the content of file f
	#return a python object out of a json object
	target=json.loads(s)
	f.close()
	val_root(target)
	model = Object(file.split(".")[0],target)
	return model

#writes the necessary files for this model
#One file for root object
#One file (library) for the rest objects
def toFile():
	pass

#TODO handle "Error 01: xx in the xx not defined!"
#handle "Error 07:Redundant object definition of "xx"!"
#handle "Error 07:Redundant relation definition of "xx"!"
#handle "Warning 02:Detect of a library member in xx, but xx is not the root object."
#handle "Warning 03: "objects" and "relations" in object A will be overriden by these of object B as A extends B"
def val_root(target):
	pass
	
#prints the model in screen
def printModel():
	print "Model"
	print model.toStr("")

#print parse("Bank.rau")
#root Object
model = parse("Bank.rau")
printModel()
print model.toJson("")

#print Object.objects
#print Object.relations
#print model["objects"]

	
