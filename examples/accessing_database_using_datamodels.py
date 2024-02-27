'''
Example demonstrating how to use Python data models to retrieve data from a Carousel-generated database.


'''

import os
import matplotlib.pyplot as plt
from itertools import groupby
from operator import itemgetter

# For this example we use a dummy database located in the examples directory
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)

# import carousel python package
from carousel import carouselDatabase, carouselModels

# Get database connection:
database_filepath = os.path.join(current_directory,'AMDatabase.db')
database_connection = carouselDatabase.DatabaseHandler(database_filepath)

# Load Project using Carousel's data models, here we load project with ID = 1
project = carouselModels.Project.load(database_connection, 1)

# To plot something, scheil simulation data is loaded from the database
project.load_scheil_simulation_data(database_connection)

for case in project.Cases:
    # First, sort the simulations by PhaseName and Temperature
    simulations_sorted = sorted(case.SheilSimulations, key=lambda x: (x.PhaseName, x.Temperature))
    
    # group by phase name
    grouped_simulations = {}
    for key, group in groupby(simulations_sorted, key=lambda x: x.PhaseName):
        grouped_simulations[key] = list(group)
    
    # sort by temperature (simulation data might invert)
    for phase_name, simulations_group in grouped_simulations.items():
        grouped_simulations[phase_name] = sorted(simulations_group, key=lambda x: x.Temperature)

    # Plot data by phase
    for phase_name, simulations_group in grouped_simulations.items():
        # Extract x and y values from simulations_group
        x_values = [simulation.Temperature for simulation in simulations_group]
        y_values = [simulation.PhaseFraction for simulation in simulations_group]

        # Plot
        plt.plot(x_values, y_values, label=f"Project {project.ID} - Case {case.ID} - Phase {phase_name}")


    # Add labels and title
    plt.xlabel('Temperature')
    plt.ylabel('Phase Fraction')
    plt.title('Scheil Simulations')
    plt.legend()

    # Display the plot
    plt.grid(True)
    plt.show()