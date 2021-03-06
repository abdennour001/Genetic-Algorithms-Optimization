# 1. Solution representation:

We are going to optimize the best outfit given a dress code, color pallet and budget. For that we will use Genetic Algorithm Optimization.

Our GA model is simple : each individual or chromosome is an Object of the ‘Outfit’ class, this class contains a piece of every category (TOP, BOTTOM, SHOES, NECK, HANDBAG) so each individual is encoded in a chromosome of the form : **< top piece, bottom piece, shoes piece, neck piece, handbag piece >** and our main goal to get the best outfit it means the best individual.

# 2. Fitness function:

We used a fitness function with three parameters; dress code, color pallet and the budget. Each of the dress code and the budget has the same importance and the color pallet is half important, so we are going to use the weights (w_0 = 0.4 **and w1 = 0.4 for dress code and budget and  w2 = 0.2 for the color pallet**). You can check that :

<p align='center'>
<img src="https://render.githubusercontent.com/render/math?math=\sum_{i=1}^{3} w_i = 1">
</p>

For each factor we present the functions (**dressCodeFitness, budgetFitness and colorPalletFitness**) that will return how much is good the dress code of this individual for example, it will return a value between 0 and 1, and the main Fitness function will return a value between 0 and 1 as well.

# 3. Genetic operators
## 3.1. Crossover
The crossover function, we will use special crossover function called ordered crossover where we select a random subset  of the first parent and fill the remainder with the genes from the second parent.

For example, if we take parent1 = <t-shirt, jeans, sneakers, tie, purse> and parent2 = <blouse, legging, mid heel, scarf, clutch>, we will randomly choose a gene from parent1 and the rest of genes form parent_2 and put it in the new offspring, if we choose the ‘top piece’ it will be offspring = <t-shirt, legging, mid heel, scarf, clutch>.
## 3.2. Mutation
The mutation function will help in exploring new solutions, we will replace a random piece in a random category.

For example, if we take offspring = <t-shirt, jeans, sneakers, tie, purse>, we will randomly choose a gene and replace it by a random piece, let’s choose the top piece ‘t-shirt’ and replace it by ‘blouse’ so the new offspring will be : <blouse, jeans, sneakers, tie, purse>.
## 3.3. Selection by roulette wheel selection
The selection function uses the roulette wheel selection method to select the parents, so the fittest individual has bigger chance of being selected.

<p align='center'>
<img src='https://www.tutorialspoint.com/genetic_algorithms/images/roulette_wheel_selection.jpg' alt='Roulette wheel selection.'/>
</p>

## 3.4. Replacement
As a replacement policy, we used the winner loser method where the parent whose got the lowest fitness is the loser and it will be replaced by the new child (offspring).
# 4. How it works
The main script Is **‘dress_up.py’** you can run it using the command line:

```$python dress_up.py [OPTIONS] <dress code> <color pallet> <budget>```

**OPTIONS:**.  
  
**-g GENERATIONS:** Number of generations.  
**-p POPULATION_LENGTH:** Population length.  
**-b:** Boost mode, to initialize an enhanced generation.  
**--error=ERROR:** Termination condition using error condition.  

**Examples:**
 
```$python dress_up.py -g 400 -p 10 --show-info casual bright 800.0```

```$python dress_up.py -g 400 -p 10 --show-info --error=0.0001 casual bright 800.0```

```$python dress_up.py -b -g 400 -p 10 --show-info --error=0.0001 casual bright 800.0```

# 5. Benchmark

**(Population: 10; Crossover: 0,6; Mutation: 0.4)**

<p align='center'>
<img src='https://i.ibb.co/BK4kN0c/g1.png' alt='G1.'/>
</p>

**(Population: 10; Crossover: 0,8; Mutation: 0.3)**

<p align='center'>
<img src='https://i.ibb.co/dPjcQzq/g2.png' alt='G2.'/>
</p>

**(Population: 10; Crossover: 0,6; Mutation: 0.2)**

<p align='center'>
<img src='https://i.ibb.co/KbX3Tf3/g3.png' alt='G3.'/>
</p>
