# Cost and Manufacturing Scoring
# Source: FSG Rules 2024, S 2.10

import tkinter as tk
from tkinter import ttk
from src.common.p_max import p_max_bpp as p_max

class CostTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        self.setup_ui()

    def calculate_cost(self):
        # non-finalist
        p_team = int(self.entry_p_team.get())
    
        score = 95 * (p_team / p_max)
        self.score_cost.config(text=f"Cost and Manufacturing score: {score:.2f}")

        # finalist
        #  96 - 100 points

        # if no cost finals, Cost and Manufacturing score = p_team

    def setup_ui(self):
        note = tk.Label(self.tab, text="Just for non-finalist.\nFinalists get 71 to 75 points.\nIf no cost finals, Cost and Manufacturing score = team's score")
        note.grid(row=0, column=0, padx=10, pady=10)

        label_p_team = tk.Label(self.tab, text="Team's score:")
        label_p_team.grid(row=1, column=0, padx=10, pady=10)

        self.entry_p_team = tk.Entry(self.tab)
        self.entry_p_team.insert(0, "0.0")
        self.entry_p_team.grid(row=1, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.tab, text="Calculate Cost and Manufacturing Score", command=self.calculate_cost)
        calculate_button.grid(row=2, column=0, columnspan=10, pady=10)

        self.score_cost = tk.Label(self.tab, text="")
        self.score_cost.grid(row=3, column=0, columnspan=10, pady=10)