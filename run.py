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
        "Property values plummeted when the municipality established nuisance grounds nearby."
    ],
    [
        "Often an invitation to engage in a fight, skoden has recently been used in battles over pipeline projects."
    ],
    [
        "Having grown up in Winnipeg, the cashier knew what his customer meant when she ordered a jambuster."
    ],
    ["Get our your scribblers and write your names on the covers."],
    ["Alina called for her friend to huck her the ball."],
    [
        "The Donnybrook Fair in Dublin, Ireland, was so rowdy that any tussle became known as a donnybrook."
    ],
    [
        "Derived from Chinook Jargon, skookum appears in many place names in the Pacific Northwest."
    ],
]


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


def username():
    """
    Asks the user to play.
    Prompt for user name.
    """
    global name
    print("-----------------")
    while True:
        game_accept = input("Do you want to test your knowledge? (Yes / No): ")
        if game_accept.lower() == "yes":
            print("We're glad you want to play!")
            break
        elif game_accept.lower() == "no":
            print("Ok maybe next time. We wish you a pleasant day")
            quit()
        else:
            print("Incorrect entry!")
            print("Your answer must be Yes or No!")
    name = input("Please enter your name: ")
    print(f"We wish you the best of luck {name}, the game can begin!")


rules_intro()
username()