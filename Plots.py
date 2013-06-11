__author__ = 'Pierzchalski'

import GetData as gd
import matplotlib.pyplot as pp
import numpy as np
import os
import shutil

maxIndex = 100
paramsToIndexes = gd.paramsToIndexesDict(maxIndex)
paramsToDicts = gd.paramsToDicts(maxIndex)
plotsDir = os.path.join('C:\\Users', 'Pierzchalski', 'IdeaProjects', 'trafficLightRL', 'out', 'plots')

def plotFn(params, figureIndex, fn, save=True, saveName = "plot", show=False):
    indexes = paramsToIndexes[params]
    pp.figure(figureIndex)
    fn(indexes)
    if save:
        plotDir = os.path.join(plotsDir, 'plot%d' % figureIndex)
        if not os.path.exists(plotDir): os.mkdir(plotDir)
        pp.savefig(os.path.join(plotDir, saveName))
    if show: pp.show()

def copyParams(figureIndex, paramsList):
    plotDir = os.path.join(plotsDir, 'plot%d' % figureIndex)
    for f in os.listdir(plotDir):
        if f.endswith('.txt'):
            os.remove(os.path.join(plotDir, f))
    for param in paramsList:
        index = paramsToIndexes[param]
        shutil.copyfile(gd.paramsFileDir(index[0]), os.path.join(plotDir, 'params%d.txt'%index[0]))

def setTitleAndAxes(plotIndex, title, xLabel, yLabel):
    pp.figure(plotIndex)
    pp.title(title)
    pp.xlabel(xLabel)
    pp.ylabel(yLabel)

def fnScores(indexes):
    for index in indexes:
        pp.plot(gd.scores(index), linestyle=':', marker='x')

def fnPointwiseAverage(indexes):
    scores = np.array([ gd.scores(index) for index in indexes ])
    averages = np.mean(scores, 0)
    pp.plot(averages, linestyle=':', marker='x')

p0 = gd.paramsFileToKey(0)
p1 = gd.paramsFileToKey(10)
p2 = gd.paramsFileToKey(20)
p3 = gd.paramsFileToKey(30)

setTitleAndAxes(0, "Comparison of Traffic Generators", "Score Index", "Score")
plotFn(p0, 0, fnPointwiseAverage)
plotFn(p1, 0, fnPointwiseAverage)
copyParams(0, [p0, p1])