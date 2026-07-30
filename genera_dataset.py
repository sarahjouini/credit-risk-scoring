import pandas as pd
import numpy as np

np.random.seed(42)

n_aziende = 300

settori = ["Alimentare", "Edilizia", "Tecnologia", "Turismo", "Manifattura"]

df = pd.DataFrame({
    "nome_azienda": ["Azienda_" + str(i) for i in range(1, n_aziende + 1)],
    "settore": np.random.choice(settori, n_aziende),
    "anni_attivita": np.random.randint(1, 40, n_aziende),
    "fatturato": np.random.randint(50000, 2000000, n_aziende),
    "debiti": np.random.randint(0, 1500000, n_aziende),
    "ritardo_medio_pagamenti": np.random.randint(0, 120, n_aziende),
    "crescita_fatturato": np.round(np.random.uniform(-20, 30, n_aziende), 1),
})

df.to_csv("aziende.csv", index=False)

print(df.head(10))
print()
print("Dataset creato:", len(df), "aziende")