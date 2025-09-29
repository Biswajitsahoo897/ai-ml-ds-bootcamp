
class KonBanegaCr:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of India?",
                "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
                "answer": "B",
                "lifeline": "Hint: It's the seat of government."
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "B",
                "lifeline": "Hint: It's named after the Roman god of war."
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Leo Tolstoy", "D. Mark Twain"],
                "answer": "B",
                "lifeline": "Hint: He is known as one of the greatest playwrights."
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
                "answer": "D",
                "lifeline": "Hint: It covers more than 63 million square miles."
            },
            {
                "question": "In which year did the Titanic sink?",
                "options": ["A. 1910", "B. 1912", "C. 1914", "D. 1916"],
                "answer": "B",
                "lifeline": "Hint: It was during its maiden voyage."
            }
        ]
        self.score = 0
        self.current_question = 0

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            print(f"\nQuestion {self.current_question + 1}: {question_data['question']}")
            for option in question_data['options']:
                print(option)
        else:
            print("\nNo more questions available!")

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.current_question]["answer"]
        if user_answer.upper() == correct_answer:
            print("Correct answer!")
            self.score += 1
            self.current_question += 1
        else:
            print("Wrong answer! Game Over.")
            print(f"Your score: {self.score}")
            return False
        return True

    def use_lifeline(self):
        print(self.questions[self.current_question]["lifeline"])

    def play_game(self):
        print("Welcome to Kaun Banega Crorepati!")
        while True:
            self.display_question()
            user_input = input("Enter your answer (A/B/C/D) or 'L' for lifeline (or 'Q' to quit): ").strip()
            if user_input.upper() == 'L':
                self.use_lifeline()
            elif user_input.upper() == 'Q':
                print("Thank you for playing! Your score: ", self.score)
                break
            else:
                if not self.check_answer(user_input):
                    break
        print("Final Score: ", self.score)

if __name__ == "__main__":
    game = KonBanegaCr()
    game.play_game()
