FROM python:3.9

WORKDIR /CHALLENGE_MLE

COPY ./requirements.txt /CHALLENGE_MLE/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /CHALLENGE_MLE/requirements.txt

COPY ./challenge/ /CHALLENGE_MLE/challenge/

CMD ["uvicorn", "challenge.api:app", "--host", "0.0.0.0", "--port", "80"]
