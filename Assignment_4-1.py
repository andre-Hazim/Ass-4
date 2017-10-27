
# Created by Andre on Oct 2017
# This shows what career I could have


import ui

def career_button_touch_up_inside(sender):
    # This is to expain the first part of the assignment.
    view['career_label'].text = "Programmer"
    view['description_label'].text = "Computer programmers typically do the following: Write programs in a variety of computer languages, such as C++ and Java. Update and expand existing programs. Debug programs by testing for and fixing errors. Build and use computer-assisted software engineering (CASE) tools to automate the writing of some code."
    view['requirements_label'].text = "Certificate or associate's degree with considerable work experience; bachelor's degree most often required; master's degree for some jobs."
    view['growth_label'].text = "It is predicted that there will be a -8% growth for 2014 - 2024."
    view['salary_label'].text = "The 2015 median was $79,530 annually."
    view['opinon_label'].text = "I would like to have the job of a programmer because it is something I enjoy doing."
def education_button_touch_up_inside(sender):
     view['school_label'].text = "Queen's University" 
     view['required_education_label'].text = "Secondary School Education."
     view['school_description_label'].text = "This is a 120 unit (4 year) program. A full year course (indicated by /6.0) is worth 6 units and a half-course counts as 3.0 units. Introduction to Computing Science I, Introduction to Computing Science II, Discrete Math I, Linear Algebra, Linear Algebra"
     view['time_label'].text = "It will take four years to complete the course."
def religon_button_touch_up_inside(sender):
     view['religon_label'].text = "I am fufilling Gods word by making life easier for others by creating programs."
     
     


view = ui.load_view()
view.present('fullscreen')
