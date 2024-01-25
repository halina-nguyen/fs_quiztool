# Autocross Scoring
# Source: FSG Rules 2024, D 6.3

import tkinter as tk
from tkinter import ttk
from src.common.penalties import autocross_doo_penalty as doo, autocross_oc_penalty as oc
from src.common.p_max import p_max_autocross as p_max

class AutocrossTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        self.setup_ui()

    # at least one manual mode run without USS, DNF or DQ
    def calculate_autocross(self):
        score = 0

        t_team = float(self.entry_t_team.get())
        t_team_cones = float(self.entry_t_team_cones.get())
        t_team_off = float(self.entry_t_team_off.get())
        t_max = float(self.entry_t_max.get())
        t_max_cones = float(self.entry_t_max_cones.get())
        t_max_off = float(self.entry_t_team_off.get())

        t_team += (t_team_cones * doo) + (t_team_off * oc)
        t_max *= 1.25 + (t_max_cones * doo) + (t_max_off * oc)

        if t_team < t_max:
            score = 0.95 * p_max * (((t_max/t_team) - 1) / 0.25)
        score += 0.05 * p_max

        self.score_autocross.config(text=f"Autocross score: {score:.2f}")

    def setup_ui(self):
        note = tk.Label(self.tab, text="Teams that finish at least one run without DNF or DQ, else 0.")
        note.grid(row=0, column=0, padx=10, pady=10)

        label_entry_t_team = tk.Label(self.tab, text="Team's best time (incl. penalties):")
        label_entry_t_team.grid(row=1, column=0, padx=10, pady=10)

        self.entry_t_team = tk.Entry(self.tab)
        self.entry_t_team.insert(0, "0.0")
        self.entry_t_team.grid(row=1, column=1, padx=10, pady=10)

        label_t_team_cones = tk.Label(self.tab, text="Number of cones hit by team:")
        label_t_team_cones.grid(row=2, column=0, padx=10, pady=10)

        self.entry_t_team_cones = tk.Entry(self.tab)
        self.entry_t_team_cones.insert(0, "0.0")
        self.entry_t_team_cones.grid(row=2, column=1, padx=10, pady=10)

        label_t_team_off = tk.Label(self.tab, text="Number of times being off-course by team:")
        label_t_team_off.grid(row=3, column=0, padx=10, pady=10)

        self.entry_t_team_off = tk.Entry(self.tab)
        self.entry_t_team_off.insert(0, "0.0")
        self.entry_t_team_off.grid(row=3, column=1, padx=10, pady=10)

        label_t_max = tk.Label(self.tab, text="Time of fastest vehicle (inc. penalties):")
        label_t_max.grid(row=4, column=0, padx=10, pady=10)

        self.entry_t_max = tk.Entry(self.tab)
        self.entry_t_max.insert(0, "0.0")
        self.entry_t_max.grid(row=4, column=1, padx=10, pady=10)

        label_t_max_cones = tk.Label(self.tab, text="Number of cones hit by fastest vehicle:")
        label_t_max_cones.grid(row=5, column=0, padx=10, pady=10)

        self.entry_t_max_cones = tk.Entry(self.tab)
        self.entry_t_max_cones.insert(0, "0.0")
        self.entry_t_max_cones.grid(row=5, column=1, padx=10, pady=10)

        label_t_max_off = tk.Label(self.tab, text="Number of times being off-course by fastest vehicle:")
        label_t_max_off.grid(row=6, column=0, padx=10, pady=10)

        self.entry_t_max_off = tk.Entry(self.tab)
        self.entry_t_max_off.insert(0, "0.0")
        self.entry_t_max_off.grid(row=6, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.tab, text="Calculate Autocross Score", command=self.calculate_autocross)
        calculate_button.grid(row=7, column=0, columnspan=10, pady=10)

        self.score_autocross = tk.Label(self.tab, text="")
        self.score_autocross.grid(row=8, column=0, columnspan=10, pady=10)