#!/usr/bin/env ruby


## Main
if __FILE__ == $0
	#Initialize an array with some sample values
    arr = [10,5,2,20,35]

	# Create a Hash table, which returns a default value of -1
    result = Hash.new(-1)
	
	# This flag is used to check if any factors of the current number are found in the array
    flag = false
	
	#sort the array, so that we could have a bottom up comparison systematically
	arr.sort!
    
	# Iterate over the elements which are sorted, so that we cover all of the smaller elements before the larger ones
	(0..arr.size-1).each do |i|
		# For each element, we access the previous elements to get the factors
		(0..i-1).reverse_each do |j|
			if arr[i] % arr[j] == 0 
                # Get the value in a variable named status. If -1 is returned, there is no value, and we create it
				status = result[arr[i]]
                if status == -1
					newList = []
                    newList << arr[j]
                    result[arr[i]] = newList
                    flag = true
				else
					status << arr[j]
                    result[arr[i]] = status
                    flag = true
                end    
			end
		end
		
		# If no factor is found in the array, enter an empty list as value in the hash
		if flag == false
            newList = []
            result[arr[i]] = newList
		end
	end
	
	# print the final hash table which contains the factors
	puts result
	
end    
 
 