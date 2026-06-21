students = {
    "Tom":80,
    "John":95,
    "Sam":70
}
max_mark=max(students.values())
for key,value in students.items():
    if value==max_mark:
        print(f"highest mark{max_mark} obtained by {key}")