# 1. Solution representation:

We are going to optimize the best outfit given a dress code, color pallet and budget. For that we will use Genetic Algorithm Optimization.

Our GA model is simple : each individual or chromosome is an Object of the ‘Outfit’ class, this class contains a piece of every category (TOP, BOTTOM, SHOES, NECK, HANDBAG) so each individual is encoded in a chromosome of the form : **<top piece, bottom piece, shoes piece, neck piece, handbag piece>** and our main goal to get the best outfit it means the best individual.

# 2. Fitness function:

We used a fitness function with three parameters; dress code, color pallet and the budget. Each of the dress code and the budget has the same importance and the color pallet is half important, so we are going to use the weights ($w_0 = 0.4$ **and $w_1 = 0.4$ for dress code and budget and  $w_2 = 0.2$ for the color pallet**). You can check that :

$$\sum_{i=1}^{3} w_i = 1$$

For each factor we present the functions (** dressCodeFitness, budgetFitness and colorPalletFitness**) that will return how much is good the dree code of this individual for example, it will return a value between 0 and 1, and the main Fitness function will return a value between 0 and 1 as well.

# 3. Genetic operators
## 3.1. Crossover
The crossover function, we will use special crossover function called ordered crossover where we select a random subset  of the first parent and fill the remainder with the genes from the second parent.

For example, if we take $parent_1$ = <$t$-$shirt, jeans, sneakers, tie, purse$> and $parent_2$ = <$blouse, legging, mid heel, scarf, clutch$>, we will randomly choose a gene from $parent_1$ and the rest of genes form $parent_2$ and put it in the new offspring, if we choose the ‘top piece’ it will be $offspring$ = <$t$-$shirt, legging, mid heel, scarf, clutch$>.
## 3.2. Mutation
The mutation function will help in exploring new solutions, we will replace a random piece in a random category.

For example, if we take $offspring$ = <$t$-$shirt, jeans, sneakers, tie, purse$>, we will randomly choose a gene and replace it by a random piece, let’s choose the top piece ‘$t$-$shirt$’ and replace it by ‘$blouse$’ so the new offspring will be : <$blouse, jeans, sneakers, tie, purse$>.
## 3.3. Selection by roulette wheel selection
The selection function uses the roulette wheel selection method to select the parents, so the fittest individual has bigger chance of being selected.

<p align='center'>
<img src='https://www.tutorialspoint.com/genetic_algorithms/images/roulette_wheel_selection.jpg' alt='Roulette wheel selection.'/>
</p>

## 3.4. Replacement
# 4. Analysis of results
