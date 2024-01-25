# Trackdrive Scoring
# Source: FSG Rules 2024, D 8.4

import tkinter as tk
from tkinter import ttk
from src.common.penalties import trackdrive_doo_penalty as doo, trackdrive_oc_penalty as oc, trackdrive_uss_penalty as uss
from src.common.p_max import p_max_trackdrive as p_max

class TrackdriveTab:
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)
        self.setup_ui()

    # If USS, then -50 points
    def calculate_trackdrive(self):
        score = 0

        t_team = float(self.entry_t_team.get())
        t_team_cones = float(self.entry_t_team_cones.get())
        t_team_off = float(self.entry_t_team_off.get())
        t_team_laps = float(self.entry_t_team_laps.get())
        t_max = float(self.entry_t_max.get())
        t_max_cones = float(self.entry_t_max_cones.get())
        t_max_off = float(self.entry_t_max_off.get())

        t_team += (t_team_cones * doo) + (t_team_off * oc)
        t_max *= 2 + (t_max_cones * doo) + (t_max_off * oc)

        if t_team < t_max:
            score = 0.75 * p_max * ((t_max/t_team) - 1)
        score += 0.05 * p_max * t_team_laps

        if self.uss.get():
            score += uss

        self.score_trachdrive.config(text=f"Trackdrive score: {score:.2f}")

    def setup_ui(self):
        note = tk.Label(self.tab, text="The vehicle uncorrected elapsed endurance time does not exceed 1.333 times the uncorrected elapsed time of the fastest vehicle.\nThe consumed fuel mass must not exceed 15 kg/100 km 98 RON or 21.75 kg/100km E85.")
        note.grid(row=0, column=0, padx=10, pady=10)

        self.uss = tk.BooleanVar()
        checkbox = tk.Checkbutton(self.tab, text="USS", variable=self.uss)
        checkbox.grid(row=1, column=0, padx=10, pady=10)

        label_t_team = tk.Label(self.tab, text="Team's best time (incl. penalties):")
        label_t_team.grid(row=2, column=0, padx=10, pady=10)

        self.entry_t_team = tk.Entry(self.tab)
        self.entry_t_team.insert(0, "0.0")
        self.entry_t_team.grid(row=2, column=1, padx=10, pady=10)

        label_t_team_cones = tk.Label(self.tab, text="Number of cones hit by team:")
        label_t_team_cones.grid(row=3, column=0, padx=10, pady=10)

        self.entry_t_team_cones = tk.Entry(self.tab)
        self.entry_t_team_cones.insert(0, "0.0")
        self.entry_t_team_cones.grid(row=3, column=1, padx=10, pady=10)

        label_t_team_off = tk.Label(self.tab, text="Number of times being off-course by team:")
        label_t_team_off.grid(row=4, column=0, padx=10, pady=10)

        self.entry_t_team_off = tk.Entry(self.tab)
        self.entry_t_team_off.insert(0, "0.0")
        self.entry_t_team_off.grid(row=4, column=1, padx=10, pady=10)

        label_t_team_laps = tk.Label(self.tab, text="Number of laps by team")
        label_t_team_laps.grid(row=5, column=0, padx=10, pady=10)

        self.entry_t_team_laps = tk.Entry(self.tab)
        self.entry_t_team_laps.insert(0, "0.0")
        self.entry_t_team_laps.grid(row=5, column=1, padx=10, pady=10)

        label_t_max = tk.Label(self.tab, text="Time of fastest vehicle (incl. penalties):")
        label_t_max.grid(row=6, column=0, padx=10, pady=10)

        self.entry_t_max = tk.Entry(self.tab)
        self.entry_t_max.insert(0, "0.0")
        self.entry_t_max.grid(row=6, column=1, padx=10, pady=10)

        label_t_max_cones = tk.Label(self.tab, text="Number of cones hit by fastest vehicle:")
        label_t_max_cones.grid(row=7, column=0, padx=10, pady=10)

        self.entry_t_max_cones = tk.Entry(self.tab)
        self.entry_t_max_cones.insert(0, "0.0")
        self.entry_t_max_cones.grid(row=7, column=1, padx=10, pady=10)

        label_t_max_off = tk.Label(self.tab, text="Number of times being off-course by fastest vehicle:")
        label_t_max_off.grid(row=8, column=0, padx=10, pady=10)

        self.entry_t_max_off = tk.Entry(self.tab)
        self.entry_t_max_off.insert(0, "0.0")
        self.entry_t_max_off.grid(row=8, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.tab, text="Calculate Trackdrive Score", command=self.calculate_trackdrive)
        calculate_button.grid(row=9, column=0, columnspan=10, pady=10)

        self.score_trachdrive = tk.Label(self.tab, text="")
        self.score_trachdrive.grid(row=10, column=0, columnspan=10, pady=10)