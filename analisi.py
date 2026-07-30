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