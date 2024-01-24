import tkinter as tk
from tkinter import ttk

from src.bpp import BPPTab
from src.cost import CostTab
from src.skidpad import SkidpadTab
from src.skidpad_dv import SkidpadDVTab
from src.skidpad_dc import SkidpadDCTab
from src.acceleration import AccelerationTab
from src.acceleration_dv import AccelerationDVTab
from src.acceleration_dc import AccelerationDCTab
from src.autocross import AutocrossTab
from src.autocross_dc import AutocrossDCTab
from src.endurance import EnduranceTab
from src.efficiency import EfficiencyTab
from src.trackdrive import TrackdriveTab
#from src.bpp_fsa import BPPFSATab
#from src.skidpad_fsa import SkidpadFSATab
#from src.acceleration_fsa import AccelerationFSATab


root = tk.Tk()
root.title("Scoring calculator")
notebook = ttk.Notebook(root)

bpp_tab = BPPTab(notebook)

cost_tab = CostTab(notebook)
skidpad_tab = SkidpadTab(notebook)
skidpad_dv_tab = SkidpadDVTab(notebook)
skidpad_dc_tab = SkidpadDCTab(notebook)
acceleration_tab = AccelerationTab(notebook)
acceleration_dv_tab = AccelerationDVTab(notebook)
acceleration_dc_tab = AccelerationDCTab(notebook)
autocross_tab = AutocrossTab(notebook)
autocross_dc_tab = AutocrossDCTab(notebook)
endurance_tab = EnduranceTab(notebook)
efficiency_tab = EfficiencyTab(notebook)
trackdrive_tab = TrackdriveTab(notebook)
#bpp_fsa_tab = BPPFSATab(notebook)
#skidpad_fsa_tab = SkidpadFSATab(notebook)
#acceleration_fsa_tab = AccelerationFSATab(notebook)

notebook.add(bpp_tab.tab, text="BPP")
notebook.add(cost_tab.tab, text="Cost")
notebook.add(skidpad_tab.tab, text="Skidpad")
notebook.add(skidpad_dv_tab.tab, text="Skidpad DV")
notebook.add(skidpad_dc_tab.tab, text="Skidpad DC")
notebook.add(acceleration_tab.tab, text="Acceleration")
notebook.add(acceleration_dv_tab.tab, text="Acceleration DV")
notebook.add(acceleration_dc_tab.tab, text="Acceleration DC")
notebook.add(autocross_tab.tab, text="Autocross")
notebook.add(autocross_dc_tab.tab, text="Autocross DC")
notebook.add(endurance_tab.tab, text="Endurance")
notebook.add(efficiency_tab.tab, text="Efficiency")
notebook.add(trackdrive_tab.tab, text="Trackdrive")
#notebook.add(bpp_fsa_tab.tab, text="BPP FSA")
#notebook.add(skidpad_fsa_tab.tab, text="Skidpad FSA")
#notebook.add(acceleration_fsa_tab.tab, text="Acceleration FSA")

notebook.pack(pady=10)

root.mainloop()