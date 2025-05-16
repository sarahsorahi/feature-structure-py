from .feature_structure import FeatureStructure

class FeatureMap:
    def __init__(self):
        self.map = {}

    def add(self, label, feature_structure):
        if not isinstance(feature_structure, FeatureStructure):
            raise TypeError("Value must be a FeatureStructure instance.")
        self.map[label] = feature_structure

    def get(self, label):
        return self.map.get(label, None)

    def __str__(self):
        lines = []
        for label, fs in self.map.items():
            lines.append(f"{label}:\n{fs}")
        return "\n\n".join(lines)
