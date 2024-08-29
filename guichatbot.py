import aiml
import os
import tkinter as tk
from tkinter import scrolledtext, Entry, Button

class LabChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Lab Chatbot")

        self.create_widgets()

        self.kernel = aiml.Kernel()
        self.load_aiml_files()

    def create_widgets(self):
        self.chat_output = scrolledtext.ScrolledText(self.master, width=60, height=20, wrap=tk.WORD)
        self.chat_output.pack(padx=10, pady=10)

        self.user_input = Entry(self.master, width=50)
        self.user_input.pack(padx=10, pady=10)

        self.send_button = Button(self.master, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

    def load_aiml_files(self):
        aiml_dir = 'C:/Users/pk/Desktop/5th sem BE/projects/AIML/lab_chatbot'  # Replace with the path to your AIML files
        for file in os.listdir(aiml_dir):
            if file.endswith(".aiml"):
                aiml_file = os.path.join(aiml_dir, file)
                self.kernel.learn(aiml_file)

    def send_message(self):
        user_input = self.user_input.get()
        self.user_input.delete(0, tk.END)

        if user_input.lower() == 'exit':
            self.master.destroy()
        else:
            bot_response = self.kernel.respond(user_input)
            self.display_message("You: " + user_input)
            self.display_message("Labwiz: " + bot_response)

    def display_message(self, message):
        self.chat_output.insert(tk.END, message + "\n")
        self.chat_output.yview(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    chatbot_gui = LabChatbotGUI(root)
    root.mainloop()
