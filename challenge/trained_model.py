import pickle
import re
from pathlib import Path


BASED_DIR = Path(__file__).resolve(strict=True).parent

with open("f{BASED_DIR}/challenge/trained_log_reg-0.1.0.pkl","rb") as f:
    model = pickle.load(f)