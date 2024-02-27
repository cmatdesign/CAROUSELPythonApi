'''
Low-Level Carousel API Usage Example

This file serves as an illustrative example demonstrating the loading and utilization of the low-level Carousel API.

Note: This file is exclusively intended for developers. Direct usage of the API is discouraged unless you know what you are doing.
'''

import os
import matplotlib.pyplot as plt
from itertools import groupby
from operator import itemgetter

# import carousel python package
from carousel import carouselApi

# Get the path of the currently executed file
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)

# Initializing carouselApi.Carousel loads the dynamic-link library (DLL) containing all implementations. 
# In this case, we use the library designed for use in combination with MatCalc.
api_handle = carouselApi.Carousel(os.path.join(current_directory, 'AM_MATCALC_Lib.dll'))

# Example on how to set the working directory using the api
result = carouselApi.configuration_get_working_directory(api_handle)
result = carouselApi.configuration_set_working_directory(api_handle, b'/DummyWorkspace')
result = carouselApi.configuration_get_working_directory(api_handle)