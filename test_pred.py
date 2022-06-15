import pickle
import pandas as pd
import pytest
from app import predict

my_dict2 = {'Age': 68,
 'RestingBP': 150,
 'Cholesterol': 195,
 'Oldpeak': 0.0,
 'FastingBS': 1,
 'MaxHR': 132,
 }

my_data= pd.DataFrame([my_dict2])

def test_predict():
    assert 1==predict(my_data)
