import random

quizdata = [
    {
        "question": "WHICH TEAM HAS WON MORE IPl TROPHIES?",
        "options": ["A. CSK", "B. MI", "C. Both A and B", "D. RCB"],
        "answer": "C"
    },
    {
        "question": "DEFENDING CHAMPIONS?",
        "options": ["A. KKR", "B. MI", "C. CSK", "D. RCB"],
        "answer": "D"
    },
    {
        "question": "MOST NO.OF WICKETS IN IPL?",
        "options": ["A. ASHWIN", "B. CHAHAL", "C. BRAVO", "D. BUMRAH"],
        "answer": "B"
    },
    {
        "question": "MOST RUNS IN IPL?",
        "options": ["A. KOHLI", "B. DHONI", "C. ROHIT", "D. RAINA"],
        "answer": "A"
    },
    {
        "question": "MOST EXPENSIVE PLAYER?",
        "options": ["A. IYER", "B.CUMMINS ", "C. PANT", "D. BUMRAH"],
        "answer": "C"
    },
    {
        "question": "MOST EXPENSIVE PLAYER IN FOREIGN PLAYER?",
        "options": ["A. GREEN", "B. STRAC", "C. SAM CURRAN", "D. All of the above"],
        "answer": "A"
    },
    {
        "question": "MOST EXPENSIVE UNCAPPED PLAYER?",
        "options": ["A. KARTHICK SHARMA", "B. PRASANTH VEER", "C. BOTH A AND B", "D. AVESH KHAN"],
        "answer": "C"
    },
    {
        "question": "MOST DISMISSAL BY A PLAYER?",
        "options": ["A. KARTHICK", "B. PANT", "C. DHONI", "D. BUTLER"],
        "answer": "C"
    },
    {
        "question": "MOST WINS AS A CAPTAIN?",
        "options": ["A. DHONI", "B. ROHIT", "C. KOHLI", "D. SACHIN"],
        "answer": "A"
    },
    {
        "question": "MOST TROPHIES AS A CAPTAIN?",
        "options": ["A. DHONI", "B. ROHIT", "C. BOTH A AND B", "D. GAUTAM GAMBHIR"],
        "answer": "C"
    },
    {
        "question": "MOST SIXES ?",
        "options": ["A. ROHIT", "B. KOHLI", "C. GAYLE", "D.DHONI"],
        "answer": "C"
    },
    {
        "question": "MOST FOURS?",
        "options": ["A. ROHIT", "B. KOHLI", "C. RAINA", "D. GAYLE"],
        "answer": "B"
    },
    {
        "question": "MOST RUNS IN A SEASON?",
        "options": ["A. KOHLI", "B. DHONI", "C. ABD", "D. ROHIT"],
        "answer": "A"
    },
    {
        "question": "MOST WICKETS IN A SEASON?",
        "options": ["A. BRAVO", "B. HARSHAL PATEL", "C. BOTH A AND B", "D. BUMRAH"],
        "answer": "C"
    },
    {
        "question": "HIGHEST RUN BY A PLAYER IN A MATCH?",
        "options": ["A. GAYLE", "B. KOHLI", "C. RAINA", "D. DHAWAN"],
        "answer": "A"
    },
    {
        "question": "MOST WICKETS IN A MATCH",
        "options": ["A. BRAVO", "B. ALZARRI JOSEPH", "C. ISHANT SHARMA", "D. BUMRAH"],
        "answer": "B"
    },
    {
        "question": "WHICH TEAM HIGHEST SCORE IN A MATCH?",
        "options": ["A. CSK", "B. MI", "C. SRH", "D. RCB"],
        "answer": "C"
    },
    {
        "question": "HIGHEST RUN CHASE?",
        "options": ["A. PBKS", "B. MI", "C. RCB", "D. CSK"],
        "answer": "A"
    },
    {
        "question": "MOST FAIRPLAY AWARD",
        "options": ["A. SRH", "B. MI", "C. CSK", "D. RCB"],
        "answer": "C"
    }
]

def askquestion(questiondata):
    print(questiondata["question"])
    for option in questiondata["options"]:
        print(option)
    user_answer = input("Enter your answer (A,B,C,D): ").upper()
    if user_answer == questiondata["answer"]:
        return True
    else:
        return False

if __name__=="__main__":
    score=0
    random.shuffle(quizdata)
    for i in range(1,11):
        print(f'Question {i} of 10')
        if askquestion(quizdata[i]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {quizdata[i]['answer']}.\n")

    print(f"You scored {score}/10.")
