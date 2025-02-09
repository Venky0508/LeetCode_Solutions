class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []

        for point in points:
            x = point[0]
            y = point[1]
            dist = x ** 2 + y ** 2
            distance.append(dist)

        sorted_pairs = sorted(zip(distance, points)) 
        sorted_distance, sorted_points = zip(*sorted_pairs)
        result = sorted_points[:k]
        return result