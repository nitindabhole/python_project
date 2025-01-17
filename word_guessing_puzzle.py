import random

class WordGuessingPuzzle:
    def __init__(self, word_list):
        """
        Constructor to initialize the game.
        :param word_list: Dictionary of words with hints.
        """
        self.word_list = word_list
        self.name = ""
        self.score = 0
        self.level = 1

    def greet_user(self):
        """Get the user's name and greet them."""
        self.name = input("What is your name? ")
        print(f"Hello {self.name}, welcome to the Word Guessing Puzzle!")

    def play_level(self, chosen_word, hint):
        """
        Play a single level of the game.
        :param chosen_word: The word the user has to guess.
        :param hint: A hint for the word.
        :return: True if the user guesses correctly, False otherwise.
        """
        attempts = 3
        print(f"\nLevel {self.level}:")
        print(f"Hint: {hint}")
        
        while attempts > 0:
            guess = input("Guess the word: ").lower()
            if guess == chosen_word:
                print(f"Congratulations, {self.name}! You guessed the word '{chosen_word}' correctly!")
                self.score += attempts * 10  # Update score based on remaining attempts
                self.level += 1
                return True
            else:
                attempts -= 1
                print(f"Wrong guess. You have {attempts} attempts left.")

        print(f"Sorry, {self.name}. You lost at Level {self.level}. The correct word was '{chosen_word}'.")
        return False

    def play_game(self):
        """Main game loop to play all levels."""
        self.greet_user()
        self.score = 0  # Reset score for a new game
        self.level = 1  # Reset level for a new game

        puzzles = random.sample(list(self.word_list.items()), 10)  # Select 10 random puzzles

        for chosen_word, hint in puzzles:
            if not self.play_level(chosen_word, hint):
                print(f"Your final score is: {self.score}")
                return False

        print(f"\nCongratulations, {self.name}! You successfully completed all 10 levels!")
        print(f"Your final score is: {self.score}")
        return True

# Initialize the game and allow restarting
if __name__ == "__main__":
    word_list = {
        "python": "A popular programming language named after a snake.",
        "java": "A versatile programming language, often associated with coffee.",
        "javascript": "The language of the web for interactive features.",
        "ruby": "A precious stone and also a programming language.",
        "html": "The standard markup language for creating web pages.",
        "css": "Stylesheets that make web pages look beautiful.",
        "react": "A popular JavaScript library for building user interfaces.",
        "django": "A high-level Python web framework.",
        "flask": "A lightweight Python web framework.",
        "bootstrap": "A popular CSS framework for responsive design."
    }

    while True:
        game = WordGuessingPuzzle(word_list)
        success = game.play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break
