def swap(a,n1,n2):
    tmp1 = a[n1]
    tmp2 = a[n2]
    a[n1] = tmp2
    a[n2] = tmp1
    
    
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
total = 0
i = j = 0
for i in range(n):
    # Track number of elements swapped during a single array traversal
    numberOfSwaps = 0;
    
    for j in range(n-1):
    
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):
            swap(a,j,(j + 1))
            numberOfSwaps+=1
            total +=1
        
    
    
    # If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0):
        break;
    

print("Array is sorted in",total,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])
