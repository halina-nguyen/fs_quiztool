# Driverless Autocross Scoring
# Source: FSG Rules 2024, D 6.5

import tkinter as tk
from tkinter import ttk
from src.common.penalties import autocross_doo_penalty as doo, autocross_oc_penalty as oc
from src.common.p_max import p_max_autocross as p_max

class AutocrossDCTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        self.setup_ui()

    # at least one run without USS, DNF or DQ
    def calculate_autocross_dc(self):
        score = 0

        t_team1 = float(self.entry_t_team1.get())
        t_team1_cones = float(self.entry_t_team1_cones.get())
        t_team1_off = float(self.entry_t_team1_off.get())
        t_team2 = float(self.entry_t_team2.get())
        t_team2_cones = float(self.entry_t_team2_cones.get())
        t_team2_off = float(self.entry_t_team2_off.get())
        t_max = float(self.entry_t_max.get())
        t_min = float(self.entry_t_min.get())
        t_min_cones = float(self.entry_t_min_cones.get())
        t_min_off = float(self.entry_t_min_off.get())

        t_team1 += (t_team1_cones * doo) + (t_team1_off * oc)
        t_team2 += (t_team2_cones * doo) + (t_team2_off * oc)
        t_team_total = min(t_team1, (t_team1 + t_team2)/2)
        t_min += (t_min_cones * doo) + (t_min_off * oc)
        
        if t_team_total < t_max:
            score = 0.9 * p_max * ((t_max - t_team_total) / (t_max - t_min))
        score += 0.1 * p_max

        self.score_autocross_dc.config(text=f"Autocross DC score: {score:.2f}")

    def setup_ui(self):
        note = tk.Label(self.tab, text="Teams that finish at least one run without USS, DNF or DQ, else 0.")
        note.grid(row=0, column=0, padx=10, pady=10)

        label_entry_t_team1 = tk.Label(self.tab, text="Team's time in run 1 (incl. penalties):")
        label_entry_t_team1.grid(row=1, column=0, padx=10, pady=10)

        self.entry_t_team1 = tk.Entry(self.tab)
        self.entry_t_team1.insert(0, "0.0")
        self.entry_t_team1.grid(row=1, column=1, padx=10, pady=10)

        label_t_team1_cones = tk.Label(self.tab, text="Number of cones hit by team in run 1:")
        label_t_team1_cones.grid(row=2, column=0, padx=10, pady=10)

        self.entry_t_team1_cones = tk.Entry(self.tab)
        self.entry_t_team1_cones.insert(0, "0.0")
        self.entry_t_team1_cones.grid(row=2, column=1, padx=10, pady=10)

        label_t_team1_off = tk.Label(self.tab, text="Number of times being off-course by team in run 1:")
        label_t_team1_off.grid(row=3, column=0, padx=10, pady=10)

        self.entry_t_team1_off = tk.Entry(self.tab)
        self.entry_t_team1_off.insert(0, "0.0")
        self.entry_t_team1_off.grid(row=3, column=1, padx=10, pady=10)

        label_entry_t_team2 = tk.Label(self.tab, text="Team's time in run 2 (incl. penalties):")
        label_entry_t_team2.grid(row=4, column=0, padx=10, pady=10)

        self.entry_t_team2 = tk.Entry(self.tab)
        self.entry_t_team2.insert(0, "0.0")
        self.entry_t_team2.grid(row=4, column=1, padx=10, pady=10)

        label_t_team2_cones = tk.Label(self.tab, text="Number of cones hit by team in run 2:")
        label_t_team2_cones.grid(row=5, column=0, padx=10, pady=10)

        self.entry_t_team2_cones = tk.Entry(self.tab)
        self.entry_t_team2_cones.insert(0, "0.0")
        self.entry_t_team2_cones.grid(row=5, column=1, padx=10, pady=10)

        label_t_team2_off = tk.Label(self.tab, text="Number of times being off-course by team in run 2:")
        label_t_team2_off.grid(row=6, column=0, padx=10, pady=10)

        self.entry_t_team2_off = tk.Entry(self.tab)
        self.entry_t_team2_off.insert(0, "0.0")
        self.entry_t_team2_off.grid(row=6, column=1, padx=10, pady=10)

        label_t_max = tk.Label(self.tab, text="Time for driving the lap with 6 m/s:")
        label_t_max.grid(row=7, column=0, padx=10, pady=10)

        self.entry_t_max = tk.Entry(self.tab)
        self.entry_t_max.insert(0, "0.0")
        self.entry_t_max.grid(row=7, column=1, padx=10, pady=10)

        label_t_min = tk.Label(self.tab, text="Time of fastest vehicle (incl. penalties):")
        label_t_min.grid(row=8, column=0, padx=10, pady=10)

        self.entry_t_min = tk.Entry(self.tab)
        self.entry_t_min.insert(0, "0.0")
        self.entry_t_min.grid(row=8, column=1, padx=10, pady=10)

        label_t_min_cones = tk.Label(self.tab, text="Number of cones hit by fastest vehicle:")
        label_t_min_cones.grid(row=9, column=0, padx=10, pady=10)

        self.entry_t_min_cones = tk.Entry(self.tab)
        self.entry_t_min_cones.insert(0, "0.0")
        self.entry_t_min_cones.grid(row=9, column=1, padx=10, pady=10)

        label_t_min_off = tk.Label(self.tab, text="Number of times being off-course by fastest vehicle:")
        label_t_min_off.grid(row=10, column=0, padx=10, pady=10)

        self.entry_t_min_off = tk.Entry(self.tab)
        self.entry_t_min_off.insert(0, "0.0")
        self.entry_t_min_off.grid(row=10, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.tab, text="Calculate Autocross DC Score", command=self.calculate_autocross_dc)
        calculate_button.grid(row=11, column=0, columnspan=10, pady=10)

        self.score_autocross_dc = tk.Label(self.tab, text="")
        self.score_autocross_dc.grid(row=12, column=0, columnspan=10, pady=10)