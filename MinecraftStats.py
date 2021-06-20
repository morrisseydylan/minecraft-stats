# take json values from one file and additively combine with another file
import json

# stats files in a MC world are named according to the player UUID
# prior to the script running, the files should be renamed 1.json and 2.json
with open('1.json') as file:
    data1 = json.load(file)
oldStats = data1["stats"]
dataVersion = data1["DataVersion"]
# DataVersion is a number assigned by MC that corresponds to the MC version the world was last loaded on
# stats data may be formatted differently on different data versions

with open('2.json') as file:
    data2 = json.load(file)
newStats = data2["stats"]
versionMatch = dataVersion == data2["DataVersion"]

if not versionMatch:
    while True:
        print("The Minecraft versions of the files don't match. Proceed anyway? y/n:")
        proceed = input()
        if proceed == 'y' or proceed == 'n':
            break

if versionMatch or proceed == 'y':
    combinedStats = oldStats
    # stats are organized by type
    for (statType, stats) in newStats.items():
        if statType not in combinedStats:
            combinedStats[statType] = stats
        else:
            for (statName, statValue) in newStats[statType].items():
                if statName not in combinedStats[statType]:
                    combinedStats[statType][statName] = statValue
                else:
                    combinedStats[statType][statName] += statValue
    with open('3.json', 'w') as file:
        # output file will need to be renamed to player's UUID to be used in the world
        json.dump({ "stats": combinedStats, "DataVersion": dataVersion}, file, separators = [',', ':'])
