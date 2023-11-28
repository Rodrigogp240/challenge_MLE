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
