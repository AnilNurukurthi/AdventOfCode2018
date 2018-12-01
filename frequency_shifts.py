from functools import reduce

frequencies_file = open('data\input1.txt', 'r')

def getFinalFrequency():
    print(reduce(lambda x, y : x + y, map(lambda x: int(x), frequencies_file.readlines())))


# Needs to be more efficient
def getFirstRepeatedFrequency():
    freq_dict = {0: 1}
    cum_freq = 0
    frequencies = list(map(lambda x: int(x), frequencies_file.readlines()))
    findx = 0
    while True:
        cum_freq += frequencies[findx % len(frequencies)]
        if (cum_freq in freq_dict):
            print(cum_freq)
            break
        else:
            freq_dict[cum_freq] = 1
        findx = findx + 1

getFirstRepeatedFrequency()
