import tkinter as tk
import time
import random

root= tk.Tk()
root.title("Typing Speed Calculator by Ajaz")
root.geometry("700x500")

texts=["Typing fast is arguabily one of the most technical skill.","While making this i had lot of fun",
       "I wanted to work in Google.","If you actually try your best you cant loose."]

target_text=random.choice(texts)


text_label = tk.Label(root, text=target_text, font=("Helvetica", 14), wraplength=500)
text_label.pack(pady=20)

entry = tk.Entry(root, width=50, font=("Helvetica", 14))
entry.pack(pady=10)

timer_label=tk.Label(root,text="Time: 0.00 sec",font=("Helvetica", 14),fg="purple")
timer_label.pack(pady=10)

start_time=0
running=False

def update_timer():
    if running:
        ellapsed=time.time()-start_time
        timer_label.config(text=f"Time : {ellapsed:.2f} sec")
        root.after(100,update_timer)



def start_typing():
    global start_time,running
    entry.delete(0,tk.END)
    entry.focus()
    start_time=time.time()
    running=True
    update_timer()

def calculate_speed(event):
    global running
    running =False 
    end_time=time.time()
    total_time=end_time-start_time

    typed_text=entry.get()
    target_words=target_text.split()
    typed_words=typed_text.split()

    correct_words=0
    for i in range(min(len(typed_words),len(target_words))):
        if target_words[i]==typed_words[i]:
            correct_words+=1
    if target_words:
        accuracy=(correct_words/len(target_words) )*100
    else:
        accuracy=0

                 

    word_count=len(typed_words)
    wpm=(word_count/total_time)*60 if total_time>0 else 0     
    result = (
        f"Your typing speed is {wpm:.2f} words per minute.\n"
        f"Accuracy: {accuracy:.2f}% ({correct_words} correct out of {len(target_words)})"
    )
    result_label.config(text=result) 

def restart():
    global target_text
    entry.delete(0,tk.END)
    result_label.config(text="")
    target_text=random.choice(texts)
    text_label.config(text=target_text)    



start_button=tk.Button(root,text="Start the test",command=start_typing)
start_button.pack(pady=10)

restart_button=tk.Button(root,text="Restart",command=restart)
restart_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="green")
result_label.pack(pady=10)


entry.bind("<Return>",calculate_speed)

root.mainloop()

