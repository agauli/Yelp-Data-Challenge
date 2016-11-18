#!/usr/bin/python
import sys
import csv

def print_dict(dict):
    count_str = '\t'
    a = ['', 'beer_and_wine','none', 'full_bar' ]
    for e in a:
        if e in dict:
            count_str = count_str + str(dict[e])
        else:
            count_str = count_str + '0'
        count_str = count_str + "\t"
    return count_str

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    prevCity = None
    f = None
    alchol_count = {}
    
    for line in reader:
        if(len(line) == 2):
            currentCity, alchol = line
        if prevCity and prevCity != currentCity:
            print prevCity, alchol_count.values()
            alchol_count = {}
        prevCity = currentCity
        if alchol in alchol_count:
                alchol_count[alchol] = alchol_count[alchol]  + 1
        else:
                alchol_count[alchol] = 1
    if prevCity != None:
        print prevCity, print_dict(alchol_count)
if __name__ == "__main__":
    reducer()


