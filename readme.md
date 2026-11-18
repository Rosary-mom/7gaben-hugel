# Forschungsprojekt: Biosiegel-Qualität & Enzym-Simulation

## Projektziel
Dieses Projekt nutzt moderne KI-Methoden (Google DeepMind / AlphaFold), um historische Feldforschungsdaten zur Bodenqualität neu zu bewerten. Ziel ist es, Zusammenhänge zwischen Anbaumethoden (Biosiegel-Varianten) und der enzymatischen Aktivität auf molekularer Ebene sichtbar zu machen.

## Methodik: "Vom Feld ins Silico"
Wir kombinieren klassische biochemische Daten mit KI-Simulationen:
1.  **Datenbasis:** Historische Varianzanalysen (HPLC, Spektrometrie) von Bodenproben (Varianten OK, OM, PMS etc.).
2.  **Strukturen:** Kristallstruktur der Modell-Protease PDB 1SCJ (Subtilisin E, UniProt P04189, *Bacillus subtilis*; Jain et al. 1998) sowie AlphaFold-DB-Vorhersagen zu P04189 und zum Vergleich Subtilisin Carlsberg (P00780). Eigene Faltungsläufe (AlphaFold 2 / ColabFold auf T4/A100) bleiben optional möglich; die aktuelle Demo nutzt die AlphaFold-DB-API (`https://alphafold.ebi.ac.uk/api/prediction/<ID>`, Modellversion dynamisch, derzeit v6).
3.  **Hypothesenrahmen:** F&E-Hypothesen H1/H² zum Rosary-Hügelbeet-Effekt (CDH/Glycinbetain, `schutz_faktor 0.8` als gesetzter Protokollwert) und zum Qualitäts- bzw. Q-Hebel-Index; `eta_raw 30000` ist author_claim/Protokollwert, kein Assay-Messwert.
4.  **Optimierung:** (Geplant) Nutzung von D-Wave Quantencomputern zur Berechnung optimaler Enzym-Kombinationen basierend auf Qualitätsindizes (z.B. Goldener Schnitt).

## Technische Pipeline
* **Code-Basis:** Python (Google Colab)
* **Hardware:** Google Colab T4 GPU (Geräteprobe; für optionale eigene Inferenz)
* **Strukturquellen:** RCSB PDB, [AlphaFold DB / EMBL-EBI](https://alphafold.ebi.ac.uk/) (CC-BY 4.0; Jumper et al. 2021, Varadi et al. 2022)
* **Visualisierung:** py3Dmol
* **Speicher:** GitHub (Code) & Google Drive (PDB-Daten)

## Status (November 2026)
* ✅ Initiale Verbindung Colab <-> GitHub hergestellt.
* ✅ 1SCJ in py3Dmol als Kristallstruktur geladen (Subtilisin E, P04189); AlphaFold-DB-Modelle zu P04189 und P00780 über die Prediction-API eingebunden (pLDDT 91.25 / 91.19, Version derzeit v6).
* ✅ Notebook `02_AlphaFold_Human_Proteins.ipynb` mit menschlichen Referenzstrukturen (P00367, P02452, P04406).
* 🔄 Nächster Schritt: Massen-Import der historischen PDF-Daten via NotebookLM.
