import random

class QuizGame:
    def __init__(self, topics):
        self.topics = topics
        self.score = 0
    
    def display_question(self, question):
        print('\nQuestion:' + question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}.{option}")
        
    def choose_topic(self):
        print('Choose a topic with difficulty:')
        for i, topic in enumerate(self.topics, start=1):
            print(f"{i}.{topic['name']} ({topic['difficult']})")
        while True:
            try:
                choice = int(input('Enter the number of your choice: '))
                if 1 <= choice <= len(self.topics):
                    self.current_topic = self.topics[choice - 1]
                    break
                else:
                    print('Invalid choice. Please enter a valid number')
            except ValueError:
                print('Invalid input, Please enter a number in topic')
    
    

    def get_user_answer(self):
        while True:
            try:
                user_answer = int(input("Your answer: "))
                if 1 <= user_answer <= 4:
                    return user_answer
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, question, user_answer):
        correct_answer = question["correct_option"]
        if user_answer == correct_answer:
            self.score += 1
            print("Correct! Well done.")
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")

        current_topic_name = self.current_topic['name']
        current_difficulty_level = self.current_topic['difficult']
        print(f"Your current score for {current_topic_name} ({current_difficulty_level}): {self.score}/{len(self.current_topic['questions'])}")

    def play(self):  
        self.choose_topic()

        print(f"\n--- {self.current_topic['name']} ({self.current_topic['difficult']}) Quiz ---")
        questions_of_difficulty = [q for q in self.current_topic["questions"] if q["difficulty"] == self.current_topic["difficult"]]
        random.shuffle(questions_of_difficulty)

        for question in questions_of_difficulty:
            self.display_question(question)
            user_answer = self.get_user_answer()
            self.check_answer(question, user_answer)

        print(f"\n{self.current_topic['name']} Quiz completed!")

        print("\nOverall Quiz completed!")
        print(f"Your final score: {self.score}/{len(questions_of_difficulty)}")


easy_geography_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "correct_option": 2,
        "difficulty": "Easy",
    },
    {
        "question": "Which river flows through Paris?",
        "options": ["The Seine", "The Rhine", "The Danube", "The Thames"],
        "correct_option": 1,
        "difficulty": "Easy",
    },
    {
        "question":"What is the name of the smallest country in the world?",
        "options": ["Vatican City", "Monaco", "Singapore", "Nauru"],
        "correct_option": 1,
        "difficulty": "Easy",
    },
    {
        "question": "Who painted the famous painting 'Mona Lisa'?",
        "options": ["Leonardo da Vinci", "Michelangelo", "Rembrandt", "Vincent van Gogh"],
        "correct_option": 1,
        "difficulty": "Easy",
    },

]

hard_geography_questions = [
    {
        "question": "Which mountain is the highest peak in North America?",
        "options": ["Denali", "K2", "Mount Everest", "Aconcagua"],
        "correct_option": 1,
        "difficulty": "Hard",
    },
    {
        "question": "Where is the Great Barrier Reef located?",
        "options": ["Indonesia", "New Zealand", "Australia", "South Africa"],
        "correct_option": 3,
        "difficulty": "Hard",
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["6", "7", "5", "4"],
        "correct_option": 2,
        "difficulty": "Hard",
    }

]

medium_geography_questions = [
    {
        "question": "Which river is the longest in the world?",
        "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
        "correct_option": 1,
        "difficulty": "Medium",
    },
        {
        "question": "Where was the first World War fought?",
        "options": ["France", "Germany", "Austria-Hungary", "Russia"],
        "correct_option": 1,
        "difficulty": "Medium",
    },
    {
        "question":"What African country has Portuguese as its official language?",
        "options": ["Angola", "Mozambique", "Portugal", "Brazil"],
        "correct_option": 2,
        "difficulty": "Medium",
    },
]

hard_science_questions = [
    {
        "question": "Which planet is known as the Blue Planet?",
        "options": ["Mars", "Venus", "Earth", "Neptune"],
        "correct_option": 3,
        "difficulty": "Hard",
    },
    {
        "question": "Who discovered DNA structure?",
        "options": ["Charles Darwin", "Francis Crick", "James Watson", "Thomas Hunt Morgan"],
        "correct_option": 3,
        "difficulty": "Hard",
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Canberra", "Sydney", "Perth", "Adelaide"],
        "correct_option": 1,
        "difficulty": "Hard",
    }
]

easy_science_questions = [
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "O2", "CH4"],
        "correct_option": 1,
        "difficulty": "Easy",
    },
    {
        "question": "How many atoms are there in a molecule of oxygen gas?",
        "options": ["6", "2", "9", "7"],
        "correct_option":2 ,
        "difficulty": "Easy",
    },
    {
        "question": "What is the boiling point of mercury?",
        "options": ["85.0°C", "100.7°C", "356.7°C","140.0°C"],
        "correct_option": 3,
        "difficulty": "Easy",
    }
]

medium_science_questions = [
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Fe", "Hg"],
        "correct_option": 1,
        "difficulty": "Medium",
    },
    {
        "question": "What is the atomic number of carbon?",
        "options": ["7", "6", "8", "9"],
        "correct_option": 2,
        "difficulty": "Medium",
    },
    {
        "question": "Which element has the highest melting and boiling points?",
        "options": ["Tungsten", "Iron", "Gold", "Mercury"],
        "correct_option": 1,
        "difficulty": "Medium",
    }
]

topics = [
    {"name": "Geography", "difficult": "Hard", "questions": hard_geography_questions},
    {"name": "Geography", "difficult": "Easy", "questions": easy_geography_questions},
    {"name": "Geography", "difficult": "Medium", "questions": medium_geography_questions},
    {"name": "Science", "difficult": "Hard", "questions": hard_science_questions},
    {"name": "Science", "difficult": "Easy", "questions": easy_science_questions},
    {"name": "Science", "difficult": "Medium", "questions": medium_science_questions},
]

quiz_game = QuizGame(topics)
quiz_game.play()