__author__ = 'Pierzchalski'

import GetData as gd
import matplotlib.pyplot as pp
import numpy as np
import os
import shutil

maxIndex = 720
paramsToIndexes = gd.paramsToIndexesDict(maxIndex)
paramsToDicts = gd.paramsToDicts(maxIndex)
plotsDir = os.path.join('C:\\Users', 'Pierzchalski', 'IdeaProjects', 'trafficLightRL', 'out', 'plots')


def plotFn(params, figureIndex, fn, save=True, saveName="plot", show=False):
    indexes = paramsToIndexes[params]
    pp.figure(figureIndex)
    fn(indexes)
    if save:
        plotDir = os.path.join(plotsDir, 'plot%d' % figureIndex)
        if not os.path.exists(plotDir): os.makedirs(plotDir)
        pp.savefig(os.path.join(plotDir, saveName))
    if show: pp.show()


def copyReplaceParams(figureIndex, paramsList):
    plotDir = os.path.join(plotsDir, 'plot%d' % figureIndex)
    for f in os.listdir(plotDir):
        if f.endswith('.txt'):
            os.remove(os.path.join(plotDir, f))
    for param in paramsList:
        index = paramsToIndexes[param]
        shutil.copyfile(gd.paramsFileDir(index[0]), os.path.join(plotDir, 'params%d.txt' % index[0]))


def setTitleAndAxes(plotIndex, title, xLabel, yLabel):
    pp.figure(plotIndex)
    pp.title(title)
    pp.xlabel(xLabel)
    pp.ylabel(yLabel)


def insertLegend(figureIndex, save=True, saveName="plot", loc='lower right'):
    pp.figure(figureIndex)
    pp.legend(loc=loc)
    if save:
        plotDir = os.path.join(plotsDir, 'plot%d' % figureIndex)
        if not os.path.exists(plotDir): os.makedirs(plotDir)
        pp.savefig(os.path.join(plotDir, saveName))


def fnScores(legendLabel, assessment=True):
    def fn(indexes):
        for index in indexes:
            if assessment:
                scores = gd.assessmentScores(index)
            else:
                scores = gd.trainingScores(index)
            pp.plot(scores, linestyle=':', marker='x', label=legendLabel)
    return lambda indexes: fn(indexes)


def fnPointwiseAverage(legendLabel, assessment=True):
    def fn(indexes):
        scores = []
        for index in indexes:
            if assessment:
                scores += [gd.assessmentScores(index)]
            else:
                scores += [gd.trainingScores(index)]
        scores = np.array(scores)
        averages = np.mean(scores, 0)
        pp.plot(averages, linestyle=':', marker='x', label=legendLabel)
    return lambda indexes: fn(indexes)


def fnErrorBar(legendLabel, assessment=True):
    def fn(indexes):
        scores = []
        for index in indexes:
            if assessment:
                scores += [gd.assessmentScores(index)]
            else:
                scores += [gd.trainingScores(index)]
        scores = np.array(scores)
        meanScores = np.mean(scores, 0)
        highErrors = np.max(scores, 0) - meanScores
        lowErrors = meanScores - np.min(scores, 0)
        pp.errorbar(x=[i for i in range(0, len(meanScores))], y=meanScores, yerr=[lowErrors, highErrors], label=legendLabel)
    return lambda indexes: fn(indexes)

# def fnBarPlot(assessment=True):
#     def fn(indexes):
#         scores = []
#         for index in indexes:
#             if assessment:
#                 scores += [gd.assessmentScores(index)]
#             else:
#                 scores += [gd.trainingScores(index)]
#         scores = np.array(scores)
#         pp.boxplot(scores)
#     return lambda indexes: fn(indexes)