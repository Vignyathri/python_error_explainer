# Smart Python Error Explainer (GUI Version)
import tkinter as tk
from tkinter import messagebox

error_count = {}

# Detect error type
def detect_error_type(error):
    error = error.lower()

    error_map = {
        "syntaxerror": "SyntaxError",
        "indentationerror": "IndentationError",
        "taberror": "TabError",
        "nameerror": "NameError",
        "typeerror": "TypeError",
        "valueerror": "ValueError",
        "indexerror": "IndexError",
        "keyerror": "KeyError",
        "attributeerror": "AttributeError",
        "zerodivisionerror": "ZeroDivisionError",
        "importerror": "ImportError",
        "modulenotfounderror": "ModuleNotFoundError",
        "filenotfounderror": "FileNotFoundError",
        "permissionerror": "PermissionError",
        "oserror": "OSError",
        "ioerror": "IOError",
        "overflowerror": "OverflowError",
        "memoryerror": "MemoryError",
        "runtimeerror": "RuntimeError",
        "recursionerror": "RecursionError",
        "assertionerror": "AssertionError",
        "eoferror": "EOFError",
        "floatingpointerror": "FloatingPointError",
        "keyboardinterrupt": "KeyboardInterrupt",
        "notimplementederror": "NotImplementedError",
        "unboundlocalerror": "UnboundLocalError"
    }

    for key in error_map:
        if key in error:
            return error_map[key]

    return "Unknown"


# Explain errors
def explain_error(error_type):
    explanations = {
        "SyntaxError": "❌ Syntax Error\nCheck missing ':' or brackets.\n\nExample:\nif x > 5:\n    print(x)",

        "IndentationError": "❌ Indentation Error\nFix spacing (use 4 spaces).\n\nExample:\nif True:\n    print('Hello')",

        "TabError": "❌ Tab Error\nMixing tabs and spaces.\n\nFix: Use consistent indentation",

        "NameError": "❌ Name Error\nVariable not defined.\n\nExample:\nx = 10\nprint(x)",

        "TypeError": "❌ Type Error\nWrong data types.\n\nExample:\nprint(str(5) + ' apples')",

        "ValueError": "❌ Value Error\nInvalid value.\n\nExample:\nint('10')",

        "IndexError": "❌ Index Error\nIndex out of range.\n\nExample:\na = [1,2,3]\nprint(a[2])",

        "KeyError": "❌ Key Error\nWrong dictionary key.\n\nExample:\nd = {'a':1}\nprint(d['a'])",

        "AttributeError": "❌ Attribute Error\nObject has no attribute.\n\nExample:\n'hello'.append('a')",

        "ZeroDivisionError": "❌ Division by Zero\nCannot divide by zero.\n\nExample:\n10/0",

        "ImportError": "❌ Import Error\nModule cannot be imported.\n\nExample:\nimport unknownmodule",

        "ModuleNotFoundError": "❌ Module Not Found\nModule not installed.\n\nExample:\nimport numpy",

        "FileNotFoundError": "❌ File Not Found\nFile path incorrect.\n\nExample:\nopen('file.txt')",

        "PermissionError": "❌ Permission Error\nAccess denied.\n\nExample:\nWriting to restricted folder",

        "OSError": "❌ OS Error\nSystem-related issue.\n\nExample:\nFile system problem",

        "IOError": "❌ IO Error\nInput/output operation failed.\n\nExample:\nFile read/write issue",

        "OverflowError": "❌ Overflow Error\nNumber too large.\n\nExample:\nimport math\nmath.exp(1000)",

        "MemoryError": "❌ Memory Error\nSystem ran out of memory.\n\nExample:\nCreating huge list",

        "RuntimeError": "❌ Runtime Error\nGeneral runtime issue.\n\nExample:\nUnexpected failure",

        "RecursionError": "❌ Recursion Error\nToo many recursive calls.\n\nExample:\ndef f(): f()",

        "AssertionError": "❌ Assertion Error\nAssertion failed.\n\nExample:\nassert x > 0",

        "EOFError": "❌ EOF Error\nUnexpected end of input.\n\nExample:\ninput() issue",

        "FloatingPointError": "❌ Floating Point Error\nInvalid numeric operation",

        "KeyboardInterrupt": "❌ Interrupted by User\nProgram stopped manually (Ctrl+C)",

        "NotImplementedError": "❌ Not Implemented\nFeature not implemented",

        "UnboundLocalError": "❌ Unbound Local Error\nVariable used before assignment",

        "Unknown": "⚠️ Unknown Error\nCheck syntax or logic."
    }

    return explanations.get(error_type)


# Track stats
def update_stats(error_type):
    error_count[error_type] = error_count.get(error_type, 0) + 1


# Explain button function
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

    entry.delete(0, tk.END)


# Show stats
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
