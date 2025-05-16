from fs.feature_structure import FeatureStructure
from fs.feature_map import FeatureMap

# Create some FeatureStructures
fs_np = FeatureStructure({
    "CAT": "NP",
    "NUM": "sg",
    "CASE": "nom"
})

fs_vp = FeatureStructure({
    "CAT": "VP",
    "TENSE": "past",
    "AGR": {
        "NUM": "sg",
        "PERS": 3
    }
})

# Wrap AGR as a FeatureStructure
fs_vp.set("AGR", FeatureStructure(fs_vp.get("AGR")))

# Create a FeatureMap
fm = FeatureMap()
fm.add("subject", fs_np)
fm.add("predicate", fs_vp)

# Print the FeatureMap
print("📦 FeatureMap contents:\n")
print(fm)
