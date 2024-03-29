#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

#---------------------------------------------------------------------------------------------

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib
    
    def find(city):
        if parent[city] != city:
            parent[city] = find(parent[city])
        return parent[city]
    
    def union(city1, city2):
        root1, root2 = find(city1), find(city2)
        if root1 != root2:
            parent[root1] = root2
    
    parent = list(range(n+1))
    
    for city1, city2 in cities:
        union(city1, city2)
        
    components = sum([1 for i in range(1, n+1) if parent[i] == i])
    road_req = n - components
    
    return components * c_lib + road_req * c_road
  
#---------------------------------------------------------------------------------------------        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
