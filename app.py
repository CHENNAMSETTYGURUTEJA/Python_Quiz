import tkinter as tk
from tkinter import messagebox
import random
import sys

# ---------------------- QUIZ DATA ---------------------- #
questions = [
    ("What is the output of print(type([]))?",
     ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"], 0),

    ("Which of the following is immutable in Python?",
     ["list", "set", "dict", "tuple"], 3),

    ("What is the default value of 'end' in print()?",
     ["\\n", "space", "tab", "None"], 0),

    ("Which keyword is used for function in Python?",
     ["def", "func", "function", "lambda"], 0),

    ("Which operator is used for exponentiation in Python?",
     ["^", "**", "%", "//"], 1),

    ("What is the maximum possible length of an identifier in Python?",
     ["16", "32", "128", "No limit"], 3),

    ("What does PEP stand for in Python?",
     ["Python Enhancement Proposal", "Programming Environment for Python", "Python Event Processing", "Performance Evaluation Protocol"], 0),

    ("Which function is used to get the length of a list?",
     ["count()", "length()", "len()", "size()"], 2),

    ("What is the output of 3 * 'abc'?",
     ["abcabcabc", "Error", "abc*3", "None"], 0),

    ("Which method is used to add an element to a set?",
     ["append()", "add()", "insert()", "extend()"], 1),

    ("What does the 'break' keyword do?",
     ["Exits the loop", "Skips current iteration", "Ends program", "Continues loop"], 0),

    ("Which symbol is used to start a comment in Python?",
     ["//", "#", "/*", "<!--"], 1),

    ("What is the output of bool('False')?",
     ["False", "True", "Error", "None"], 1),

    ("Which keyword is used to define a class in Python?",
     ["define", "class", "struct", "object"], 1),

    ("Which method removes the last item from a list?",
     ["delete()", "remove()", "pop()", "discard()"], 2),

    ("Which loop runs at least once regardless of condition?",
     ["for", "while", "do-while", "None"], 3),

    ("Which library is used for data analysis in Python?",
     ["numpy", "pandas", "scipy", "seaborn"], 1),

    ("What is the output of 5 // 2?",
     ["2.5", "3", "2", "Error"], 2),

    ("Which keyword is used to handle exceptions?",
     ["try", "except", "catch", "handle"], 1),

    ("Which function is used to get user input in Python 3?",
     ["input()", "scan()", "read()", "get()"], 0),

    ("What will be the output of sorted([3,1,2], reverse=True)?",
     ["[1,2,3]", "[3,2,1]", "[2,3,1]", "Error"], 1),

    ("Which module in Python is used for regular expressions?",
     ["regex", "pyregex", "re", "regexp"], 2),

    ("What is the output of list(range(2,10,2))?",
     ["[2,4,6,8]", "[2,3,4,5,6,7,8,9]", "[2,10]", "Error"], 0),

    ("What is the output of 'hello'.capitalize()?",
     ["Hello", "HELLO", "hello", "Error"], 0),

    ("Which of the following is not a valid way to import a module?",
     ["import os", "import sys as system", "from math import *", "import 123math"], 3),

    ("What will be the result of 2 ** 3 ** 2?",
     ["64", "512", "16", "Error"], 1),

    ("Which function converts an object into a string?",
     ["int()", "str()", "repr()", "format()"], 1),

    ("What is the result of set([1,2,2,3])?",
     ["{1,2,2,3}", "{1,2,3}", "[1,2,3]", "(1,2,3)"], 1),

    ("Which statement is true about Python memory management?",
     ["Python has no garbage collector", "It uses reference counting and GC", "It requires manual free()", "It uses malloc/free directly"], 1),

    ("What is the output of type(lambda x: x)?",
     ["<class 'function'>", "<class 'lambda'>", "<class 'method'>", "Error"], 0)
]

# Pick 10 random questions
questions = random.sample(questions, 10)

# ---------------------- QUIZ APP ---------------------- #
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Mini Quiz")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e293b")

        self.time_left = 15 * 60
        self.q_index = 0
        self.score = 0
        self.selected_option = tk.IntVar()

        # Heading
        self.title = tk.Label(root, text="PYTHON MINI QUIZ", font=("Helvetica", 40, "bold"),
                              bg="#1e293b", fg="#38bdf8")
        self.title.pack(pady=20)

        # Timer display
        self.timer_label = tk.Label(root, text="Time Left: 30:00", font=("Helvetica", 20, "bold"),
                                    bg="#1e293b", fg="#facc15")
        self.timer_label.pack(pady=10)

        # Question label
        self.question_label = tk.Label(root, text="", font=("Arial", 24, "bold"),
                                       wraplength=700, bg="#1e293b", fg="#f8fafc")
        self.question_label.pack(pady=20)

        # Options
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.selected_option, value=i,
                                font=("Arial", 18), bg="#1e293b", fg="#e2e8f0",
                                activebackground="#1e293b", activeforeground="#38bdf8",
                                selectcolor="white")
            rb.pack(anchor="w", padx=200, pady=5)
            self.radio_buttons.append(rb)

        # Next button
        self.next_button = tk.Button(root, text="Next", command=self.check_answer,
                                     font=("Arial", 12, "bold"), bg="#38bdf8", fg="black",
                                     relief="raised", padx=20, pady=10)
        self.next_button.pack(pady=30)

        self.show_question()
        self.update_timer()

    def show_question(self):
        q, options, _ = questions[self.q_index]
        self.selected_option.set(-1)
        self.question_label.config(text=f"Q{self.q_index + 1}. {q}")
        for i, option in enumerate(options):
            self.radio_buttons[i].config(text=option)

        # Track selected option to update font + black dot
        self.selected_option.trace_add("write", self.update_fonts)

    # Update fonts + radio button dot color
    def update_fonts(self, *args):
        selected = self.selected_option.get()
        for i, rb in enumerate(self.radio_buttons):
            if i == selected:
                rb.config(font=("Arial", 16, "bold"), selectcolor="black")
            else:
                rb.config(font=("Arial", 14, "normal"), selectcolor="white")

    def check_answer(self):
        q, options, correct_index = questions[self.q_index]
        chosen = self.selected_option.get()

    # Feedback window
        feedback = tk.Toplevel(self.root)
        feedback.configure(bg="#0f172a")
        feedback.title("Answer Check")
    
    # Set popup size
        popup_width = 220
        popup_height = 100

    # Get main window position
        root_x = self.root.winfo_x()
        root_y = self.root.winfo_y()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

    # Calculate center position
        x = root_x + (root_width // 2) - (popup_width // 2)
        y = root_y + (root_height // 2) - (popup_height // 2)

        feedback.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        if chosen == correct_index:
            self.score += 1
            msg = tk.Label(feedback, text="✅ Correct!", font=("Helvetica", 22, "bold"),
                       fg="#22c55e", bg="#0f172a")
        else:
            msg = tk.Label(feedback, text="❌ Incorrect!", font=("Helvetica", 22, "bold"),
                       fg="#ef4444", bg="#0f172a")
        msg.pack(expand=True)

    # Auto close and show next
        self.root.after(750, lambda: (feedback.destroy(), self.next_question()))



    
    def next_question(self):
        self.q_index += 1
        if self.q_index < len(questions):
            self.show_question()
        else:
            self.end_quiz()

    def update_timer(self):
        mins, secs = divmod(self.time_left, 60)
        self.timer_label.config(text=f"Time Left: {mins:02d}:{secs:02d}")
        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.end_quiz()

    def end_quiz(self):
        result_window = tk.Toplevel(self.root)
        result_window.title("Quiz Completed")
        result_window.geometry("600x400")
        result_window.configure(bg="#0f172a")

        heading = tk.Label(result_window, text="🎉 THANK YOU 🎉",
                           font=("Helvetica", 28, "bold"), fg="#38bdf8", bg="#0f172a")
        heading.pack(pady=30)

        message = tk.Label(result_window, text="You have successfully completed the quiz!",
                           font=("Helvetica", 18), fg="#f8fafc", bg="#0f172a")
        message.pack(pady=10)

        score_text = tk.Label(result_window,
                              text=f"Your Score: {self.score}/{len(questions)}",
                              font=("Helvetica", 22, "bold"), fg="#facc15", bg="#0f172a")
        score_text.pack(pady=20)

        exit_btn = tk.Button(result_window, text="Exit", font=("Arial", 16, "bold"),
                             bg="#ef4444", fg="white", padx=20, pady=10,
                             command=lambda: (result_window.destroy(), self.root.destroy(), sys.exit()))
        exit_btn.pack(pady=30)


# ---------------------- MAIN ---------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
