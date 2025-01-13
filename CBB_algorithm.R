# Load required libraries
library(MASS)

# Define the CBB algorithm
cbb_algorithm <- function(user_ratings, group_means, group_variances, B, C, D) {
  n_users <- nrow(user_ratings)
  n_items <- ncol(user_ratings)
  n_groups <- nrow(group_means)
  
  # Initialize output matrix to store group assignments
  group_assignments <- matrix(NA, nrow = n_users, ncol = n_items)
  
  # Step 1: Select initial groups for all users
  initial_groups <- sample(1:n_groups, n_users, replace = TRUE)
  
  for (user_idx in 1:n_users) {
    cat("Processing user:", user_idx, "\n")
    
    # Initialize for the current user
    current_group <- initial_groups[user_idx]
    explored_items <- numeric(0)  # Keep track of rated items
    group_assignments[user_idx, 1] <- current_group  # Save initial group assignment
    
    # Immediate exploration of the initial group
    next_item <- select_next_item(current_group, explored_items, group_means, group_variances)
    explored_items <- rate_item(user_idx, current_group, explored_items, user_ratings, group_means, group_variances, next_item)
    
    # Main exploration loop
    for (item_step in 2:n_items) {
      # Define candidate groups (Mn)
      Mn <- define_candidate_groups(n_groups, explored_items, user_ratings[user_idx, ], group_means, C)
      
      # Select the next group and item to explore
      if (length(Mn) > 0) {
        current_group <- select_best_group(Mn, explored_items, user_ratings[user_idx, ], group_means)
      } else {
        res <- find_best_group_and_item(explored_items, group_means, group_variances)
        current_group <- res$best_group
        next_item <- res$best_item
      }
      
      next_item <- select_next_item(current_group, explored_items, group_means, group_variances)
      explored_items <- rate_item(user_idx, current_group, explored_items, user_ratings, group_means, group_variances, next_item)
      
      # Stop criteria
      if (length(explored_items) >= B || (length(Mn) == 1 && item_step > D * log2(n_groups))) {
        group_assignments[user_idx, item_step] <- current_group
        break
      }
      
      group_assignments[user_idx, item_step] <- current_group
    }
  }
  
  return(group_assignments)
}

# Define candidate groups
define_candidate_groups <- function(n_groups, explored_items, user_ratings, group_means, C) {
  candidate_groups <- c()
  for (g in 1:n_groups) {
    Rn <- sapply(1:n_groups, function(h) {
      calculate_Rn(g, h, explored_items, user_ratings, group_means)
    })
    if (all(abs(Rn - 1) <= C)) {
      candidate_groups <- c(candidate_groups, g)
    }
  }
  return(candidate_groups)
}

# Select the next item to rate
select_next_item <- function(current_group, explored_items, group_means, group_variances) {
  remaining_items <- setdiff(1:ncol(group_means), explored_items)
  if (length(remaining_items) == 0) stop("No remaining items to rate!")
  
  item_scores <- sapply(remaining_items, function(item) {
    mean_diff <- group_means[current_group, item]
    variance <- group_variances[current_group, item]
    return(mean_diff^2 / variance)
  })
  
  return(remaining_items[which.max(item_scores)])
}

# Rate the selected item
rate_item <- function(user_idx, current_group, explored_items, user_ratings, group_means, group_variances, next_item) {
  simulated_rating <- group_means[current_group, next_item] + rnorm(1, 0, sqrt(group_variances[current_group, next_item]))
  user_ratings[user_idx, next_item] <<- simulated_rating
  return(c(explored_items, next_item))
}

# Calculate Rn for a group
calculate_Rn <- function(g, h, explored_items, user_ratings, group_means) {
  if (g == h || length(explored_items) == 0) return(1)
  sum(sapply(explored_items, function(v) {
    (user_ratings[v] - group_means[g, v]) / (group_means[g, v] - group_means[h, v])
  }))
}

# Select the best group from candidate groups
select_best_group <- function(Mn, explored_items, user_ratings, group_means) {
  scores <- sapply(Mn, function(g) {
    min(sapply(setdiff(Mn, g), function(h) {
      calculate_Rn(g, h, explored_items, user_ratings, group_means)
    }))
  })
  return(Mn[which.max(scores)])
}

# Find the best group and item to explore
find_best_group_and_item <- function(explored_items, group_means, group_variances) {
  best_group <- NULL
  best_item <- NULL
  max_gain <- -Inf
  
  for (g in 1:nrow(group_means)) {
    for (item in 1:ncol(group_means)) {
      if (!(item %in% explored_items)) {
        gain <- group_means[g, item] / (1 + group_variances[g, item])
        if (gain > max_gain) {
          max_gain <- gain
          best_group <- g
          best_item <- item
        }
      }
    }
  }
  
  return(list(best_group = best_group, best_item = best_item))
}

set.seed(42)  # For reproducibility
user_ratings <- read.csv('C:/Users/ameli/OneDrive/Studium/TU Wien/WS2024/Experiment Design/Exercise 2/test/goodreads4_1000.csv', sep=",", header=FALSE)
group_means <- read.csv('C:/Users/ameli/OneDrive/Studium/TU Wien/WS2024/Experiment Design/Exercise 2/dilina-r-mcts-rec-e89fbc1/dilina-r-mcts-rec-e89fbc1/data/mu_goodreads4.csv', sep=",", header=FALSE)
group_variances <- read.csv('C:/Users/ameli/OneDrive/Studium/TU Wien/WS2024/Experiment Design/Exercise 2/dilina-r-mcts-rec-e89fbc1/dilina-r-mcts-rec-e89fbc1/data/sigma_goodreads4.csv', sep=",", header=FALSE)
groups <- c(rep(1,1000), rep(2, 1000), rep(3, 1000), rep(4, 1000))
B <- 10
C <- 0.1
D <- 5
result <- cbb_algorithm(user_ratings, group_means, group_variances, B, C, D)
print(result[1:10, ])
