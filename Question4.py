class PairFinder:
    def find_pair(self, numbers, target):
        num_dict = {}  # A dictionary to store numbers and their indices
        
        for i, num in enumerate(numbers):
            complement = target - num
            
            if complement in num_dict:
                return num_dict[complement], i
            
            num_dict[num] = i
        
        return None

# Example usage:
pair_finder = PairFinder()
numbers = [90, 20, 10, 40, 50, 60, 70]
target = 50
result = pair_finder.find_pair(numbers, target)

if result:
    print(result[0], result[1])
else:
    print("No pair found")
