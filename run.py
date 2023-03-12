from tabulate import tabulate
from operator import itemgetter


questions = {
    "Bunny hug": "C",
    "Miskeen": "C",
    "Dep": "A",
    "Nuisance grounds": "A",
    "Skoden": "B",
    "Jambuster": "A",
    "Scribbler": "A",
    "Huck": "C",
    "Donnybrook": "A",
    "Skookum": "B",
}


possible_answers = [
    ["A) Chocolate Easter egg", "B) Fuzzy slippers", "C) Hooded sweatshirt"],
    ["A) Petty thief", "B) Patchwork quilt", "C) Pathetic"],
    ["A) Corner store", "B) Mason jar", "C) Certainly"],
    ["A) Garbage dump", "B) Schoolyard", "C) Legion branch"],
    ["A) Snowmobile tracks", "B) Let's go, then", "C) Family picnic"],
    [
        "A) Jam-filled doughnut",
        "B) Kitchen party",
        "C) Tugboat sent to break up logjams",
    ],
    ["A) Notebook", "B) Leaky boat engine", "C) Defensive hockey player"],
    ["A) Eat quickly", "B) Hitchhike", "C) Throw"],
    ["A) Brawl", "B) Good-looking boy", "C) Swimming hole"],
    ["A) In the sky", "B) Strong or brave", "C) Grandmother"],
]


explanations = [
    ["A bunny hug is cozy on a cold night."],
    ["Look at this miskeen guy, he's never been to Canada's Wonderland"],
    ["Ming asked his roommate to pick up some milk at the dep."],
    [
        "Property values plummeted"
        "when the municipality established nuisance grounds nearby."
    ],
    [
        "Often an invitation to engage in a fight, "
        "skoden has recently been used in battles over pipeline projects."
    ],
    [
        "Having grown up in Winnipeg, the cashier knew "
        "what his customer meant when she ordered a jambuster."
    ],
    ["Get our your scribblers and write your names on the covers."],
    ["Alina called for her friend to huck her the ball."],
    [
        "The Donnybrook Fair in Dublin, Ireland, "
        "was so rowdy that any tussle became known as a donnybrook."
    ],
    [
        "Derived from Chinook Jargon, "
        "skookum appears in many place names in the Pacific Northwest."
    ],
]


score_table = []


def rules_intro():
    """
    Prints the rules of the game.
    """
    print("Welcome to Canadian Slang Quiz")
    print(
        """

 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣄⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣴⣿⡄⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠰⣶⣾⣿⣿⣿⣿⣿⡇⠀⢠⣷⣤⣶⣿⡇⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣀⣿⣿⣿⣿⣿⣧⣀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⣷⣦⣀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀
 ⠀⠀⠀⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠚⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠂⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢻⣿⣿⡿⠛⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """

        )
    print("Perfect your Canadian slang with a fun quiz!!!")
    print("The rules are simple:")
    print("- You get a term and three suggested answers.")
    print("- It's up to you to guess correctly!")
    print("- Choose A, B or C and hit enter.")
    print("- You will get the result and an explanation of the term.")
    username()


def username():
    """
    Asks the user to play.
    Prompt for user name.
    """
    global name
    print("---------------------------------------------------------")
    while True:
        game_accept = input(
            "Do you want to test your knowledge? (Yes / No):\n")
        if game_accept.lower() == "yes":
            print("---------------------------------------------------------")
            print("We're glad you want to play!")
            break
        elif game_accept.lower() == "no":
            print("---------------------------------------------------------")
            print("Ok, maybe next time. We wish you a pleasant day!")
            quit()
        else:
            print("\n******************************")
            print("Incorrect entry!")
            print("Your answer must be Yes or No!")
            print("******************************\n")
    name = input("Please enter your name:\n")
    print(f"We wish you the best of luck {name}, the game can begin!")
    print("=========================================================")


def game():
    """
    Iterate through questions, possible_answers and explanations.
    And asks for user answer
    """
    rules_intro()
    answers_num = 1
    explanations_num = 1
    score = 0
    for key, value in questions.items():
        print("*********************************************************\n")
        print(key)
        print("")
        correct_answer = value
        for possible_answer in possible_answers[answers_num - 1]:
            print(possible_answer)
        answers_num += 1
        for explanation in explanations[explanations_num - 1]:
            meaning = explanation
        explanations_num += 1
        while True:
            print("---------------------------------------------------------")
            user_answer = input(
                "What do you think the meaning of the term is? A, B or C:\n")
            user_answer = user_answer.upper()
            if validate_answer(user_answer):
                score += check_answer(user_answer, correct_answer, meaning)
                break
    scoreboard(score)
    ranking_list(name, result)


def validate_answer(user_answer):
    """
    Inside try, checks if user input is not one of three possible.
    Raise ValueError if input is anything else than A, B or C
    Return True if it is not valid, so that user can input again
    (see line 141, while loop for user_answer input)
    """
    valid_user_input = ["A", "B", "C"]
    try:
        if user_answer not in valid_user_input:
            raise ValueError("your answer must be A, B or C")
        return True
    except ValueError as e:
        print(f"Invalid entry, {e}, please try again.")


def check_answer(user_answer, correct_answer, meaning):
    """
    Checks whether the user's answer is correct
    """
    if user_answer == correct_answer:
        print(f"Well done! Answer {user_answer} is correct!")
        print(f"Example of use: {meaning}")
        return 1
    else:
        print(f"That was the wrong answer!")
        return 0


def scoreboard(score):
    """
    Calculates the percentage of correct answers
    """
    global result
    result = int((score / len(questions)) * 100)
    print(f"You have completed the quiz with {result}% correct answers.")


def ranking_list(user_name, final_result):
    """
    Add results to list
    Print ranking list from highest to lowest score
    https://www.statology.org/create-table-in-python/
    """
    col_names = ["User", "Score (%)"]
    score_table.append([user_name, final_result])
    sorted_table = sorted(score_table, key=itemgetter(1), reverse=True)
    print(tabulate(
        sorted_table,
        headers=col_names,
        tablefmt="pretty",
        showindex="always"))


def new_game(user_name, final_result):
    """
    Prints different messages depend on score
    Asks user for new game
    """
    while True:
        if final_result == 100:
            print(f"Wonderful {user_name}, {final_result}% score, "
                  "you have perfected Canadian slang!")
            play_again = input("Do you want to confirm your knowledge or "
                               "have one of your friends try? (Yes / No):\n")
            if play_again.lower() == "yes":
                return True
            elif play_again.lower() == "no":
                return False
            else:
                print("Please enter your Yes or No!")
                continue
        elif final_result >= 50:
            print(f"Congratulations {user_name} on {final_result}% score, "
                  "we believe you can score 100% in the next round!")
            play_again = input("Do you want to try again? "
                               "Maybe your friends want to try? (Yes / No):\n")
            if play_again.lower() == "yes":
                return True
            elif play_again.lower() == "no":
                return False
            else:
                print("Please enter your Yes or No!")
                continue
        elif final_result < 50:
            print(f"Well {user_name}, "
                  f"we think you can do more than {final_result}%!")
            play_again = input("Do you want to try your luck? "
                               "Maybe your friends want to try? (Yes / No):\n")
            if play_again.lower() == "yes":
                return True
            elif play_again.lower() == "no":
                return False
            else:
                print("Please enter your Yes or No!")
                continue


def main():
    """
    Run all game function
    """
    game()
    while new_game(name, result):
        game()


main()
