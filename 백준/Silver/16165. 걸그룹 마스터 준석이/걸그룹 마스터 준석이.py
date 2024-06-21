n, m = map(int, input().split())    # 걸그룹의 수, 맞혀야 할 문제의 수
idol_dic = {}

for _ in range(n):
    team_name = input()
    team_member_num = int(input())
    team_member = []
    for _ in range(team_member_num):
        team_member.append(input())

    idol_dic[team_name] = team_member


for _ in range(m):
    quiz = input()
    quiz_type = int(input())

    if quiz_type == 0:  # 팀 이름 주어짐
        for member in sorted(idol_dic[quiz]):
            print(member)

    else:   # 팀 멤버 주어짐
        for team, member in idol_dic.items():
            if quiz in member:
                print(team)
                break