import tkinter as tk
from tkinter import ttk
import random


WORDS = ["python", "java", "javascript", "kotlin", "hangman", "computer", "programming"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.configure(bg="black")  
        
        
        self.word = random.choice(WORDS).lower()
        self.word_state = ["_"] * len(self.word)
        self.guesses = set()
        self.max_attempts = 6
        self.attempts = 0
        
       
        self.setup_ui()

    def setup_ui(self):
      
        self.word_label = tk.Label(self.root, text=" ".join(self.word_state), font=("Arial", 24), fg="green", bg="black")
        self.word_label.pack(pady=20)
        
     
        self.canvas = tk.Canvas(self.root, width=400, height=300, bg="black", highlightthickness=0)
        self.canvas.pack(pady=20)
        self.draw_hangman()  #
        
        self.input_entry = tk.Entry(self.root, font=("Arial", 18), fg="green", bg="black", insertbackground="green")
        self.input_entry.pack(pady=10)
        
        self.guess_button = ttk.Button(self.root, text="Guess", command=self.guess_letter)
        self.guess_button.pack(pady=10)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 18), fg="green", bg="black")
        self.feedback_label.pack(pady=20)

        self.play_again_button = ttk.Button(self.root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)
        self.play_again_button.pack_forget()  
        
        style = ttk.Style()
        style.configure("TButton", foreground="green", background="black", font=("Arial", 18), padding=10)
        style.map("TButton", background=[("active", "black")], foreground=[("active", "green")])

    def draw_hangman(self):
        self.canvas.delete("all")  
        self.canvas.create_line(50, 250, 150, 250, fill="green", width=2)  
        self.canvas.create_line(100, 250, 100, 50, fill="green", width=2)  
        self.canvas.create_line(100, 50, 200, 50, fill="green", width=2)  
        self.canvas.create_line(200, 50, 200, 70, fill="green", width=2)  
        
        if self.attempts > 0:
            self.canvas.create_oval(185, 70, 215, 100, outline="green", width=2) 
        if self.attempts > 1:
            self.canvas.create_line(200, 100, 200, 170, fill="green", width=2)
        if self.attempts > 2:
            self.canvas.create_line(200, 120, 170, 150, fill="green", width=2) 
        if self.attempts > 3:
            self.canvas.create_line(200, 120, 230, 150, fill="green", width=2) 
        if self.attempts > 4:
            self.canvas.create_line(200, 170, 170, 220, fill="green", width=2)  
        if self.attempts > 5:
            self.canvas.create_line(200, 170, 230, 220, fill="green", width=2)  

    def guess_letter(self):
        letter = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END) 
        
        if not letter.isalpha() or len(letter) != 1:
            self.feedback_label.config(text="Please enter a valid single letter.")
            return

        if letter in self.guesses:
            self.feedback_label.config(text="You've already guessed that letter.")
            return

        self.guesses.add(letter)
        if letter in self.word:
           
            for i, l in enumerate(self.word):
                if l == letter:
                    self.word_state[i] = letter
            self.word_label.config(text=" ".join(self.word_state))
            self.feedback_label.config(text="Good guess!")
        else:
           
            self.attempts += 1
            self.draw_hangman()
            self.feedback_label.config(text=f"Incorrect guess! {self.max_attempts - self.attempts} attempts left.")
        
        self.check_win_loss()

    def check_win_loss(self):
        if "_" not in self.word_state:
            self.feedback_label.config(text="Congratulations! You won!")
            self.end_game()
        elif self.attempts >= self.max_attempts:
            self.feedback_label.config(text=f"Game Over! The word was '{self.word}'.")
            self.end_game()

    def end_game(self):
        self.guess_button.config(state=tk.DISABLED)
        self.play_again_button.pack()

    def reset_game(self):
        self.word = random.choice(WORDS).lower()
        self.word_state = ["_"] * len(self.word)
        self.guesses.clear()
        self.attempts = 0
        self.word_label.config(text=" ".join(self.word_state))
        self.draw_hangman()
        self.feedback_label.config(text="")
        self.guess_button.config(state=tk.NORMAL)
        self.play_again_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
