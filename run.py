from astrohelper import functions
import numpy as np

messier_arr = functions.load_variable_column_file("Messier.txt")
NGC_arr = functions.load_variable_column_file("NGC.txt")
IC_arr = functions.load_variable_column_file("IC.txt")


data_arr = np.vstack((messier_arr, NGC_arr, IC_arr))

#Location data of your observation point (e.g., Dr. Remeis Observatory)
Lon = 10.88846 
Lat = 49.88474 
ele = 282   # in meters

functions.TelescopeData()

selected_date = "2025-04-15"
timezone = "Europe/Berlin"

final_best = functions.Final_Best(data_arr, obs_date=selected_date, timezone=timezone, Lon=Lon, ele=ele, min_frac=0.2, Galaxies = 1)
functions.PlotBestObjects(objects=data_arr, obs_date=selected_date, timezone=timezone, Lon=Lon, Lat=Lat, ele=ele, k = 5, Galaxies = 1)