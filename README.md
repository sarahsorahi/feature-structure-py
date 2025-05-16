# feature-structure-py

Custom Python classes for representing **feature structures (FS)** and **feature maps (FM)** — widely used in **computational linguistics**, NLP, and grammar frameworks like HPSG and LFG.

---

## 📦 Features

- Create and manipulate typed or untyped feature structures
- Support for **reentrancy** (shared substructures)
- Unification and subsumption (coming soon)
- Nested structures and deep printing
- JSON/AVM-style visualization
- Easily extendable with custom features

---

## 🚀 Quick Example

```python
from fs.feature_structure import FeatureStructure

person = FeatureStructure({
    "CAT": "NP",
    "NUM": "sg",
    "PERS": "3",
    "GENDER": "fem"
})

clause = FeatureStructure({
    "SUBJ": person,
    "TENSE": "past"
})

print(clause)
