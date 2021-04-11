import time 

print("""
------------------------------------------------

  WELCOME TO THE KNOWLEDGE COMPETITION

------------------------------------------------
------------------------------------------------

                !ATTENTION!

  Pay attention to the spelling rules!
  You have 15 minutes for each question result!

------------------------------------------------
""")

#--------------------------------------------------------------------------------------------------------------------------0

question = 10 #It has been put to see if it is successful

question_list = [] #All the answers given are listed

true_list = [] #The correct answers given are listed

false_list = [] #Wrong answers given are listed

timeout = [] #Expired answers

#--------------------------------------------------------------------------------------------------------------------------1

start_time1 = time.time()

ask1 = input("When was Python started to be developed?\n")
question_list.append(ask1)

finish_time1 = time.time()

if finish_time1 - start_time1 <= 15 :
    if ask1 == "1990":
        time.sleep(0.5)
        print("Congratulations your answer is correct :)\n")
        true_list.append(ask1)

    else:
        question -=1
        false_list.append(ask1)
        time.sleep(0.5)
        print("Sorry your answer is wrong!\n")
else:
    question -=1
    timeout.append(ask1)
    print("You timed out be careful!\n")

#--------------------------------------------------------------------------------------------------------------------------2

start_time2 = time.time()

ask2 = input("\nInstrument used to study the sky?\n")
question_list.append(ask2)

finish_time2 = time.time()

if finish_time2 - start_time2 <= 15 :
    if ask2 == "telescope" or ask2 == "Telescope" or ask2 == "TELESCOPE":
        time.sleep(0.5)
        print("Congratulations your answer is correct :)\n")
        true_list.append(ask2)
        
    else:
        question -=1
        false_list.append(ask2)
        time.sleep(0.5)
        print("Sorry your answer is wrong!\n")
else:
    question -=1
    timeout.append(ask2)
    print("You timed out be careful!\n")

#--------------------------------------------------------------------------------------------------------------------------3

start_time3 = time.time()

ask3 = input("\nWhat is a satellite of the world?\n")
question_list.append(ask3)

finish_time3 = time.time()

if finish_time3 - start_time3 <= 15 :
    if ask3 == "Moon" or ask3 ==  "moon" or ask3 == "MOON":
        time.sleep(0.5)
        print("Congratulations your answer is correct :)\n")
        true_list.append(ask3)

    else:
        question -=1
        false_list.append(ask3)
        time.sleep(0.5)
        print("Sorry your answer is wrong!\n")
else:
    question -=1
    timeout.append(ask3)
    print("You timed out be careful!\n")

#--------------------------------------------------------------------------------------------------------------------------4

start_time4 = time.time()

ask4 = input("\nWhat is the geometric shape whose interior angles add up to 180°?\n")
question_list.append(ask4)

finish_time4 = time.time()

if finish_time4 - start_time4 <= 15 :
    if ask4 == "Triangle" or ask4 == "triangle" or ask4 == "TRIANGLE":
        time.sleep(0.5)
        print("Congratulations your answer is correct :)\n")
        true_list.append(ask4)

    else:
        question -=1
        false_list.append(ask4)
        time.sleep(0.5)
        print("Sorry your answer is wrong!\n")
else:
    question -=1
    timeout.append(ask4)
    print("You timed out be careful!\n")

#--------------------------------------------------------------------------------------------------------------------------5

start_time5 = time.time()

ask5 = input("\nWhat is the blood pumping organ in the human body?\n")
question_list.append(ask5)

finish_time5 = time.time()

if finish_time5 - start_time5 <= 15 : 
    if ask5 == "Heart" or ask5 == "heart" or ask5 == "HEART":
        time.sleep(0.5)
        print("Congratulations your answer is correct :)\n")
        true_list.append(ask5)

    else:
        question -=1
        false_list.append(ask5)
        time.sleep(0.5)
        print("Sorry your answer is wrong!\n")
else:
    question -=1
    timeout.append(ask5)
    print("You timed out be careful!\n")
    
#--------------------------------------------------------------------------------------------------------------------------6

start_time6 = time.time()

ask6 = input("\nWhere is the capital of Turkey?\n")
question_list.append(ask6)

finish_time6 = time.time()

if finish_time6 - start_time6 <= 15 : 
    if ask6 == "Ankara" or ask6 == "ankara" or ask6 == "ANKARA":
        time.sleep(0.5)
        print("Congratulations your answer is correct :)\n")
        question_list.append(ask6)
        true_list.append(ask6)

    else:
        question -=1
        false_list.append(ask6)
        time.sleep(0.5)
        print("Sorry your answer is wrong!\n")
else:
    question -=1
    timeout.append(ask6)
    print("You timed out be careful!\n")

#--------------------------------------------------------------------------------------------------------------------------8

start_time7 = time.time()

ask7 = input("\nWhat is the name of the highest mountain in the world?\n")
question_list.append(ask7)

finish_time7 = time.time()

if finish_time7 - start_time7 <= 15 : 
    if ask7 == "Everest" or ask7 == "everest" or ask7 == "EVEREST":
        time.sleep(0.5)
        print("Congratulations your answer is correct :)\n")
        true_list.append(ask7)

    else:
        question -=1
        false_list.append(ask7)
        time.sleep(0.5)
        print("Sorry your answer is wrong!\n")
else:
    question -=1
    timeout.append(ask7)
    print("You timed out be careful!\n")
    
#--------------------------------------------------------------------------------------------------------------------------9

start_time8 = time.time()

ask8 = input("\nWhat is the name of the most populous country in the world?\n")
question_list.append(ask8)

finish_time8 = time.time()

if finish_time8 - start_time8<= 15 :
    if ask8 == "China" or ask8 == "china" or ask8 == "CHINA":
        time.sleep(0.5)
        print("Congratulations your answer is correct :)\n")
        true_list.append(ask8)

    else:
        question -=1
        false_list.append(ask8)
        time.sleep(0.5)
        print("Sorry your answer is wrong!\n")
else:
    question -=1
    timeout.append(ask8)
    print("You timed out be careful!\n")

#--------------------------------------------------------------------------------------------------------------------------10

start_time9 = time.time()

ask9 = input("\nWho is the famous mathematician nicknamed the 'father of algebra'?\n")
question_list.append(ask9)

finish_time9 = time.time()

if finish_time9 - start_time9<= 15 :
    if ask9 == "Al-Khwarizmi" or ask9 == "al-khwarizmi" or ask9 == "AL-KHWARIZMI" or ask9 == "Al-khwarizmi":
        time.sleep(0.5)
        print("Congratulations your answer is correct :)\n")
        true_list.append(ask9)

    else:
        question -=1
        false_list.append(ask9)
        time.sleep(0.5)
        print("Sorry your answer is wrong!\n")
else:
    question -=1
    timeout.append(ask9)
    print("You timed out be careful!\n")
    
#--------------------------------------------------------------------------------------------------------------------------11

start_time10 = time.time()

ask10 = input("\nWho is the winner of the 2019 eurovision competition?\n")
question_list.append(ask10)

finish_time10 = time.time()

if finish_time10 - start_time10<= 15 :
    if ask10 == "Duncan Laurence" or ask10 == "duncan laurence" or ask10 == "DUNCAN LAURENCE" or ask10 == "Duncan laurence":
        time.sleep(0.5)
        print("Congratulations your answer is correct :)\n")
        true_list.append(ask10)

    else:
        question -=1
        false_list.append(ask10)
        time.sleep(0.5)
        print("Sorry your answer is wrong!\n")
else:
    question -=1
    timeout.append(ask10)
    print("You timed out be careful!\n")
    
#--------------------------------------------------------------------------------------------------------------------------13

if question <= 5: #Evaluation block
    print("""          RESULT
******************************************************

Test Failed!!!\nYou answered {} questions incorrectly

******************************************************
""".format(question))

else:
    print("""          RESULT
******************************************************

Congratulations you passed the test successfully :)\nYou answered {} questions correctly

******************************************************

""".format(question))

#--------------------------------------------------------------------------------------------------------------------------14
    
print("""                                                                   LISTS
------------------------------------------------------------------------------------------------------------------------------------------------------------------
\nAll your answers to the test:{}\n
\nThe correct answers you gave to the test:{}\n
\nAll the wrong answers you gave to the test:{}\n
\nAnswers you timed out:{}\n
------------------------------------------------------------------------------------------------------------------------------------------------------------------
""".format(question_list,true_list,false_list,timeout))

    

    






