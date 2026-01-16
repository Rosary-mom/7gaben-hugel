# Forschungsprojekt: Biosiegel-Qualität & Enzym-Simulation

## Projektziel
Dieses Projekt nutzt moderne KI-Methoden (Google DeepMind / AlphaFold), um historische Feldforschungsdaten zur Bodenqualität neu zu bewerten. Ziel ist es, Zusammenhänge zwischen Anbaumethoden (Biosiegel-Varianten) und der enzymatischen Aktivität auf molekularer Ebene sichtbar zu machen.

## Methodik: "Vom Feld ins Silico"
Wir kombinieren klassische biochemische Daten mit KI-Simulationen:
1.  **Datenbasis:** Historische Varianzanalysen (HPLC, Spektrometrie) von Bodenproben (Varianten OK, OM, PMS etc.).
2.  **Simulation:** 3D-Strukturvorhersage der beteiligten Enzyme (Protease, Katalase, etc.) mittels AlphaFold 2 auf T4/A100 GPUs.
3.  **Optimierung:** (Geplant) Nutzung von D-Wave Quantencomputern zur Berechnung optimaler Enzym-Kombinationen basierend auf Qualitätsindizes (z.B. Goldener Schnitt).

## Technische Pipeline
* **Code-Basis:** Python (Google Colab)
* **Hardware:** Google Cloud T4 GPU (für Inferenz)
* **Visualisierung:** py3Dmol
* **Speicher:** GitHub (Code) & Google Drive (PDB-Daten)

## Status (Januar 2026)
* ✅ Initiale Verbindung Colab <-> GitHub hergestellt.
* ✅ Erfolgreicher Testlauf der Protein-Faltung (Boden-Protease 1SCJ).
* 🔄 Nächster Schritt: Massen-Import der historischen PDF-Daten via NotebookLM.
