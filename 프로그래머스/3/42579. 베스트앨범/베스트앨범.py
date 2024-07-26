def solution(genres, plays):
    answer = []
    genre_of_paly = {}

    # 장르별 총 재생수와, 장르별 곡 재생수 해시 생성
    for i in range(len(genres)):
        if genres[i] not in genre_of_paly:
            genre_of_paly[genres[i]] = [plays[i]]   # 해당 장르의 총 재생수
            genre_of_paly[genres[i]].append([i, plays[i]])  # 해당 장르에 속한 곡의 재생수
        else:
            genre_of_paly[genres[i]][0] += plays[i]
            genre_of_paly[genres[i]].append([i, plays[i]])

    # 각 해시에 대해 재생수 높은 순으로 정렬
    genre_of_paly = sorted(genre_of_paly.items(), key=lambda x : x[1], reverse=True)
    genre_of_paly = dict(genre_of_paly)


    for genre, play_cnt in genre_of_paly.items():
        play_cnt.pop(0)
        play_cnt.sort(key=lambda x: x[1], reverse=True)

        if len(play_cnt) == 1:
            answer.append(play_cnt[0][0])
        else:
            answer.append(play_cnt[0][0])
            answer.append(play_cnt[1][0])
            
    return answer