# Credit Risk Scoring

Un sistema che valuta il **rischio di credito** di un'impresa: dato un insieme di aziende che potrebbero chiedere un prestito, assegna a ciascuna una fascia di rischio — **Basso, Medio o Alto** — in base ai suoi numeri.

In pratica: mi metto nei panni della banca e costruisco le regole che dicono "a questa impresa presto tranquilla, a questa con cautela, a quest'altra meglio di no".

## L'idea di partenza

Quando una banca presta soldi a un'azienda, la domanda è sempre una: **riuscirà a restituirli?** Per rispondere non basta guardare un numero, bisogna leggere la storia e la situazione dell'impresa. Ragionando su cosa rende un'azienda affidabile o rischiosa, ho individuato i segnali che contano davvero:

- **Il suo passato**: ha già preso prestiti in passato? Li ha restituiti in tempo? Chi ha una buona storia alle spalle probabilmente si comporterà bene anche in futuro.
- **La capacità di generare reddito futuro**: sta investendo in attività che porteranno guadagni? Perché è con quei guadagni che ripagherà la banca.
- **La sua situazione attuale**: quanto incassa e quanto paga, quanti debiti ha già sulle spalle, quanti crediti deve ancora riscuotere.
- **La solidità nel tempo**: da quanti anni esiste. Un'azienda giovane è più incerta di una con una lunga storia.

Questi ragionamenti sono, in fondo, gli stessi criteri che le banche usano davvero per valutare il credito.

## Dai ragionamenti ai dati

Per lavorarci, ho tradotto questi segnali in dati concreti e misurabili. Siccome i dati veri sul credito sono **riservati** (le banche non li rendono pubblici), ho creato un dataset **sintetico**: aziende finte, ma con numeri realistici e coerenti tra loro. Saper costruire dati credibili quando quelli veri non sono disponibili è parte del lavoro.

Il dataset contiene **300 aziende**, ognuna con:

| Dato | Cosa rappresenta |
|---|---|
| `settore` | Il ramo in cui opera l'azienda (alcuni più stabili, altri più esposti) |
| `anni_attivita` | Da quanti anni esiste |
| `fatturato` | Quanto incassa in un anno |
| `debiti` | Quanti debiti ha già |
| `ritardo_medio_pagamenti` | In media, quanti giorni di ritardo accumula nei pagamenti |
| `crescita_fatturato` | Se il fatturato sta crescendo o calando (in %) |

## Come funziona lo scoring

Il punto chiave, che è il cuore del ragionamento: **un numero da solo non dice niente, conta la proporzione**. Cinquecentomila euro di debiti sono poca cosa per un'azienda che fattura 5 milioni, ma un disastro per una che ne fattura 300.000. Per questo non guardo il debito secco, ma il **rapporto tra debiti e fatturato**.

Il rapporto si calcola così: `debiti / fatturato`. E in base al risultato assegno la fascia di rischio:

- rapporto **sotto 0,5** → i debiti sono leggeri → rischio **Basso**
- rapporto **tra 0,5 e 1** → debiti importanti ma ancora sostenibili → rischio **Medio**
- rapporto **sopra 1** → l'azienda deve più di quanto guadagna in un anno → rischio **Alto**

## Sviluppi futuri

Per ora lo scoring si basa sul rapporto debiti/fatturato, che è il fattore più importante. Il passo successivo è **arricchirlo con gli altri segnali** che avevo individuato — soprattutto i ritardi nei pagamenti, gli anni di attività e la crescita del fatturato — per avvicinarsi a come ragiona davvero una banca, che non guarda mai un solo numero ma tanti insieme.

## Strumenti usati

- **Python** e **pandas** per generare il dataset e costruire lo scoring
- Dati **sintetici**, creati con logica di business realistica

## Com'è fatto il progetto

- `genera_dataset.py` — crea il dataset sintetico delle 300 aziende e lo salva in `aziende.csv`.
- `analisi.py` — calcola il rapporto debiti/fatturato e assegna la fascia di rischio a ogni azienda.
- `aziende.csv` — i dati delle aziende.

## Cosa ho imparato

Questo progetto parte da dove sono più forte: il ragionamento economico. Prima ho pensato a *cosa* rende un'impresa rischiosa, poi ho tradotto quel ragionamento in regole e in codice. La parte tecnica è al servizio dell'idea, non il contrario — ed è così che dovrebbe funzionare l'analisi dei dati.