# Experiment-Design
The original paper can be found [here](https://dl.acm.org/doi/10.1145/3523227.3546786) and the github-repository of the authers can be found [here](https://github.com/dilina-r/mcts-rec?tab=readme-ov-file).

The mcts code from the authors has been adjusted so that it supports seeding for the pseudo random generator and outputs results in a csv format for easier usage in python. The columns of the csv are the ground_truth followed by iters1 to iters25 corresponding to the number of items a user rated also from 1 to 25. A run.sh script has been added that runs all experiments for a given seed and a schedule.sh has been added that runs all experiments for all seeds.

Group sizes 4, 8 have been generated with 100 users per group. Results have been generated using this script and can be found in folders named according to the seeds (73308559, 83638859, 63381133, 61451749, 88666223, 45755797, 34521869, 93643757) with _100 at the end. All grousizes have been generated with 15 users per group which can be found in teh foders with _15 at the end. Additionally, the bigger datasets were also calculated with 100 users per group, but only for the seed 61451749 with the expetion of netflix32 where we ran out of memory. Theses files can also be found in the folder 61451749_100. Three datasets were also created with 1000 users per group. These results can be found in the folder users1000. Lastly, teh results for the decision tree and random forest can be found in the folder Results_dt_and_rf. Each result file is named according to the dataset and the groups size used.  Furthermore goodreads32 only contains 24 groups as the source files only contains 24 groups which is probably a small oversight by the authors.

The source of the experiments are the files in the data directory which have been kept from the original repository for the sake of reproducability of the authors results. The authors generated these files according to the following paragraph from the paper:
```
Clustering Users. We use training data to cluster users into groups
and estimate the mean μ(A,v) and variance σ(A,v) of the ratings
by each group A for item v. We use the BLC matrix-factorization
clustering algorithm [4] for this, although other clustering algorithms
might also be used. We vary the number of groups/clusters
from 4 to 32 and report results for each.
```
These means and sigmas are then used to model new users as multinormal distributions in the code of the authors. They note that they do not obeserve much difference to when they use the actual ratings. We did not verify this claim.
The following is from the original repository of the paper and should still work for installing the modified program:

# How to set up
Install GNU Scientific Library [(GDL)](https://www.gnu.org/software/gsl/)

# How to run
make ./bin/mcts -t <samples per group> -n <num recommendations>

# Decision tree and random forest
The R files called decision_tree and ransom_forest cotain the code for our implementation of the decision tree algorithm and our try for a random forest algorithm. As input data we used the test files that linked in the original [github-repository of the authors](https://github.com/dilina-r/mcts-rec?tab=readme-ov-file). The output format is the same as for the mcdt-implementation.

# Additional Code
The file PlotsAndCalcuations contains the code to recreate the plots and tables from the paper as well as some additional plots, calculations and statistical tests.
