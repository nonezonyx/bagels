import random

def guess(input: int|str,answer: int|str) -> list[str]:
    """guess(input: int|str,answer: int|str) -> list[str]:
returns list of answers:
Bagels  - No digit is correct.
Pico - One digit is correct but in the wrong position.
Fermi - One digit is correct and in the right position.
Wrong input - Amount of digits is not equal.
"""
    input,answer=map(str,[input,answer])
    if len(answer)!=len(input): return ["Wrong input"];
    ans=[]
    for i in range(len(answer)):
        if input[i]==answer[i]:
             ans.append("Fermi")
        elif answer.count(input[i])>=1:
            ans.append("Pico")
    return (["Bagels"],ans)[len(ans)>0]

def get_answer(length:int)->str:
    correct_answer=list("0123456789")
    random.shuffle(correct_answer)
    return "".join(correct_answer[:length])

def play(num_length: int=3, guesses: int=10) -> bool:
    """play(num_length: int=3, guesses: int=10) -> bool:
main game function.
returns True if player won and False otherwise.
"""

    correct_answer=get_answer(num_length)
    guess_num=1
    while  guess_num <= guesses:
        guess_answer=guess(input(f"Guess #{guess_num}: "),correct_answer)
        if "Wrong input" in guess_answer:
            print("Wrong input")
        elif guess_answer == ["Fermi" for _ in range(num_length)]:
            print("You got it!")
            return True
        else:
            print(*sorted(guess_answer))
            guess_num+=1
    print(f"You've lost! Answer is {correct_answer}.")
    return False

def main():
    print("""Bagels, a deductive logic game.
I am thinking of a number. Try to guess what it is.
Here are some clues:
When I say:\tThat means:
 Pico   \tOne digit is correct but in the wrong position.
 Fermi  \tOne digit is correct and in the right position.
 Bagels \tNo digit is correct.
 """)

    while True:
        play(*map(int,[input("Number of digits: "),input("Number of guesses: ")]))
        print("Do you want to play again? (y/n)")
        if input().upper()!='Y':
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()
