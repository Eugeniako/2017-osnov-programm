import sys
import re

def getNounMorphology(word):
    dict = {}
    getDict = open(sys.argv[1], 'r')
    for line in getDict:
        line = line.replace('\n','')
        line_split = line.split('\t')
        if line_split[0] not in dict:
            dict[line_split[0]] = [line_split[1] + ' ' + line_split[2] + ' ' + line_split[3] + ' ' + line_split[4]]
        else:
            dict[line_split[0]].append(line_split[1] + ' ' + line_split[2] + ' ' + line_split[3] + ' ' + line_split[4])
    for ending in dict:
        if ending != '-':
            if word[-1*len(ending):len(word)] == ending:
                result = dict[ending]
        if ending == '-':
            result = dict[ending]
    #return(result)
    phrase_res = 'The word can have the following forms:\n'
    for var in result:
        phrase_res = phrase_res + '\n' + var + ';'
    return(phrase_res)
if re.search('[,-;!?:$@%&0-9]', sys.argv[2]):
    print('Please, input the word in the correct form')
else:
    print(getNounMorphology(sys.argv[2]))
