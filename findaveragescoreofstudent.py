if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = student_marks[query_name]
    aver = (float((sum(average))/(len(average))))
    result = format(aver, '.2f')

    print(result)
