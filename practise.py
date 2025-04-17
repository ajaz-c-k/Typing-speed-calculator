import tkinter as tk
import time
import random
import string

def clean(word):
    return word.strip(string.punctuation).lower()

root = tk.Tk()
root.title("Typing Speed Calculator by Ajaz")
root.geometry("700x500")

texts = [
    "Typing fast is arguabily one of the most technical skills.",
    "While making this i was having lot of fun",
    "I wanted to work in Google.",
    "If you actually try your best you cant loose.",
    "rasha is cute and beautiful"
]

target_text = random.choice(texts)

text_label = tk.Label(root, text=target_text, font=("Helvetica", 14), wraplength=500)
text_label.pack(pady=20)

entry = tk.Entry(root, width=50, font=("Helvetica", 14), state="disabled")
entry.pack(pady=10)

timer_label = tk.Label(root, text="Time: 0.00 sec", font=("Helvetica", 14), fg="purple")
timer_label.pack(pady=10)

start_time = 0
running = False

def update_timer():
    if running:
        elapsed = time.time() - start_time
        timer_label.config(text=f"Time : {elapsed:.2f} sec")
        root.after(100, update_timer)

def start_typing():
    global start_time, running
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.focus()
    start_time = time.time()
    running = True
    update_timer()

def calculate_speed(event):
    global running
    running = False
    entry.config(state="disabled")

    end_time = time.time()
    total_time = end_time - start_time

    typed_text = entry.get()
    target_words = target_text.split()
    typed_words = typed_text.split()

    correct_words = 0
    for i in range(min(len(typed_words), len(target_words))):
        if clean(typed_words[i]) == clean(target_words[i]):
            correct_words += 1

    accuracy = (correct_words / len(target_words)) * 100 if target_words else 0

    highlighted_result = ""
    for i in range(min(len(typed_words), len(target_words))):
        if clean(typed_words[i]) == clean(target_words[i]):
            highlighted_result += f" ✅ {typed_words[i]}"
        else:
            highlighted_result += f" ❌ {typed_words[i]}"

    if len(typed_words) > len(target_words):
        for word in typed_words[len(target_words):]:
            highlighted_result += f" ❌ {word}"

    if len(typed_words) < len(target_words):
        for word in target_words[len(typed_words):]:
            highlighted_result += f" ❌ [missing: {word}]"

    highlight_label.config(text=highlighted_result)

    word_count = len(typed_words)
    wpm = (word_count / total_time) * 60 if total_time > 0 else 0

    result = (
        f"Your typing speed is {wpm:.2f} words per minute.\n"
        f"Accuracy: {accuracy:.2f}% ({correct_words} correct out of {len(target_words)})"
    )
    result_label.config(text=result)

def restart():
    global target_text, running
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.config(state="disabled")
    result_label.config(text="")
    highlight_label.config(text="")
    timer_label.config(text="Time: 0.00 sec")
    running = False
    target_text = random.choice(texts)
    text_label.config(text=target_text)

start_button = tk.Button(root, text="Start the test", command=start_typing)
start_button.pack(pady=10)

restart_button = tk.Button(root, text="Restart", command=restart)
restart_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="green")
result_label.pack(pady=10)

highlight_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left", wraplength=600)
highlight_label.pack(pady=10)

entry.bind("<Return>", calculate_speed)

root.mainloop()
