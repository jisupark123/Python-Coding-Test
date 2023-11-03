import sys
import heapq

input = sys.stdin.readline


N = int(input())


times = sorted([list(map(int, input().split())) for _ in range(N)])
meetings = [times[0][1]]  # 회의실 (끝나는 시간만 저장)


for start, end in times[1:]:
    # 시작 시간이 가장 빨리 끝나는 회의보다 빠르다면 회의실 추가
    # else: 해당 회의와 change
    if start < meetings[0]:
        heapq.heappush(meetings, end)
    else:
        heapq.heappop(meetings)
        heapq.heappush(meetings, end)

print(len(meetings))
