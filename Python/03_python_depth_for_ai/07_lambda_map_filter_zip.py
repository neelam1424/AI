numbers = [1,2,3,4,5]

square = list(map(lambda number:number*number, numbers))
print("Squares",square)

accuracies = [0.72, 0.85, 0.91, 0.67, 0.88]


good_score = list(filter(lambda score:score >=0.85, accuracies ))

models = ["Logistic Regression", "Decision Tree", "Random Forest"]
scores = [0.82, 0.76, 0.91]

model_results = list(zip(models,scores))
print("Model Results:", model_results)

model_score_dict = dict(zip(models, scores))
print("Model Score Dictionary:", model_score_dict)