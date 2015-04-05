#!/usr/bin/env ruby


## Main
if __FILE__ == $0
    arr = [10,5,2,20,35]

    result = Hash.new(-1)
    flag = false
	
	# Sort the array, as any element at index i should access all the elements at index (i-1)
	arr.sort!
	puts arr
    
	(0..arr.size-1).each do |i|
		puts "i=#{i}"
		(0..i-1).reverse_each do |j|
			if arr[i] % arr[j] == 0 
                status = result[arr[i]]
                if status == -1
					puts "In if loop"
					newList = []
                    newList << arr[j]
                    result[arr[i]] = newList
                    flag = true
				else
					puts "in else"
					status << arr[j]
                    result[arr[i]] = status
                    flag = true
                end    
			end
		end
		
		if flag == false
            newList = []
            result[arr[i]] = newList
		end
	end
	
	puts result 
	
end    
 
 