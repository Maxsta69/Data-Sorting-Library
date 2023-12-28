# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Roland Neill Max Bui Ethan Van Diepen Jacky Chen"

# Update "" with your team (e.g. T102)
__team__ = "T142"

# ========================================== #
# Place your sort_students_age_bubble function after this line


def sort_students_age_bubble(students: list, order) -> list:
    """
    This function sorts students list in ascending or descending order based on there Age.
    If the Age key is not in the dictionary the function will print out a statement.

    Preconditions: order = A or D

    Examples:

    >>> sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]

    >>> sort_students_age_bubble([{"Age":20,"School":"GP"},{"Age":19,"School":"MS"}], "A")
    [{"Age": 19, "School":"MS"}, {"Age":20, "School":"GP"}]

    >>> sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    "Age" key is not present.
    [{"School":"GP"}, {"School":"MS"}]
    """
    for k in range(len(students)):
        if "Age" not in students[k]:
            print('"Age" key is not present.')
            return students

    for i in range(len(students)):
        ordered = True
        for j in range(len(students) - 1 - i):
            if students[j]["Age"] > students[j + 1]["Age"]:
                students[j], students[j + 1] = students[j + 1], students[j]
                ordered = False
        if ordered:
            break

    if order in ("A", "a"):
        return students

    elif order in ("D", "d"):
        return students[::-1]


# ========================================== #
# Place your sort_students_time_selection function after this line


def sort_students_time_selection(students: list[dict], order: str) -> list[dict]:
    """Returns ordered list of StudyTime, in either ascending or descending.

    Preconditions: Order must be either A or D, students["StudyTime"] == int, float

    >>> sort_students_time_selection ( [{"StudyTime":-0.2,"School":"GP"}, {"StudyTime":0.1,"School":"MS"}], "D")
    [{"StudyTime": 0.1, "School":"MG"}, {"StudyTime":-0.2, "School":"NH"}]

    >>>sort_students_time_selection([{"School":"NH"},{"School":"MG"}], "A")
    "StudyTime" key is not present
    [{"School":"NH"}, {"School":"MG"}]

    >>>sort_students_time_selection([{"StudyTime":-0.2,"School":"GP"}, {"StudyTime":0.1,"School":"MS"}, {"StudyTime": 2,"School":"GP"}, {"StudyTime": -11,"School":"MS"}], "A")
    [{"StudyTime": -11,"School":"MG"}, {"StudyTime":-0.2,"School":"NH"}, {"StudyTime": 0.1,"School":"MG"}, {"StudyTime": 2,"School":"NH"}]

    """
    if all('StudyTime' in attributes for attributes in students):
        for i in range(len(students)):
            min_idx = i
            for j in range(i + 1, len(students)):
                if order == 'A' or order == 'a':
                    if students[j]['StudyTime'] < students[min_idx]['StudyTime']:
                        min_idx = j
                        students[i], students[min_idx] = students[min_idx], students[i]
                elif order == 'D' or order == 'd':
                    if students[j]['StudyTime'] > students[min_idx]['StudyTime']:
                        min_idx = j
                        students[i], students[min_idx] = students[min_idx], students[i]
        return students
    else:
        print("\"StudyTime\" key is not present")
        return students

# ========================================== #
# Place your sort_students_g_avg_insertion function after this line


def sort_students_g_avg_insertion(lst: list[dict[str, any]], order: str) -> list[dict[str, any]]:
    """Returns a list of dictionaries sorted according to the G_Avg value in the dictionary
    with the same entries as the input. Sorts in ascending order of 'A' is passes as parameter
    order, sorts in descending order if 'D' is passed. If G_Avg key is not present it will
    print an error message and return the original list.

    Preconditions:
        Dictionary contains G_Avg as a key
        type(dict['G_AVG']) == float, int

    list_1 = [{'Name': 'A', 'G_Avg': 5.9}, {'Name': 'B', 'G_Avg': 0}, {'Name': 'C', 'G_Avg':
    10}]

    list_2 = [{'Name': 'A', 'Avg': 5.9}, {'Name': 'B', 'Avg': 0}, {'Name': 'C', 'Avg': 10}]

    >>> sort_students_g_avg_insertion(list_1, 'A')
    [{'Name': 'B', 'G_Avg': 0}, {'Name': 'A', 'G_Avg': 5.9}, {'Name': 'C', 'G_Avg': 10}]

    >>> sort_students_g_avg_insertion(list_1, 'D')
    [{'Name': 'C', 'G_Avg': 10}, {'Name': 'A', 'G_Avg': 5.9}, {'Name': 'B', 'G_Avg': 0}]

    >>> sort_students_g_avg_insertion(list_2, 'A')
    '"G_Avg" key is not present'
    [{'Name': 'A', 'Avg': 5.9}, {'Name': 'B', 'Avg': 0}, {'Name': 'C', 'Avg': 10}]
    """
    if 'G_Avg' in lst[0]:
        if order in ('A', 'a'):
            for i in range(1, len(lst)):
                key = lst[i]
                j = i - 1
                while j >= 0 and key['G_Avg'] < lst[j]['G_Avg']:
                    lst[j + 1] = lst[j]
                    j -= 1
                lst[j + 1] = key
            return lst
        elif order in ('D', 'd'):
            for i in range(1, len(lst)):
                key = lst[i]
                j = i - 1
                while j >= 0 and key['G_Avg'] > lst[j]['G_Avg']:
                    lst[j + 1] = lst[j]
                    j -= 1
                lst[j + 1] = key
            return lst
    else:
        print('“G_Avg” key is not present')
        return lst

# ========================================== #
# Place your sort_students_failures_bubble function after this line


def sort_students_failures_bubble(dict_list: list[dict], order: str) -> list[dict]:
    """Given a list of dictionaries, return the sorted list in ascending/descending
    order using the bubble sort based on the value in the "Failures" key of the
    dictionary. If the "Failures" key is not present in the list of dictionaries,
    it prints that the key is not present and returns the given list of dictionaries.

    A = Ascending order
    D = Descending order

    Preconditions: order == "A" or order == "D"

    >>> sort_students_failures_bubble(student_school_list("student-test.csv", "CF"), "D")
    [{'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7},
    {'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0},
    {'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}]

    >>> sort_students_failures_bubble(student_school_list("student-test.csv", "CF"), "A")
    [{'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12},
    {'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7},
    {'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}]

    >>> sort_students_failures_bubble(student_failures_list("student-test.csv", 2), "A")
    "Failures" key is not present.
    [{'School': 'CF', 'StudyTime': 5.0, 'Age': 15, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7},
    {'School': 'CF', 'StudyTime': 1.0, 'Age': 17, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}]

    >>> sort_students_failures_bubble(student_failures_list("student-test.csv", 2), "D")
    "Failures" key is not present.
    [{'School': 'CF', 'StudyTime': 5.0, 'Age': 15, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7},
    {'School': 'CF', 'StudyTime': 1.0, 'Age': 17, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}]

    >>> sort_students_failures_bubble([{"Failures":10, "School":"GP"}, {"Failures":19, "School":"MS"}], "A")
    [{'Failures': 10, 'School': 'MS'}, {'Failures': 19, 'School': 'GP'}]

    >>> sort_students_failures_bubble([{"Failures":10, "School":"GP"}, {"Failures":19, "School":"MS"}], "D")
    [{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]

    >>> sort_students_failures_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    "Failures" key is not present.
    [{'School': 'GP'}, {'School': 'MS'}]
    """

    # Initializes variables
    copy = dict_list.copy()
    swap = True

    # Checks if the first key contains "Failures", if not it prints that it is not present and returns the given list of dictionaries
    if copy[0].get("Failures") is None:
        print("\"Failures\" key is not present.")
        return dict_list

    # Returns list of dictionaries in acsending order of failures using bubble sort
    if (order == "A") or (order == "a"):
        while swap:
            swap = False
            for i in range(1, len(dict_list)):
                if (copy[i].get("Failures") < copy[i - 1].get("Failures")):
                    temp = copy[i]
                    copy[i] = copy[i - 1]
                    copy[i - 1] = temp
                    swap = True

    # Returns list of dictionaries in decsending order of failures using bubble sort
    if (order == "D") or (order == "d"):
        while swap:
            swap = False
            for i in range(1, len(dict_list)):
                if (copy[i].get("Failures") > copy[i - 1].get("Failures")):
                    temp = copy[i]
                    copy[i] = copy[i - 1]
                    copy[i - 1] = temp
                    swap = True
    return copy  # Returns the sorted list

# ========================================== #
# Place your sort_by_key function after this line


def sort(input_lst: list[dict[str, any]], sort_order: str, sort_filter: str) -> list[dict[str, any]]:
    """Returns the input list of dictionaries sorted by ascending order if sort_order is passed as "A" or
    descending of sort_order is "D". the list is sorted accoring to "Age", "StudyTime", "G_Avg", or "Failures"
    depending on the value of sort_filter. If the sort_filtert value is not a valid parameter it
    prints 'Invalid Parameter: Can not be sorted by "sort_filter"' and returns the original list.

    >>> sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}], "D", "Age")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]

    >>> sort([{"School":"GP"}, {"School":"MS"}], "D", "School")
    Cannot be sorted by "School"
    [{"School":"GP"}, {"School":"MS"}]
    """

    if sort_filter == 'Age' or sort_filter == 'age':
        result = sort_students_age_bubble(input_lst, sort_order)
        return result
    elif sort_filter == 'StudyTime' or sort_filter == 'studytime' or sort_filter == 'studyTime':
        return sort_students_time_selection(input_lst, sort_order)
    elif sort_filter == 'G_Avg' or sort_filter == 'g_Avg' or sort_filter == 'G_avg':
        return sort_students_g_avg_insertion(input_lst, sort_order)
    elif sort_filter == 'Failures' or sort_filter == 'failures':
        return sort_students_failures_bubble(input_lst, sort_order)
    else:
        print('Invalid Parameter: Can not be sorted by "', sort_filter, '"', sep='')
        return input_lst


# Do NOT include a main script in your submission
