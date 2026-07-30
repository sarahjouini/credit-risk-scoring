import pandas as pd

df = pd.read_csv("aziende.csv")

df["rapporto_debiti"] = df["debiti"] / df["fatturato"]

print(df[["nome_azienda", "debiti", "fatturato", "rapporto_debiti"]].head(10))
def assegna_rischio(rapporto):
    if rapporto < 0.5:
        return "Basso"
    elif rapporto < 1:
        return "Medio"
    else:
        return "Alto"

df["rischio"] = df["rapporto_debiti"].apply(assegna_rischio)

print(df[["nome_azienda", "rapporto_debiti", "rischio"]].head(10))
def punti_ritardo(giorni):
    if giorni < 30:
        return 0
    elif giorni < 90:
        return 1
    else:
        return 2
df["punti_ritardo"] = df["ritardo_medio_pagamenti"].apply(punti_ritardo)

print(df[["nome_azienda", "ritardo_medio_pagamenti", "punti_ritardo"]].head(10))