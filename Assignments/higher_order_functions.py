# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Higher Order Functions & Grouping (Student Data)
# File    : higher_order_functions.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Higher Order Functions on Student Data
#
#   generate_student_data(n_students, courses, cities, random_seed=42)
#       Generate a list of student dicts with rollno, city, and course marks.
#       Uses random.choice and random.randint with a fixed seed for consistency.
#
#   groupby(data: list, key: callable)
#       Group list items into a dict by a key function.
#
#   apply_to_groups(groups: dict, func: callable)
#       Apply a function to the value list of each group. Returns new dict.
#
#   min_course_marks(student_data, course)
#       Return the minimum marks in a given course across all students.
#
#   max_course_marks(student_data, course)
#       Return the maximum marks in a given course across all students.
#
#   rollno_of_max_marks(student_data, course)
#       Return the rollno of the student with the highest marks in a course.
#
#   sort_rollno_by_marks(student_data, course1, course2, course3)
#       Return a list of rollnos sorted by marks in course1, then course2,
#       then course3 (ascending). Uses tuple key for tie-breaking.
#
#   count_students_by_cities(student_data)
#       Return dict of {city: number of students from that city}.
#
#   city_with_max_no_of_students(student_data)
#       Return the city name with the highest student count.
#
#   group_rollnos_by_cities(student_data)
#       Return dict of {city: sorted list of rollnos of students in that city}.
#
#   city_with_max_avg_course_mark(student_data, course)
#       Return the city with the highest average marks in a given course.
# -----------------------------------------------------------------------------

import random


def generate_student_data(n_students, courses, cities, random_seed=42):
    """Generate list of student dicts with rollno, city, and per-course marks."""
    random.seed(random_seed)
    return [
        {
            "rollno": i,
            "city": random.choice(cities),
            **{course: random.randint(1, 100) for course in courses}
        }
        for i in range(1, n_students + 1)
    ]


def groupby(data: list, key: callable):
    """Group list items into a dict by a key function."""
    result = {}
    for item in data:
        k = key(item)
        if k not in result:
            result[k] = []
        result[k].append(item)
    return result


def apply_to_groups(groups: dict, func: callable):
    """Apply func to the value list of each group. Returns new dict."""
    return dict(map(lambda kv: (kv[0], func(kv[1])), groups.items()))


def min_course_marks(student_data, course):
    """Return minimum marks in a given course."""
    return min(map(lambda s: s[course], student_data))


def max_course_marks(student_data, course):
    """Return maximum marks in a given course."""
    return max(map(lambda s: s[course], student_data))


def rollno_of_max_marks(student_data, course):
    """Return rollno of student with highest marks in a course."""
    return max(student_data, key=lambda s: s[course])["rollno"]


def sort_rollno_by_marks(student_data, course1, course2, course3):
    """Return rollnos sorted by course1, course2, course3 marks (ascending)."""
    sorted_students = sorted(
        student_data,
        key=lambda s: (s[course1], s[course2], s[course3])
    )
    return list(map(lambda s: s["rollno"], sorted_students))


def count_students_by_cities(student_data):
    """Return dict of {city: student count}."""
    return apply_to_groups(groupby(student_data, lambda s: s["city"]), len)


def city_with_max_no_of_students(student_data):
    """Return city name with the highest student count."""
    counts = count_students_by_cities(student_data)
    return max(counts.items(), key=lambda x: x[1])[0]


def group_rollnos_by_cities(student_data):
    """Return dict of {city: sorted list of rollnos}."""
    groups = groupby(student_data, lambda s: s["city"])
    return dict(
        map(
            lambda kv: (kv[0], sorted(map(lambda s: s["rollno"], kv[1]))),
            groups.items()
        )
    )


def city_with_max_avg_course_mark(student_data, course):
    """Return city with highest average marks in a given course."""
    groups      = groupby(student_data, lambda s: s["city"])
    avg_per_city = dict(
        map(
            lambda kv: (
                kv[0],
                sum(map(lambda s: s[course], kv[1])) / len(kv[1])
            ),
            groups.items()
        )
    )
    return max(avg_per_city.items(), key=lambda x: x[1])[0]


# --- driver code ---
if __name__ == "__main__":
    courses = input("enter course names (space-separated): ").split()
    cities  = input("enter city names  (space-separated): ").split()
    n       = int(input("enter number of students: "))

    student_data = generate_student_data(n, courses, cities)
    print("\ngenerated student data:")
    for s in student_data:
        print(s)

    course = input("\nenter a course name to query: ")
    print("min marks            :", min_course_marks(student_data, course))
    print("max marks            :", max_course_marks(student_data, course))
    print("rollno of max marks  :", rollno_of_max_marks(student_data, course))

    if len(courses) >= 3:
        c1, c2, c3 = courses[0], courses[1], courses[2]
        print("sorted rollnos       :", sort_rollno_by_marks(student_data, c1, c2, c3))

    print("students by city     :", count_students_by_cities(student_data))
    print("city max students    :", city_with_max_no_of_students(student_data))
    print("rollnos by city      :", group_rollnos_by_cities(student_data))
    print("city max avg marks   :", city_with_max_avg_course_mark(student_data, course))