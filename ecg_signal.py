def return_stats(nums:list[float]) -> tuple:
    if len(nums) < 1:
        raise ValueError("List cannot be empty.") 
    sum = 0
    count = 0
    minimum = float('inf')
    maximum = float('-inf')

    for i in range(len(nums)):
        sum += nums[i]
        count += 1
        if nums[i] < minimum:
            minimum = nums[i]
        if nums[i] > maximum:
            maximum = nums[i]
    
    avg = sum/count
    
    return sum, avg, minimum, maximum

class ECGSignal:
    def __init__(self, samples:list[float]):
        self.samples = samples

    def length(self):
        return len(self.samples)
    
    def summary(self):
        _, mean, min_val, max_val = return_stats(self.samples)
        print(f"Mean: {mean}")
        print(f"Min:  {min_val}")
        print(f"Max:  {max_val}")