class FeatureStructure:
    def __init__(self, features=None):
        self.features = features if features else {}

    def get(self, feature):
        return self.features.get(feature, None)

    def set(self, feature, value):
        self.features[feature] = value

    def unify(self, other):
        result = FeatureStructure(self.features.copy())

        for key, val in other.features.items():
            if key in result.features:
                own_val = result.features[key]
                if isinstance(own_val, FeatureStructure) and isinstance(val, FeatureStructure):
                    unified = own_val.unify(val)
                    if unified is None:
                        return None
                    result.features[key] = unified
                elif own_val != val:
                    return None
            else:
                result.features[key] = val

        return result

    def __str__(self):
        visited = {}
        return self._str_helper(self.features, visited, indent=0)

    def _str_helper(self, fs, visited, indent):
        lines = []
        indent_str = '  ' * indent

        obj_id = id(fs)
        if obj_id in visited:
            return f"{indent_str}*{visited[obj_id]}"

        tag = len(visited) + 1
        visited[obj_id] = tag

        lines.append(f"{indent_str}*{tag} [")
        for k, v in fs.items():
            if isinstance(v, FeatureStructure):
                lines.append(f"{indent_str}  {k}:")
                lines.append(v._str_helper(v.features, visited, indent + 2))
            else:
                lines.append(f"{indent_str}  {k}: {v}")
        lines.append(f"{indent_str}]")
        return '\n'.join(lines)

