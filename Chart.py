import numpy as np
import matplotlib.pyplot as pyplot

def drawLineChart(x,y,title,xlabel,ylabel):
    linefig = pyplot.figure()
    pyplot.title(title)
    pyplot.ylabel(ylabel)
    pyplot.xlabel(xlabel)

    pyplot.plot(x,y,marker='o')
    pyplot.show()

def drawBarChart(x,y,title,xlabel,ylabel):
    barfig = pyplot.figure()
    pyplot.title(title)
    pyplot.ylabel(ylabel)
    pyplot.xlabel(xlabel)

    pyplot.bar(x,y)
    pyplot.show()