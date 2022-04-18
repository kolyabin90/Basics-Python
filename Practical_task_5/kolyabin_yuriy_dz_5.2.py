try:
    # def nums_gen(n):                    # 1 задача
    #     for num in range(1, n + 1):
    #         if num % 2 != 0:
    #             yield num
    # nums = nums_gen(7)
    n = 7
    nums = (num for num in range(1, n + 1) if num % 2 != 0)
    print(next(nums))
    print(next(nums))
    print(next(nums))
    print(next(nums))
    print(next(nums))
except StopIteration:
    print('...StopIteration...')
