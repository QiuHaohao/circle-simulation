import click
from copy import deepcopy
import math
import random
import pandas as pd

from Arc import Arc
from constants import *
		
def randomRad():
	return 2 * PI * random.random()

def shiftLeft(l):
	lCopy = deepcopy(l)
	lCopy.append(lCopy.pop(0))
	return lCopy

def generatePoints(n_points):
	points = [randomRad() for _ in range(n_points)]
	points.sort()
	return points

def getPointPairs(points):
	return list(zip(points, shiftLeft(points)))

def play(target, n_points):
	points = generatePoints(n_points)
	pointPairs = getPointPairs(points)
	arcs = map(lambda x : Arc(*x),
					pointPairs)
	targetArc = list(filter(lambda x: x.include(target),
					arcs))
	assert len(targetArc) == 1
	return targetArc[0].length()

@click.command()
@click.argument('n_times', type=click.INT, default=10000000)
@click.argument('n_points', type=click.INT, default=3)
def main(n_times, n_points):
	results = [play(POINT_TARGET, n_points) for _ in range(n_times)]
	print(pd.Series(results).describe(percentiles=[.1,.2,.3,.4,.5,.6,.7,.8,.9]))

if __name__ == "__main__":
	main()