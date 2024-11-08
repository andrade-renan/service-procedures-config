import pandas as pd
import json

with open('procedures.json', 'r') as file:
    procedures = json.load(file)

with open('services.json', 'r') as file:
    services = json.load(file)
    

print(procedures)