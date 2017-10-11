total = 13
max_stable = 3
partition = 2
partial = []
partial.append(total)
if total<=max_stable:
    print 1
else:
    if total<=partition:
        print total
    else:
        while max(partial)>max_stable:   
            max_height = max(partial)
            a = max_height%partition
            partial.remove(max_height)
            
            for i in range(partition):    
                
                if i==partition-1:
                    partial.append(max_height/partition+a)
                
                else:
                    partial.append(max_height/partition)
        print len(partial)