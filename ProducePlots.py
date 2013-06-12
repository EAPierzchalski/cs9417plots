__author__ = 'Pierzchalski'


import Plots as plots
import GetData as gd


params = [ key for key in plots.paramsToIndexes.keys() ]

plotIndex = 0


def myCmp(a, b):
    return cmp(sorted(plots.paramsToIndexes[a])[0], sorted(plots.paramsToIndexes[b])[0])


for param in sorted(params, myCmp):
    print("Plotting %d"%plotIndex)
    #plots.plotFn(param, plotIndex, fn=plots.fnPointwiseAverage(legendLabel="Assessment scores", assessment=True), save=False)
    #plots.plotFn(param, plotIndex, fn=plots.fnPointwiseAverage(legendLabel="Training scores", assessment=False), save=False)
    plots.plotFn(param, plotIndex, fn=plots.fnErrorBar(legendLabel="Assessment scores", assessment=True), save=False)
    plots.plotFn(param, plotIndex, fn=plots.fnErrorBar(legendLabel="Training scores", assessment=False), save=False)
    plots.setTitleAndAxes(plotIndex, title="", xLabel="Score index", yLabel="Score")
    plots.insertLegend(plotIndex, save=True)
    plots.copyReplaceParams(plotIndex, [param])
    plotIndex += 1

