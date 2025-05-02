# %%
# Example usage

import astrohelper as ah
import numpy as np

# Loading the object files
messier_arr = ah.load_variable_column_file("Messier.txt")
NGC_arr = ah.load_variable_column_file("NGC.txt")
IC_arr = ah.load_variable_column_file("IC.txt")

data_arr = np.vstack((messier_arr, NGC_arr, IC_arr))

#Location data of your observation point (e.g., Dr. Remeis Observatory)
Lon = 10.88846
Lat = 49.88474
ele = 282

ah.TelescopeData() # Function to set your telescope data. (Focal length, Pixel Size, Dimensions)

selected_date = "2024-04-15" # Example date in format "YYYY-MM-DD"
timezone = "Europe/Berlin" # Example timezone

final_best = ah.Final_Best(data_arr, obs_date = selected_date, Lon = Lon, Lat = Lat, ele = ele, timezone = timezone, min_frac = 0.08, max_frac = 0.8, Galaxies = 1, Nebulae = 1) # Example function call to get the best objects
ah.PlotBestObjects(objects = data_arr, obs_date = selected_date, Lon = Lon, Lat = Lat, ele = ele, timezone = timezone, min_frac = 0.08, max_frac = 0.8, k = 5, Galaxies = 1, Nebulae = 1) # Example function call to plot the best objects