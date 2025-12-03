a = {100, 200, 300, 400, 500}
b = {400, 500, 600, 700, 800}

# intersection_update 실행
a1 = a.copy()
a1.intersection_update(b)
print("intersection_update 결과:", a1)

# difference_update 실행
a2 = a.copy()
a2.difference_update(b)
print("difference_update 결과:", a2)

# symmetric_difference_update 실행
a3 = a.copy()
a3.symmetric_difference_update(b)
print("symmetric_difference_update 결과:", a3)
