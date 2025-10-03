import tkinter as tk
from tkinter import ttk
import random

CHAMPIONS = {
    "Top": ["Aatrox", "Akali", "Aurora", "Ambessa", "Camille", "Cho'Gath", "Darius", "Dr. Mundo", "Fiora", "Gangplank",
            "Garen", "Gnar", "Gragas", "Heimerdinger", "Illaoi", "Irelia", "Jax", "Jayce", "Kayle", "Kennen", "K'Sante",
            "Maokai", "Mordekaiser", "Nasus", "Olaf", "Ornn", "Poppy", "Quinn", "Renekton", "Riven", "Rumble", "Ryze",
            "Sett", "Shen", "Singed", "Sion", "Skarner", "Sylas", "Tahm Kench", "Teemo", "Trundle", "Tryndamere",
            "Urgot", "Vladimir", "Volibear", "Varus", "Warwick", "Wukong", "Yone", "Yorick"],
    "Jungle": ["Amumu", "Bel'Veth", "Briar", "Diana", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Graves", "Hecarim",
               "Ivern", "Jarvan IV", "Jax", "Karthus", "Kayn", "Kha'Zix", "Kindred", "Lee Sin", "Lillia", "Master Yi",
               "Nidalee", "Nocturne", "Nunu & Willump", "Olaf", "Rammus", "Rek'Sai", "Rengar", "Sejuani", "Shaco",
               "Skarner", "Taliyah", "Talon", "Udyr", "Vi", "Viego", "Warwick", "Wukong", "Xin Zhao", "Zac", "Zed"],
    "Mid": ["Ahri", "Akali", "Akshan", "Anivia", "Annie", "Aurelion Sol", "Aurora", "Azir", "Cassiopeia", "Corki",
            "Ekko", "Fizz", "Galio", "Kassadin", "Katarina", "LeBlanc", "Lissandra", "Lux", "Malphite", "Malzahar",
            "Mel", "Neeko", "Orianna", "Pantheon", "Qiyana", "Ryze", "Seraphine", "Sylas", "Syndra", "Smolder", "Talon",
            "Twisted Fate", "Veigar", "Vel'Koz", "Vex", "Viktor", "Vladimir", "Xerath", "Yasuo", "Yone", "Zed", "Ziggs",
            "Zoe"],
    "Bot": ["Aphelios", "Ashe", "Caitlyn", "Corki", "Draven", "Ezreal", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Kog'Maw",
            "Lucian", "Miss Fortune", "Nilah", "Samira", "Sivir", "Smolder", "Tristana", "Twitch", "Varus", "Vayne",
            "Xayah", "Yunara", "Ziggs"],
    "Support": ["Alistar", "Bard", "Blitzcrank", "Brand", "Braum", "Janna", "Karma", "Leona", "Lulu", "Lux", "Maokai",
                "Mel", "Milio", "Morgana", "Nami", "Nautilus", "Pantheon", "Pyke", "Rakan", "Renata Glasc", "Senna",
                "Seraphine", "Sona", "Soraka", "Swain", "Taric", "Thresh", "Yuumi", "Zilean", "Zyra"]
}

LINES = list(CHAMPIONS.keys())


class LoLRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Losowanie Postaci i Linii LoL")
        self.root.geometry("500x500")

        self.create_widgets()

    def create_widgets(self):
        self.line_frame = ttk.LabelFrame(self.root, text="Losowanie Linii")
        self.line_frame.pack(padx=10, pady=10, fill="x")

        self.roll_line_button = ttk.Button(self.line_frame, text="Wylosuj Glowna Linie", command=self.roll_main_line)
        self.roll_line_button.pack(pady=5)

        self.main_line_label = ttk.Label(self.line_frame, text="Glowna Linia: Brak", font=("Helvetica", 12, "bold"))
        self.main_line_label.pack(pady=5)

        self.roll_secondary_line_button = ttk.Button(self.line_frame, text="Wylosuj Druga Linie",
                                                     command=self.roll_secondary_line, state="disabled")
        self.roll_secondary_line_button.pack(pady=5)

        self.secondary_line_label = ttk.Label(self.line_frame, text="Druga Linia: Brak", font=("Helvetica", 12, "bold"))
        self.secondary_line_label.pack(pady=5)

        # Sekcja losowania postaci
        self.champion_frame = ttk.LabelFrame(self.root, text="Losowanie Postaci")
        self.champion_frame.pack(padx=10, pady=10, fill="x")

        self.line_selection_label = ttk.Label(self.champion_frame, text="Wybierz linie do losowania postaci:")
        self.line_selection_label.pack(pady=5)

        self.line_combobox = ttk.Combobox(self.champion_frame, values=LINES, state="readonly")
        self.line_combobox.set("Wybierz...")
        self.line_combobox.pack(pady=5)
        self.line_combobox.bind("<<ComboboxSelected>>", self.on_line_selected)

        self.roll_champion_button = ttk.Button(self.champion_frame, text="Wylosuj Postac", command=self.roll_champion,
                                               state="disabled")
        self.roll_champion_button.pack(pady=5)

        self.champion_result_label = ttk.Label(self.champion_frame, text="Wylosowana Postac: Brak",
                                               font=("Helvetica", 12, "bold"))
        self.champion_result_label.pack(pady=5)

        self.current_main_line = None
        self.current_secondary_line = None

    def roll_main_line(self):
        self.current_main_line = random.choice(LINES)
        self.main_line_label.config(text=f"Glowna Linia: {self.current_main_line}")

        self.roll_secondary_line_button.config(state="enabled")
        self.secondary_line_label.config(text="Druga Linia: Brak")
        self.current_secondary_line = None

        self.line_combobox.set(self.current_main_line)
        self.on_line_selected()

    def roll_secondary_line(self):
        other_lines = [line for line in LINES if line != self.current_main_line]
        self.current_secondary_line = random.choice(other_lines)
        self.secondary_line_label.config(text=f"Druga Linia: {self.current_secondary_line}")

    def on_line_selected(self, event=None):
        selected_line = self.line_combobox.get()
        if selected_line in CHAMPIONS:
            self.roll_champion_button.config(state="enabled")
        else:
            self.roll_champion_button.config(state="disabled")

    def roll_champion(self):
        selected_line = self.line_combobox.get()
        if selected_line in CHAMPIONS:
            champion = random.choice(CHAMPIONS[selected_line])
            self.champion_result_label.config(text=f"Wylosowana Postac: {champion}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoLRollerApp(root)
    root.mainloop()

