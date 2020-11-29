import clsapp as cls
import json

def refresh_and_save():
    cls.start_session()
    courses = cls.get_courses()
    with open('courses.json', 'w') as json_file:
        json.dump({'Courses': courses}, json_file)

    all_due_tasks_list = []
    for course in courses:
        task_list = cls.get_due_tasks(course)
        course_name = course['name']
        task_dict = {}
        task_dict['courseName'] = course_name
        task_dict['task'] = task_list
        all_due_tasks_list.append(task_dict)
    print(all_due_tasks_list)
    with open('due_tasks.json', 'w') as json_file:
        json.dump({'Tasks Due': all_due_tasks_list}, json_file)

def get_courses_json():
    with open('courses.json', 'r') as json_file:
        courses = json.load(json_file)
        courses = courses["Courses"]
    return courses
