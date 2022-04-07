import logging
import smtplib

from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

from tempfile import NamedTemporaryFile
from typing import TYPE_CHECKING, Dict, List, Optional, Sequence, Union

from airflow.exceptions import AirflowException
from airflow.models import BaseOperator
import smtplib

def sendmail():
    gmail_user = 'jenish.other@gmail.com'
    gmail_password = 'JenishAdhikari@1995$'
    sent_from = gmail_user
    to = ['solid@speedrent.com', 'binaya@speedrent.com']
    subject = 'OMG Super Important Message'
    body = 'Hey, whats up from airflow'
    email_text = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % (sent_from, ", ".join(to), subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')
   	 
with DAG(
	dag_id="send_mail",
	start_date=datetime(2022, 3, 6),
	schedule_interval=timedelta(minutes=2),
	catchup=False,
) as dag:

  t1 = PythonOperator(
    	task_id="sendmail",
    	python_callable=sendmail)
   	 
  t1