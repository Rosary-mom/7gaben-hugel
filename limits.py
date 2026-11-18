"""Starred limit classes for the protease notebook. Annotation, not a veto."""

LIMITS = [
    {"id": "*simulation", "class": "assumption", "text": "schutz_faktor 0.8 is set, not measured."},
    {"id": "*phi", "class": "assumption", "text": "Distance to phi is a scale, not soil quality."},
    {"id": "*gpu", "class": "runtime", "text": "GPU check is a device probe, not an AlphaFold run."},
    {"id": "*pdb", "class": "database", "text": "1SCJ is the crystal structure of Subtilisin E (UniProt P04189, Bacillus subtilis), Jain et al. 1998. Not Subtilisin Carlsberg (P00780), which we keep as a comparison."},
    {"id": "*not-eta", "class": "scope", "text": "eta_enz stays empty. eta_DHG 8.5 is not imported. eta_raw 30000 is an author_claim/Protokollwert, not an assay measurement."},
    {"id": "*pred", "class": "database", "text": "An AlphaFold DB model is a structure prediction, not a measurement of activity or stability."},
    {"id": "*plddt", "class": "scale", "text": "pLDDT is per-residue confidence; PAE is expected position error. Neither is an activity or thermostability assay."},
    {"id": "*thermo", "class": "scope", "text": "These structures do not prove thermostability or field efficacy."},
]


def classify():
    for item in LIMITS:
        print(item["id"], item["class"])
        print(item["text"])
    return LIMITS


if __name__ == "__main__":
    classify()
