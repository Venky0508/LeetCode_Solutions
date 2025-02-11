class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        cardMap = {}
        rankMap = {}

        for i in range(len(suits)):
            if suits[i] not in cardMap:
                cardMap[suits[i]] = 1
            else:
                cardMap[suits[i]] += 1

            if str(ranks[i]) not in rankMap:
                rankMap[str(ranks[i])] = 1
            else:
                rankMap[str(ranks[i])] += 1

        if len(cardMap) == 1:
            return "Flush"

        max_val = 0
        for val in rankMap.values():
            if val > max_val:
                max_val = val

        if max_val >= 3:
            return "Three of a Kind"
        elif max_val == 2:
            return "Pair"
        else:
            return "High Card"


