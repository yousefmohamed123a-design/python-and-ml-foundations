import time

questions = (
    "Which planet in our solar system has the shortest day, rotating once in under 10 hours?",
    "What is the chemical symbol for gold?",
    "Which strait separates Asia from North America at their closest point?",
    "Who painted The Starry Night in 1889?",
)

options = (
    (("A) Mars"), ("B) Jupiter"), ("C) Saturn"), ("D) Mercury")),
    (("A) Gd"), ("B) Go"), ("C) Au"), ("D) Ag")),
    (
        ("A) Strait of Malacca"),
        ("B) Bering Strait"),
        ("C) Strait of Hormuz"),
        ("D) Bab-el-Mandeb"),
    ),
    (
        ("A) Claude Monet"),
        ("B) Pablo Picasso"),
        ("C) Vincent van Gogh"),
        ("D) Salvador Dalí"),
    ),
)

answers = ("B", "C", "B", "C")


cnt = 0
score = 0
for quest, cnt in zip(questions, range(5)):
    print("------------\n")
    print(quest, "\n")

    print(f"Question {cnt + 1}")
    for option in options[cnt]:
        print(option)

    ans = input("\nEnter your answer letter : ")
    if ans.upper() == answers[cnt]:
        print(f"Correct, you are a genius {ans}")
        score += 1
        time.sleep(2)
    else:
        print(f"\nIncorrect Solution the correct answer is {answers[cnt]}")
        time.sleep(2)
    print("\n------------")

print(f"Your score is {score}/4")
print("Congrats!!" if score == 4 else "Better luck next time")
