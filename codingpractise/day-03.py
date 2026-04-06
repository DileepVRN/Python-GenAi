def max_sum_of(arr,k):
    if k > len(arr):
        return "k can't be greater than arr.length"
    win_sum=sum(arr[:k])
    max_sum=win_sum
    for i in range(k,len(arr)):l
        win_sum+=arr[i]
        win_sum-=arr[i-k]
        max_sum=max(win_sum,max_sum)
    return max_sum

def main():
    arr,k=[2, 1, 5, 1, 3, 2], 3
    print(f"maximume sum is {max_sum_of(arr,k)}")

if __name__=="__main__":
    main()


     