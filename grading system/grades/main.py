#simple program to imitate grading system

def grades(marks):

    marks = int(input('Enter marks'))
    if(marks > 100):
        print('invalid input')
    elif(marks >= 80 and marks):
        print('A')
        print('Excellent!')
    elif(marks >= 60 and marks <= 79):
        print('B')
        print('Good')
    elif (marks >= 50 and marks <= 59):
        print('C')
        print('Fair')
    elif(marks >= 40 and marks <= 49):
        print('D')
        print('Pass')
    elif(marks < 40):
        print('E')
        print('Failed!, Repeat')
    else:
        print('Missing marks')





if __name__ == '__main__':
    grades("marks")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
