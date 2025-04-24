#analyze_flux.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#Configuration
DATA_FILE = "flux_final.txt"
DISTANCE_LY = 34.13				#Distance between earth and system in light-years
DISTANCE_M = DISTANCE_LY * 9.461e15 		#Convert distance in ligh-years to meters
SAVE_DIR = "figs"

#Create Output Folder
os.makedirs(SAVE_DIR, exist_ok=True)

#Load Data
df = pd.read_csv(DATA_FILE, delimiter="\t")
print("Data preview:")
print(df.head())

#Plot Relative Flux (Light Curve)
plt.figure()
plt.plot(df["HJD_UTC"], df["rel_flux_T1"], marker='o', linestyle='-')
plt.xlabel("HJD (UTC)")
plt.ylabel("Relative Flux (T1)")
plt.title("Light Curve of Target 1")
plt.grid(True)
plt.savefig(f"{SAVE_DIR}\light_curve.png", dpi=300)
plt.close()

#Compute Luminosity 
df["Luminosity"] = 4 * np.pi * (DISTANCE_M**2) * df["rel_flux_T1"]

#Plot Luminsity 
plt.figure()
plt.plot(df["HJD_UTC"], df["Luminosity"], color='orange', linestyle='-')
plt.xlabel("HJD (UTC)")
plt.ylabel("Estimated Luminosity (arbitrary units)")
plt.title("Intrinsic Luminosity of Target 1")
plt.grid(True)
plt.savefig(os.path.join(SAVE_DIR, "luminisity_curve.png"), dpi=300)
plt.close()

#Eclipse Analysis
min_idx = df["rel_flux_T1"].idxmin()
min_flux = df.loc[min_idx, "rel_flux_T1"]
min_time = df.loc[min_idx, "HJD_UTC"]
max_flux = df["rel_flux_T1"].max()
mean_flux = df["rel_flux_T1"].mean()
depth = max_flux - min_flux

#Estimate eclipse duration (< mean)
eclipse_points = df[df["rel_flux_T1"] < mean_flux]
eclipse_duration = eclipse_points["HJD_UTC"].max() - eclipse_points["HJD_UTC"].min()

print(f"Minimum flux: {min_flux:.5f} at HJD {min_time}")
print(f"Eclipse depth: {depth:.5f}")
print(f"Eclipse duration: {eclipse_duration:.5f} days")


#Light Curve with Analysis
plt.figure()
plt.plot(df["HJD_UTC"], df["rel_flux_T1"], marker='o', label="Flux")
plt.axhline(mean_flux, color='blue', linestyle='--', label = f"Mean Flux ≈ {mean_flux:.4f}")
plt.axhline(min_flux, color='black', linestyle='--', label = f"Min Flux ≈ {min_flux:.4f}")
plt.axvline(min_time, color='red', linestyle=':', label = f"Eclipse at HJD ≈ {min_time:.4f}")
plt.xlabel("HJD (UTC)")
plt.ylabel("Relative Flux (T1)")
plt.title("Light Curve with Primary Eclipse")
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(SAVE_DIR, "analyzed_light_curve.png"), dpi=300)
plt.close()

print(f"Plots saved to ./{SAVE_DIR}/")
