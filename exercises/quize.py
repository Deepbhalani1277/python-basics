queations = [
    ["Q1. Which of the following is the largest planet in our Solar System?", 
    "A. Earth"
    ,"B. Jupiter"
    ,"C. Saturn"
    ,"D. Mars"
    ,2]
    ,
    ["Q2. What is the capital of France?",
    "A. Berlin"
    ,"B. Madrid"
    ,"C. Paris"
    ,"D. Rome"
    ,3
    ]
    ,
    ["Q3. Who wrote 'To Kill a Mockingbird'?",
    "A. Harper Lee"
    ,"B. Mark Twain"
    ,"C. F. Scott Fitzgerald"
    ,"D. Ernest Hemingway"
    ,1]
]

levels = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
money = 0
for i in range(0, len(queations)):
    queation = queations[i]
    print(f"queation for rs. {levels[i]}")
    print(queation[1])
    print(queation[2])
    print(queation[3])
    print(queation[4])
    reply = int(input("enter your answer(1-4):"))
    if (reply == queation[-1]):
        print(f"correct answer, you won RS. {levels[i]}")
        if(i==4):
            money = levels[4]
        elif(i==9):
            money = levels[9]
    else:
            print("wrong answer!")
            break
print(f"you take home rs. {money}")