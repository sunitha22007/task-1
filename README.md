
Hangman Game

Description:

This is a simple text-based Hangman Game developed using Python. The player tries to guess a randomly selected word one letter at a time. The player has a maximum of 6 incorrect attempts to guess the word.

Features:

Random word selection from a predefined list.
User-friendly console interface.
Maximum of 6 incorrect guesses.
Displays the guessed letters and hidden letters using underscores (_).
Win and Lose conditions.

Technologies Used:

Python
Random Module

How It Works:

1. The program selects a random word from a predefined list.
2. The player enters one letter at a time.
3. If the letter is correct, it is revealed in the word.
4. If the letter is incorrect, the number of remaining attempts decreases.
5. The game continues until:
The player guesses the complete word (Win), or
The player uses all 6 attempts (Lose).

Sample Word List

python
apple
computer
program
school


Output Example

---
Enter a letter: p
p _ _ _ _ _
Enter a letter: y
p y _ _ _ _
...
You Win!

Learning Outcomes:

Understanding Python loops.
Using conditional statements.
Working with lists and strings.
Implementing user input handling.
Using the random module.

GitHub Link: https://github.com/sunitha22007/task-1.git