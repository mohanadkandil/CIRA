import tkinter
import customtkinter as tk
import os
from PIL import Image
from elevenlabs import generate, play

class TUMRobot(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TUMRobot")
        self.geometry("900x450")
        self.language = "Spanish"
        
        self.hello_icon = tk.CTkImage(Image.open(os.path.join("goodbye.png")), size = (100, 100))
        self.sleeping_icon = tk.CTkImage(Image.open(os.path.join("sleeping.png")), size = (100, 100))
        self.book_icon = tk.CTkImage(Image.open(os.path.join("book.png")), size = (100, 100))
        
        self.create_widgets()
   
    def create_widgets(self):
        self.navigation_frame = tk.CTkFrame(self, fg_color = "transparent")
        self.navigation_frame.pack(pady=80)

        self.language_menu = tk.CTkOptionMenu(self.navigation_frame, values = ["Spanish", "English"], command = self.change_language)
        self.language_menu.pack(side = tk.TOP, pady = 20)
        
        self.home_button = tk.CTkButton(self.navigation_frame, image = self.hello_icon, text = "", width = 250, height = 250, fg_color = "#27ae60", hover_color = "#2ecc71", command = self.greet)
        self.home_button.pack(side=tk.LEFT, padx=10)

        self.book_button = tk.CTkButton(self.navigation_frame, image = self.book_icon, text = "", width = 250, height = 250, fg_color = "#c0392b", hover_color = "#e74c3c", command = self.study)
        self.book_button.pack(side=tk.LEFT, padx=10)

        self.settings_button = tk.CTkButton(self.navigation_frame, image = self.sleeping_icon, text = "", width = 250, height = 250, fg_color = "#f39c12", hover_color = "#f1c40f", command = self.sleep)
        self.settings_button.pack(side=tk.LEFT, padx=10)

    def change_language(self):
        self.language = self.language_menu.get()

    def greet(self):
        text = ""
        if self.language_menu.get() == "Spanish":
            text = "¡Buenos días, Jamie! Hoy es un día completamente nuevo lleno de oportunidades."
        else:
            text = "Good morning, Jamie! Today is a brand new day filled with opportunities"
        audio = generate(
            text = text,
            voice = "Elli",
            model="eleven_multilingual_v2"
        )
        play(audio)
    
    def study(self):
        text = ""
        if self.language_menu.get() == "Spanish":
            text = "¡La hora de estudiar es una aventura para tu cerebro! Descubramos cosas nuevas y resolvamos algunos acertijos. Tú puedes con esto, y estoy muy orgulloso/a de lo mucho que te esfuerzas."
        else:
            text = "Study time is adventure time for your brain! Let's discover new things and solve some puzzles. You've got this, and I'm so proud of how hard you're trying"
        audio = generate(
            text = text,
            voice = "Elli",
            model="eleven_multilingual_v2"
        )
        play(audio)


    def sleep(self):
        text = ""
        if self.language_menu.get() == "Spanish":
            text = "Cierra los ojos, descansa, y sueña con nuevas aventuras; recuerda, siempre estoy aquí para ti. ¡Dulces sueños!"
        else:
            text = "Close your eyes, rest, and dream of new adventures; remember, I'm always here for you. Sweet dreams!"
        audio = generate(
            text = text,
            voice = "Elli",
            model="eleven_multilingual_v2"
        )
        play(audio)


if __name__ == "__main__":
    app = TUMRobot()
    app.mainloop()
