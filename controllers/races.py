import requests
import json
import pandas as pd

from controllers import pilots
from controllers.pilots import getPilotResultFromCircuit


def getLastResult():
    url = 'http://ergast.com/api/f1/current/last/results.json'
    r = requests.get(url)
    raceResult = json.loads(r.text).get('MRData').get('RaceTable').get('Races')[0].get('Results')
    pilotList = []
    for pilot in raceResult:
        pilotList.append(pilot.get('Driver').get('code'))

    print(pd.Series(pilotList))


def getLastQualif():
    url = 'http://ergast.com/api/f1/current/last/qualifying.json'
    r = requests.get(url)
    raceResult = json.loads(r.text).get('MRData').get('RaceTable').get('Races')[0].get('QualifyingResults')
    pilotList = []
    for pilot in raceResult:
        pilotList.append(pilot.get('Driver').get('code'))

    print(pd.Series(pilotList))


def getCircuitsId():
    url = 'http://ergast.com/api/f1/circuits.json'
    r = requests.get(url)
    circuitsList = json.loads(r.text).get('MRData').get('CircuitTable').get('Circuits')
    results = []
    for circuit in circuitsList:
        object = {
            'name': circuit.get('circuitName'),
            'id': circuit.get('circuitId'),
        }

        results.append(object)

    print(pd.DataFrame(results))

def predictRaceFromLastYearCircuit(circuit, season):
    pilotsList = pilots.getDriversId(str(int(season) - 1))
    averageResult = []

    for pilot in pilotsList['id'].to_numpy():
        result = getPilotResultFromCircuit(pilot, circuit, 0)
        object = {
            'pilot': pilot,
            'grid': result.loc[pilot, 'grid'],
            'position': result.loc[pilot, 'position'],
        }

        averageResult.append(object)

    averageResult.sort(key=lambda x: x.get('grid'))
    print('***********************')
    print('Predicted qualif for ' + circuit + ' ' + str(season))
    qualifList = getPilotsNamesList(averageResult)
    print(qualifList)
    print('***********************')

    averageResult.sort(key=lambda x: x.get('position'))
    print('Predicted result for ' + circuit + ' ' + str(season))
    resultList = getPilotsNamesList(averageResult)
    print(resultList)
    print('***********************')


def getPilotsNamesList(pilots):
    pilotsNames = []
    for pilot in pilots:
        pilotsNames.append(pilot.get('pilot'))

    return pd.DataFrame(pilotsNames)
