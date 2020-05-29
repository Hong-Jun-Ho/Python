def arraysum(arr1, sum):
    count = 0
    for i in range(len(arr1)-1,0,-1):
        if arr1[i] == sum:
            count += 1
        else :
            if arr1[i] +arr1[i-1]==sum:
                count+=1
    return count

print(arraysum([1, 2, 3, 4, 5, 3, 4, 2, 3, 1, 4, 5], 5))
