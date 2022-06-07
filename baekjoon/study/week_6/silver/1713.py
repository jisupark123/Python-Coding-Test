# 후보 추천하기


def delete_photo():  # 추천을 가장 적게 받은 학생을 지우는 함수
    global frame, reco_cnt
    min_reco = []  # 추천을 적게 받은 학생이 여러명이 나올 수 있기 때문에 배열에 모두 저장한다.
    min_value = min(reco_cnt.values())

    # 닥셔너리를 순회하며 가장 작은 값의 key를 min_reco 배열에 저장
    for key in reco_cnt:
        if reco_cnt[key] == min_value:
            min_reco.append(key)

    # 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는
    # 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.

    for i in range(len(frame)):
        for key in min_reco:
            if frame[i] == key:  # 만약 사진틀에 있는 번호와 딕셔너리에서 추출한 최솟값의 키 값이 서로 같다면
                del frame[i]  # 사진틀에서 삭제하고
                del reco_cnt[key]  # 딕셔너리에서도 삭제한다.
                return


frame_cnt = int(input())  # 사진틀의 개수
reco_ = int(input())  # 전체 학생의 총 추천 횟수 (사용 안함)
reco_nums = list(map(int, input().split()))  # 추천받은 학생을 나타내는 번호

frame = []  # 게시할 사진틀 (마지막에 나올 결과값)
reco_cnt = {}  # 학생마다 추천받은 횟수를 저장


for num in reco_nums:
    if num in reco_cnt:  # 만약 현재 사진이 게시된 학생이 다른 학생의 추천을 받으면
        reco_cnt[num] += 1  # 추천받은 횟수만 증가시킨다.
        continue

    if len(frame) >= frame_cnt:  # 만약 비어있는 사진틀이 없다면 delete_photo() 함수 실행
        delete_photo()

    frame.append(num)
    reco_cnt[num] = 1


for i in sorted(frame):  # 오름차순으로 정렬해서 출력
    print(i, end=" ")
