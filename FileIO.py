import numpy as np


class FileIO:
    file_name = "CalgaryWeather.csv"
    dataTable = np.loadtxt(file_name, delimiter=',' , dtype=float, skiprows=1)