#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:33:09 2023

@author: taiebehtahmasebi
"""

import math
import tkinter as tk
from scipy import stats
import matplotlib.pyplot as plt

# Function to calculate the difference between two proportions and its confidence interval
def calculate_prop_diff(conf_level, d1, n1, d2, n2):
    p1 = d1/n1
    p2 = d2/n2
    prop_diff = p1 - p2
    std_error = math.sqrt((p1*(1-p1)/n1) + (p2*(1-p2)/n2))
    z_score = abs(round(stats.norm.ppf((1-conf_level/100)/2), 2))
    margin_error = std_error * z_score
    lower_bound = prop_diff - margin_error
    upper_bound = prop_diff + margin_error
    p_value = 2*(1 - stats.norm.cdf(abs(prop_diff/std_error)))
    return prop_diff, lower_bound, upper_bound, p_value, p1, p2

# Function to plot the two proportions
def plot_props(p1, p2):
    labels = ['Group 1', 'Group 2']
    proportions = [p1, p2]
    plt.bar(labels, proportions)
    plt.ylim([0, 1])
    plt.title('Proportions of Failures in Two Groups')
    plt.ylabel('Proportion')
    plt.show()

# Function to get the user input and calculate the proportions, confidence interval, and statistical significance
def calculate_diff():
    d1 = int(e1.get())
    n1 = int(e2.get())
    d2 = int(e3.get())
    n2 = int(e4.get())
    conf_level = int(e5.get())

    prop_diff, lower_bound, upper_bound, p_value, p1, p2 = calculate_prop_diff(conf_level, d1, n1, d2, n2)

    if p_value < 0.05:
        diff_result.config(text="Difference between two proportions: {:.4f}\nConfidence interval: ({:.4f}, {:.4f})\nStatistical significance: Yes".format(prop_diff, lower_bound, upper_bound))
    else:
        diff_result.config(text="Difference between two proportions: {:.4f}\nConfidence interval: ({:.4f}, {:.4f})\nStatistical significance: No".format(prop_diff, lower_bound, upper_bound))
    plot_props(p1, p2)

# Create the app window and input fields
window = tk.Tk()
window.title("Two Proportion Calculator")
window.geometry("700x500")

# Create the label for the footer
footer = tk.Label(text="Copyright@TaiebehTahmasebi-2023, ENRE640-UMD, Dr. Vasiliy")
footer.pack(side="bottom", pady=5)


l1 = tk.Label(text="Number of failures in group 1:")
l1.pack()
e1 = tk.Entry()
e1.pack()

l2 = tk.Label(text="Total samples tested in group 1:")
l2.pack()
e2 = tk.Entry()
e2.pack()

l3 = tk.Label(text="Number of failures in group 2:")
l3.pack()
e3 = tk.Entry()
e3.pack()

l4 = tk.Label(text="Total samples tested in group 2:")
l4.pack()
e4 = tk.Entry()
e4.pack()

l5 = tk.Label(text="Confidence level (e.g. 90, 95, 99):")
l5.pack()
e5 = tk.Entry()
e5.pack()

# Create the button to calculate the difference and plot the proportions
button = tk.Button(text="Calculate Difference", command=calculate_diff)
button.pack()

# Create a label to display the results
diff_result = tk.Label(text="")
diff_result.pack()

# Run the app
window.mainloop()