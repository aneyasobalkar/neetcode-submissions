class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        #[1,1,2,8]
        #[48, 24, 6, 1]

        #[6,4,2,1]
        #[1, 6, 24, 48]
        prefix_product = 1
        for index, num in enumerate(nums):
            output.append(prefix_product)
            prefix_product *= num
        print(output)
        suffix_product = 1
        for index, num in enumerate(nums[::-1]):
            insert_index = len(nums) - 1 - index
            output[insert_index] = output[insert_index]  * suffix_product
            suffix_product *= num
        print(output)
        return output