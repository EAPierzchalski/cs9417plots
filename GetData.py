__author__ = 'Pierzchalski'

import os
import re

sim_data_dir = os.path.join('C:\\Users', 'Pierzchalski', 'IdeaProjects', 'trafficLightRL', 'out', 'sim')


def paramsFileToKey(index, withSeed=False):
    """

    :param index: sim index
    :param withSeed: whether to include the seed with the map
    :return: a tuple acting as an immutable key sort magic thing
    """
    return tuple(sorted(paramsFileToDict(index, withSeed=withSeed).items()))


def paramsFileToDict(index, withSeed=False):
    """

    :param index: sim index
    :param with_seed: whether to include the seed with the map
    :return: a tuple acting as an immutable key sort magic thing
    """
    myFile = getParamsFile(index)
    paramPattern = re.compile('^\s*(.+?)\s*:\s*(.+?)$')
    lines = myFile.readlines()
    myFile.close()
    lines = [line for line in filter(lambda s: re.match(paramPattern, s) is not None, lines)]
    matches = [re.match(paramPattern, line) for line in lines]
    kv = {match.group(1): match.group(2) for match in matches}
    if not withSeed: kv.pop('seed')
    return kv


def assessmentScores(index):
    """

    :param index: index of the sim
    :return: an array of ints indicating the score of the sim every number of time steps
    """
    myFile = getAssessmentScoresFile(index)
    scorePattern = re.compile('(-?[\d]+)\)$')
    lines = myFile.readlines()
    myFile.close()
    scores = [int(re.search(scorePattern, line).group(1)) for line in lines]
    return scores


def paramsFileDir(index):
    return os.path.join(sim_data_dir, 'data%d' % index, 'params.txt')


def getParamsFile(index):
    return open(paramsFileDir(index), 'r')


def assessmentScoresFileDir(index):
    return os.path.join(sim_data_dir, 'data%d' % index, 'assessmentScores.txt')


def trainingScoresFileDir(index):
    return os.path.join(sim_data_dir, 'data%d' % index, 'learningScores.txt')


def getAssessmentScoresFile(index):
    return open(assessmentScoresFileDir(index), 'r')


def getTrainingScoresFile(index):
    return open(trainingScoresFileDir(index), 'r')


def paramsToIndexesDict(maxIndex):
    paramIndexes = dict()
    for index in range(0, maxIndex):
        params = paramsFileToKey(index)
        if params not in paramIndexes: paramIndexes[params] = []
        paramIndexes[params] += [index]
    return paramIndexes


def paramsToDicts(maxIndex):
    paramDicts = dict()
    for index in range(0, maxIndex):
        paramsKey = paramsFileToKey(index)
        paramsDict = paramsFileToDict(index)
        paramDicts[paramsKey] = paramsDict
    return paramDicts


def paramString(param):
    name = re.sub('\'', '', re.sub('\\.', '_', str(param)))
    print(len(name))
    return name