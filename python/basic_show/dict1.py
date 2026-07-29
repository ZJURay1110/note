course_counts = {}
while True:
    s = input()
    if s == "#":
        break
    stu, lect = s.split()
    
    # 这一行替代了原本的 if-else 4行代码
    course_counts[lect] = course_counts.get(lect, 0) + 1

for lect in sorted(course_counts):
    print(f"{lect}: {course_counts[lect]}")