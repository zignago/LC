package main

func twoSum(nums []int, target int) []int {

	//declare hashmap
	var hashmap = make(map[int]int)
	var result []int

	//loop through all numbers with i
	for i := 0; i < len(nums); i++ {

		//determine complement
		complement := target - nums[i]

		//search hashmap for complement
		index, exists := hashmap[complement]

		//if complement is a key in the hashmap, assign indices of current index and complement to result variable and break loop
		if exists {
			result = []int{index, i}
			break
		}

		//else, add index to hashmap with key being value
		hashmap[nums[i]] = i
	}

	return result
}

//time complexity: O(n), as only one pass-through is needed
