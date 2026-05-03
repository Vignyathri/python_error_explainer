# Smart Python Error Explainer (GUI Version)

import tkinter as tk
from tkinter import messagebox

error_count = {}

def detect_error_type(error):
    error = error.lower()

    if "syntaxerror" in error:
        return "SyntaxError"
    elif "indentationerror" in error:
        return "IndentationError"
    elif "nameerror" in error:
        return "NameError"
    elif "typeerror" in error:
        return "TypeError"
    elif "valueerror" in error:
        return "ValueError"
    elif "indexerror" in error:
        return "IndexError"
    elif "keyerror" in error:
        return "KeyError"
    else:
        return "Unknown"


def explain_error(error_type):
    explanations = {
        "SyntaxError": "❌ Syntax Error\nCheck missing ':' or brackets.\n\nExample:\nif x > 5:\n    print(x)",
        "IndentationError": "❌ Indentation Error\nFix spacing (use 4 spaces).\n\nExample:\nif True:\n    print('Hello')",
        "NameError": "❌ Name Error\nVariable not defined.\n\nExample:\nx = 10\nprint(x)",
        "TypeError": "❌ Type Error\nWrong data types.\n\nExample:\nprint(str(5) + ' apples')",
        "ValueError": "❌ Value Error\nInvalid value.\n\nExample:\nint('10')",
        "IndexError": "❌ Index Error\nIndex out of range.\n\nExample:\na = [1,2,3]\nprint(a[2])",
        "KeyError": "❌ Key Error\nWrong dictionary key.\n\nExample:\nd = {'a':1}\nprint(d['a'])",
        "Unknown": "⚠️ Unknown Error\nCheck syntax or logic."
    }

    return explanations.get(error_type)


def update_stats(error_type):
    error_count[error_type] = error_count.get(error_type, 0) + 1


def explain():
    user_input = entry.get()

    if not user_input.strip():
        messagebox.showwarning("Input Error", "Please enter an error message")
        return

    error_type = detect_error_type(user_input)
    update_stats(error_type)

    result = explain_error(error_type)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


def show_stats():
    stats = "📊 Error Statistics:\n"
    if not error_count:
        stats += "No data yet."
    else:
        for key, value in error_count.items():
            stats += f"{key} → {value} times\n"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, stats)


# GUI Window
root = tk.Tk()
root.title("Smart Python Error Explainer")
root.geometry("500x500")

# Title
title = tk.Label(root, text="Smart Error Explainer", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Input field
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

explain_btn = tk.Button(btn_frame, text="Explain Error", command=explain)
explain_btn.grid(row=0, column=0, padx=10)

stats_btn = tk.Button(btn_frame, text="Show Stats", command=show_stats)
stats_btn.grid(row=0, column=1, padx=10)

# Output area
output_text = tk.Text(root, height=15, width=60)
output_text.pack(pady=10)

# Run app
root.mainloop()
