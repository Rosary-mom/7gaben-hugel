"""Starred limit classes for the protease notebook. Annotation, not a veto."""

LIMITS = [
    {"id": "*simulation", "class": "assumption", "text": "schutz_faktor 0.8 is set, not measured."},
    {"id": "*phi", "class": "assumption", "text": "Distance to phi is a scale, not soil quality."},
    {"id": "*gpu", "class": "runtime", "text": "GPU check is a device probe, not an AlphaFold run."},
    {"id": "*pdb", "class": "database", "text": "1SCJ is Subtilisin Carlsberg from the PDB."},
    {"id": "*not-eta", "class": "scope", "text": "eta_enz stays empty. eta_DHG 8.5 is not imported."},
]

def classify():
    for item in LIMITS:
        print(item["id"], item["class"])
        print(item["text"])
    return LIMITS

if __name__ == "__main__":
    classify()
