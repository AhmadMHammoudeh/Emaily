FROM python:3
ADD src/ /
ADD test/ /
RUN pip3 install pandas
RUN pip3 install requests
RUN pip3 install python-dotenv
CMD [ "./student-search.py", "nayran" , "email" ]
#CMD [ "bash", "tests.sh" ]
