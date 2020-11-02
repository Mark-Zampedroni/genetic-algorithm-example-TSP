<h1 align="center"><b>Example of Genetic Algorithm application to TSP</b></h1>

The idea is to provide an easy, short and non-optimized example of an approximed solution to the [TSP](https://en.wikipedia.org/wiki/Travelling_salesman_problem) through a [Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm). 
By no means the aim was to write a well performing algorithm, it's only intended as an example of GAs (from students for students) to give an hint of their usefulness in solving NP-hard problems. 

The script works both on python 2.7 and 3. The only dependency is turtle, used for the graphical methods and easily installable through pip.

## Model
An acceptable solution is an [Hamiltonian path](https://en.wikipedia.org/wiki/Hamiltonian_path) that cycles on the N nodes. Using the [permutation encoding](https://www.obitko.com/tutorials/genetic-algorithms/encoding.php) paradigm it's representable as an array of length N containing at every i-th position (from 1 to N) the label of the node to visit at the step i. One array is regarded as an individual in the GAs context.

The algorithm starts with a population of ```N_POPULATION``` inviduals, each individual is of length ```N_CITIES``` and generated randomly (abiding to the rules of Hamiltonian paths). 

- The fitness function uses the total length of the path to score the quality of each individual.
- Selection occurs through a [tournament](https://en.wikipedia.org/wiki/Tournament_selection) of size ```K_TOURNAMENT``` and uniform probability.
- Crossover is a [single point crossover](https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)) and takes place between the ```P_ELITISM * N_POPULATION``` of best fit individuals .
- Mutation is a [bit string mutation](https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm)) that swaps two values in the array.


## Examples
The following two examples are both results (with a different seed) of the provided [TSP_GA_example.py](https://github.com/Mark-Zampedroni/genetic-algorithm-example-TSP/blob/main/TSP_GA_example.py) script. All the parameters are freely modifiable, different values will result in better/worse solutions. The disposition of the points (vertices, cities) can swap between circular and random changing the constant ```IS_CIRCLE```.

### E.g 1, Circular disposition
The nodes are placed in circle to highlight the improvements of each generation, it's visibly obvious that the best possible Hamiltonian path is the one that draws the circle itself and in this example, using a circle radius of 200p, the global optimum length (the circumference) is 1256p. 

Each image shows the best individual of its generation:

<p align="center" width="100%">
    <img width="40%" src="https://github.com/Mark-Zampedroni/genetic-algorithm-example-TSP/blob/main/images/cricle/GC1p.png"> 
    <img width="40%" src="https://github.com/Mark-Zampedroni/genetic-algorithm-example-TSP/blob/main/images/cricle/GC1p.png"> 
</p>
<p align="center" width="100%">
    <img width="40%" src="https://github.com/Mark-Zampedroni/genetic-algorithm-example-TSP/blob/main/images/cricle/GC1p.png"> 
    <img width="40%" src="https://github.com/Mark-Zampedroni/genetic-algorithm-example-TSP/blob/main/images/cricle/GC1p.png"> 
</p>

### E.g 2, Random disposition
x
