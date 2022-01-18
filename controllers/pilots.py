import requests
import json
import pandas as pd

def getDriversId(season):
    url = 'http://ergast.com/api/f1/' + season + '/drivers.json'
    r = requests.get(url)
    circuitsList = json.loads(r.text).get('MRData').get('DriverTable').get('Drivers')
    results = []
    for circuit in circuitsList:
        object = {
            'name': circuit.get('familyName'),
            'id': circuit.get('driverId'),
        }

        results.append(object)

    return pd.DataFrame(results)

def getPilotResultFromSeason(pilot, season, printResult):
    url = 'http://ergast.com/api/f1/' + season + '/drivers/' + pilot + '/results.json'
    r = requests.get(url)
    raceResult = json.loads(r.text).get('MRData').get('RaceTable').get('Races')
    results = []
    for result in raceResult:
        object = {
            'pilot': pilot,
            'race': result.get('raceName'),
            'date': result.get('date'),
            'grid': int(result.get('Results')[0].get('grid')),
            'position': int(result.get('Results')[0].get('position')),
            'gainedPlaces': int(result.get('Results')[0].get('grid')) - int(result.get('Results')[0].get('position')),
            'finished': result.get('Results')[0].get('status') == 'Finished'
        }

        results.append(object)

    resultTable = pd.DataFrame(results)
    finishedRaces = resultTable[(resultTable['finished'])]

    if printResult:
        print('**********************************************')
        print('result of ' + pilot + ' in ' + season)
        print(resultTable)
        print('**********************************************')
        print('average result of ' + pilot + ' in ' + season)
        print(resultTable.groupby('pilot').mean())
        print('**********************************************')
    else:
        return resultTable.groupby('pilot').mean()


def getPilotResultFromCircuit(pilot, circuit, printResult):
    url = 'http://ergast.com/api/f1/drivers/' + pilot + '/circuits/' + circuit + '/results.json'
    r = requests.get(url)
    raceResult = json.loads(r.text).get('MRData').get('RaceTable').get('Races')
    results = []
    for result in raceResult:
        object = {
            'pilot': pilot,
            'date': result.get('date'),
            'grid': int(result.get('Results')[0].get('grid')),
            'position': int(result.get('Results')[0].get('position')),
            'gainedPlaces': int(result.get('Results')[0].get('grid')) - int(result.get('Results')[0].get('position')),
            'finished': result.get('Results')[0].get('status') == 'Finished'
        }

        results.append(object)

    resultTable = pd.DataFrame(results)
    finishedRaces = resultTable[(resultTable['finished'])]

    if printResult:
        print('**********************************************')
        print('result of ' + pilot + ' in ' + circuit)
        print(resultTable)
        print('**********************************************')
        print('average result of ' + pilot + ' in ' + circuit)
        print(resultTable.groupby('pilot').mean())
        print('**********************************************')
    else:
        return resultTable.groupby('pilot').mean()

