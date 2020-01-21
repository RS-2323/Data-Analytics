
"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""

#take input from user their first assignments marks 

assignments_1=float(input("enter your first assignments marks>"))

#take input from user their second assignments marks 

assignments_2=float(input("enter your second assignments marks>"))

#take input from user their third assignments marks 

assignments_3=float(input("enter your third assignments marks>"))

#take input from user their first examination marks

exam_1=float((input("enter your first exam marks>")))

#take input from user their second examination marks

exam_2=float((input("enter your second exam marks>")))

#Here we discribe respective weighted
assignments_1_weighted=.1
assignments_2_weighted=.1
assignments_3_weighted=.1

exam_1_weighted=.35
exam_2_weighted=.35

#Now we finally calculate weighted score

weighted_score = round( assignments_1 + assignments_2 + assignments_3 ) *assignments_1_weighted + (exam_1 + exam_2 ) *exam_1_weighted

#Now we print finally calculate weighted score
print ("finally calculate weighted score={}".format(weighted_score))