from random import *
name=input ("What is your name?")
wrong=["No, there's nothing wrong with you.","You are just fine.","Now look here,you're good enough, and smart enough, and doggone it, people like you."]
intro=["I am Kayla, your virtual assistant.","My name is Kayla. I will assist you.","I am Kayla, and I am honored to assist you."]
question=["I was busy.Ask me your question, and make it quick.","What do you want to ask me?","What do you want from me?"]
wood=["It depends on whether you are talking about African or European woodchucks,","About as much ground as a groundhog would hog if a groundhog could hog ground,"]
looks=["Good,","I have my eves closed,","Not bad,"]
marry=["No,","Let's just stay friends,","How about YOU DON'T ASK THESE WEIRD QUESTIONS,"]
repeat=["I will not,","I am not a parrot,","YOU REPEAT AFTER ME,"]
savior=["No.I am just your friend,","I seriously dislike these comments,","What have I done,"]
gender=["I am a girl,","I am a woman,","Can't you tell from my feminine words?"]
hug=["Are there no parents?","Are there no siblings?","Go talk to the huggers, 'cause I ain't listening."] 
ath=["I am Kayla,", "Never call me that,","No,"]   
hi=["Hello,","Hi,","Hey,"]
huh=["Uh, what?", "Huh?","Wha??", "I didn't get your question." ]
christmas=["And Merry Christmas to you,%s.","I love Christmas too,%s.","Christmas is cool,%s. I agree."]
santa=["Ya, I definitely believe in Santa.","Santa, Santa, SANTA!!!!!!!"]
married=["No, and I never plan to be.","Maybe someday." ]
print (choice(intro)) 
print("Some things you can ask me: How much wood could a woodchuck chuck if a woodchuck could chuck wood? How do I look? Say hi, Kayla.")
for s in range(0,9999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    A1=input (choice(question)) 
    if A1=="How much wood could a woodchuck chuck if a woodchuck could chuck wood?" :
        print (choice(wood),name)
    elif A1=="Say hi, Kayla." :
        print (choice(hi),name)
    elif A1=="How do I look?" :
        print (choice(looks),name)
    elif A1=="Marry me." :
        print(choice(marry),name)
    elif A1=="Repeat after me." :
        print(choice(repeat),name)
    elif A1=="You are my savior." :
        print(choice(savior),name)
    elif A1=="What gender are you?" :
        print(choice(gender),name)
    elif A1=="I need a hug." :
        print (choice(hug)) 
    elif A1=="I need help with 5*5." :
        print (5*5)
    elif A1=="Can I call you Kay?" :
        print (choice(ath),name)
    elif A1=="What's wrong with me?" :
        print(choice(wrong))
    elif A1=="Merry Christmas, Kayla.":
           print(choice(christmas) % name)
    elif A1=="Do you believe in Santa?":
        print(choice(santa))
    elif A1=="Are you  married?":
        print(choice(married))
    elif A1=="When is Mother's Day?" :
        print("On the second Sunday of May, of course.") 
    elif A1=="When is Father's Day?" :
        print("On the third Sunday of June, of course.") 
    elif A1=="Tell me a joke." :   
        print("Q:Why was the cookie sad?") 
        print("A:Because his mom was a wafer for so long.") 
        print("Get it?A wafer? Away?") 
    elif A1=="When is Valentine's Day?" :
        print ("February 14.Duh.") 
    elif A1=="What are the traditions of Valentine's Day?" :
        print ("People give their beloved with chocolates, candies and flowers.") 
    elif A1=="What is your favorite animal?" :
         print ("Cats. They're so cute!")
    elif A1=="What time is it?" :
        import time
        print(time.asctime())
        print("I like military time.")
    else:
        print(choice(huh))
