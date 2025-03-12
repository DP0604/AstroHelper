from lib import functions
import numpy as np

messier_arr = functions.load_variable_column_file("Messier.txt")
NGC_arr = functions.load_variable_column_file("NGC.txt")
IC_arr = functions.load_variable_column_file("IC.txt")


data_arr = np.vstack((messier_arr, NGC_arr, IC_arr))

Lon = functions.dms_to_deg(12, 0, 57)
Lat = functions.dms_to_deg(48, 40, 54)
ele = 450

functions.TelescopeData(1624, 2.4, 5496, 3672)

selected_date = "2025-03-08"
timezone = "Europe/Berlin"

final_best = functions.Final_Best(data_arr, obs_date=selected_date, timezone=timezone, Lon=Lon, ele=ele, min_frac=0.2, Only_Galaxies = 1)
function.PlotBestObjects(objects=final_best, obs_date=selected_date, timezone=timezone, Lon=Lon, Lat=Lat, ele=ele, k = 6, Only_Galaxies = 1)