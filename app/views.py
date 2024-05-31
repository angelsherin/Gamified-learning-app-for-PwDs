from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
import random 
from django.db.models import Sum, Count
from django.db import connection
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
import os
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import operator
import datetime
import speech_recognition as sr
import time
def takeCommand():     
    r = sr.Recognizer()     
    with sr.Microphone() as source:         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   		
        print("Unable to Recognize your voice.")     
    return query
	
def speak(audio):
	engine = pyttsx3.init('sapi5')
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.say(audio)
	engine.runAndWait()
def enter_msg(request):
	speak("Hi Welcome How May I Help You? Whether You Want to  Attend The quiz or Know About who is top scorer")
	print("Hi Welcome Want to Attend quiz or Know aboard Leader Board")
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)
		print("Recognizing...")   
		query = r.recognize_google(audio, language ='en-in')
		if query == 'attend quiz':
			hour = int(datetime.datetime.now().hour)
			if hour>= 0 and hour<12:
				speak("Good Morning!")
				speak("Welcome")
				time.sleep(3)
				speak("Please Login Using Your Quiz ID")
				r = sr.Recognizer()
				with sr.Microphone() as source:
					print("Listening...")
					r.pause_threshold = 1
					audio = r.listen(source)
					print("Recognizing...")   
					query = r.recognize_google(audio, language ='en-in')
					crt=UserDetail.objects.filter(quiz_id=query)
					if crt:
						request.session['username']=query
						ids=UserDetail.objects.only('id').get(quiz_id=query).id
						request.session['user_id']=ids
						return redirect('exam')
					else:
						speak("Invalid QuizID")
						return render(request,'home.html',{})
			elif hour>= 12 and hour<18:
				speak("Good Afternoon!")  
				speak("Welcome")
				time.sleep(3)
				speak("Please Login Using Your Quiz ID")
				r = sr.Recognizer()
				with sr.Microphone() as source:
					print("Listening...")
					r.pause_threshold = 1
					audio = r.listen(source)
					print("Recognizing...")   
					query = r.recognize_google(audio, language ='en-in')
					crt=UserDetail.objects.filter(quiz_id=query)
					if crt:
						request.session['username']=query
						ids=UserDetail.objects.only('id').get(quiz_id=query).id
						request.session['user_id']=ids
						return redirect('exam')
					else:
						speak("Invalid QuizID")
						return render(request,'home.html',{})
			else:
				speak("Good Evening!")
				speak("Welcome")
				time.sleep(3)
				speak("Please Login Using Your Quiz ID")
				r = sr.Recognizer()
				with sr.Microphone() as source:
					print("Listening...")
					r.pause_threshold = 1
					audio = r.listen(source)
					print("Recognizing...")   
					query = r.recognize_google(audio, language ='en-in')
					crt=UserDetail.objects.filter(quiz_id=query)
					if crt:
						request.session['username']=query
						ids=UserDetail.objects.only('id').get(quiz_id=query).id
						request.session['user_id']=ids
						return redirect('exam')
					else:
						speak("Invalid QuizID")
						return render(request,'home.html',{})
				return render(request,'home.html',{})
		elif query == 'who is top scorer':
			def calculate_top_scorer_mark():
				all_answers = Answer_Detail.objects.all()
				user_scores = {}
				for answer in all_answers:
				    question = Quiz_Question.objects.get(pk=answer.question)
				    if answer.ans == question.answer:
				        user_scores[answer.user_id.id] = user_scores.get(answer.user_id.id, 0) + 1

				sorted_users = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
				if sorted_users:
				    top_scorer_id, top_score = sorted_users[0]
				    top_scorer = UserDetail.objects.get(pk=top_scorer_id)
				    return top_scorer, top_score
				else:
				    return None, None

			top_scorer, top_score = calculate_top_scorer_mark()
			a = str(top_scorer)
			b = str(top_score)
			speak("The Top Scorer Name "+ a + "and the Mark "+b+"out of 20")
			return render(request, 'top_scorer.html', {'top_scorer': top_scorer, 'top_score': top_score})
	return render(request,'enter.html',{})
def home(request):
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning!")
		speak("Welcome")
		time.sleep(3)
		speak("Please Login Using Your Quiz ID")
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...")
			r.pause_threshold = 1
			audio = r.listen(source)
			print("Recognizing...")   
			query = r.recognize_google(audio, language ='en-in')
			crt=UserDetail.objects.filter(quiz_id=query)
			if crt:
				request.session['username']=query
				ids=UserDetail.objects.only('id').get(quiz_id=query).id
				request.session['user_id']=ids
				return redirect('exam')
			else:
				speak("Invalid QuizID")
				return render(request,'home.html',{})
	elif hour>= 12 and hour<18:
		speak("Good Afternoon!")  
		speak("Welcome")
		time.sleep(3)
		speak("Please Login Using Your Quiz ID")
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...")
			r.pause_threshold = 1
			audio = r.listen(source)
			print("Recognizing...")   
			query = r.recognize_google(audio, language ='en-in')
			crt=UserDetail.objects.filter(quiz_id=query)
			if crt:
				request.session['username']=query
				ids=UserDetail.objects.only('id').get(quiz_id=query).id
				request.session['user_id']=ids
				return redirect('exam')
			else:
				speak("Invalid QuizID")
				return render(request,'home.html',{})
	else:
		speak("Good Evening!")
		speak("Welcome")
		time.sleep(3)
		speak("Please Login Using Your Quiz ID")
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...")
			r.pause_threshold = 1
			audio = r.listen(source)
			print("Recognizing...")   
			query = r.recognize_google(audio, language ='en-in')
			crt=UserDetail.objects.filter(quiz_id=query)
			if crt:
				request.session['username']=query
				ids=UserDetail.objects.only('id').get(quiz_id=query).id
				request.session['user_id']=ids
				return redirect('exam')
			else:
				speak("Invalid QuizID")
				return render(request,'home.html',{})
	return render(request,'home.html',{})
def student_login(request):
	return render(request,'login.html',{})

def student_dashboard(request):
	if request.session.has_key('user_id'):
		return render(request,'student_dashboard.html',{})
	else:
		return render(request,'student_login.html',{})
def logout(request):
    try:
        del request.session['user_id']
    except:
     pass
    return render(request, 'student_login.html', {})

def exam(request):
	if request.session.has_key('user_id'):
			uid = request.session['user_id']
			user_id = UserDetail.objects.get(id=int(uid))
			questions = list(Quiz_Question.objects.all())		
			r_num =  random.randrange(1000,9999)
			num = r_num+int(uid)
			if Answer_Detail.objects.filter(rand_num=num).exists():
				s_num = random.randrange(1000,9999)
				num=num+s_num			
			speak('Start Quiz')
			print('Start Quiz')			
			time.sleep(2)
			for idx, question in enumerate(questions):
				ques = question.question
				q1 = question.option1
				q2 = question.option2
				q3 = question.option3
				q4 = question.option4
				speak(f"Question {idx+1}: {ques}")
				print(f"Question {idx+1}: {ques}")				
				time.sleep(2)
				speak("The Options Are")
				time.sleep(1)
				speak("a"+q1)
				print(q1)
				time.sleep(1)
				speak("b"+q2)
				print(q2)
				time.sleep(1)
				speak("c"+q3)
				print(q3)
				time.sleep(1)
				speak("d"+q4)
				print(q4)
				r = sr.Recognizer()
				with sr.Microphone() as source:
					print("Listening...")
					r.pause_threshold = 2
					audio = r.listen(source)
					print("Recognizing...")  
					try: 
						ans_quiz = r.recognize_google(audio, language ='en-in')
						crt = Answer_Detail.objects.create(question=question.id, rand_num=num,ans=ans_quiz,user_id=user_id)				
					except:
						speak("Sorry! Answer Does not recognize")								
			if crt:
				return redirect('answer_view',num=num)
			return render(request,'exam.html',{'question':question})
	else:
		return render(request,'student_login.html',{})

def answer_view(request,num):
	if request.session.has_key('user_id'):
			uid = request.session['user_id']
			user_id = UserDetail.objects.get(id=int(uid))
			user_answers = Answer_Detail.objects.filter(rand_num=num)
			quiz_questions = Quiz_Question.objects.all()
			correct_count = 0
			for user_answer in user_answers:
				question = quiz_questions.filter(id=user_answer.question).first()
				if question and user_answer.ans == question.answer:
					correct_count += 1
					count = str(correct_count)
	print("You answered correctly "+count+" out of "+str(len(user_answers)))
	speak("You answered correctly "+count+" out of "+str(len(user_answers)))
	return redirect('result_exam_data')


		
def result_exam_data(request):
	if request.session.has_key('user_id'):
		speak("You Have Completed Your Quiz")
		return render(request,'result_exam_data.html',{})
	else:
		return render(request,'student_login.html',{})
def student_login_dump(request):
	if request.session.has_key('user_id'):
		return render(request,'student_dashboard.html',{})
	else:
		if request.method == 'POST':
			name=request.POST.get('username')
			pwd=request.POST.get('password')
			user_exist=UserDetail.objects.filter(quiz_id=name,password=pwd)
			if user_exist:
				request.session['name']= request.POST.get('username')
				a = request.session['name']
				sess = UserDetail.objects.only('id').get(quiz_id=a).id
				request.session['user_id']= sess
				return redirect('student_dashboard')
			else:
				messages.success(request,'Invalid username or Password')
		return render(request,'student_login_dump.html',{})

def exam_detail(request):
	if request.session.has_key('user_id'):
			uid = request.session['user_id']
			user_id = UserDetail.objects.get(id=int(uid))
			question = Quiz_Question.objects.all()
			r_num =  random.randrange(20, 50, 3)
			num = r_num+int(uid)
			if request.method == 'POST':
				question_id = request.POST.getlist('question_id')
				ran_num = request.POST.get('random_num')
				ans = request.POST.getlist('answer')
				length = len(ans)
				for i in range(0,length):
					crt = Answer_Detail.objects.create(question=int(question_id[i]),rand_num=ran_num,ans=ans[i],user_id=user_id)
				if crt:
					return redirect('result')
			return render(request,'exam_detail.html',{'question':question,'num':num})
	else:
		return render(request,'student_login_dump.html',{})
def result(request):
	if request.session.has_key('user_id'):
		num = request.POST.get('random_num')
		user_id = request.session['user_id']
		cursor = connection.cursor()
		tt = cursor.execute('''SELECT app_answer_detail.rand_num from app_answer_detail where 
		app_answer_detail.user_id_id= '%d' order by app_answer_detail.id DESC''' % (int(user_id)))
		row_user = cursor.fetchone()
		cat_name = Answer_Detail.objects.filter(rand_num=row_user[0])
		sql = ''' SELECT COUNT(a.ans) from app_quiz_question as q INNER JOIN app_answer_detail as a ON
		q.answer=a.ans where a.rand_num='%s' AND a.user_id_id= '%d' ''' % (row_user[0],int(user_id))
		post = cursor.execute(sql)
		row = cursor.fetchall()
		return render(request,'result.html',{'row':row,'cat_name':cat_name})
	else:
		return render(request,'student_login_dump.html',{})
def exam_results(request):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		cursor = connection.cursor()
		sql = ''' SELECT COUNT(a.ans) from app_quiz_question as q INNER JOIN app_answer_detail as a ON
		q.answer=a.ans  where a.user_id_id= '%d'  GROUP BY a.rand_num''' % (int(user_id))
		post = cursor.execute(sql)
		row = cursor.fetchall()
		lenth = len(row)
		return render(request,'exam_results.html',{'row':row,'lenth':lenth})
	else:
		return render(request,'student_login_dump.html',{})

def top_scorer_view(request):
    def calculate_top_scorer():
        all_answers = Answer_Detail.objects.all()
        user_scores = {}
        for answer in all_answers:
            question = Quiz_Question.objects.get(pk=answer.question)
            if answer.ans == question.answer:
                user_scores[answer.user_id.id] = user_scores.get(answer.user_id.id, 0) + 1

        sorted_users = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
        if sorted_users:
            top_scorer_id, top_score = sorted_users[0]
            top_scorer = UserDetail.objects.get(pk=top_scorer_id)
            return top_scorer, top_score
        else:
            return None, None

    top_scorer, top_score = calculate_top_scorer()
    return render(request, 'top_scorer.html', {'top_scorer': top_scorer, 'top_score': top_score})
def all_user_scores(request):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		cursor = connection.cursor()
		sql = ''' SELECT COUNT(a.ans),u.name from app_quiz_question as q INNER JOIN app_answer_detail as a ON
		q.answer=a.ans INNER JOIN app_userdetail as u ON a.user_id_id=u.id  GROUP BY a.rand_num''' 
		post = cursor.execute(sql)
		row = cursor.fetchall()
		lenth = len(row)
		return render(request,'all_user_scores.html',{'row':row,'lenth':lenth})
	else:
		return render(request,'student_login_dump.html',{})
def score_board(request):
    def calculate_top_scorer_mark():
        all_answers = Answer_Detail.objects.all()
        user_scores = {}
        for answer in all_answers:
            question = Quiz_Question.objects.get(pk=answer.question)
            if answer.ans == question.answer:
                user_scores[answer.user_id.id] = user_scores.get(answer.user_id.id, 0) + 1

        sorted_users = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
        if sorted_users:
            top_scorer_id, top_score = sorted_users[0]
            top_scorer = UserDetail.objects.get(pk=top_scorer_id)
            return top_scorer, top_score
        else:
            return None, None

    top_scorer, top_score = calculate_top_scorer_mark()
    speak("The Top Scorer Name is"+ top_scorer + "and the Mark is"+top_score+"out of 20")
    return render(request, 'top_scorer.html', {'top_scorer': top_scorer, 'top_score': top_score})