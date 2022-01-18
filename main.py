# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import controllers.races
import controllers.pilots


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # lastResult = controllers.races.getLastResult()
    # lastQualif = controllers.races.getLastQualif()
    # print(lastResult)
    # print(lastQualif)
    #
    # print(controllers.pilots.getDriversId('2021'))
    controllers.pilots.getPilotResultFromSeason('hamilton', '2021', 1)
    controllers.pilots.getPilotResultFromSeason('max_verstappen', '2021', 1)
    controllers.pilots.getPilotResultFromSeason('leclerc', '2021', 1)
    #

    # controllers.pilots.getPilotResultFromCircuit('hamilton', 'bahrain', 1)
    # controllers.pilots.getPilotResultFromCircuit('max_verstappen', 'bahrain', 1)
    controllers.races.predictRaceFromLastYearCircuit('bahrain', 2022)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
