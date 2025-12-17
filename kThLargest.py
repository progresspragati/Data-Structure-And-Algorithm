class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.num_list = nums

    def add(self, val: int) -> int:
        self.num_list.append(val)
        self.num_list.sort()
        return self.num_list[-self.k]