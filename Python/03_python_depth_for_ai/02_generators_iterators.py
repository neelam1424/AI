"""
Topic: Generators and Iterators
Goal: Understand memory-efficient data processing.
"""


numbers = [1,2,3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Generator example


def read_large_dataset():
    """
    Simulates reading data one row at a time.
    In real AI/ML projects, this could be rows from a large CSV file.
    """

    data = [
        {"name": "Neelam", "score": 85},
        {"name": "Aarav", "score": 91},
        {"name": "Priya", "score": 78},
    ]

    for row in data:
        yield row


print("\n Genrator Output")

for student in read_large_dataset():
    print(student)


# -----------------------------
# Generator for ML Batches
# -----------------------------


def batch_generator(data, batch_size):
    """
    Generates small batches from a large dataset.
    This idea is used in deep learning training.
    """
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

dataset = [1,2,3,4,5,6,7,8,9]

print("\n Batch output")

for batch in batch_generator(dataset,3):
    print(batch)