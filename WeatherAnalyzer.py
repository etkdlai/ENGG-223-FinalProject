import numpy as np
from FileIO import FileIO
from Date import Date
from TemperatureData import TemperatureData

class WeatherAnalyzer:

    year = TemperatureData.year
    month = TemperatureData.month
    minTemp = TemperatureData.minTemp
    maxTemp = TemperatureData.maxTemp
    snowFall = TemperatureData.snowFall
    
    
    def getMinTemp(self):
        allmin = [self.minTemp]
        absminT = np.amin(allmin)
        return absminT
    
    def getMaxTemp(self):
        allmax = [self.maxTemp]
        absmaxT = np.amax(allmax)
        return absmaxT
    
    def avgSnowFall(self):
        snow = [self.snowFall]
        avg = np.average(snow)
        return avg
    
    def getMinTempAnnually(self):
        minTA = []
        TbyYear = []
        for x in range(30):
            for i in range(12):
                if (x*12) + i == 359:
                    break
                TbyYear.append(self.minTemp[(x*12)+i])
            minTA.append(np.amin(TbyYear))
            TbyYear.clear()
            year = [i for i in range(1990,2020)]
        return np.array([year, minTA])

    def getMaxTempAnnually(self):
        maxTA = []
        TbyYear = []
        for x in range(30):
            for i in range(12):
                if (x * 12) + i == 359:
                    break
                TbyYear.append(self.maxTemp[(x*12)+i])
            maxTA.append(np.amax(TbyYear))
            TbyYear.clear()
            year = [i for i in range(1990,2020)]
        return np.array([year, maxTA])

    def getAvgSnowFallAnnually(self):
        avgSF = []
        SbyYear = []
        for x in range(30):
            for i in range(12):
                if (x * 12) + i == 359:
                    break
                SbyYear.append(self.snowFall[(x*12)+i])
            avgSF.append(np.average(SbyYear))
            SbyYear.clear()
            year = [i for i in range(1990,2020)]
        return np.array([year, avgSF])

    def getAvgTempAnnually(self):
        avgTA = []
        MinbyYear = []
        MaxbyYear = []
        AvgbyYear = []

        for x in range(30):
            for i in range(12):
                if (x * 12) + i == 359:
                    break
                MaxbyYear.append(self.maxTemp[(x*12)+i])
                MinbyYear.append(self.minTemp[(x*12)+i])
                AvgbyYear.append((MinbyYear[i]+MaxbyYear[i]) / 2)
            avgTA.append(np.average(AvgbyYear))
            AvgbyYear.clear()
            MinbyYear.clear()
            MaxbyYear.clear()
            year = [i for i in range(1990,2020)]
        return np.array([year, avgTA])