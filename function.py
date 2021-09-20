#def greet(name,time):
#    print(f"Good {time} , {name}")

#greet("Taka","Morning")

#greet("Naung Naung","Evening")

#default parameter
def greet(name="Mg Mg",time="Morning"):
    print(f"Good {time} , {name}")

greet("aung aung")
greet(name="Taka",time="Evening")
greet(time="afternoon",name="Robin")
greet(time="night")
