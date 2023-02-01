import random
import sys
import decimal

flash_cards = []
decimal.getcontext().prec = 3


def ask_question(card):
    # Asks the user a question from a card
    question = card["question"]
    correct_answer = card["answer"]

    user_answer = input(f"{question}: ")

    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect! The correct answer is {correct_answer}.\n")
        return False


def add_card():
    # Adds a card to the deck
    answer = input("Enter an answer or term: ")
    question = input("Enter the question or definition: ")
    flash_cards.append({"question": question, "answer": answer})
    print("New card added!\n")


while True:
    # Main Program
    questions_asked = 0
    score = 0

    if not flash_cards:
        # If flash_cards is empty
        choice = input("No flash cards found. Please enter a new card or exit.\n"
                       "Enter 1 to add a new card.\n"
                       "Enter 'exit' to quit.\n")
        if choice.lower() == 'exit':
            sys.exit()
        elif choice == "1":
            add_card()
        else:
            print("Invalid option.\n")
    else:
        choice = input("What would you like to do?\n"
                       "Enter 1 to add a new card.\n"
                       "Enter 2 to answer flash card questions.\n"
                       "Enter 'exit' to quit.\n")
        if choice.lower() == 'exit':
            sys.exit()
        elif choice == "1":
            add_card()
        elif choice == "2":
            curr_cards_left = flash_cards.copy()
            while curr_cards_left:
                new_card = random.choice(curr_cards_left)
                new_question = ask_question(new_card)
                questions_asked += 1
                if new_question:
                    score += 1
                curr_cards_left.remove(new_card)
            if not curr_cards_left:
                final_score = decimal.Decimal(score) / decimal.Decimal(questions_asked)
                print("All cards have been asked!\n"
                      "Your score is: ", score, "/", questions_asked, " (", final_score, "%)\n")
        else:
            print("Invalid option.")
