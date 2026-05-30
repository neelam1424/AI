# Python for AI/ML & Data Science Portfolio Notes

This repository contains my learning journey from intermediate Python concepts to NumPy, Pandas, and Data Visualization.
The goal is to build strong foundations for AI/ML, Data Science, and software engineering projects.

---

# 1. Python Depth You Need

## 1.1 List, Dict, and Set Comprehensions

Comprehensions are a shorter and cleaner way to create lists, dictionaries, and sets.

### List Comprehension

```python
numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]
print(squares)
```

This means: for every number in the list, square it and store it in a new list.

Used in AI/ML for cleaning data, filtering values, and transforming columns.

Example:

```python
accuracies = [0.72, 0.85, 0.91, 0.67, 0.88]
good_scores = [score for score in accuracies if score >= 0.85]
print(good_scores)
```

---

### Dict Comprehension

```python
models = ["Logistic Regression", "Random Forest"]
scores = [0.82, 0.91]

model_scores = {model: score for model, score in zip(models, scores)}
print(model_scores)
```

Used to store model names with their scores.

---

### Set Comprehension

```python
skills = ["Python", "SQL", "Python", "ML"]
unique_skills = {skill for skill in skills}
print(unique_skills)
```

Sets remove duplicates.

---

## 1.2 Generators and Iterators

Generators produce values one by one instead of storing everything in memory.

```python
def generate_numbers():
    yield 1
    yield 2
    yield 3

for number in generate_numbers():
    print(number)
```

`yield` gives one value, pauses the function, and continues later.

Used in AI/ML for reading large datasets in batches.

```python
def data_batches(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

dataset = [10, 20, 30, 40, 50, 60]

for batch in data_batches(dataset, 2):
    print(batch)
```

---

## 1.3 Decorators

Decorators add extra behavior to a function without changing the original function.

```python
def log_function_call(function):
    def wrapper():
        print("Function started")
        function()
        print("Function ended")
    return wrapper

@log_function_call
def train_model():
    print("Training model...")

train_model()
```

Used in frameworks like Flask, FastAPI, PyTorch, and TensorFlow.

---

### `@property`

`@property` lets us use a method like a variable.

```python
class ModelResult:
    def __init__(self, accuracy):
        self.accuracy = accuracy

    @property
    def is_good_model(self):
        return self.accuracy >= 0.85

result = ModelResult(0.91)
print(result.is_good_model)
```

---

## 1.4 Context Managers

Context managers handle setup and cleanup automatically.

Most common use:

```python
with open("report.txt", "w") as file:
    file.write("Model Accuracy: 0.91")
```

The file closes automatically.

Used for files, databases, APIs, model saving, and resource management.

---

## 1.5 Type Hints

Type hints make code easier to understand.

```python
def calculate_accuracy(correct: int, total: int) -> float:
    return correct / total
```

Meaning:

* `correct` should be an integer
* `total` should be an integer
* return value should be a float

Used in professional Python projects, APIs, ML pipelines, and backend systems.

---

## 1.6 `*args` and `**kwargs`

`*args` handles multiple positional arguments.

```python
def average_score(*scores):
    return sum(scores) / len(scores)

print(average_score(0.82, 0.91, 0.88))
```

`**kwargs` handles named arguments.

```python
def show_model_details(**details):
    for key, value in details.items():
        print(key, value)

show_model_details(model="Random Forest", accuracy=0.91)
```

Used heavily in ML libraries where functions accept flexible inputs.

---

## 1.7 Lambda, Map, Filter, Zip

### Lambda

A small one-line function.

```python
square = lambda x: x * x
print(square(5))
```

---

### Map

Applies a function to every item.

```python
numbers = [1, 2, 3]
squares = list(map(lambda x: x * x, numbers))
print(squares)
```

---

### Filter

Keeps only matching values.

```python
scores = [0.72, 0.85, 0.91]
good_scores = list(filter(lambda score: score >= 0.85, scores))
print(good_scores)
```

---

### Zip

Combines multiple lists.

```python
models = ["LR", "RF"]
scores = [0.82, 0.91]

combined = dict(zip(models, scores))
print(combined)
```

---

## 1.8 Virtual Environments, pip, Poetry

A virtual environment keeps project libraries separate.

```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy matplotlib
pip freeze > requirements.txt
```

Install dependencies later:

```bash
pip install -r requirements.txt
```

Poetry is a modern project manager:

```bash
pip install poetry
poetry new my-project
poetry add pandas numpy
poetry run python main.py
```

---

# 2. NumPy

NumPy is used for fast numerical computing.
AI/ML data is mostly numbers, so NumPy is a must.

---

## 2.1 ndarray Creation and Operations

An ndarray is NumPy’s main data structure.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
```

Operations happen on the full array:

```python
marks = np.array([80, 85, 90])
print(marks + 5)
print(np.mean(marks))
print(np.max(marks))
```

Used for numerical features, model inputs, and calculations.

---

## 2.2 Broadcasting

Broadcasting lets NumPy apply operations between arrays of different shapes.

```python
scores = np.array([80, 85, 90])
updated_scores = scores + 5
print(updated_scores)
```

The value `5` is added to every item.

ML example:

```python
data = np.array([
    [10, 200],
    [20, 300],
    [30, 400]
])

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

normalized = (data - mean) / std
print(normalized)
```

Broadcasting is used in normalization.

---

## 2.3 Vectorization vs Loops

Vectorization means using array operations instead of Python loops.

Loop way:

```python
numbers = [1, 2, 3]
squares = []

for number in numbers:
    squares.append(number * number)
```

Vectorized way:

```python
numbers = np.array([1, 2, 3])
squares = numbers * numbers
print(squares)
```

Vectorization is much faster and used in ML training.

---

## 2.4 Reshaping, Slicing, Fancy Indexing

### Reshaping

```python
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print(reshaped)
```

Used for images, batches, and neural network inputs.

---

### Slicing

```python
arr = np.array([10, 20, 30, 40])
print(arr[1:3])
```

---

### 2D Slicing

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[:, 0])
print(data[1:, 1:])
```

---

### Fancy Indexing

```python
arr = np.array([10, 20, 30, 40])
print(arr[[0, 2]])
```

---

## 2.5 Linear Algebra with `np.linalg`

Linear algebra is the math behind ML.

```python
features = np.array([1, 2, 3])
weights = np.array([0.2, 0.5, 0.3])

prediction = np.dot(features, weights)
print(prediction)
```

This means:

```text
features · weights = prediction
```

Matrix multiplication:

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)
```

Other operations:

```python
print(np.linalg.det(A))
print(np.linalg.inv(A))
print(np.linalg.norm(np.array([3, 4])))
```

---

## 2.6 Random Numbers and Seed

Randomness is used for model initialization, train-test split, and synthetic data.

```python
np.random.seed(42)

uniform_values = np.random.uniform(0, 1, 5)
normal_values = np.random.normal(0, 1, 5)

print(uniform_values)
print(normal_values)
```

Seed makes results reproducible.

---

## 2.7 Boolean Masking and `np.where`

Boolean masking filters arrays.

```python
scores = np.array([45, 60, 75, 90])
passing_scores = scores[scores >= 60]
print(passing_scores)
```

`np.where` works like if-else:

```python
labels = np.where(scores >= 60, "Pass", "Fail")
print(labels)
```

Used for filtering data and creating labels.

---

## 2.8 Saving and Loading Arrays

```python
features = np.array([[1.2, 3.4], [2.1, 4.3]])

np.save("features.npy", features)

loaded = np.load("features.npy")
print(loaded)
```

Used to save processed data, embeddings, and model inputs.

---

# 3. Pandas

Pandas is used for working with table data.

It is like Excel in Python, but more powerful.

---

## 3.1 Series and DataFrame

A Series is one column.

```python
import pandas as pd

marks = pd.Series([85, 90, 78])
print(marks)
```

A DataFrame is a full table.

```python
students = pd.DataFrame({
    "name": ["Neelam", "Aarav", "Priya"],
    "marks": [85, 90, 78],
    "attendance": [92, 88, 75]
})

print(students)
```

In ML:

* rows = examples
* columns = features

---

## 3.2 Loading CSV, JSON, Excel, SQL

CSV:

```python
df = pd.read_csv("data/students.csv")
```

JSON:

```python
df = pd.read_json("data/courses.json")
```

Excel:

```python
df = pd.read_excel("data/students.xlsx")
```

SQL:

```python
import sqlite3

connection = sqlite3.connect("students.db")
df = pd.read_sql_query("SELECT * FROM students", connection)
```

---

## 3.3 Filter, Select, loc, iloc

Select one column:

```python
df["name"]
```

Select multiple columns:

```python
df[["name", "marks"]]
```

Filter rows:

```python
high_scores = df[df["marks"] >= 85]
```

Multiple conditions:

```python
good_students = df[(df["marks"] >= 80) & (df["attendance"] >= 85)]
```

`loc` uses names:

```python
df.loc[0, "name"]
```

`iloc` uses positions:

```python
df.iloc[0, 1]
```

---

## 3.4 groupby, agg, pivot_table

Group data by category:

```python
df.groupby("course")["marks"].mean()
```

Multiple aggregations:

```python
df.groupby("course").agg({
    "marks": ["mean", "max", "min"],
    "attendance": "mean"
})
```

Pivot table:

```python
pd.pivot_table(
    df,
    values="marks",
    index="course",
    aggfunc="mean"
)
```

Used for summaries and analysis.

---

## 3.5 merge, join, concat

Used to combine datasets.

```python
merged = pd.merge(students, courses, on="course", how="left")
```

`concat` stacks DataFrames:

```python
all_students = pd.concat([students1, students2], ignore_index=True)
```

Used when data is split across multiple tables.

---

## 3.6 Missing Data

Missing values appear as `NaN`.

Check missing values:

```python
df.isnull().sum()
```

Drop missing rows:

```python
df.dropna()
```

Fill missing values:

```python
df["marks"] = df["marks"].fillna(df["marks"].mean())
df["city"] = df["city"].fillna(df["city"].mode()[0])
```

Imputation means replacing missing values with meaningful values.

Common strategy:

* mean for numerical columns
* median when outliers exist
* mode for categorical columns

---

## 3.7 apply, map, lambda

`map` works on one column.

```python
df["result"] = df["marks"].map(lambda mark: "Pass" if mark >= 60 else "Fail")
```

`apply` can work row-wise.

```python
def assign_performance(row):
    if row["marks"] >= 85 and row["attendance"] >= 85:
        return "Excellent"
    return "Needs Improvement"

df["performance"] = df.apply(assign_performance, axis=1)
```

Used for feature engineering.

---

## 3.8 Time Series: resample and rolling

Time series data is data with dates.

```python
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
```

Resample:

```python
weekly_sales = df.resample("W").sum()
```

Rolling average:

```python
df["rolling_3_day_avg"] = df["sales"].rolling(window=3).mean()
```

Used in stock prices, sales, weather, and app analytics.

---

# 4. Data Visualization

Visualization helps us understand data using charts.

Used for:

* finding patterns
* detecting outliers
* checking distributions
* understanding correlations
* presenting insights

---

## 4.1 Matplotlib: Figure, Axes, Subplots

Matplotlib is the basic plotting library.

```python
import matplotlib.pyplot as plt

students = ["Neelam", "Aarav", "Priya"]
marks = [85, 90, 78]

plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
```

Concepts:

* Figure = full canvas
* Axes = chart area
* Plot = actual chart

---

### Subplots

Subplots show multiple charts in one figure.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].bar(students, marks)
axes[0].set_title("Marks")

axes[1].plot(students, marks)
axes[1].set_title("Marks Line Chart")

plt.tight_layout()
plt.show()
```

---

## 4.2 Seaborn

Seaborn is used for beautiful statistical charts.

```python
import seaborn as sns
```

---

### Heatmap

Shows correlation.

```python
numeric_df = df[["marks", "attendance", "study_hours"]]
correlation = numeric_df.corr()

sns.heatmap(correlation, annot=True)
plt.show()
```

---

### Boxplot

Shows spread and outliers.

```python
sns.boxplot(data=df, x="course", y="marks")
plt.show()
```

---

### Pairplot

Shows relationships between multiple numerical columns.

```python
sns.pairplot(numeric_df)
plt.show()
```

---

## 4.3 Plotly Interactive Charts

Plotly creates interactive charts.

```python
import plotly.express as px

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    color="course",
    hover_data=["name", "attendance"],
    title="Study Hours vs Marks"
)

fig.show()
fig.write_html("charts/interactive_chart.html")
```

Used for demos and portfolio dashboards.

---

## 4.4 EDA Workflow

EDA means Exploratory Data Analysis.

Basic EDA steps:

```python
df.head()
df.shape
df.info()
df.isnull().sum()
df.describe()
```

Then visualize:

```python
sns.histplot(df["marks"], kde=True)
plt.show()

sns.scatterplot(data=df, x="study_hours", y="marks")
plt.show()

sns.heatmap(df[["marks", "attendance", "study_hours"]].corr(), annot=True)
plt.show()
```

EDA helps answer:

* What does the data look like?
* Are there missing values?
* Are there outliers?
* Which features are related?
* Which columns may help prediction?

---

## 4.5 Saving Publication-Quality Charts

Charts can be saved for GitHub, reports, and presentations.

```python
plt.savefig("charts/student_marks.png", dpi=300, bbox_inches="tight")
```

Meaning:

* `dpi=300` gives high quality
* `bbox_inches="tight"` removes extra white space

---

# 5. Mini Portfolio Project Ideas

## Project 1: Python Depth Practice

Demonstrate:

* comprehensions
* generators
* decorators
* context managers
* type hints
* args and kwargs
* lambda, map, filter, zip

---

## Project 2: NumPy ML Preprocessing Toolkit

Demonstrate:

* array creation
* normalization
* broadcasting
* vectorization
* matrix multiplication
* masking
* saving/loading arrays

---

## Project 3: Pandas Student Performance Analysis

Demonstrate:

* loading data
* handling missing values
* filtering
* grouping
* merging
* feature engineering
* saving cleaned CSV

---

## Project 4: Data Visualization Dashboard

Demonstrate:

* Matplotlib charts
* Seaborn heatmaps and boxplots
* Plotly interactive charts
* EDA workflow
* saved high-quality charts

---

# 6. Recommended Learning Order

1. Python Depth
2. NumPy
3. Pandas
4. Visualization
5. Scikit-learn
6. Machine Learning projects
7. Deep Learning with PyTorch
8. End-to-end AI/ML portfolio projects

---

# 7. GitHub Commands

```bash
git init
git add .
git commit -m "Added Python AI ML data science learning notes"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_LINK
git push -u origin main
```

---

# 8. Final Summary

This repository covers the core Python and Data Science skills required before starting Machine Learning.

By completing these topics, I learned:

* how to write clean Python code
* how to work with arrays using NumPy
* how to clean and analyze tabular data using Pandas
* how to visualize insights using Matplotlib, Seaborn, and Plotly
* how to structure beginner-friendly but portfolio-ready projects

These skills are the foundation for AI/ML engineering, data science, analytics, and backend development.
