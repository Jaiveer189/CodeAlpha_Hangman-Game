import random
import tkinter as tk
from tkinter import messagebox

# ==================== 1. GAME DATA & STATE ====================
words_pool = ["python", "guitars", "coffee", "coding", "planets", "hangman", "hacker"]
chosen_word = random.choice(words_pool)
attempts_left = 6
guessed_letters = []
streak = 0          # for tracking the player winning rate 
is_dark_mode = True # Initial theme is dark mode for better aesthetics 


# ==================== 2. THEME TOGGLE LOGIC ====================
def toggle_theme():
    global is_dark_mode
    
    if is_dark_mode:
        # LIGHT MODE COLORS
        root.config(bg="#f5f6fa")
        title_label.config(bg="#f5f6fa", fg="#2c3e50")
        word_label.config(bg="#f5f6fa", fg="#2c3e50")
        attempts_label.config(bg="#f5f6fa", fg="#e74c3c")
        streak_label.config(bg="#f5f6fa", fg="#2c3e50")
        theme_button.config(text="🌙 Dark Mode", bg="#2c3e50", fg="white")
        is_dark_mode = False
    else:
        # DARK MODE COLORS
        root.config(bg="#2c3e50")
        title_label.config(bg="#2c3e50", fg="white")
        word_label.config(bg="#2c3e50", fg="#f1c40f")
        attempts_label.config(bg="#2c3e50", fg="#e74c3c")
        streak_label.config(bg="#2c3e50", fg="white")
        theme_button.config(text="☀️ Light Mode", bg="#f1c40f", fg="black")
        is_dark_mode = True


# ==================== 3. GAME RESET LOGIC ====================
def reset_game(won=True):
    global chosen_word, attempts_left, guessed_letters, streak
    
    if won:
        streak += 1  # Increment streak if player won
    else:
        streak = 0   # decrement streak if player lost 
        
    chosen_word = random.choice(words_pool)
    attempts_left = 6
    guessed_letters = []
    
    # Update UI elements with new game state
    word_label.config(text="_ " * len(chosen_word))
    attempts_label.config(text=f"Attempts Left: {attempts_left}")
    streak_label.config(text=f"Streak: 🔥 {streak}")


# ==================== 4. GUESS HANDLING LOGIC ====================
# event none becuase when player press enter button it can trigger this function and we want to precvent default behavior of enter key which is to submit the form and cause a page refresh in web apps, here it will prevent any duplicate events from firing when enter is pressed
def make_a_guess(event=None):
    global attempts_left
    
    # 1. Remove input letter for better spacing and convert to Lowercases for uniformity.
    guess = guess_entry.get().strip().lower()
    guess_entry.delete(0, tk.END)
    
    # 2. Ignore when player clicks guess without entering anything 
    if not guess:
        return "break"
        
    # 3. If more then one letter is entered or if it's not an alphabet show warning.
    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Warning", "Please enter a single valid letter!")
        return "break"
        
    if guess in guessed_letters:
        messagebox.showinfo("Info", f"You already guessed '{guess}'!")
        return "break"
        
    guessed_letters.append(guess)
    
    if guess not in chosen_word:
        attempts_left -= 1
        
    # Genrate new display word with guessed letters.
    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            
    word_label.config(text=display_word)
    attempts_label.config(text=f"Attempts Left: {attempts_left}")
    
    # WIN CONDITION
    if "_" not in display_word:
        messagebox.showinfo("Winner!", "🎉 Correct guess! Moving to the next word...")
        reset_game(won=True)
        return "break"
        
    # LOSS CONDITION
    if attempts_left == 0:
        messagebox.showerror("Game Over", f"💀 Out of attempts! The word was: {chosen_word}")
        reset_game(won=False)
        
    return "break"  # Yeh Tkinter ko duplicate events chalane se rokta hai
        
    # LOSS CONDITION
    if attempts_left == 0:
        messagebox.showerror("Game Over", f"💀 Out of attempts! The word was: {chosen_word}")
        reset_game(won=False)


# ==================== 5. ADVANCED UI LAYOUT ====================
root = tk.Tk()
root.title("Advanced Hangman Engine")
root.geometry("450x450")
root.config(bg="#2c3e50")

# Top Bar (Theme Toggle Button)
theme_button = tk.Button(root, text="☀️ Light Mode", font=("Arial", 10, "bold"), bg="#f1c40f", fg="black", command=toggle_theme)
theme_button.pack(anchor="ne", padx=15, pady=10) # 'ne' ka matlab North-East (top right corner)

# Streak Indicator
streak_label = tk.Label(root, text=f"Streak: 🔥 {streak}", font=("Arial", 12, "bold"), bg="#2c3e50", fg="white")
streak_label.pack(anchor="nw", padx=15, pady=0)  # 'nw' ka matlab North-West (top left corner)

# Main Titles & Labels
title_label = tk.Label(root, text="⚡ HANGMAN PRO ⚡", font=("Arial", 22, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=10)

word_label = tk.Label(root, text="_ " * len(chosen_word), font=("Arial", 26, "bold"), bg="#2c3e50", fg="#f1c40f")
word_label.pack(pady=25)

attempts_label = tk.Label(root, text=f"Attempts Left: {attempts_left}", font=("Arial", 14), bg="#2c3e50", fg="#e74c3c")
attempts_label.pack(pady=5)

# Input Box & Action Button
guess_entry = tk.Entry(root, font=("Arial", 18), width=6, justify="center")
guess_entry.pack(pady=15)

guess_button = tk.Button(root, text="GUESS", font=("Arial", 12, "bold"), bg="#2ecc71", fg="white", width=12, height=1, command=make_a_guess)
guess_button.pack(pady=10)

# ==================== KEYBOARD BINDINGS ====================
# when player in the input box he will press enter key to submit the guess .
guess_entry.bind("<Return>", make_a_guess)
root.bind("<Return>", make_a_guess)

root.mainloop()

# ==================== 6. GAME RESET LOGIC (CONTINUED) ====================
def reset_game(won=True):
    global chosen_word, attempts_left, guessed_letters, streak
    
    if won:
        streak += 1  # Increment streak if player won
    else:
        streak = 0   # decrement streak if player lost 
        
    chosen_word = random.choice(words_pool)



