class Solution:
    def _find_left_max(self, left_max: List[int], height: List[int], n: int):
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
    
    def _find_right_max(self, right_max: List[int], height: List[int], n: int):
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
    
    def _calculate_total_water(self, left_max: List[int], right_max: List[int], height):
        water = 0
        i = 0
        for i in range(len(height)):
            water_i = min(left_max[i], right_max[i]) - height[i]
            water +=water_i
            i+= 1
        return water

        
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)

        left_max = [0] * n
        right_max = [0] * n

        self._find_left_max(left_max, height, n)
        self._find_right_max(right_max, height, n)

        return self._calculate_total_water(left_max, right_max, height)




        