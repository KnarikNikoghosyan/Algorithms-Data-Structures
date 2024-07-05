class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        freq_list = []
        for num, freq in freq_dict.items():
            freq_list.append((num, freq))

        for i in range(len(freq_list)):
            for j in range(i + 1, len(freq_list)):
                if (freq_list[i][1] > freq_list[j][1]) or (
                        freq_list[i][1] == freq_list[j][1] and freq_list[i][0] < freq_list[j][0]):
                    freq_list[i], freq_list[j] = freq_list[j], freq_list[i]

        result = []
        for value, freq in freq_list:
            result.extend([value] * freq)

        return result

res = Solution()
nums = [1, 1, 2, 2, 2, 3]
print(res.frequencySort(nums))  # Output: [3, 1, 1, 2, 2, 2]
