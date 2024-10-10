def can_enroll(student, course):
    """
    Checks if a student can enroll in a course based on their grade level and the course's grade requirement.
    """
    grade_req = course["grade_requirement"]
    grade_level = student["grade_level"]
    if grade_level > grade_req:
        return True
    else:
        return False

student = {'name': 'Bob', 'grade_level': 11}
course = {'title': 'Advanced Mathematics', 'grade_requirement': 10}


result = can_enroll(student, course)
print(result)  # True expected

"""
To complete this exercise:
--------------------------
No any implementation notes.
"""
