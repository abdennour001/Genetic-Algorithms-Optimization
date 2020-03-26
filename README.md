# 1. Solution representation:

We are going to optimize the best outfit given a dress code, color pallet and budget. For that we will use Genetic Algorithm Optimization.

Our GA model is simple : each individual or chromosome is an Object of the ‘Outfit’ class, this class contains a piece of every category (TOP, BOTTOM, SHOES, NECK, HANDBAG) so each individual is encoded in a chromosome of the form : **<top piece, bottom piece, shoes piece, neck piece, handbag piece>** and our main goal to get the best outfit it means the best individual.

# 2. Fitness function:

We used a fitness function with three parameters; dress code, color pallet and the budget. Each of the dress code and the budget has the same importance and the color pallet is half important, so we are going to use the weights (<img src="/tex/16d35dd9410373596bca580f64c4ffb5.svg?invert_in_darkmode&sanitize=true" align=middle width=62.06524169999999pt height=21.18721440000001pt/> **and <img src="/tex/8dd63897c011cc22bba4c567ac2f9072.svg?invert_in_darkmode&sanitize=true" align=middle width=62.06524169999999pt height=21.18721440000001pt/> for dress code and budget and  <img src="/tex/aa6faedaff79216675c5e795ae43296d.svg?invert_in_darkmode&sanitize=true" align=middle width=62.06524169999999pt height=21.18721440000001pt/> for the color pallet**). You can check that :

<p align="center"><img src="/tex/e6bc4cc4d341787109596a4f2b4fefd5.svg?invert_in_darkmode&sanitize=true" align=middle width=73.86214439999999pt height=47.35857885pt/></p>

For each factor we present the functions (** dressCodeFitness, budgetFitness and colorPalletFitness**) that will return how much is good the dree code of this individual for example, it will return a value between 0 and 1, and the main Fitness function will return a value between 0 and 1 as well.

# 3. Genetic operators
## 3.1. Crossover
The crossover function, we will use special crossover function called ordered crossover where we select a random subset  of the first parent and fill the remainder with the genes from the second parent.

For example, if we take <img src="/tex/5e71d8dae1afc49e37473fba6897d9b6.svg?invert_in_darkmode&sanitize=true" align=middle width=54.84233369999998pt height=20.221802699999984pt/> = <<img src="/tex/4f4f4e395762a3af4575de74c019ebb5.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>-<img src="/tex/74ba26e40b7b9095ba230347ed0c04e6.svg?invert_in_darkmode&sanitize=true" align=middle width=233.88892724999994pt height=22.831056599999986pt/>> and <img src="/tex/8fa20eacee8aee8c136f956a5ed5532f.svg?invert_in_darkmode&sanitize=true" align=middle width=54.84233369999998pt height=20.221802699999984pt/> = <<img src="/tex/1860e51f5f3ac2d32338c8ccbad203ea.svg?invert_in_darkmode&sanitize=true" align=middle width=271.16729805pt height=22.831056599999986pt/>>, we will randomly choose a gene from <img src="/tex/5e71d8dae1afc49e37473fba6897d9b6.svg?invert_in_darkmode&sanitize=true" align=middle width=54.84233369999998pt height=20.221802699999984pt/> and the rest of genes form <img src="/tex/8fa20eacee8aee8c136f956a5ed5532f.svg?invert_in_darkmode&sanitize=true" align=middle width=54.84233369999998pt height=20.221802699999984pt/> and put it in the new offspring, if we choose the ‘top piece’ it will be <img src="/tex/8282f2bd72038b75f559a71856398670.svg?invert_in_darkmode&sanitize=true" align=middle width=75.41235734999998pt height=22.831056599999986pt/> = <<img src="/tex/4f4f4e395762a3af4575de74c019ebb5.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>-<img src="/tex/19d12538749e5c6367cc120946f72020.svg?invert_in_darkmode&sanitize=true" align=middle width=262.79508914999997pt height=22.831056599999986pt/>>.
## 3.2. Mutation
The mutation function will help in exploring new solutions, we will replace a random piece in a random category.

For example, if we take <img src="/tex/8282f2bd72038b75f559a71856398670.svg?invert_in_darkmode&sanitize=true" align=middle width=75.41235734999998pt height=22.831056599999986pt/> = <<img src="/tex/4f4f4e395762a3af4575de74c019ebb5.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>-<img src="/tex/74ba26e40b7b9095ba230347ed0c04e6.svg?invert_in_darkmode&sanitize=true" align=middle width=233.88892724999994pt height=22.831056599999986pt/>>, we will randomly choose a gene and replace it by a random piece, let’s choose the top piece ‘<img src="/tex/4f4f4e395762a3af4575de74c019ebb5.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>-<img src="/tex/2f9cd00cf1146d98b600409e805afe41.svg?invert_in_darkmode&sanitize=true" align=middle width=36.64887269999999pt height=22.831056599999986pt/>’ and replace it by ‘<img src="/tex/286c3abe7428eb634978aea745da5d62.svg?invert_in_darkmode&sanitize=true" align=middle width=45.02108159999999pt height=22.831056599999986pt/>’ so the new offspring will be : <<img src="/tex/5a7755913533467b7ddc5d960f8616f2.svg?invert_in_darkmode&sanitize=true" align=middle width=242.26113614999997pt height=22.831056599999986pt/>>.
## 3.3. Selection by roulette wheel selection
The selection function uses the roulette wheel selection method to select the parents, so the fittest individual has bigger chance of being selected.

<p align='center'>
<img src='https://www.tutorialspoint.com/genetic_algorithms/images/roulette_wheel_selection.jpg' alt='Roulette wheel selection.'/>
</p>

## 3.4. Replacement
# 4. Analysis of results
