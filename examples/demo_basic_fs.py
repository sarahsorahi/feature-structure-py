from fs.feature_structure import FeatureStructure

# FS1: common subject
fs1 = FeatureStructure({
    "CAT": "NP",
    "NUM": "sg",
    "PERS": 3
})

# FS2: adds gender info
fs2 = FeatureStructure({
    "GENDER": "fem",
    "NUM": "sg"  # compatible
})

# FS3: conflict on NUM
fs3 = FeatureStructure({
    "NUM": "pl",  # conflicting value
    "PERS": 3
})

# Try unifying fs1 and fs2
unified1 = fs1.unify(fs2)
print("✅ Unified FS1 + FS2:")
print(unified1 if unified1 else "Unification failed")

# Try unifying fs1 and fs3
unified2 = fs1.unify(fs3)
print("\n❌ Unified FS1 + FS3:")
print(unified2 if unified2 else "Unification failed")


