dogs=[]
Inventory=["water bowl","food bowl"]
money=50
dogs.append("eoo")
print("Hello, and welcome to Woofy Dogz Virtual Pets!")
site = input ("Where would you like to go? (Mall,Junkyard, Pet shop, help)")
if site=="Mall" :
    shop = input ("What would you like to buy?")
    if shop=="Puppy chow" :
        print ("Puppy chow costs $10 dollars.") 
        print (" You have %s" % money)
        pupchow=input ("Are you sure?")
    if pupchow=="Yes" :
           money=money-10
           Inventory.append("puppy chow")    
if site=="Pet Shop":
    gender=input ("Boy or girl?")
    breed=input ("Breed?")
    print("Alright, the sources came in. We have ONE %s %s." % (breed, gender))
    print("It costs 20 bucks. You have %s." % money)
    sure=input ("Are you sure?(Y or N)")
    if sure=="Y":
        money=money-20
        dogs.append("A %s %s" % (breed, gender))
    
