# # Quiz app
user_name = input("Enter your name : ").strip().title()
quiz = [      
        {
            "question" :"Who is the winner of IPL 2018 : ",
            "options"  : ["A.MI","B.CSK","C.PBSK","D.HYD"],
            "Answer"   : "B"
        },
        {
            "question" :"Who is the captiane of CSK in 2022 : ",
            "options"  : ["A.Dhoni","B.Jadaja","C.Dube","D.Ruturaj"],
            "Answer"   : "D"
        },
        {
            "question" :"Name the one IPL team having only lolipop in every seseaon : ",
            "options"  : ["A.RCB","B.CSK","C.PBSK","D.MI"],
            "Answer"   : "A"
        },
        {
            "question" :"In IPL which team having 12 playars : ",
            "options"  : ["A.MI","B.CSK","C.PBSK","D.HYD"],
            "Answer"   : "A"
        },
        
]

score = 0 
for q in quiz:
    print("\n" + q["question"])  
    for options in q["options"]:
     print(f"{options}")
    
    user_answer = input(f"Enter your option (A/B/C/D) : ").strip().upper()
    if user_answer == q["Answer"]:
        print("✅Correct answer")
        score += 1
    else:
        print(f"❌Incorrect answer. Correct answer is {q['Answer']}")

print("\n🎉 Quiz Finished!",user_name)
print(f"Your Score: {score} out of {len(quiz)}")
percentage = (score / len(quiz)) * 100
print(f"Percentage: {percentage:.2f}%")
print("hello")
