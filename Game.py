import random
import time
class Game():
    def __init__(self):
        print("Welcome to the Quiz Gamee")
        self.score = 0
        self.player_name = input("What is your name? ")
        self.questions = []
        self.correct_answers = {"option":"","answer":""}
        self.params = {'amount':'',"category":"","difficulty":"","type":""}

    def game_init(self):
        # Get the number of questions
        num_questions = self.get_user_input(prompt="How many questions would you like to answer(1-15)? ",lower_limit=1,upper_limit=15)
        self.params['amount'] = num_questions
        # Get the difficulty level
        difficulty = self.get_user_input(prompt="Choose your difficulty(1=Easy 2=Medium 3=Hard)? ",lower_limit=1,upper_limit=3)
        self.processed_difficulty(difficulty=str(difficulty))
        # Get the category
        category = self.get_user_input(prompt="What category would you love(9-32)? ",lower_limit=9,upper_limit=32)
        self.params['category'] = category
        # Get the type of questions
        type = self.get_user_input(prompt="What type of question do you want?(1=Multiple choice 2=TrueFalse) ",lower_limit=1,upper_limit=2)
        self.processed_type(type=str(type))


    def processed_difficulty(self,difficulty):
        if difficulty == '1':
            self.params['difficulty'] = 'easy'
        elif difficulty == '2':
            self.params['difficulty'] = 'medium'
        elif difficulty == '3':
            self.params['difficulty'] = 'hard'

    def processed_type(self,type):
        if type == "1":
            self.params['type'] = 'multiple'
        elif type == "2":
            self.params['type'] = 'boolean'

    def get_user_input(self,prompt, lower_limit, upper_limit):
        while True:
            try:
                user_input = int(input(prompt))
                if lower_limit <= user_input <= upper_limit:
                    return user_input
                else:
                    print(f"Not a valid input. Please enter a number between {lower_limit} and {upper_limit}.")
            except ValueError:
                print("Not a valid input. Please enter a valid integer.")

    def load_questions(self,list_of_questions):
        for question_info in list_of_questions:
            question = question_info['question']
            answers = question_info['incorrect_answers']
            answers.append(question_info['correct_answer'])
            self.questions.append({"question":question,"answers":answers})


    def display_question_and_processing(self,questions):
        ques_ind = 1
        print("--------------GAME START -----------")
        print(f"PLAYER NAME: {self.player_name}")
        print(f"CURRENT SCORE: {self.score}/{len(self.questions)}")
        while questions:
            # Randomly choose a question
            rand_ques_index = random.randint(0, len(questions) - 1)
            # Remove and print the selected question
            selected_question = questions.pop(rand_ques_index)
            print(f"Question {ques_ind} : {selected_question['question']}")
            self.randomly_select_and_present_options(selected_question['answers'])

            while True:
                try:
                    user_input = str(input("Enter your choice(A-B-C-D): "))
                    if user_input.lower() in ['a','b','c','d']:
                        time.sleep(1)
                        self.check_user_answer(user_input)
                        break
                    else:
                        print(f"Not a valid input.Please enter a valid choice")
                except ValueError:
                    print("Not a valid input. ")

            ques_ind += 1
        if ques_ind > len(self.questions):
            print(f"TOTAL SCORE: {self.score}/{self.params['amount']}")
            while True:
                try:
                    user_input = str(input("Would you like to play again (Y||N): "))
                    if user_input.lower() in ["y","n"]:
                        time.sleep(1)
                        self.check_user_answer(user_input)
                        break
                    else:
                        print(f"Not a valid input.Please enter a valid choice")
                except ValueError:
                    print("Not a valid input. ")

    def present_options(self,list_of_answers):
        options = ['A', 'B', 'C', 'D']

        for option, answer in zip(options,list_of_answers):
            if self.correct_answers['answer'] == answer:
                self.correct_answers["option"] = option.lower()
                print(f"{self.correct_answers}")
            print(f"{option}. {answer}")

    def randomly_select_and_present_options(self,answers):
        self.correct_answers = {"option":"","answer":answers[3]}

        random.shuffle(answers)
        self.present_options(answers)

    def check_user_answer(self,user_answer):
        if self.correct_answers['option'] == user_answer.lower():
            self.score += 1
            print("Yahoo! You got it")
            print(f"CURRENT SCORE: {self.score}")
            print("------------------------------")
        elif user_answer == "Y":
            self.game_init()

        elif user_answer == "N":
            print("Goodbye!")
        else:
            print(f"CURRENT SCORE: {self.score}")
            print("Sorry, the answer you entered is incorrect!")
            print("------------------------------")