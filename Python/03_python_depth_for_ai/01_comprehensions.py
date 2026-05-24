# List Comprehension

numbers=[1,2,3,4,5]

squares=[number * number for number in numbers]

print("Squares", squares)



# filtering with list comprehension

accuracies = [0.72, 0.85, 0.91, 0.66, 0.88]

good_models = [accuracy for accuracy in accuracies if accuracy >=0.85]

print("Good Model Scores: ", good_models)


# dict comprehension

models = ["Logistic Regression", "Random Forest", "KNN"]
scores = [0.82, 0.91, 0.76]

model_scores = {model: score for model,score in zip(models,scores)}
print("Model Scores:", model_scores)

# set comprehension

skills = ["Python", "SQL", "Python", "ML", "SQL"]

unique_skills={ skill for skill in skills}

print("Unique Skills:", unique_skills)