student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

heigest_score =0
for score in student_scores:
    if score > heigest_score:
      heigest_score = score
print(f"the heigest score in class is {heigest_score} ")
