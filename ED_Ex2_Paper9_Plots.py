import os
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import numpy as np
import matplotlib.pyplot as plt


def figure1(dataset, path = None, name = None):
    accuracy = []
    for group in range(0, len(dataset['ground_truth'].unique())):
        gr = dataset[dataset['ground_truth'] == group]
        nr_total = gr.shape[0]
        nr_true = ((gr.iloc[:, -1:]) == group).sum()
        accuracy.append((nr_true / nr_total).values[0])
    #print(accuracy)
    groups = range(len(accuracy))
    groups = [x + 1 for x in groups]
    plt.bar(groups, accuracy)
    plt.xlabel('Group')
    plt.ylabel('Accuracy')
    plt.title('Accuracy by Group')
    if path is not None:
        plt.savefig(f"{path}/figure1_{name}.png")
    else:
        plt.show()
    plt.close()

def figure2(dataset, group, path = None, name = None):
    dataset_group = dataset[dataset['ground_truth'] == group]
    nr_total = dataset_group.shape[0]
    probs = []
    for gr in range(len(dataset['ground_truth'].unique())):
        prob = []
        for iter in range(1, 11):
            nr_true = ((dataset_group.iloc[:, iter:iter + 1]) == gr).sum()  # Adjust slicing for single column
            prob.append((nr_true / nr_total).values[0])  # Calculate probability
        probs.append(prob)
    probs = np.array(probs)
    #print(probs)
    plt.figure(figsize=(10, 6))
    for i in range(probs.shape[0]):
        plt.plot(range(0, probs.shape[1]), probs[i], label=f'Group {i+1}')
    plt.title("Probability Progression by Group")
    plt.xlabel("Iteration")
    plt.ylabel("Probability")
    plt.legend()
    plt.grid(True)
    if path is not None:
        plt.savefig(f"{path}/figure2_{name}.png")
    else:
        plt.show()
    plt.close()

def figure3(dataset_without, dataset_rollout, path = None, name = None):
    acc_without = []
    nr_total_without = dataset_without.shape[0]
    acc_rollout = []
    nr_total_rollout = dataset_rollout.shape[0]
    for iter in range(1, dataset_without.shape[1]):
        correct_without = dataset_without['ground_truth'] == dataset_without.iloc[:, iter]
        acc_without.append(correct_without.sum()/nr_total_without)
    for iter in range(1, dataset_rollout.shape[1]):
        correct_rollout = dataset_rollout['ground_truth'] == dataset_rollout.iloc[:, iter]
        acc_rollout.append(correct_rollout.sum() / nr_total_rollout)
    plt.figure(figsize=(10, 6))
    plt.plot(range(0, 11), acc_without[:11], label='Without rollback')
    plt.plot(range(0, 11), acc_rollout[:11], label='With rollback')
    plt.title("Probability Progression by Group")
    plt.xlabel("Iteration")
    plt.ylabel("Probability")
    plt.legend()
    plt.grid(True)
    if path is not None:
        plt.savefig(f"{path}/figure3_{name}.png")
    else:
        plt.show()
    plt.close()

def figure4(dataset_MCT, dataset_DT, dataset_CBB, path = None, name = None):
    acc_MCT = []
    nr_total_MCT = dataset_MCT.shape[0]
    acc_DT = []
    nr_total_DT = dataset_DT.shape[0]
    acc_CBB = []
    nr_total_CBB = dataset_CBB.shape[0]
    for iter in range(1, dataset_MCT.shape[1]):
        correct_without = dataset_MCT['ground_truth'] == dataset_MCT.iloc[:, iter]
        acc_MCT.append(correct_without.sum()/nr_total_MCT)
    for iter in range(1, dataset_DT.shape[1]):
        correct_rollout = dataset_DT['ground_truth'] == dataset_DT.iloc[:, iter]
        acc_DT.append(correct_rollout.sum() / nr_total_DT)
    for iter in range(1, dataset_CBB.shape[1]):
        correct_rollout = dataset_CBB['ground_truth'] == dataset_CBB.iloc[:, iter]
        acc_CBB.append(correct_rollout.sum() / nr_total_CBB)
    plt.figure(figsize=(10, 6))
    plt.plot(range(0, 11), acc_MCT[:11], label='MCT')
    plt.plot(range(0, 11), acc_DT[:11], label='DT')
    plt.plot(range(0, 11), acc_CBB[:11], label='CBB')
    plt.title("Probability Progression by Group")
    plt.xlabel("Iteration")
    plt.ylabel("Probability")
    plt.legend()
    plt.grid(True)
    if path is not None:
        plt.savefig(f"{path}/figure4_{name}.png")
    else:
        plt.show()
    plt.close()

def figure5(dataset_MCT, dataset_DT, dataset_CBB, path = None, name = None):
    accuracy_MCT = []
    accuracy_DT = []
    accuracy_CBB = []
    for group in range(0, len(dataset_MCT['ground_truth'].unique())):
        gr_MCT = dataset_MCT[dataset_MCT['ground_truth'] == group]
        nr_total = gr_MCT.shape[0]
        nr_true = ((gr_MCT.iloc[:, -1:]) == group).sum()
        accuracy_MCT.append((nr_true / nr_total).values[0])
    print(accuracy_MCT)
    for group in range(0, len(dataset_DT['ground_truth'].unique())):
        gr_DT = dataset_DT[dataset_DT['ground_truth'] == group]
        nr_total = gr_DT.shape[0]
        nr_true = ((gr_DT.iloc[:, -1:]) == group).sum()
        accuracy_DT.append((nr_true / nr_total).values[0])
    print(accuracy_DT)
    for group in range(0, len(dataset_CBB['ground_truth'].unique())):
        gr_CBB= dataset_CBB[dataset_CBB['ground_truth'] == group]
        nr_total = gr_CBB.shape[0]
        nr_true = ((gr_CBB.iloc[:, -1:]) == group).sum()
        accuracy_CBB.append((nr_true / nr_total).values[0])
    print(accuracy_CBB)
    categories = range(0, len(dataset_MCT['ground_truth'].unique()))
    n_groups = len(categories)
    bar_width = 0.2
    x = np.arange(n_groups)
    x2 = x + bar_width
    x3 = x + 2 * bar_width
    plt.figure(figsize=(10, 6))
    plt.bar(x, accuracy_MCT, width=bar_width, label='MCT', color='b')
    plt.bar(x2, accuracy_DT, width=bar_width, label='DT', color='g')
    plt.bar(x3, accuracy_CBB, width=bar_width, label='CBB', color='r')
    plt.title("Probability Progression by Group")
    plt.xlabel("Iteration")
    plt.ylabel("Probability")
    plt.xticks(x + bar_width, categories)  # Center the ticks
    plt.legend(loc='lower right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    if path is not None:
        plt.savefig(f"{path}/figure5_{name}.png")
    plt.close()


##### READ IN DATASETS #####
os.chdir("C:/Users/ameli/OneDrive/Studium/TU Wien/WS2024/Experiment Design/Exercise 2")
os.makedirs("plots", exist_ok=True)

netflix_4_34521869 = pd.read_csv('34521869/netflix4.csv', sep=",")
netflix_8_34521869 = pd.read_csv('34521869/netflix8.csv', sep=",")
netflix_8_norollout_34521869 = pd.read_csv('34521869/netflix8_norollout.csv', sep=",")
jester_4_34521869 = pd.read_csv('34521869/jester4.csv', sep=",")
jester_8_34521869 = pd.read_csv('34521869/jester8.csv', sep=",")
jester_8_norollout_34521869 = pd.read_csv('34521869/jester8_norollout.csv', sep=",")
jester_16_34521869 = pd.read_csv('34521869/jester16.csv', sep=",")
jester_32_34521869 = pd.read_csv('34521869/jester32.csv', sep=",")
goodreads_4_34521869 = pd.read_csv('34521869/goodreads4.csv', sep=",")
goodreads_8_34521869 = pd.read_csv('34521869/goodreads8.csv', sep=",")
goodreads_8_norollout_34521869 = pd.read_csv('34521869/goodreads8_norollout.csv', sep=",")
goodreads_16_34521869 = pd.read_csv('34521869/goodreads16.csv', sep=",")
goodreads_32_34521869 = pd.read_csv('34521869/goodreads32.csv', sep=",")

netflix_4_93643757 = pd.read_csv('93643757/netflix4.csv', sep=",")
netflix_8_93643757 = pd.read_csv('93643757/netflix8.csv', sep=",")
netflix_8_norollout_93643757 = pd.read_csv('93643757/netflix8_norollout.csv', sep=",")
jester_4_93643757 = pd.read_csv('93643757/jester4.csv', sep=",")
jester_8_93643757 = pd.read_csv('93643757/jester8.csv', sep=",")
jester_8_norollout_93643757 = pd.read_csv('93643757/jester8_norollout.csv', sep=",")
jester_16_93643757 = pd.read_csv('93643757/jester16.csv', sep=",")
jester_32_93643757 = pd.read_csv('93643757/jester32.csv', sep=",")
goodreads_4_93643757 = pd.read_csv('93643757/goodreads4.csv', sep=",")
goodreads_8_93643757 = pd.read_csv('93643757/goodreads8.csv', sep=",")
goodreads_8_norollout_93643757 = pd.read_csv('93643757/goodreads8_norollout.csv', sep=",")
goodreads_16_93643757 = pd.read_csv('93643757/goodreads16.csv', sep=",")
goodreads_32_93643757 = pd.read_csv('93643757/goodreads32.csv', sep=",")


##### SEED 34521869 ######
print("-----------------------------------------------")
print("---------------- SEED 34521869 ----------------")
os.makedirs("plots/34521869", exist_ok=True)
current = 'C:/Users/ameli/OneDrive/Studium/TU Wien/WS2024/Experiment Design/Exercise 2/plots/34521869/'

print("Figure 1: 34521869")
figure1(netflix_4_34521869, path = current, name = 'netflix_4_34521869')
figure1(netflix_8_34521869, path = current, name = 'netflix_8_34521869')
figure1(netflix_8_norollout_34521869, path = current, name = 'netflix_8_norollout_34521869')
figure1(jester_4_34521869, path = current, name = 'jester_4_34521869')
figure1(jester_8_34521869, path = current, name = 'jester_8_34521869')
figure1(jester_8_norollout_34521869, path = current, name = 'jester_8_norollout_34521869')
figure1(goodreads_4_34521869, path = current, name = 'goodreads_4_34521869')
figure1(goodreads_8_34521869, path = current, name = 'goodreads_8_34521869')
figure1(goodreads_8_norollout_34521869, path = current, name = 'goodreads_8_norollout_34521869')

print("Figure 2: 34521869")
figure2(netflix_4_34521869, group = 3, path = current, name = 'netflix_4_34521869')
figure2(netflix_8_34521869, group = 4, path = current, name = 'netflix_8_34521869')
figure2(netflix_8_norollout_34521869, group = 4, path = current, name = 'netflix_8_norollout_34521869')
figure2(jester_4_34521869, group = 3, path = current, name = 'jester_4_34521869')
figure2(jester_8_34521869, group = 4, path = current, name = 'jester_8_34521869')
figure2(jester_8_norollout_34521869, group = 4, path = current, name = 'jester_8_norollout_34521869')
figure2(goodreads_4_34521869, group = 3, path = current, name = 'goodreads_4_34521869')
figure2(goodreads_8_34521869, group = 4, path = current, name = 'goodreads_8_34521869')
figure2(goodreads_8_norollout_34521869, group = 4, path = current, name = 'goodreads_8_norollout_34521869')

print("Figure 3: 34521869")
figure3(dataset_without=netflix_8_norollout_34521869, dataset_rollout=netflix_8_34521869, path = current, name = 'netflix')
figure3(dataset_without=jester_8_norollout_34521869, dataset_rollout=jester_4_34521869, path = current, name = 'jester')
figure3(dataset_without=goodreads_8_norollout_34521869, dataset_rollout=goodreads_4_34521869, path = current, name = 'goodreads')

print("Figure 4: 34521869")
figure4(dataset_MCT=jester_4_34521869, dataset_DT=jester_8_34521869, dataset_CBB=jester_16_34521869, path = current, name = 'jester')
figure4(dataset_MCT=goodreads_4_34521869, dataset_DT=goodreads_8_34521869, dataset_CBB=goodreads_16_34521869, path = current, name = 'goodreads')

print("Figure 5: 34521869")
figure5(dataset_MCT=netflix_4_34521869, dataset_DT=jester_4_34521869, dataset_CBB=goodreads_4_34521869, path = current, name = 'group4')
figure5(dataset_MCT=netflix_8_34521869, dataset_DT=jester_8_34521869, dataset_CBB=goodreads_8_34521869, path = current, name = 'group8')


##### SEED 93643757 ######
print("-----------------------------------------------")
print("---------------- SEED 93643757 ----------------")
os.makedirs("plots/93643757", exist_ok=True)
current = 'C:/Users/ameli/OneDrive/Studium/TU Wien/WS2024/Experiment Design/Exercise 2/plots/93643757/'

print("Figure 1: 93643757")
figure1(netflix_4_93643757, path = current, name = 'netflix_4_93643757')
figure1(netflix_8_93643757, path = current, name = 'netflix_8_93643757')
figure1(netflix_8_norollout_93643757, path = current, name = 'netflix_8_norollout_93643757')
figure1(jester_4_93643757, path = current, name = 'jester_4_93643757')
figure1(jester_8_93643757, path = current, name = 'jester_8_93643757')
figure1(jester_8_norollout_93643757, path = current, name = 'jester_8_norollout_93643757')
figure1(goodreads_4_93643757, path = current, name = 'goodreads_4_93643757')
figure1(goodreads_8_93643757, path = current, name = 'goodreads_8_93643757')
figure1(goodreads_8_norollout_93643757, path = current, name = 'goodreads_8_norollout_93643757')

print("Figure 2: 93643757")
figure2(netflix_4_93643757, group = 3, path = current, name = 'netflix_4_93643757')
figure2(netflix_8_93643757, group = 4, path = current, name = 'netflix_8_93643757')
figure2(netflix_8_norollout_93643757, group = 4, path = current, name = 'netflix_8_norollout_93643757')
figure2(jester_4_93643757, group = 3, path = current, name = 'jester_4_93643757')
figure2(jester_8_93643757, group = 4, path = current, name = 'jester_8_93643757')
figure2(jester_8_norollout_93643757, group = 4, path = current, name = 'jester_8_norollout_93643757')
figure2(goodreads_4_93643757, group = 3, path = current, name = 'goodreads_4_93643757')
figure2(goodreads_8_93643757, group = 4, path = current, name = 'goodreads_8_93643757')
figure2(goodreads_8_norollout_93643757, group = 4, path = current, name = 'goodreads_8_norollout_93643757')

print("Figure 3: 93643757")
figure3(dataset_without=netflix_8_norollout_93643757, dataset_rollout=netflix_8_93643757, path = current, name = 'netflix')
figure3(dataset_without=jester_8_norollout_93643757, dataset_rollout=jester_4_93643757, path = current, name = 'jester')
figure3(dataset_without=goodreads_8_norollout_93643757, dataset_rollout=goodreads_4_93643757, path = current, name = 'goodreads')

print("Figure 4: 93643757")
figure4(dataset_MCT=jester_4_93643757, dataset_DT=jester_8_93643757, dataset_CBB=jester_16_93643757, path = current, name = 'jester')
figure4(dataset_MCT=goodreads_4_93643757, dataset_DT=goodreads_8_93643757, dataset_CBB=goodreads_16_93643757, path = current, name = 'goodreads')

print("Figure 5: 93643757")
figure5(dataset_MCT=netflix_4_93643757, dataset_DT=jester_4_93643757, dataset_CBB=goodreads_4_93643757, path = current, name = 'group4')
figure5(dataset_MCT=netflix_8_93643757, dataset_DT=jester_8_93643757, dataset_CBB=goodreads_8_93643757, path = current, name = 'group8')
