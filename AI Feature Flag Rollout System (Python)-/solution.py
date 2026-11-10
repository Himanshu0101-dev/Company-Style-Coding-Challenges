class Solution:
    def _hash(self, user_id, feature):
        s = str(user_id) + feature
        h = 0

        for ch in s:
            h = (h * 31 + ord(ch)) % 100

        return h

    def featureRollout(self, operations):
        features = {}
        result = []

        for op in operations:
            action = op[0]

            if action == "enable":
                feature = op[1]
                percentage = int(op[2])
                features[feature] = percentage

            elif action == "disable":
                feature = op[1]
                features.pop(feature, None)

            else:
                user_id = op[1]
                active = []

                for feature, percentage in features.items():
                    if self._hash(user_id, feature) < percentage:
                        active.append(feature)

                result.append(sorted(active))

        return result


# Example
operations = [
    ["enable", "AI_Search", "30"],
    ["enable", "SmartReply", "50"],
    ["query", "1001"],
    ["disable", "AI_Search"],
    ["query", "1001"]
]

print(Solution().featureRollout(operations))
