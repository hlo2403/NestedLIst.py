if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    scores=sorted(set(student[1] for student in students))
    second_small=scores[1]
    result=sorted([student[0] for student in students if student[1]==second_small])
    
    for name in result:
        print(name)
