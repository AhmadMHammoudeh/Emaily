#!/usr/local/bin/python3


import requests
import sys
import os
import csv
import pandas as pd
from dotenv import load_dotenv
from utils import get_user_id
from utils import url_join
from utils import dict_seats_one
from utils import dict_seats_two
from utils import dict_seats_three
from utils import dict_seats_one_rev
from utils import dict_seats_two_rev
from utils import dict_seats_three_rev
from utils import bytetodict
import json
import smtplib, ssl



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
    # print(token)
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
        # print(x)
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
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    back = 0
    while (i <= num_students and i <= labonecapacity):
        j = 1
        if (back == 0):
            while (labone[j-1] != 0):
                j+=1
            students[student_name[rev]] = dict_seats_one[j]
            endpoint = '/users/%s/locations' % studentnames[rev][0]
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
    return num_students - i +1

def lab_two_strategy(students, studentnames, headers):   
    labtwo = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labtwocapacity = 32
    num_students = len(students)
    student_name = list(students)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    back = 0
    while (i <= num_students and i <= labtwocapacity):
        # if (labtwo[i] == 0):
        j = 1
        if (back == 0):
            while (labtwo[j-1] != 0):
                j+=1
            students[student_name[rev]] = dict_seats_two[j]
            endpoint = '/users/%s/locations' % studentnames[rev][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (j == 1):
                students[student_name[rev]] = response.json()[0]['host']
            if (response.json()[0]['host'] == students[student_name[rev]]):
                students[student_name[rev]] = dict_seats_two[j + 1]
                labtwo[j] = 1
                back +=2
            else:
                labtwo[j -1] = 1
                back +=1
            rev+=1
        else:
            while (labtwo[j-1] != 0):
                j+=1
            students[student_name[nums]] = dict_seats_two[j]
            endpoint = '/users/%s/locations' % studentnames[nums][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (response.json()[0]['host'] == students[student_name[nums]]):
                students[student_name[nums]] = dict_seats_two[j + 1]
                labtwo[j] = 1
            else:
                labtwo[j -1] = 1
            back -=1
            nums -= 1
        i+=1
    return num_students - i +1
        
def lab_three_strategy(students, studentnames, headers):   
    labthree = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labthreecapacity = 64
    num_students = len(students)
    student_name = list(students)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    back = 0
    while (i <= num_students and i <= labthreecapacity):
        j = 1
        if (back == 0):
            while (labthree[j-1] != 0):
                j+=1
            students[student_name[rev]] = dict_seats_three[j]
            endpoint = '/users/%s/locations' % studentnames[rev][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (j == 1):
                students[student_name[rev]] = response.json()[0]['host']
            if (response.json()[0]['host'] == students[student_name[rev]]):
                students[student_name[rev]] = dict_seats_three[j + 1]
                labthree[j] = 1
                back +=2
            else:
                labthree[j -1] = 1
                back +=1
            rev+=1
            # nums -= 1
        else:
            while (labthree[j-1] != 0):
                j+=1
            students[student_name[nums]] = dict_seats_three[j]
            endpoint = '/users/%s/locations' % studentnames[nums][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (response.json()[0]['host'] == students[student_name[nums]]):
                students[student_name[nums]] = dict_seats_three[j + 1]
                labthree[j] = 1
            else:
                labthree[j -1] = 1
            back -=1
            nums -= 1
        i+=1
    return num_students - i +1

# ------------------------------------------------------------------------------------------------
def lab_one_carryover_strategy(students, studentnames, headers):   
    labone = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labonecapacity = 30
    num_students = len(students)
    student_name = list(students)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    back = 0
    while (i <= num_students and i <= labonecapacity):
        j = 1
        if (back == 0):
            while (labone[j-1] != 0):
                j+=1
            students[student_name[rev]] = dict_seats_one_rev[j]
            endpoint = '/users/%s/locations' % studentnames[rev][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (j == 1):
                students[student_name[rev]] = response.json()[0]['host']
            if (response.json()[0]['host'] == students[student_name[rev]]):
                students[student_name[rev]] = dict_seats_one_rev[j + 1]
                labone[j] = 1
                back +=2
            else:
                labone[j -1] = 1
                back +=1
            rev+=1
        else:
            while (labone[j-1] != 0):
                j+=1
            students[student_name[nums]] = dict_seats_one_rev[j]
            endpoint = '/users/%s/locations' % studentnames[nums][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (response.json()[0]['host'] == students[student_name[nums]]):
                students[student_name[nums]] = dict_seats_one_rev[j + 1]
                labone[j] = 1
            else:
                labone[j -1] = 1
            back -=1
            nums -= 1
        i+=1
    return num_students - i +1

def lab_two_carryover_strategy(students, studentnames, headers):   
    labtwo = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labtwocapacity = 24
    num_students = len(students)
    student_name = list(students)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    back = 0
    while (i <= num_students and i <= labtwocapacity):
        j = 1
        if (back == 0):
            while (labtwo[j-1] != 0):
                j+=1
            students[student_name[rev]] = dict_seats_two_rev[j]
            endpoint = '/users/%s/locations' % studentnames[rev][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (j == 1):
                students[student_name[rev]] = response.json()[0]['host']
            if (response.json()[0]['host'] == students[student_name[rev]]):
                students[student_name[rev]] = dict_seats_two_rev[j + 1]
                labtwo[j] = 1
                back +=2
            else:
                labtwo[j -1] = 1
                back +=1
            rev+=1
        else:
            while (labtwo[j-1] != 0):
                j+=1
            students[student_name[nums]] = dict_seats_two_rev[j]
            endpoint = '/users/%s/locations' % studentnames[nums][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (response.json()[0]['host'] == students[student_name[nums]]):
                students[student_name[nums]] = dict_seats_two_rev[j + 1]
                labtwo[j] = 1
            else:
                labtwo[j -1] = 1
            back -=1
            nums -= 1
        i+=1
    return num_students - i +1
        
def lab_three_carryover_strategy(students, studentnames, headers):   
    labthree = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labthreecapacity = 48
    num_students = len(students)
    student_name = list(students)
    j = 0
    while(j <= num_students):
        if (students[student_name[j]] != '0'):
            j+=1
        else:
            break
    nums = num_students - 1 - j
    rev = j
    i = 1
    back = 0
    while (i <= num_students and i <= labthreecapacity):
        j = 1
        if (back == 0):
            while (labthree[j-1] != 0):
                j+=1
            students[student_name[rev]] = dict_seats_three_rev[j]
            endpoint = '/users/%s/locations' % studentnames[rev][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (j == 1):
                students[student_name[rev]] = response.json()[0]['host']
            if (response.json()[0]['host'] == students[student_name[rev]]):
                students[student_name[rev]] = dict_seats_three_rev[j + 1]
                labthree[j] = 1
                back +=2
            else:
                labthree[j -1] = 1
                back +=1
            rev+=1
        else:
            while (labthree[j-1] != 0):
                j+=1
            students[student_name[nums]] = dict_seats_three_rev[j]
            endpoint = '/users/%s/locations' % studentnames[nums][0]
            url = url_join(endpoint)
            response = requests.get(url, headers=headers)
            if (response.json()[0]['host'] == students[student_name[nums]]):
                students[student_name[nums]] = dict_seats_three_rev[j + 1]
                labthree[j] = 1
            else:
                labthree[j -1] = 1
            back -=1
            nums -= 1
        i+=1
        return num_students - i +1
    
       
    
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
        # print(i)
        j+=1
        endpoint = '/projects/%s/projects_users?filter[status]=in_progress&filter[campus]=43&page=%i' % ((1319 + i), (j))
        url = url_join(endpoint)
        response = requests.get(url, headers=headers)
        temp1 = response.json()
        if (temp1):
            temp += response.json()
    with open("data_file2.json", "w") as write_file:
       json.dump(temp, write_file, indent=4)
    with open("data_file2.json", "r") as read_file:
       decoded_hand = json.load(read_file)
    # print('This is exam number %s' % (i + 2))
    for x in decoded_hand:
        if (user_in_abuDhabi(x['user']['login'], headers)):
            if (x['status'] == 'in_progress' and x['validated?'] != True):
                students[x['user']['email']]= '0'
                studentnames.append([x['user']['login']])


def randomize_students(students, lab, studentnames,headers):
    carry_over = 1
    for x in lab:
        if (x == 1 and carry_over):
            carry_over = lab_one_strategy(students,studentnames,headers)
            # print('Lab 1')
        if (x == 3 and carry_over):
            carry_over = lab_three_strategy(students,studentnames,headers)
            # print('Lab 3')
        if (x == 2 and carry_over):
            carry_over = lab_two_strategy(students,studentnames,headers)
            # print('Lab 2')
    for x in lab:
        if (x == 1 and carry_over):
            carry_over = lab_one_carryover_strategy(students,studentnames,headers)
            # print('Lab 1')
        if (x == 3 and carry_over):
            carry_over = lab_three_carryover_trategy(students,studentnames,headers)
            # print('Lab 3')
        if (x == 2 and carry_over):
            carry_over = lab_two_carryover_strategy(students,studentnames,headers)
            # print('Lab 2')

def student_search():
    token = get_token()
    headers = {'Authorization': 'Bearer %s' % token}
    students = {}
    studentnames = []
    for i in range(1,5):
         exam_search(i, headers, students, studentnames)
    lab = check_where_exam(headers)
    randomize_students(students, lab, studentnames, headers)
    # print(studentnames)
    return students




def main():
    students = student_search()
    # # field_names = ['Assigned Seat']
    # # print(students)
    # students = {"marcos@42abudhabi.ae":"lab3r3s12", "hammoudeh.ahmad@hotmail.com":"lab3r1s12"}
    with open('temp.csv', 'w') as f:
        f.write("%s,%s, %s\n"%("Student","Seat","Checked In"))
        for key in students.keys():
            f.write("%s,%s\n"%(key,students[key]))
    with open('temp.csv') as f:
        data = sorted(csv.reader(f))
    with open('SeatingPlan.csv', 'w') as f:
        csv.writer(f).writerows(data)
    os.remove('temp.csv')
    os.remove('data_file2.json')


    
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
