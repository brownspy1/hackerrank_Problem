if __name__ == '__main__':
    Score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Score.append([name, score])
    Score_next = [x[1] for x in Score]
    Sorted_set = sorted(set(Score_next))
    Name_st = sorted([x[0] for x in Score if Sorted_set[1] == x[1]])
for f in Name_st:
    print(f)