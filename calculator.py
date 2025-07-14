
import tkinter as tk
root = tk.Tk()
root.title("Calculator Pro")
root.geometry("320x570")
root.configure(bg="#e6ecf0")
root.resizable(True, True)

FONT = ("Segoe UI", 20)
BTN_FONT = ("Segoe UI", 16, "bold")


display = tk.Entry(root, font=FONT, borderwidth=0, relief="flat", justify="right", bg="#f8fafc", fg="#222", highlightthickness=2, highlightbackground="#b0b0b0")
display.pack(fill="both", padx=12, pady=12, ipady=12)

clear_btn = tk.Button(root, text="Clear", font=BTN_FONT, bg="#ff6b6b", fg="#fff",
                      activebackground="#bcdffb", activeforeground="#fff", bd=0, relief="flat",
                      highlightthickness=0, command=lambda: on_button_click("C"))
clear_btn.pack(fill="x", padx=12, pady=(0, 8))



button_frame = tk.Frame(root, bg="#e6ecf0")
button_frame.pack(expand=True, fill="both", padx=8, pady=0)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]


def on_button_click(value):
    if value == "=":
        try:
            result = str(eval(display.get()))
            history.insert(tk.END, f"{display.get()} = {result}")
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, value)


btn_colors = {
    "C": {"bg": "#ff6b6b", "fg": "#fff"},
    "/": {"bg": "#4e8cff", "fg": "#fff"},
    "*": {"bg": "#4e8cff", "fg": "#fff"},
    "-": {"bg": "#4e8cff", "fg": "#fff"},
    "+": {"bg": "#4e8cff", "fg": "#fff"},
    "=": {"bg": "#2ecc71", "fg": "#fff"},
}

def on_enter(e):
    val = e.widget["text"]
    if is_dark:
        if val == "=":
            e.widget["bg"] = "#2bbd7e"
        elif val in ["/", "*", "-", "+"]:
            e.widget["bg"] = "#274690"
        elif val == "Clear":
            e.widget["bg"] = "#c62828"
        else:
            e.widget["bg"] = "#2c3654"
    else:
        if val == "=":
            e.widget["bg"] = "#27ae60"
        elif val in ["/", "*", "-", "+"]:
            e.widget["bg"] = "#bcdffb"
        elif val == "Clear":
            e.widget["bg"] = "#bcdffb"
        else:
            e.widget["bg"] = "#d1e3fa"

def on_leave(e):
    val = e.widget["text"]
    if is_dark:
        if val == "Clear":
            e.widget["bg"] = "#e57373"
        elif val in ["/", "*", "-", "+"]:
            e.widget["bg"] = "#5b8def"
        elif val == "=":
            e.widget["bg"] = "#43d39e"
        else:
            e.widget["bg"] = "#232b3b"
    else:
        if val == "Clear":
            e.widget["bg"] = "#ff6b6b"
        elif val in ["/", "*", "-", "+"]:
            e.widget["bg"] = "#4e8cff"
        elif val == "=":
            e.widget["bg"] = "#2ecc71"
        else:
            e.widget["bg"] = "#f8fafc"

for row_index, row in enumerate(buttons):
    for col_index, label in enumerate(row):
        color = btn_colors.get(label, {"bg": "#f8fafc", "fg": "#222"})
        btn = tk.Button(
            button_frame,
            text=label,
            font=BTN_FONT,
            bg=color["bg"],
            fg=color["fg"],
            activebackground="#bcdffb",
            activeforeground=color["fg"],
            bd=0,
            relief="flat",
            highlightthickness=0,
            command=lambda val=label: on_button_click(val)
        )
        btn.grid(row=row_index, column=col_index, sticky="nsew", padx=5, pady=5, ipadx=0, ipady=10)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)




history = tk.Listbox(root, height=5, font=("Segoe UI", 12), bg="#f8fafc", fg="#222", borderwidth=0, highlightthickness=1, highlightbackground="#b0b0b0")
history.pack(fill="both", padx=12, pady=(0, 12))

is_dark = False

def toggle_theme():
    global is_dark
    if not is_dark:
        # Modern dark theme colors
        root.configure(bg="#1a2233")
        display.configure(bg="#232b3b", fg="#f8fafc", insertbackground="#f8fafc", highlightbackground="#3a4660")
        button_frame.configure(bg="#1a2233")
        history.configure(bg="#232b3b", fg="#f8fafc", highlightbackground="#3a4660")
        for child in button_frame.winfo_children():
            val = child["text"]
            if val == "C":
                child.configure(bg="#e57373", fg="#fff", activebackground="#c62828", activeforeground="#fff")
            elif val in ["/", "*", "-", "+"]:
                child.configure(bg="#5b8def", fg="#fff", activebackground="#274690", activeforeground="#fff")
            elif val == "=":
                child.configure(bg="#43d39e", fg="#fff", activebackground="#1b5e20", activeforeground="#fff")
            else:
                child.configure(bg="#232b3b", fg="#f8fafc", activebackground="#2c3654", activeforeground="#f8fafc")
        is_dark = True
    else:
        root.configure(bg="#e6ecf0")
        display.configure(bg="#f8fafc", fg="#222", insertbackground="#222", highlightbackground="#b0b0b0")
        button_frame.configure(bg="#e6ecf0")
        history.configure(bg="#f8fafc", fg="#222", highlightbackground="#b0b0b0")
        for child in button_frame.winfo_children():
            val = child["text"]
            if val == "C":
                child.configure(bg="#ff6b6b", fg="#fff", activebackground="#bcdffb", activeforeground="#fff")
            elif val in ["/", "*", "-", "+"]:
                child.configure(bg="#4e8cff", fg="#fff", activebackground="#bcdffb", activeforeground="#fff")
            elif val == "=":
                child.configure(bg="#2ecc71", fg="#fff", activebackground="#bcdffb", activeforeground="#fff")
            else:
                child.configure(bg="#f8fafc", fg="#222", activebackground="#d1e3fa", activeforeground="#222")
        is_dark = False

theme_btn = tk.Button(root, text="Toggle Theme", command=toggle_theme, font=("Arial", 12))
theme_btn.pack(pady=(0, 10))


root.mainloop()