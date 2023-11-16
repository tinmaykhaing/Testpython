this =["apple","banana","mango","chherry"]
newlist=[x for x in this if "a" in x]
new=[x.upper() for x in this]
new1=['Hello' for x in this]
new2=[x if x != "banana" else "orange" for x in this]
print(new2)