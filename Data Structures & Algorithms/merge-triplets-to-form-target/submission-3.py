class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr_triplet = [0,0,0]
        for triplet in triplets:
            if max(triplet[0], curr_triplet[0]) <= target[0]:
                #curr_triplet[0] = max(triplet[0], curr_triplet[0])
                if max(triplet[1], curr_triplet[1]) <= target[1]:
                    #curr_triplet[1] = max(triplet[1], curr_triplet[1])
                    if max(triplet[2], curr_triplet[2]) <= target[2]:
                        #curr_triplet[2] = max(triplet[2], curr_triplet[2])
                        curr_triplet = [max(triplet[0], curr_triplet[0]), max(triplet[1], curr_triplet[1]),max(triplet[2], curr_triplet[2])]
        for i in range(3):
            if curr_triplet[i] != target[i]:
                return False
        return True
