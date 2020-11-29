from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = [
'https://www.googleapis.com/auth/classroom.announcements',
'https://www.googleapis.com/auth/classroom.courses',
'https://www.googleapis.com/auth/classroom.coursework.me',
'https://www.googleapis.com/auth/classroom.courseworkmaterials',
'https://www.googleapis.com/auth/classroom.guardianlinks.me.readonly',
'https://www.googleapis.com/auth/classroom.profile.emails',
'https://www.googleapis.com/auth/classroom.profile.photos',
'https://www.googleapis.com/auth/classroom.push-notifications',
'https://www.googleapis.com/auth/classroom.rosters.readonly',
'https://www.googleapis.com/auth/classroom.student-submissions.me.readonly',
'https://www.googleapis.com/auth/classroom.topics.readonly',
]

service = None

def start_session():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes=SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    global service
    service = build('classroom', 'v1', credentials=creds)

def get_courses():
    # Call the Classroom API
    results = service.courses().list(studentId='me', courseStates='ACTIVE').execute()
    courses = results.get('courses', [])
    if not courses:
        print('No courses found.')
    else:
        return courses



#def get_students(course: dict):
    #results = service.courses().students().list(courseId=course['id']).execute()
    #return results

def get_courses():
    #Retrieves all course data where requester is student
    results = service.courses().list(studentId='me', courseStates='ACTIVE').execute()
    courses = results.get('courses', [])
    return courses

def get_coursework(course: dict):
    #takes a course dict input, and returns all coursework info; a list of dictionaries
    the_courseid = course['id']
    results = service.courses().courseWork().list(courseId=the_courseid).execute()
    all_course_work = results.get('courseWork', [])
    return all_course_work

def get_due_tasks(course: dict):
    #takes a course dict input, and returns all non-turned in or returned tasks as a list
    all_course_work = get_coursework(course)
    all_course_work_ids = []
    for task in all_course_work:
        the_id = task['id']
        all_course_work_ids.append(the_id)
    due_tasks = []
    for course_work_id in all_course_work_ids:
        results = service.courses().courseWork().studentSubmissions().list(courseId = course['id'] ,courseWorkId=course_work_id).execute()
        submission = results.get('studentSubmissions', [])[0]
        sub_state = submission['state']
        #checks if task has not been submitted
        if sub_state != "TURNED_IN" and sub_state != "RETURNED":
            task = service.courses().courseWork().get(courseId=course['id'], id=course_work_id).execute()
            #due_tasks[task['title']] = task
            due_tasks.append(task)
    return due_tasks

def get_teachers(course:dict):
    #takes a course dict input, and returns all teachers of that course
    results = service.courses().teachers().list(courseId = course['id']).execute()
    teachers = results.get('teachers', [])
    course_teachers = {}
    for teacher in teachers:
        teacher_name = teacher['profile']['name']['fullName']
        course_teachers[teacher_name] = teacher
    return course_teachers

def get_coursework_links(course: dict):
    all_course_work = get_coursework(course)
    links = []
    for task in all_course_work:
        links.append(task['alternateLink'])
    return links

