# Experiment-Design
The code has been adjusted so that it supports seeding for the pseudo random generator and outputs results in a csv format for easier usage in python. The columns of the csv are the ground_truth followed by iters1 to iters25 corresponding to the number of items a user rated also from 1 to 25. A run.sh script has been added that runs all experiments for a given seed and a schedule.sh has been added that runs all experiments for all seeds.

Eight results have been generated using this script and can be found in folders named according to the seeds (73308559, 83638859, 63381133, 61451749, 88666223, 45755797, 34521869, 93643757) used for generation. Each result file is named according to the dataset and the groups size used. Group sizes 4, 8, 16 and 32 have been generated with the exception of netflix16 and netflix32 which failed due to an out of memory exception. Furthermore goodreads32 only contains 24 groups as the source files only contains 24 groups which is probably a small oversight by the authors.

The source of the experiments are the files in the data directory which have been kept from the original repository for the sake of reproducability of the authors results (we probably should check though that we can reach similar data from the original datasets). The authors generated these files according to the following paragraph from the paper:

Clustering Users. We use training data to cluster users into groups 
and estimate the mean µ(д,v) and variance σ(д,v) 2 of the ratings
by each group д for item v. We use the BLC matrix-factorization
clustering algorithm [4] for this, although other clustering algorithms 
might also be used. We vary the number of groups/clusters
from 4 to 32 and report results for each.
These means and sigmas are then used to model new users as multinormal distributions in the code of the authors as they note that they do not obeserve much difference to the actual user ratings. I am going to verify their claim (by adding new functionality to the code that can work with actual user ratings) but in order to follow their method the results are now generated using users drawn from the multinormal.

The following is from the original repository of the paper and should still work for installing the modified program:

mcts-rec
Introduction
The C++ implementation for the publication "Fast And Accurate User Cold-Start Learning Using Monte Carlo Tree Search". The paper can be found here.

How to set up
Install GNU Scientific Library (GSL).

Installing gsl in macOS

brew install gsl
Preprocessed Data
The item distribution data (mean and variance) of the clusters for each dataset can be found here.

The test data can be found here.

How to run
make
./bin/mcts -t <samples per group> -n <num recommendations>
