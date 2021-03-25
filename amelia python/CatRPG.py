from random import*
momname=["Mouse","Scarlet", "Flower","Wolf"]
moomname = (choice(momname))
print("Hello, and welcome to CatRPG! Hunt, fight, and have fun being a cat!")
gender = input("Mom: my little kitten, are you  a girl or a boy?")
if gender=="girl":
    himer = "her"
else:
    himer = "his"
print("Mom:A %s?" % gender)
name = input("Mom:What is your name?")
print("Mom:Oh, my dear %s, how lovely the world is!" % name)
print("Dad: %s, are you done kitting? *He looks at you.* Oh, a lovely lil' kit! What is %s name?" % (moomname, himer))
choicce1 = input("Do you want to tell Dad your name, or should Mom?(A for Mom and B for you.)")
if choicce1=="A":
    print("Mom:Her name is %s." % name)
else:
    print("You: My name is %s!!!" % name)
    print("Dad:Ah, what a sweet girl.")
    
