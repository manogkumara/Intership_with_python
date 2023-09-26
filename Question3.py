class SubsetGenerator:
    def get_unique_subsets(self, nums):
        def backtrack(start, subset):
            subsets.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        subsets = []
        backtrack(0, [])
        return subsets


# Example usage:
subset_generator = SubsetGenerator()
input_list = [4, 5, 6]
result = subset_generator.get_unique_subsets(input_list)
print(result)
