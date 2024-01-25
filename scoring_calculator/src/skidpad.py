# Manual Skidpad Scoring
# Source: FSG Rules 2024, D 4.4

import tkinter as tk
from tkinter import ttk
from src.common.penalties import skidpad_doo_penalty as doo
from src.common.p_max import p_max_skidpad as p_max

class SkidpadTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        self.setup_ui()

    # at least one manual mode run without OC, USS, DNF or DQ
    def calculate_skidpad(self):
        score = 0

        t_team = float(self.entry_t_team.get())
        t_team_cones = float(self.entry_t_team_cones.get())
        t_max = float(self.entry_t_max.get())
        t_max_cones = float(self.entry_t_max_cones.get())

        t_team += (t_team_cones * doo)
        t_max *= 1.25 + (t_max_cones * doo)

        if t_team < t_max:
            score = 0.95 * p_max * (((t_max/t_team)**2 - 1) / 0.5625)
        score += 0.05 * p_max

        self.score_skidpad.config(text=f"Skidpad score: {score:.2f}")

    def setup_ui(self):
        note = tk.Label(self.tab, text="Teams that finish at least one run without OC, USS, DNF or DQ.")
        note.grid(row=0, column=0, padx=10, pady=10)

        label_t_team = tk.Label(self.tab, text="Team's best time (incl. penalties):")
        label_t_team.grid(row=1, column=0, padx=10, pady=10)

        self.entry_t_team = tk.Entry(self.tab)
        self.entry_t_team.insert(0, "0.0")
        self.entry_t_team.grid(row=1, column=1, padx=10, pady=10)

        label_t_team_cones = tk.Label(self.tab, text="Number of cones hit by team:")
        label_t_team_cones.grid(row=2, column=0, padx=10, pady=10)

        self.entry_t_team_cones = tk.Entry(self.tab)
        self.entry_t_team_cones.insert(0, "0.0")
        self.entry_t_team_cones.grid(row=2, column=1, padx=10, pady=10)

        label_t_max = tk.Label(self.tab, text="Time of fastest vehicle (incl. penalties):")
        label_t_max.grid(row=3, column=0, padx=10, pady=10)

        self.entry_t_max = tk.Entry(self.tab)
        self.entry_t_max.insert(0, "0.0")
        self.entry_t_max.grid(row=3, column=1, padx=10, pady=10)

        label_t_max_cones = tk.Label(self.tab, text="Number of cones hit by fastest vehicle:")
        label_t_max_cones.grid(row=4, column=0, padx=10, pady=10)

        self.entry_t_max_cones = tk.Entry(self.tab)
        self.entry_t_max_cones.insert(0, "0.0")
        self.entry_t_max_cones.grid(row=4, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.tab, text="Calculate Skidpad Score", command=self.calculate_skidpad)
        calculate_button.grid(row=5, column=0, columnspan=10, pady=10)

        self.score_skidpad = tk.Label(self.tab, text="")
        self.score_skidpad.grid(row=6, column=0, columnspan=10, pady=10)