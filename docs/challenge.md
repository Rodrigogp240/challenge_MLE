# Part 1

## Notebook

  I fixed the Matplotlib error for all the charts. Then, I chose Logistic Regression with Feature Importance and Balance because it produces similar results to XGBoost, and it's a simpler algorithm.

## Model Class

  **Procces**:
    Firstly, I created a module to encapsulate my helper functions. Another option could have been to make these functions static methods of the class, but I believe that organizing them into a dedicated module aligns better with the SOLID principles. Subsequently, I utilized a relative import to incorporate these functions into the model.py file. Given that the challenge is a module itself, this approach enhances code clarity.
    Following the import, I executed all the necessary transformations on the data. Finally, I utilized the target_column as a boolean flag to determine the correct return value.

  **Fit**:
    I obtained the *n_y0* and *n_y1* values from the notebook and proceeded to train the model using scikit-learn.

  **Predict**:
    I incorporated a check into the code to handle the scenario where the model (self._model) has not been trained yet. If this is the case (i.e., the model is None), I raise a ValueError with a message advising users to first call the 'fit' method to train the model.
    Assuming the model has been trained, the next step involves using the predict method on the trained model to generate predictions based on the provided features. These predictions are initially in float format, so I use the map function to convert them into a list of integers.

# Part 2

## FastAPI Application

I've crafted this FastAPI application for predicting flight delays, and here's a succinct breakdown:

### Pydantic Models

I've defined two Pydantic models:

1. **FlightItem:**
    - Attributes: `OPERA` (string), `TIPOVUELO` (string with regex validation for 'I' or 'N'), `MES` (integer between 1 and 12).

2. **FlightData:**
    - Attribute: `flights` (a list of FlightItem objects).

### Exception Handler

I've implemented an exception handler to catch validation errors during input data processing.

### Prediction Endpoint

The main prediction endpoint (`@app.post("/predict")`) takes input data of type FlightData, conducts a placeholder prediction, and returns a JSON response with the predicted values.

The current implementation includes a placeholder statement (`data`) and always returns a prediction of [0]. The actual prediction logic based on a trained model needs to be incorporated.





