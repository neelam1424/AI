# *args

def add_numbers(*args):
    total = sum(args)
    return total
print(add_numbers(10,20,30,40))


# **kwargs


def show_model_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_model_details(
    model="Random Forest",
    accuracy=0.91,
    f1_score=0.89
)        



# 06_args_kwargs.py

def average_score(*scores: float) -> float:
    return sum(scores) /len(scores)

print("Average Score:", average_score(0.82, 0.91,0.88))




def show_model_details(**details):
    print("\n Model Details: ")
    for key, value in details.items():
        print(f"{key}: {value}")

show_model_details(
     model="Random Forest",
    accuracy=0.91,
    f1_score=0.89,
    dataset="House Price Dataset"
)