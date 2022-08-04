clear
echo 'USER_ID = 64676'
./student-search.py 64676

read -p "Press anything to continue" -n1 -s
clear

echo 'INTRA_LOGIN = nasimon-'
./student-search.py nasimon-

read -p "Press anything to continue" -n1 -s
clear

echo 'inexistent USER_ID = 123456'
./student-search.py 123456

read -p "Press anything to continue" -n1 -s
clear

echo 'inexistent INTRA_LOGIN = dougadams'
./student-search.py dougadams

read -p "Press anything to continue" -n1 -s
clear

echo 'FLAGS'
echo 'ID'
./student-search.py nasimon- id

echo 'EMAIL'
./student-search.py nasimon- email

echo 'LOGIN'
./student-search.py nasimon- login

echo 'FIRST_NAME'
./student-search.py nasimon- first_name

echo 'LAST_NAME'
./student-search.py nasimon- last_name

echo 'URL'
./student-search.py nasimon- url 

echo 'PHONE'
./student-search.py nasimon- phone 

echo 'DISPLAYNAME'
./student-search.py nasimon- displayname 

echo 'IMAGE_URL'
./student-search.py nasimon- image_url

echo 'STAFF?'
./student-search.py nasimon- staff

echo 'CORRECTION_POINT'
./student-search.py nasimon- correction_point

echo 'POOL_MONTH'
./student-search.py nasimon- pool_month

echo 'POOL_YEAR'
./student-search.py nasimon- pool_year

echo 'LOCATION'
./student-search.py nasimon- location

echo 'WALLET'
./student-search.py nasimon- wallet

echo 'ANONYMIZE_DATE'
./student-search.py nasimon- anonymize_date

echo 'CURSUS_USERS'
./student-search.py nasimon- cursus_users

echo 'PROJECTS_USERS'
./student-search.py nasimon- projects_users

echo 'LANGUAGES_USERS'
./student-search.py nasimon- languages_users

echo 'ACHIEVEMENTS'
./student-search.py nasimon- achievements

echo 'CAMPUS'
./student-search.py nasimon- campus

echo 'CAMPUS_USERS'
./student-search.py nasimon- campus_users

echo 'EMPTY FLAG'
echo 'GROUPS'
./student-search.py nasimon- groups

read -p "Press anything to continue" -n1 -s
clear
