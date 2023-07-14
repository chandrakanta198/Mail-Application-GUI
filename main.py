import tkinter as tk
from tkinter import messagebox, scrolledtext

# handle click event
def send_mail():
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    messagebox.showinfo("Success", "Mail sent successfully.")

# main window
window = tk.Tk()
window.title("Mail Application")

#color code
PRIMARY_COLOR = "#ff4500"  
SECONDARY_COLOR = "#00aaff"  
TEXT_COLOR = "#ffffff"  

window.configure(bg=PRIMARY_COLOR)

recipient_label = tk.Label(window, text="Recipient:", bg=PRIMARY_COLOR, fg=TEXT_COLOR)
recipient_label.pack()
recipient_entry = tk.Entry(window, width=90)
recipient_entry.pack()

subject_label = tk.Label(window, text="Subject:", bg=PRIMARY_COLOR, fg=TEXT_COLOR)
subject_label.pack()
subject_entry = tk.Entry(window, width=90)
subject_entry.pack()

message_label = tk.Label(window, text="Message:", bg=PRIMARY_COLOR, fg=TEXT_COLOR)
message_label.pack()
message_text = scrolledtext.ScrolledText(window, height=20)
message_text.pack()

send_button = tk.Button(window, height=2, width=20, text="Send", bg=SECONDARY_COLOR, fg=TEXT_COLOR, command=send_mail)
send_button.pack()



#start point
window.mainloop()
