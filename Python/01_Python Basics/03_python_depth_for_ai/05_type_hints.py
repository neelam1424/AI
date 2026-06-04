def calculate_accuracy(correct: int, total:int)-> float:
    return correct / total

def evaluate_model(model_name: str, accuracy: float)-> str:
    if accuracy >=0.85:
        return f"{model_name} is a good model."
    return f"{model_name} needs improvement."

accuracy = calculate_accuracy(92,100)
print("Accuracy:" ,accuracy)
print(evaluate_model("Random Forest", accuracy))