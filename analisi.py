import pandas as pd

df = pd.read_csv("aziende.csv")

df["rapporto_debiti"] = df["debiti"] / df["fatturato"]


def punti_debiti(rapporto):
    if rapporto < 0.5:
        return 0
    elif rapporto < 1:
        return 1
    else:
        return 2


def punti_ritardo(giorni):
    if giorni < 30:
        return 0
    elif giorni < 90:
        return 1
    else:
        return 2


def rischio_finale(punti):
    if punti <= 1:
        return "Basso"
    elif punti == 2:
        return "Medio"
    else:
        return "Alto"


df["punti_debiti"] = df["rapporto_debiti"].apply(punti_debiti)
df["punti_ritardo"] = df["ritardo_medio_pagamenti"].apply(punti_ritardo)

df["punti_totali"] = df["punti_debiti"] + df["punti_ritardo"]

df["rischio_finale"] = df["punti_totali"].apply(rischio_finale)

print(df[["nome_azienda", "punti_debiti", "punti_ritardo", "punti_totali", "rischio_finale"]].head(10))