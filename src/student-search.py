#!/usr/local/bin/python3


import requests
import sys
import os
import pandas as pd
from dotenv import load_dotenv
from utils import bytetodict
from utils import get_user_id
from utils import url_join
from utils import error
from utils import print_infos
import json
import smtplib, ssl


dict_seats_one = {1: 'lab1r1s1',
              2: 'lab1r1s3',
              3: 'lab1r1s5',
              4: 'lab1r1s7',
              5: 'lab1r1s8',
              6: 'lab1r1s10',
              7: 'lab1r1s12',
              8: 'lab1r1s14',
              9: 'lab1r2s1',
              10: 'lab1r2s3',
              11: 'lab1r2s5',
              12: 'lab1r2s7',
              13: 'lab1r2s8',
              14: 'lab1r2s10',
              15: 'lab1r2s12',
              16: 'lab1r2s14',
              17: 'lab1r3s1',
              18: 'lab1r3s3',
              19: 'lab1r3s5',
              20: 'lab1r3s7',
              21: 'lab1r3s8',
              22: 'lab1r3s10',
              23: 'lab1r3s12',
              24: 'lab1r3s14',
              25: 'lab1r4s1',
              26: 'lab1r4s3',
              27: 'lab1r4s5',
              28: 'lab1r4s7',
              29: 'lab1r4s8',
              30: 'lab1r4s10',
              31: 'lab1r4s12',
              32: 'lab1r4s14',
              33: 'lab1r5s1',
              34: 'lab1r5s3',
              35: 'lab1r5s5',
              36: 'lab1r5s7',
              37: 'lab1r5s8',
              38: 'lab1r5s10',
              39: 'lab1r5s12',
              40: 'lab1r5s14',
              }

dict_seats_one_rev = {1: 'lab1r1s2',
              2: 'lab1r1s4',
              3: 'lab1r1s6',
              4: 'lab1r1s9',
              5: 'lab1r1s11',
              6: 'lab1r1s13',
              7: 'lab1r2s2',
              8: 'lab1r2s4',
              9: 'lab1r2s6',
              10: 'lab1r2s9',
              11: 'lab1r2s11',
              12: 'lab1r2s13',
              13: 'lab1r3s2',
              14: 'lab1r3s4',
              15: 'lab1r3s6',
              16: 'lab1r3s9',
              17: 'lab1r3s11',
              18: 'lab1r3s13',
              19: 'lab1r4s2',
              20: 'lab1r4s4',
              21: 'lab1r4s6',
              22: 'lab1r4s9',
              23: 'lab1r4s11',
              24: 'lab1r4s13',
              25: 'lab1r5s2',
              26: 'lab1r5s4',
              27: 'lab1r5s6',
              28: 'lab1r5s9',
              29: 'lab1r5s11',
              30: 'lab1r5s13',
              }


dict_seats_two = {1: 'lab2r1s1',
              2: 'lab2r1s3',
              3: 'lab2r1s5',
              4: 'lab2r1s7',
              5: 'lab2r1s8',
              6: 'lab2r1s10',
              7: 'lab2r1s12',
              8: 'lab2r1s14',
              9: 'lab2r2s1',
              10: 'lab2r2s3',
              11: 'lab2r2s5',
              12: 'lab2r2s7',
              13: 'lab2r2s8',
              14: 'lab2r2s10',
              15: 'lab2r2s12',
              16: 'lab2r2s14',
              17: 'lab2r3s1',
              18: 'lab2r3s3',
              19: 'lab2r3s5',
              20: 'lab2r3s7',
              21: 'lab2r3s8',
              22: 'lab2r3s10',
              23: 'lab2r3s12',
              24: 'lab2r3s14',
              25: 'lab2r4s1',
              26: 'lab2r4s3',
              27: 'lab2r4s5',
              28: 'lab2r4s7',
              29: 'lab2r4s8',
              30: 'lab2r4s10',
              31: 'lab2r4s12',
              32: 'lab2r4s14',
              }

dict_seats_two_rev = {1: 'lab2r1s2',
              2: 'lab2r1s4',
              3: 'lab2r1s6',
              4: 'lab2r1s9',
              5: 'lab2r1s11',
              6: 'lab2r1s13',
              7: 'lab2r2s2',
              8: 'lab2r2s4',
              9: 'lab2r2s6',
              10: 'lab2r2s9',
              11: 'lab2r2s11',
              12: 'lab2r2s13',
              13: 'lab2r3s2',
              14: 'lab2r3s4',
              15: 'lab2r3s6',
              16: 'lab2r3s9',
              17: 'lab2r3s11',
              18: 'lab2r3s13',
              19: 'lab2r4s2',
              20: 'lab2r4s4',
              21: 'lab2r4s6',
              22: 'lab2r4s9',
              23: 'lab2r4s11',
              24: 'lab2r4s13',
              }

dict_seats_three = {1: 'lab3r1s1',
              2: 'lab3r1s3',
              3: 'lab3r1s5',
              4: 'lab3r1s7',
              5: 'lab3r1s8',
              6: 'lab3r1s10',
              7: 'lab3r1s12',
              8: 'lab3r1s14',
              9: 'lab3r2s1',
              10: 'lab3r2s3',
              11: 'lab3r2s5',
              12: 'lab3r2s7',
              13: 'lab3r2s8',
              14: 'lab3r2s10',
              15: 'lab3r2s12',
              16: 'lab3r2s14',
              17: 'lab3r3s1',
              18: 'lab3r3s3',
              19: 'lab3r3s5',
              20: 'lab3r3s7',
              21: 'lab3r3s8',
              22: 'lab3r3s10',
              23: 'lab3r3s12',
              24: 'lab3r3s14',
              25: 'lab3r4s1',
              26: 'lab3r4s3',
              27: 'lab3r4s5',
              28: 'lab3r4s7',
              29: 'lab3r4s8',
              30: 'lab3r4s10',
              31: 'lab3r4s12',
              32: 'lab3r4s14',
              33: 'lab3r5s1',
              34: 'lab3r5s3',
              35: 'lab3r5s5',
              36: 'lab3r5s7',
              37: 'lab3r5s8',
              38: 'lab3r5s10',
              39: 'lab3r5s12',
              40: 'lab3r5s14',
              41: 'lab3r6s1',
              42: 'lab3r6s3',
              43: 'lab3r6s5',
              44: 'lab3r6s7',
              45: 'lab3r6s8',
              46: 'lab3r6s10',
              47: 'lab3r6s12',
              48: 'lab3r6s14',
              49: 'lab3r7s1',
              50: 'lab3r7s3',
              51: 'lab3r7s5',
              52: 'lab3r7s7',
              53: 'lab3r7s8',
              54: 'lab3r7s10',
              55: 'lab3r7s12',
              56: 'lab3r7s14',
              57: 'lab3r8s1',
              58: 'lab3r8s3',
              59: 'lab3r8s5',
              60: 'lab3r8s7',
              61: 'lab3r8s8',
              62: 'lab3r8s10',
              63: 'lab3r8s12',
              64: 'lab3r8s14',
              }


dict_seats_three_rev = {1: 'lab3r1s2',
              2: 'lab3r1s4',
              3: 'lab3r1s6',
              4: 'lab3r1s9',
              5: 'lab3r1s11',
              6: 'lab3r1s13',
              7: 'lab3r2s2',
              8: 'lab3r2s4',
              9: 'lab3r2s6',
              10: 'lab3r2s9',
              11: 'lab3r2s11',
              12: 'lab3r2s13',
              13: 'lab3r3s2',
              14: 'lab3r3s4',
              15: 'lab3r3s6',
              16: 'lab3r3s9',
              17: 'lab3r3s11',
              18: 'lab3r3s13',
              19: 'lab3r4s2',
              20: 'lab3r4s4',
              21: 'lab3r4s6',
              22: 'lab3r4s9',
              23: 'lab3r4s11',
              24: 'lab3r4s13',
              25: 'lab3r5s2',
              26: 'lab3r5s4',
              27: 'lab3r5s6',
              28: 'lab3r5s9',
              29: 'lab3r5s11',
              30: 'lab3r5s13',
              31: 'lab3r6s2',
              32: 'lab3r6s4',
              33: 'lab3r6s6',
              34: 'lab3r6s9',
              35: 'lab3r6s11',
              36: 'lab3r6s13',
              37: 'lab3r7s2',
              38: 'lab3r7s4',
              39: 'lab3r7s6',
              40: 'lab3r7s9',
              41: 'lab3r7s11',
              42: 'lab3r7s13',
              43: 'lab3r8s2',
              44: 'lab3r8s4',
              45: 'lab3r8s6',
              46: 'lab3r8s9',
              47: 'lab3r8s11',
              48: 'lab3r8s13',
              }
# Funcao que requere a token, versao em python do cURL disponibilizado pelo API
# tambem faz o tratamento de dados para retornar somente a token
def get_token():
    load_dotenv()
    data = {
      'grant_type': 'client_credentials',
      'client_id': os.getenv("CLIENT_ID"),
      'client_secret': os.getenv("CLIENT_SECRET")
    }
    response = requests.post('https://api.intra.42.fr/oauth/token', data=data)
    token = bytetodict(response.content)
    print(token)
    return token['access_token']


# Grava a token e user_id e define o header que sera enviado na requisicao,
# analisa erros de input, pega a flag recebida e define o endpoint para
# requisitar os dados do usuario. Converte a resposta do servidor em DataFrame
# e manda imprimir.

def user_in_abuDhabi(user_login, headers):
    endpoint = '/users/%s/' % user_login
    url = url_join(endpoint)
    response = requests.get(url, headers=headers)
    temp = response.json()
    # print(json.dumps(temp, indent=4))
    if temp['campus'][0]['id'] == 43:
        return True

def check_where_exam(headers):
    endpoint = '/campus/%s/exams/' % 43
    url = url_join(endpoint)
    response = requests.get(url, headers=headers)
    temp = response.json()
    # print(temp[0]['location'])
    Lab = []
    for x in temp[0]['location']:
        print(x)
        if (x == '1'):
            Lab.append(1)
        if (x == '2'):
            Lab.append(2)
        if (x == '3'):
            Lab.append(2)
    return Lab

def lab_one_strategy(students, studentnames, headers):   
    labone = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labonecapacity = 40
    num_students = len(students)
    student_name = list(students)
    # print(student_name)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    print(j)
    rev = j
    i = 1
    back = 0
    while (i <= num_students and i <= labonecapacity):
        # if (labone[i] == 0):
        j = 1
        if (back == 0):
            while (labone[j-1] != 0):
                j+=1
            students[student_name[rev]] = dict_seats_one[j]
            endpoint = '/users/%s/locations' % studentnames[rev][0]
            print(studentnames[rev][0])
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (j == 1):
                students[student_name[rev]] = response.json()[0]['host']
            if (response.json()[0]['host'] == students[student_name[rev]]):
                students[student_name[rev]] = dict_seats_one[j + 1]
                labone[j] = 1
                back +=2
            else:
                labone[j -1] = 1
                back +=1
            rev+=1
            # nums -= 1
        else:
            while (labone[j-1] != 0):
                j+=1
            students[student_name[nums]] = dict_seats_one[j]
            endpoint = '/users/%s/locations' % studentnames[nums][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (response.json()[0]['host'] == students[student_name[nums]]):
                students[student_name[nums]] = dict_seats_one[j + 1]
                labone[j] = 1
            else:
                labone[j -1] = 1
            back -=1
            nums -= 1
        i+=1
    # print(labone)
    # print(num_students -i +1)
    return num_students - i +1

def lab_two_strategy(students):   
    labtwo = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labtwocapacity = 32
    num_students = len(students)
    student_name = list(students)
    # print(student_name)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    while (i <= num_students and i <= labtwocapacity):
        # if (labone[i] == 0):
        if ((i -1) % 2 == 0):
            labtwo[i -1] = 1
            students[student_name[rev]] = dict_seats_two[i]
            rev+=1
            # nums -= 1
        else:
            labtwo[i - 1] = 1
            students[student_name[nums]] = dict_seats_two[i]
            nums -= 1
        i+=1
    # print(labtwo)
    # print(num_students -i +1)
    return num_students - i +1
        
def lab_three_strategy(students):   
    labthree = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labthreecapacity = 64
    num_students = len(students)
    student_name = list(students)
    # print(student_name)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    while (i <= num_students and i <= labthreecapacity):
        # if (labone[i] == 0):
        if ((i -1) % 2 == 0):
            labthree[i -1] = 1
            students[student_name[rev]] = dict_seats_three[i]
            rev+=1
            # nums -= 1
        else:
            labthree[i - 1] = 1
            students[student_name[nums]] = dict_seats_three[i]
            nums -= 1
        i+=1
    # print(labthree)
    # print(num_students -i +1)
    return num_students - i +1

# ------------------------------------------------------------------------------------------------
def lab_one_carryover_strategy(students):   
    labone = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labonecapacity = 30
    num_students = len(students)
    student_name = list(students)
    # print(student_name)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    while (i <= num_students and i <= labonecapacity):
        # if (labone[i] == 0):
        if ((i -1) % 2 == 0):
            labone[i -1] = 1
            students[student_name[rev]] = dict_seats_one_rev[i]
            rev+=1
            # nums -= 1
        else:
            labone[i - 1] = 1
            students[student_name[nums]] = dict_seats_one_rev[i]
            nums -= 1
        i+=1
    # print(labone)
    # print(num_students -i +1)
    return num_students - i +1

def lab_two_carryover_strategy(students):   
    labtwo = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labtwocapacity = 24
    num_students = len(students)
    student_name = list(students)
    # print(student_name)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    while (i <= num_students and i <= labtwocapacity):
        # if (labone[i] == 0):
        if ((i -1) % 2 == 0):
            labtwo[i -1] = 1
            students[student_name[rev]] = dict_seats_two_rev[i]
            rev+=1
            # nums -= 1
        else:
            labtwo[i - 1] = 1
            students[student_name[nums]] = dict_seats_two_rev[i]
            nums -= 1
        i+=1
    # print(labtwo)
    # print(num_students -i +1)
    return num_students - i +1
        
def lab_three_carryover_strategy(students):   
    labthree = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labthreecapacity = 48
    num_students = len(students)
    student_name = list(students)
    # print(student_name)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    while (i <= num_students and i <= labthreecapacity):
        # if (labone[i] == 0):
        if ((i -1) % 2 == 0):
            labthree[i -1] = 1
            students[student_name[rev]] = dict_seats_three_rev[i]
            rev+=1
            # nums -= 1
        else:
            labthree[i - 1] = 1
            students[student_name[nums]] = dict_seats_three_rev[i]
            nums -= 1
        i+=1
    # print(labthree)
    # print(num_students -i +1)
    return num_students - i +1
        
        
        # for i in range(0,5):
        #     for j in range(0,8):
        #         if (labone[i][j] == 0):
        #             if (j % 2 == 0):
        #                 labone[i][j] = 1
        #                 students[student_name[rev]][i][j] = 1
        #                 rev+=1
        #                 num_students -= 1
        #                 break
        #             else:
        #                 labone[i][j] = students.keys([num_students])
        #                 num_students -= 1
        #                 break
    
       
    
def exam_search(i, headers,students, studentnames):
    j = 1
    # endpoint = '/campus/%s/exams/' % 43
    # endpoint = '/users/%s/' % user_id
    endpoint = '/projects/%s/projects_users?filter[status]=in_progress&filter[campus]=43&page[100]&page=%i' % ((1319 + i), (j))
    url = url_join(endpoint)
    response = requests.get(url, headers=headers)
    temp = response.json()
    temp1 = response.json()
    while (bool(temp1)):
        print(i)
        j+=1
        endpoint = '/projects/%s/projects_users?filter[status]=in_progress&filter[campus]=43&page=%i' % ((1319 + i), (j))
        url = url_join(endpoint)
        response = requests.get(url, headers=headers)
        temp1 = response.json()
        if (temp1):
            temp += response.json()
    # endpoint2 = '/projects/%s/projects_users?filter[status]=in_progress&filter[campus]=43&page[100]&page=2' % (1320)
    # response = bytetodict(response.content)
    # if response == {}:
    #     error('Login not found')
    # df = pd.Series(response)
    # print_infos(df, flag)
    # print(response.json())
    with open("data_file2.json", "w") as write_file:
       json.dump(temp, write_file, indent=4)
    with open("data_file2.json", "r") as read_file:
       decoded_hand = json.load(read_file)
    print('This is exam number %s' % (i + 2))
    for x in decoded_hand:
        if (user_in_abuDhabi(x['user']['login'], headers)):
            if (x['status'] == 'in_progress' and x['validated?'] != True):
            # if ( x['validated?'] == True):
                students[x['user']['email']]= '0'
                studentnames.append([x['user']['login']])
                # print(x)
                # print('\n')
    # for x in decoded_hand:
    #     if (user_in_abuDhabi(x['user']['login'], headers)):
    #         if (x['validated?'] != True):
    #             students.append(x['user']['login'])
    #             print(x['user']['email'])
    #             print('\n')
    # print(json.dumps(decoded_hand, indent=4))


def randomize_students(students, lab, studentnames,headers):
    carry_over = 1
    for x in lab:
        if (x == 1 and carry_over):
            carry_over = lab_one_strategy(students,studentnames,headers)
            print('Lab 1')
        if (x == 3 and carry_over):
            carry_over = lab_three_strategy(students,studentnames,headers)
            print('Lab 3')
        if (x == 2 and carry_over):
            carry_over = lab_two_strategy(students,studentnames,headers)
            print('Lab 2')
    for x in lab:
        if (x == 1 and carry_over):
            carry_over = lab_one_carryover_strategy(students,studentnames,headers)
            print('Lab 1')
        if (x == 3 and carry_over):
            carry_over = lab_three_carryover_trategy(students,studentnames,headers)
            print('Lab 3')
        if (x == 2 and carry_over):
            carry_over = lab_two_carryover_strategy(students,studentnames,headers)
            print('Lab 2')

def student_search():
    token = get_token()
    headers = {'Authorization': 'Bearer %s' % token}
    # endpoint = '/users/ihormi' 
    # url = url_join(endpoint)
    # response = requests.get(url, headers=headers)
    # # temp = response.json()
    # print(json.dumps(response.json(), indent=4))
    # endpoint = '/campus/43/events' 
    # url = url_join(endpoint)
    # response = requests.get(url, headers=headers)
    # # temp = response.json()
    # print(json.dumps(response.json(), indent=4))
    students = {}
    studentnames = []
    for i in range(1,5):
         exam_search(i, headers, students, studentnames)
    # exam_search(1, headers, user_id, students)
    lab = check_where_exam(headers)
    randomize_students(students, lab, studentnames, headers)
    print(studentnames)
    return students




def main():
    students = student_search()
    # print(students)
    # students = {"marcos@42abudhabi.ae":"lab3r3s12", "hammoudeh.ahmad@hotmail.com":"Lab2"}
    
    # SenderAddress = "42adtestemail@gmail.com"
    # password = "uzpbberomtdewpnv"

    # emails = list(students)
    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.starttls()
    # server.login(SenderAddress, password)
    # subject = "EXAM SEATING"
    # for email in emails:
    #     msg = "Your Assigned Seats is %s \n" % students[email]
    #     body = "Subject: {}\n\n{}".format(subject,msg)
    #     server.sendmail(SenderAddress, email, body)
    # server.quit()


if __name__ == "__main__":
    main()
