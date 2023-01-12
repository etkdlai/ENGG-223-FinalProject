import numpy as np
from FileIO import FileIO
from Date import Date
from TemperatureData import TemperatureData
from WeatherAnalyzer import WeatherAnalyzer
from Chart import drawLineChart,drawBarChart

w = WeatherAnalyzer()

while True:
    print()
    print("1 - Get Minimum Temperature of 1990-2019",
    "2 - Get Maximum Temperature of 1990-2019",
    "3 - Get Minimum Temperature of 1990-2019 Annually",
    "4 - Get Maximum Temperature of 1990-2019 Annually", 
    "5 - Get Average Snowfall between 1990-2019 Annually",
    "6 - Get Average Temperature between 1990-2019 Annually",
    "7 - LineChart Minimum Temperature of 1990-2019 Annually",
    "8 - LineChart Maximum Temperature of 1990-2019 Annually",
    "9 - BarChart Average Snowfall between 1990-2019 Annually",
    "10 - BarChart Average Temperature between 1990-2019 Annually",
    "0 - Exit Program", sep='\n')
    x = int(input("Type a number(0-10)"))

    while (x < 0) or (x > 10):
        x = int(input("Pleas type a number(0-10)"))

    if x == 0:
        print("Program Finished")
        break
    elif x == 1:
        print("The minimum temperature during this time was", w.getMinTemp(), "degrees Fahrenheit")
        print()
        delay = input("Enter anything to continue")
    elif x == 2:
        print("The maximum temperature in this time period was", w.getMaxTemp(), "degrees Fahrenheit")
        print()
        delay = input("Enter anything to continue")
    elif x == 3:
       print("The annual minimum temperatures per year were", w.getMinTempAnnually(), "degrees Fahrenheit")
       print()
       delay = input("Enter anything to continue")
    elif x == 4:
       print( "The annual maximum temperatures per year were", w.getMaxTempAnnually(), "degrees Fahrenheit")
       print()
       delay = input("Enter anything to continue")
    elif x == 5:
        print("The average snowfall during this time period was", w.getAvgSnowFallAnnually(), "centimetres")
        print()
        delay = input("Enter anything to continue")
    elif x == 6:
        print("The average temperature annually ", w.getAvgTempAnnually(), "degrees Fahrenheit")
        print()
        delay = input("Enter anything to continue")
    elif x == 7:
       drawLineChart(w.getMinTempAnnually()[0],w.getMinTempAnnually()[1],"Minimum Temperature Annually","Year","Temperature(F)")
    elif x == 8:
        drawLineChart(w.getMaxTempAnnually()[0],w.getMaxTempAnnually()[1],"Maximum Temperature Annually","Year","Temperature(F)")
    elif x == 9:
       drawBarChart(w.getAvgSnowFallAnnually()[0],w.getAvgSnowFallAnnually()[1],"Average Snowfall Annually","Years","Average Snowfall(cm)")
    elif x == 10:
        drawBarChart(w.getAvgTempAnnually()[0],w.getAvgTempAnnually()[1],"Average Temperature Annually","Years","Temperature(F)")
    
    
    


