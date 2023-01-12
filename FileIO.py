import numpy as np


class FileIO:
    file_name = "ENGG233Project/CalgaryWeather.csv"
    dataTable = np.loadtxt(file_name, delimiter=',' , dtype=np.float, skiprows=1)