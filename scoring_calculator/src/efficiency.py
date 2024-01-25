# Efficiency Scoring
# Source: FSG Rules 2024, D 7.9

import tkinter as tk
from tkinter import ttk
from src.common.p_max import p_max_efficiency as p_max

class EfficiencyTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        self.setup_ui()

    # at least one manual mode run without OC, USS, DNF or DQ
    def calculate_efficiency(self):
        t_team = float(self.entry_t_team.get())
        e_team = float(self.entry_e_team.get())
        t_min = float(self.entry_t_min.get())
        e_min = float(self.entry_e_min.get())
        ef_team = float(self.entry_ef_team.get())
        ef_min = float(self.entry_ef_min.get())

        if not ef_team and t_team and e_team:
            ef_team = t_team**2 * e_team

        if not ef_min and t_min and e_min:
            ef_min = t_min**2 * e_min

        ef_max = 1.5 * ef_min

        score = 0.95 * p_max * ((ef_max - ef_team) / (ef_max - ef_min))

        self.score_efficiency.config(text=f"Efficiency score: {score:.2f}")

    def setup_ui(self):
        note = tk.Label(self.tab, text="Scores to teams that finishes least one run without OC, USS, DNF or DQ.")
        note.grid(row=0, column=0, padx=10, pady=10)

        label_t_team = tk.Label(self.tab, text="Team's time without penalties:")
        label_t_team.grid(row=1, column=0, padx=10, pady=10)

        self.entry_t_team = tk.Entry(self.tab)
        self.entry_t_team.insert(0, "0.0")
        self.entry_t_team.grid(row=1, column=1, padx=10, pady=10)

        label_e_team = tk.Label(self.tab, text="[CV] used fuel mass / [EV] used energy by team:")
        label_e_team.grid(row=2, column=0, padx=10, pady=10)

        self.entry_e_team = tk.Entry(self.tab)
        self.entry_e_team.insert(0, "0.0")
        self.entry_e_team.grid(row=2, column=1, padx=10, pady=10)

        label_t_min = tk.Label(self.tab, text="team lowest efficiency factor time without penalties:")
        label_t_min.grid(row=3, column=0, padx=10, pady=10)

        self.entry_t_min = tk.Entry(self.tab)
        self.entry_t_min.insert(0, "0.0")
        self.entry_t_min.grid(row=3, column=1, padx=10, pady=10)

        label_e_min = tk.Label(self.tab, text="[CV] used fuel mass / [EV] used energy by team with lowest efficiency factor:")
        label_e_min.grid(row=4, column=0, padx=10, pady=10)

        self.entry_e_min = tk.Entry(self.tab)
        self.entry_e_min.insert(0, "0.0")
        self.entry_e_min.grid(row=4, column=1, padx=10, pady=10)

        label_ef_team = tk.Label(self.tab, text="Team's efficiency factor:")
        label_ef_team.grid(row=5, column=0, padx=10, pady=10)

        self.entry_ef_team = tk.Entry(self.tab)
        self.entry_ef_team.insert(0, "0.0")
        self.entry_ef_team.grid(row=5, column=1, padx=10, pady=10)

        label_ef_min = tk.Label(self.tab, text="Lowest efficiency factor of all teams:")
        label_ef_min.grid(row=6, column=0, padx=10, pady=10)

        self.entry_ef_min = tk.Entry(self.tab)
        self.entry_ef_min.insert(0, "0.0")
        self.entry_ef_min.grid(row=6, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.tab, text="Calculate Efficiency Score", command=self.calculate_efficiency)
        calculate_button.grid(row=7, column=0, columnspan=10, pady=10)

        self.score_efficiency = tk.Label(self.tab, text="")
        self.score_efficiency.grid(row=8, column=0, columnspan=10, pady=10)