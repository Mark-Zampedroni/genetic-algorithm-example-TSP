#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle
import math
import time
import random

# Number of cities
N_CITIES = 100
# Population size
N_POPULATION = 300
# Probability of crossover
P_CROSSOVER = 0.95
# Probability of mutation
P_MUTATION = 0.05
# Probability of elitism
P_ELITISM = 0.05
# Partecipants to each tournament
K_TOURNAMENT = 3

# Max number of generations before stopping
MAX_GENERATIONS = 10000
# Number of populations between updating graphically the best solution 
REFRESH_FREQUENCY = 10

# If True the points will be generated in circle, if False randomly
IS_CIRCLE = True

CHROMOSOME = 0

def getRandomPoints(pointsNum):
    points = []
    for i in range(pointsNum):
        while(True):
            x = random.randrange(-500, 500)
            y = random.randrange(-150, 300)
            if ([x,y] not in points):
                break
        points.append([x,y])
    return points


def getCirclePoints(pointsNum,r):
    points = []
    for i in range(pointsNum):
        points.append([r*math.cos((i*2*math.pi)/pointsNum),r*math.sin((i*2*math.pi)/pointsNum)])
    return points

def drawCircle(pen,r): 
    pen.fillcolor('red')  
    pen.begin_fill() 
    pen.circle(r) 
    pen.end_fill() 

def drawPoints(pen,points):
    for r in points:
        pen.up()
        pen.goto(r[0],r[1])
        pen.down()
        drawCircle(t,3)

def connectPoints(pen,this,that):
    pen.up()
    pen.goto(this[0],this[1])
    pen.down()
    pen.goto(that[0],that[1])

def displayRoute(pen,route):
    pen.clear()
    drawPoints(pen,route)
    for i in range(0,len(route)-1):
        connectPoints(pen,route[i],route[i+1])
    connectPoints(pen,route[-1],route[0])

def showScore(pen,route):
    pen.up()
    pen.goto(-90,-250)
    pen.down()
    pen.write("Path length: "+str(int(getFitness(route))), font=("Arial", 16, "normal"))

def crossOver(father,mother):
    return

def mutate(this):
    if(random.random() < P_MUTATION):
        g1 = random.randrange(0,len(this)-1)
        g2 = random.randrange(0,len(this)-1)
        v1 = this[g1]
        this[g1] = this[g2]
        this[g2] = v1

# Total length of the path
def getFitness(this): 
    length = 0
    for i in range(0,len(this)-1):
        length += math.sqrt((this[i+1][0] - this[i][0])**2 + (this[i+1][1] - this[i][1])**2)
    return length

def getPopulationFitness(population):
    scores = []
    for p in population:
        scores.append((p,getFitness(p)))
    return sorted(scores, key=lambda l: l[1])

def splitPopulationFitness(population_fit):
    population = []
    fitness = []
    for i in population_fit:
        population.append(i[0])
        fitness.append(i[1])
    return population, fitness

def getElitism(population, prob):
    # it returns best chromosome in the population by %
    return population[:int(N_POPULATION * prob)]

def tournamentSelection(prev_gen_fit):
    next_gen = []
    prev_gen, prev_fit = splitPopulationFitness(prev_gen_fit)
    
    # elitism call
    for e in getElitism(prev_gen, P_ELITISM):
        next_gen.append(e)

    # tournament
    while (len(next_gen) < len(prev_gen_fit)):
        # probabilistic choices
        f1 = min(random.choices(prev_gen_fit, k = K_TOURNAMENT), key = lambda i : i[1])[CHROMOSOME]
        f2 = min(random.choices(prev_gen_fit, k = K_TOURNAMENT), key = lambda i : i[1])[CHROMOSOME]
        
        # crossover        
        p = crossOver(f1, f2)

        # mutation
        mutate(p[0])
        mutate(p[1])

        # new offsprings
        next_gen.append(p[0])
        next_gen.append(p[1])
    
    # worst chromosome deleted if population is odd
    while (len(next_gen) != len(prev_gen)):
        next_gen_fit = getPopulationFitness(next_gen)
        next_gen.remove(next_gen_fit[len(next_gen_fit) - 1][CHROMOSOME])

    return next_gen

def getNextGeneration(population):
    bestPreviousOnes = getPopulationFitness(population)
    children = tournamentSelection(bestPreviousOnes)

    return children, bestPreviousOnes[0][0]

def getNewPopulation(cities):
    if not IS_CIRCLE:
        p = getRandomPoints(cities)
    else:
        p = getCirclePoints(cities,200)
    population = []
    # First generation
    for x in range(0,N_POPULATION):
        random.shuffle(p) 
        newRoute = p[:] 
        population.append(newRoute)
    return population
 
#Turtle init
turtle.Screen().setup(width=1200, height=800, startx=740, starty=40)
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.tracer(0, 0)

population = getNewPopulation(N_CITIES)

for i in range(0,MAX_GENERATIONS):
    population, bestPreviousOne = getNextGeneration(population)
    if(i%REFRESH_FREQUENCY == 0):
        displayRoute(t,bestPreviousOne)
        showScore(t,bestPreviousOne)
        print("Population n. " + str(i))
        time.sleep(0.1)
    turtle.update()

turtle.done()


        
    

