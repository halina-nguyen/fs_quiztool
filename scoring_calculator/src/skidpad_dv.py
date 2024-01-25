# Driverless Skidpad Scoring
# Source: FSG Rules 2024, D 4.5

import tkinter as tk
from tkinter import ttk
from src.common.p_max import p_max_skidpad_dv as p_max

class SkidpadDVTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        self.setup_ui()

    # at least one manual mode run without OC, USS, DNF or DQ and time <=25 without penalties
    def calculate_skidpad_dv(self):
        n_all = int(self.entry_n_all.get())
        r_dv = int(self.entry_r_dv.get())

        score = p_max * ((n_all + 1 - r_dv) / n_all)

        self.score_skidpad_dv.config(text=f"Skidpad DV score: {score:.2f}")

    def setup_ui(self):
        note = tk.Label(self.tab, text="Teams that finish at least one run without OC, USS, DNF or DQ and have a time <=25 without penalties, else 0.")
        note.grid(row=0, column=0, padx=10, pady=10)

        label_n_all = tk.Label(self.tab, text="Number of ALL teams who finished at least one run without DNF or DQ:")
        label_n_all.grid(row=1, column=0, padx=10, pady=10)

        self.entry_n_all = tk.Entry(self.tab)
        self.entry_n_all.grid(row=1, column=1, padx=10, pady=10)

        label_r_dv = tk.Label(self.tab, text="Team's position (incl. penalties):")
        label_r_dv.grid(row=2, column=0, padx=10, pady=10)

        self.entry_r_dv = tk.Entry(self.tab)
        self.entry_r_dv.grid(row=2, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.tab, text="Calculate Skidpad DV Score", command=self.calculate_skidpad_dv)
        calculate_button.grid(row=3, column=0, columnspan=10, pady=10)

        self.score_skidpad_dv = tk.Label(self.tab, text="")
        self.score_skidpad_dv.grid(row=4, column=0, columnspan=10, pady=10)