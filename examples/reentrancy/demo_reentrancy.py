from fs.feature_structure import FeatureStructure

# Create a shared substructure
shared = FeatureStructure({
    "NUM": "sg",
    "PERS": 3
})

# Create a FeatureStructure with reentrancy
fs = FeatureStructure({
    "SUBJ": shared,
    "OBJ": shared  # Reentrant reference
})

print("🔁 Reentrant Feature Structure:")
print(fs)

