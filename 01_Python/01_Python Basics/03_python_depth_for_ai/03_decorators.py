def log_function_call(function):
    def wrapper():
        print("Function is starting...")
        function()
        print("Function has ended.")
    return wrapper


@log_function_call
def train_model():
    print("Training ML model...")

train_model()



# @property example



class ModelResult:
    def __init__(self,accuracy,loss):
        self.accuracy= accuracy
        self.loss=loss

    @property
    def is_good_model(self):
        return self.accuracy >= 0.85


result=ModelResult(accuracy=0.91,loss=0.2)

print(result.is_good_model)
