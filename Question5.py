class ThreeSumFinder:
    def find_three_sum(self, nums):
        nums.sort()  # Sort the input list

        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result

# Example usage:
three_sum_finder = ThreeSumFinder()
input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
result = three_sum_finder.find_three_sum(input_array)
print(result)
