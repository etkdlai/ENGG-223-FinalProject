import numpy as np
from FileIO import FileIO
from Date import Date

class TemperatureData:
    year = Date.year
    month = Date.month
    maxTemp = FileIO.dataTable[:,2]
    minTemp = FileIO.dataTable[:,3]
    snowFall = FileIO.dataTable[:,4]

    
    


