class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 3):
            # Пропуск дубликатов для i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Ранний выход если минимально возможная сумма > target
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # Максимально возможная сумма < target
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
                
            for j in range(i+1, n - 2):
                # Пропуск дубликатов для j
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # Ранние проверки для j
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                    
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # Пропуск дубликатов для left и right
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res
