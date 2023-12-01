# Part 1

## Notebook

I fixed the Matplotlib error for all the charts. Then, I chose Logistic Regression with Feature Importance and Balance because it produces similar results to XGBoost, and it's a simpler algorithm.

## Model Class

**Process**:
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

# Part 3

## Deployment

Using Google Cloud Run, I deployed the API stored in a Docker image on Docker Hub. I opted not to utilize Cloud Registry, as Docker Hub offers a free service. However, in a production application, I would consider using Cloud Registry for its ease of integration with Cloud Run.

# Part 4

## Continuous Integration

This CI integration was created with the following logic:

### Workflow Triggers

The workflow is triggered on pushes to the "master" branch and pull requests targeting "master". Additionally, it has read permissions for repository contents.

### Job: Build

The 'build' job runs on the latest Ubuntu environment and consists of the following steps:

1. **Checkout Code:**
    - Uses the GitHub Actions 'checkout' action to fetch the repository code.

2. **Set Up Python 3.10:**
    - Uses the 'actions/setup-python' action to set up Python 3.10 for the workflow.

3. **Set Up Virtual Environment:**
    - Creates a virtual environment named `.venv` and activates it.

4. **Cache Dependencies:**
    - Uses the 'actions/cache' action to cache the pip cache and the virtual environment. This helps speed up subsequent workflow runs by reusing dependencies.

5. **Install Dependencies:**
    - Upgrades pip and installs necessary dependencies.
    - Checks for and installs dependencies from 'requirements-dev.txt', 'requirements-test.txt', and 'requirements.txt' if these files exist.

6. **Test with Pytest:**
    - Navigates to the 'tests' directory and runs pytest for testing.

This workflow ensures a clean Python environment, installs dependencies, and runs tests using pytest.

## Continuous Deployment

I was unable to make this part of the challenge work with GitHub Actions. Although it's worth mentioning that inside the Cloud Run service, there is an option to automatically build this feature with Google Cloud Build. Still, since the challenge stated GitHub Actions, I didn't implement it.

