import random

# 1. Game Setup
words_pool = ["python", "guitars", "coffee", "coding", "planets"]
chosen_word = random.choice(words_pool)
attempts_left = 6
guessed_letters = []

print("--- Welcome to Hangman! ---")

# 2. Main Game Loop
while attempts_left > 0:
    
    # Word Progress Logic
    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            
    print("\n===============================")
    print("Word to guess: " + display_word)
    print(f"Attempts left: {attempts_left}")
    print("===============================")
    
    # Win Condition Check
    if "_" not in display_word:
        print(f"\n🎉 Congratulations! You guessed the word: {chosen_word} 🎉")
        break  

    # Player Input (Yahan spacing theek kar di hai)
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print(f"\nYou already guessed the letter '{guess}'. Try a different one!")
        continue  
        
    guessed_letters.append(guess)
    
    # Check if guess is wrong
    if guess not in chosen_word:
        attempts_left -= 1  
        print(f"\n❌ Oops! '{guess}' is not in the word.")
    else:
        print(f"\n✅ Good job! '{guess}' is in the word.")

# 3. Game Over (If attempts run out)
if attempts_left == 0:
    print("\n===============================")
    print(f"💀 Game Over! You ran out of attempts.")
    print(f"The word was: {chosen_word}")
    print("===============================")