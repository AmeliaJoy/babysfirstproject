gender=input ("What gender?(F or M)")
if gender == "F":
    genderr = 'her'
if gender == "M":
    genderr = 'his'
name=input ("What is %s name?" % genderr )
hair=input ("What color hair?")
eyes=input ("What color eyes?")
data=[gender,hair,eyes]
persondata = {name : data}
print(persondata)
