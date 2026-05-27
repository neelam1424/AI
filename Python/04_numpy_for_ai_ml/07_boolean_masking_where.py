import numpy as np

scores = np.array([45, 60, 75, 90, 55, 88])

# Boolean mask
passing_mask = scores >=60

print("Passing mask:")
print(passing_mask)

passing_scores = scores[passing_mask]

print("Passing scores:")
print(passing_scores)


# np.where

labels = np.where(scores >=60, "Pass",  "Fail")

print("Labels:")
print(labels)


accuracies = np.array([0.72, 0.85, 0.91, 0.67, 0.88])

good_accuracies = accuracies[accuracies >=0.85]

print("Good model accuracies:")
print(good_accuracies)


model_status = np.where(accuracies >= 0.85, "Good Model", "Needs Improvement")

print("Model status:")
print(model_status)