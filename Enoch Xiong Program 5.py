courses = {}

num = int(input("How many courses are you entering? "))

for i in range(num):
    course_id = input("Please enter the course ID (example: COS 2005): ")
    course_name = input("Please enter the course name: ")
    courses[course_id] = course_name

subject = input("Enter a subject to search (example: COS): ")

print("Results with:", subject)

for course_id, course_name in courses.items():
    if course_id.startswith(subject):
        print(course_id, "-", course_name)
