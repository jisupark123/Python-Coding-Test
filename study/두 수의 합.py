# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.


nums = [2, 7, 11, 15]
target = 9


# 브루투포스
def way1(nums: list[int], target: int) -> tuple[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


# in을 이용한 탐색
def way2(nums: list[int], target: int) -> tuple[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1 :]:
            return nums.index(n), nums[i + 1 :].index(complement) + (i + 1)


# 첫 번째 수를 뺀 결과 키 조회 (풀이 2번을 딕셔너리로 최적화)
def way3(nums: list[int], target: int) -> tuple[int]:
    nums_map = {}
    # 키와 값을 마꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target - num]


# 조회 구조 개선 (3번과 구현 방법, 성능은 비슷하나 코드는 더 간결하다)
def way4(nums: list[int], target: int) -> tuple[int]:
    nums_map = {}
    # 하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return nums_map[target - num], i

        nums_map[num] = i


# 투 포인터 이용 (정렬된 배열에서만 가능한 방법으로 인덱스를 반환하는 이 문제에서는 사용할 수 없다.)
def way5(nums: list[int], target: int) -> tuple[int]:
    nums.sort()
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 오른쪽 포인터를 왼쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 왼쪽 포인터를 오른쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return left, right


print(way5(nums, target))
