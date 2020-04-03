#!/usr/bin/env python

###
"""
dress_up.py

A Genetic Algorithm optimization implementation
to get the best outfit of 5 categories given a dress code,
a color pallet and a budget.

Invocation: "python dress_up.py --options dresscode color budget"

"""
###

import numpy as np # import the numpy library to make life easier with arrays 
import gatools as ga_ # outfit is our individual or chromosome.
import random
from matplotlib import pyplot as plt
from sys import argv # to access the command line arguments
import optparse


USAGE_MSG = \
"A script that performe a genetic algorithm optimization to get"\
"the best outfit of 5 categories (TOP, BOTTOM, SHOES,"\
"NECK and HANDBAG) given a dress code, a color pallet and a budget.\n\n"\
"%prog [OPTIONS] DRESSCODE COLOR BUDGET\n\n"\
"Example:\n"\
"%prog [OPTIONS] evening dark 500.0\n"

BOOST_MSG               = "Boost mode, use the boost mode to create an enhanced initial population"\
                            ", Default to False."
GENERATIONS_MSG         = "Number of generations in the GA, Default to 500 generation."
TERMINATION_COND_MSG    = "Termination condition, Default after the %generations number of generations."
POPULATION_MSG          = "Population length, Default 30 individual."

class GeneticAlgorithm:
    """
    This a class of genetic algorithm, it contains all data and necessary operations.

    Attributes: 
        popSize (int): The size of our population.
        eliteSize (int): The size of the elite group for genetic operations (mutations and crossover).
        crossoverRate (float): The chance of crossover operation between 0 and 1.
        mutationRate (float): The chance to make a mutation between 0 and 1.
        generations (int): The number of generations on our algorithm.

    """
    def __init__( 
        self, 
        popSize, 
        eliteSize, 
        crossoverRate=0.5, 
        mutationRate=0.01, 
        generations=50, 
        dressCode=None, 
        color=None, 
        budget=None,
        boost=False,
        error=None,
        show=False
        ):
        """
        The constructor for GeneticAlgorithm class. 
  
        Parameters: 
            popSize (int): The size of our population.
            eliteSize (int): The size of the elite group for genetic operations (mutations and crossover).
            crossoverRate (float): The chance of crossover operation between 0 and 1.
            mutationRate (float): The chance to make a mutation between 0 and 1.
            generations (int): The number of generations on our algorithm.
            currentGeneration (numpy.ndarray): The current generation on the algorithm.

        """
        self.popSize                    = popSize
        self.eliteSize                  = eliteSize
        self.crossoverRate              = crossoverRate
        self.mutationRate               = mutationRate
        self.generations                = generations
        self.currentGeneration          = np.array([])
        self.currentGenerationSorted    = np.array([])
        self.boost                      = boost
        self.error                      = error
        self.progress                   = []
        self.show                       = show

        # user input
        self.dressCode          = dressCode
        self.color              = color
        self.budget             = budget

    def random_top_piece(self):
        _ = 0
        top = random.sample(ga_.DataTable.top_dict.keys(), 1)[0]
        while self.boost and ((_ < 50) and ((self.dressCode not in ga_.DataTable.data[ga_.Category.TOP][top]['dress-code']) or (self.color not in ga_.DataTable.data[ga_.Category.TOP][top]['color']))):
            _ += 1
            top = random.sample(ga_.DataTable.top_dict.keys(), 1)[0]
        return top

    def random_bottom_piece(self):
        _ = 0
        bottom = random.sample(ga_.DataTable.bottom_dict.keys(), 1)[0]
        while self.boost and ((_ < 50) and ((self.dressCode not in ga_.DataTable.data[ga_.Category.BOTTOM][bottom]['dress-code']) or (self.color not in ga_.DataTable.data[ga_.Category.BOTTOM][bottom]['color']))):
            _ += 1
            bottom = random.sample(ga_.DataTable.bottom_dict.keys(), 1)[0]
        return bottom

    def random_shoes_piece(self):
        _ = 0
        shoes = random.sample(ga_.DataTable.shoes_dict.keys(), 1)[0]
        while self.boost and ((_ < 50) and ((self.dressCode not in ga_.DataTable.data[ga_.Category.SHOES][shoes]['dress-code']) or (self.color not in ga_.DataTable.data[ga_.Category.SHOES][shoes]['color']))):
            _ += 1
            shoes = random.sample(ga_.DataTable.shoes_dict.keys(), 1)[0]
        return shoes

    def random_neck_piece(self):
        _ = 0
        neck = random.sample(ga_.DataTable.neck_dict.keys(), 1)[0]
        while self.boost and ((_ < 50) and ((self.dressCode not in ga_.DataTable.data[ga_.Category.NECK][neck]['dress-code']) or (self.color not in ga_.DataTable.data[ga_.Category.NECK][neck]['color']))):
            _ += 1
            neck = random.sample(ga_.DataTable.neck_dict.keys(), 1)[0]
        return neck

    def random_handbag_piece(self):
        _ = 0
        handbag = random.sample(ga_.DataTable.handbag_dict.keys(), 1)[0]
        while self.boost and ((_ < 50) and ((self.dressCode not in ga_.DataTable.data[ga_.Category.HANDBAG][handbag]['dress-code']) or (self.color not in ga_.DataTable.data[ga_.Category.HANDBAG][handbag]['color']))):
            _ += 1
            handbag = random.sample(ga_.DataTable.handbag_dict.keys(), 1)[0]
        return handbag

    def initializeGeneration(self):

        for i in range(0, self.popSize):
            top     = self.random_top_piece()
            #print(top)
            bottom  = self.random_bottom_piece()
            #print(bottom)
            shoes   = self.random_shoes_piece()
            #print(shoes)
            neck    = self.random_neck_piece()
            #print(neck)
            handbag = self.random_handbag_piece()
            #print(handbag)

            individual = ga_.Outfit( top = top, bottom = bottom, shoes = shoes, neck = neck, handbag = handbag)
            self.currentGeneration = np.append(self.currentGeneration, individual)

    
    def applyFitness(self, outfit):
        return outfit.fitness(self.dressCode, self.color, self.budget)


    def sortByFitness(self):
        self.currentGenerationSorted = sorted(self.currentGeneration, key=self.applyFitness, reverse=True)

    
    def selection(self):
        """
        The selection function use the roulette wheel selection method to select the parents.

        Results:
            selectionResult (array): The selection results.

        """

        # sort the generation according to fitness.
        self.sortByFitness()
        # get the fitness sum.
        fitnessSum = 0
        for outfit in self.currentGeneration:
            fitnessSum += self.applyFitness(outfit)
        # generate a random number
        stop = random.uniform(0, 1)
        accumulated = 0
        offset = 0
        for outfit in self.currentGenerationSorted:
            fitness = self.applyFitness(outfit) + offset
            probability = fitness / fitnessSum
            accumulated += probability

            if stop <= accumulated:
                return outfit
        

    def crossover(self, parents):
        """
        The crossover function, we will use special crossover function called ordered crossover where we select a random subset
        of the first parent and fill the remainder with the genes from the second parent.

        Parameters:
            parents (arrat): cintains the parents.

        Returns:
            offspring (Outfit): The offspring result of the crossover.  

        """

        randomCategory = random.sample(list(ga_.Category), 1)[0]
        randomParent1 = random.sample(parents, 1)[0]
        randomParent2 = None
        for parent in parents:
            if parent != randomParent1:
                randomParent2 = parent
    

        # put randomCategory from random parent to the new offpring and the remainder from the second parent
        offspring = ga_.Outfit()
        if randomCategory == ga_.Category.TOP:
            offspring.top = randomParent1.top
            offspring.bottom = randomParent2.bottom
            offspring.shoes = randomParent2.shoes
            offspring.neck = randomParent2.neck
            offspring.handbag = randomParent2.handbag
        elif randomCategory == ga_.Category.BOTTOM:
            offspring.top = randomParent2.top
            offspring.bottom = randomParent1.bottom
            offspring.shoes = randomParent2.shoes
            offspring.neck = randomParent2.neck
            offspring.handbag = randomParent2.handbag
        elif randomCategory == ga_.Category.SHOES:
            offspring.top = randomParent2.top
            offspring.bottom = randomParent2.bottom
            offspring.shoes = randomParent1.shoes
            offspring.neck = randomParent2.neck
            offspring.handbag = randomParent2.handbag
        elif randomCategory == ga_.Category.NECK:
            offspring.top = randomParent2.top
            offspring.bottom = randomParent2.bottom
            offspring.shoes = randomParent2.shoes
            offspring.neck = randomParent1.neck
            offspring.handbag = randomParent2.handbag
        elif randomCategory == ga_.Category.HANDBAG:
            offspring.top = randomParent2.top
            offspring.bottom = randomParent2.bottom
            offspring.shoes = randomParent2.shoes
            offspring.neck = randomParent2.neck
            offspring.handbag = randomParent1.handbag

        return offspring


    
    def mutation(self, offspring):
        """
        The mutation function will help in exploring new solutions, we will replace a random piece in a random category.

        Parameters:
            offspring (Outfit): The old offspring.

        Returns 
            newoffspring (Outfit): The new offspring after the mutation.

        """
        newoffspring = offspring
        randomCategory = random.sample(list(ga_.Category), 1)[0]
        randomPiece = random.sample(list(ga_.DataTable.data[randomCategory]), 1)[0]

        if randomCategory == ga_.Category.TOP:
            newoffspring.top = randomPiece
        elif randomCategory == ga_.Category.BOTTOM:
            newoffspring.bottom = randomPiece
        elif randomCategory == ga_.Category.SHOES:
            newoffspring.shoes = randomPiece
        elif randomCategory == ga_.Category.NECK:
            newoffspring.neck = randomPiece
        elif randomCategory == ga_.Category.HANDBAG:
            newoffspring.handbag = randomPiece
        
        return newoffspring


    def replaceLoser(self, parents, newoffspring):
        """
        This function to replace the loser parent in the population by the new offspring, the loser individual is the individual is the one with lower fitness

        Parameters:
            parents (array): The parents, one of them will be remplaced in the population.
            newoffspring (Outfit): The new offspring that will be included in the population.
        """ 

        loser = min(parents, key=self.applyFitness)

        for index, individual in enumerate(self.currentGeneration):
            if (individual == loser):
                self.currentGeneration[index] = newoffspring
    
    def nextGeneration(self):
        """
        The function to get the next generation of our algorithm, this is the main function of the genetic algorithm.

        """
        # select two parents from the current generation.
        parent_1 = self.selection()
        parent_2 = self.selection()
        # to not get the same parents.
        _ = 0
        while _ < 30 and parent_2 == parent_1:
            parent_2 = self.selection()
            _ += 1
        # apply crossover on those parents (crossover_rate chance).
        crossover_chance = random.uniform(0, 1)
        parents = [parent_1, parent_2]
        if crossover_chance <= self.crossoverRate:
            offspring = self.crossover(parents)
        else:
            return 
        # apply mutations on the new offspring (mutation_rate chance).
        mutation_chance = random.uniform(0, 1)
        newoffspring = offspring
        if mutation_chance <= self.mutationRate:
            newoffspring = self.mutation(offspring)
        # replace one of the parents in the new generation, given the loser parent.
        self.replaceLoser(parents, newoffspring)

        # now the new generation is available in the self.currentGeneration
        

    def start(self):
        # Intitialize population. 
        print("[1] Initialize population.", end="\n\n")
        self.initializeGeneration()
        # sort the generation according to fitness.
        self.sortByFitness()

        print("[2] Starting genetic operations...", end="\n\n")
        # Apply the main function of the genetic algorithm 'generations' times.
        for _ in range(0, self.generations+1):
            if _ % 100 == 0 :
                self.progress.append(self.applyFitness(self.currentGenerationSorted[0]))
                if self.error :
                    if _ != 0 and self.progress[-1] - self.progress[-2] < self.error:
                        return
            if self.show:
                generation_fitness = np.array([self.applyFitness(ind) for ind in self.currentGeneration])
                print("[*] Generation #{}, Best fitness : {}, Average fitness : {}".format(_ + 1, self.progress[-1], np.mean(generation_fitness)), end="\n\n")
            self.nextGeneration()
        print("\n___________________\n")
        print("\n[3] Average fitness is: %f" % np.mean(self.progress))
        print("\n___________________\n")


    def showBestOutfit(self, number):
        print("\n\n[*] Best first %d Outfits are:" % (number))
        for index, outfit in enumerate(self.currentGenerationSorted):
            print( "\n\t{%d} %s\n" % (index, outfit) )
            if index == number-1:
                break

    def plotPerformance(self):
        print("[-] Plot the results.", end="\n\n")
        plt.plot([x for x in range(0, len(self.progress)*100, 100)], self.progress, marker='o', color='b', markevery=1)
        plt.ylabel('Fitness')
        plt.xlabel('Generation')
        plt.title('GA Performance')
        plt.grid(axis='both', alpha=.3)
        plt.show()


def runGA(dressCode, color, budget, poplength, generations, boost, error, show, best):
    """
    The function to run the genetic algorithm process.

    Parameters:
        dressCode (DressCode): The dress code.
        color (Color): The color pallet.
        budget (float): The budget.

    """

    print("[-] Running genetic algorithm...", end="\n\n")
    ga = GeneticAlgorithm( 
        popSize=poplength, 
        eliteSize=2,
        crossoverRate=0.9, 
        mutationRate=0.2, 
        generations=generations, 
        dressCode=dressCode, 
        color=color, 
        budget=budget,
        boost=boost,
        error=error,
        show=show,
        )
    # start the genetic algorithm 
    ga.start()
    if (best != -1):
        ga.showBestOutfit(best)
    ga.plotPerformance()


if __name__ == '__main__':
    print(end="\n")
    # run solution
    parser = optparse.OptionParser(usage=USAGE_MSG)
    parser.add_option('-b', dest='boost', action="store_true",
                                default=False, help=BOOST_MSG)
    parser.add_option('-g', metavar='GENERATIONS', dest='generations',
                                default=500, help=GENERATIONS_MSG)
    parser.add_option('-p', metavar='POPULATION', dest='population',
                                default=10, help=POPULATION_MSG)
    parser.add_option('--error', metavar='ERROR', dest='error',
                                default=0.0, help=TERMINATION_COND_MSG)
    parser.add_option('-i', '--show-info', dest='show', action='store_true',
                                default=False, help="Show generations growth.")
    parser.add_option("--best-outfit", metavar='BEST', dest="best",
                                default=-1, help="Give the number of best Outfits to show in the end.")


    opts, args = parser.parse_args()
    if len(args) < 3:
        parser.print_help()
        exit(0)

    runGA(ga_.DressCode[args[0].upper()], ga_.Color[args[1].upper()], float(args[2]), poplength=int(opts.population), 
                        generations=int(opts.generations), boost=opts.boost, error=float(opts.error), show=opts.show,
                        best=int(opts.best))