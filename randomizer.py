import imp


import random
import sys


def initializeCivs():
	civs = {
        "America": True,              
        "America": True,
        "Arabia": True,
        "Assyria": True,
        "Austria": True,
        "Aztecs": True,
        "Babylon": True,
        "Brazil": True,
        "Byzantium": True,
        "Carthage": True,
        "Celts": True,
        "China": True,
        "Denmark": True,
        "Egypt": True,
        "England": True,
        "Ethiopia": True,
        "France": True,
        "Germany": True,
        "Greece": True,
        "Huns": True,
        "Inca": True,
        "India": True,
        "Indonesia": True,
        "Iroquois": True,
        "Japan": True,
        "Korea": True,
        "Maya": True,
        "Mongolia": True,
        "Morocco": True,
        "Netherlands": True,
        "Ottomans": True,
        "Persia": True,
        "Poland": True,
        "Polynesia": True,
        "Portugal": True,
        "Rome": True,
        "Russia": True,
        "Shoshone": True,
        "Siam": True,
        "Songhai": True,
        "Spain": True,
        "Sweden": True,
        "Venice": True,
        "Zulus": True
    }
	return civs


def invertCivs(civs):
    res = {}
    for civ in civs.items():
        res[civ[0]] = not civ[1]
    return res


def standartCivs():
    civs = {
        "America": True,              
        "America": True,
        "Arabia": True,
        "Assyria": True,
        "Austria": True,
        "Aztecs": True,
        "Babylon": True,
        "Brazil": True,
        "Byzantium": True,
        "Carthage": True,
        "Celts": True,
        "China": True,
        "Denmark": True,
        "Egypt": True,
        "England": True,
        "Ethiopia": True,
        "France": True,
        "Germany": True,
        "Greece": True,
        "Huns": False,
        "Inca": True,
        "India": True,
        "Indonesia": True,
        "Iroquois": True,
        "Japan": True,
        "Korea": True,
        "Maya": True,
        "Mongolia": True,
        "Morocco": True,
        "Netherlands": True,
        "Ottomans": True,
        "Persia": True,
        "Poland": True,
        "Polynesia": True,
        "Portugal": True,
        "Rome": True,
        "Russia": True,
        "Shoshone": True,
        "Siam": True,
        "Songhai": True,
        "Spain": False,
        "Sweden": True,
        "Venice": False,
        "Zulus": True
    }
    return civs


def randomizeCivs(civs, players, sampleSize):
    try:
        pool = [civ[0] for civ in civs.items() if civ[1]]
        res = {}

        for i in range(int(players)):
            sample = getRandomSample(pool, sampleSize)
            pool = [civ for civ in pool if civ not in sample]
            res[i + 1] = sample

        return res      
    except:
        return {}


def getRandomSample(pool, sampleSize):    
    return random.sample(pool, sampleSize)
