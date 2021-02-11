

def create_outline():
    """
    TODO: implement your code here
    """ 
   
    print("Course Topics:")
    course_topics = set([
        "Introduction to Python",
        "Tools of the Trade",
        "How to make decisions",
        "How to repeat code",
        "How to structure data",
        "Functions",
        "Modules"
        ])
    for i in sorted(course_topics):
        print("*", i)

    print("Problems: ")
    problems = [
        'Problem 1',
        'Problem 2',
        'Problem 3'
    ]
    my_list = {}
    for item in course_topics:
        my_list[item] = problems
        print("*", item, ": " + ", ".join(my_list[item]))        

    print("Student Progress: ")
    problem = my_list[item]
    topic = sorted(list(course_topics))
    nr = ("1.", "2.", "3.", "4.", "5.", "6.", "7.")
    student_name = ("Tony", "Reed", "Johnny", "Logan", "James", "Peter", "Adam")
    s = ('[STARTED]', '[GRADED]', '[COMPLETED]')
    status = s
    st1 = (nr[0], student_name[2], topic[0], problem[0], s[0])
    st2 = (nr[1], student_name[4], topic[1], problem[0], s[0])
    st3 = (nr[2], student_name[1], topic[2], problem[1], s[1])
    st4 = (nr[3], student_name[3], topic[3], problem[1], s[1])
    st5 = (nr[4], student_name[5], topic[4], problem[2], s[2])
    st6 = (nr[5], student_name[0], topic[5], problem[2], s[2])

    st = [st1, st2, st3, st4, st5, st6]
    for nr, student_name, topic, problem, status in st:
        print("{} {} - {} - {} {}".format(nr, student_name, topic, problem, status))
        

if __name__ == "__main__":
    create_outline()
