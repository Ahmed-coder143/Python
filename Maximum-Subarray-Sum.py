def max_subarray_sum(n, arr):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    N = int(input("Enter the number: "))
    numbers = list(map(int, input("Enter the number of array list: ").split()))

    result = max_subarray_sum(N, numbers)
    print("The result of maxsubarray sum",result)