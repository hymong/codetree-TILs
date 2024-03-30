score = int(input())
need_more_score = 80-score

if score >= 80:
    print("pass")
else:
    print(f"{need_more_score} more score")