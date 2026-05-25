model_name= "Random Forest"
accuracy = 0.91
f1_score=0.89

with open("model_report.txt", "w") as file:
    file.write("Model Performance Report\n")
    file.write("------------------------\n")
    file.write(f"Model: {model_name}\n")
    file.write(f"Accuracy: {accuracy}")
    file.write(f"f1_score: {f1_score}")

print("Report saved succesfully.")


with open("model_report.txt","r") as file:
    content = file.read()

print(content)