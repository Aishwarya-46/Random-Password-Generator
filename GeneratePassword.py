import tkinter as tk
import random
import string
import pyperclip

class SecurePasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Secure Password Generator")

        self.length_label = tk.Label(self.root, text="Desired password length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack()

        self.use_uppercase_var = tk.IntVar()
        self.use_uppercase_checkbox = tk.Checkbutton(self.root, text="Include uppercase letters", variable=self.use_uppercase_var)
        self.use_uppercase_checkbox.pack()

        self.use_numbers_var = tk.IntVar()
        self.use_numbers_checkbox = tk.Checkbutton(self.root, text="Include numbers", variable=self.use_numbers_var)
        self.use_numbers_checkbox.pack()

        self.use_symbols_var = tk.IntVar()
        self.use_symbols_checkbox = tk.Checkbutton(self.root, text="Include symbols", variable=self.use_symbols_var)
        self.use_symbols_checkbox.pack()

        self.generate_button = tk.Button(self.root, text="Generate password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(self.root, text="")
        self.password_label.pack()

        self.copy_to_clipboard_button = tk.Button(self.root, text="Copy to clipboard", command=self.copy_to_clipboard)
        self.copy_to_clipboard_button.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        use_uppercase = self.use_uppercase_var.get() != 0
        use_numbers = self.use_numbers_var.get() != 0
        use_symbols = self.use_symbols_var.get() != 0

        password = ''.join(random.choice(string.ascii_lowercase + (string.ascii_uppercase if use_uppercase else '') + (string.digits if use_numbers else '') + (string.punctuation if use_symbols else '')) for _ in range(length))
        self.password_label.config(text=f"Generated password: {password}")

    def copy_to_clipboard(self):
        import pyperclip
        password = self.password_label.cget("text").split(":")[1].strip()
        pyperclip.copy(password)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = SecurePasswordGenerator()
    game.run()