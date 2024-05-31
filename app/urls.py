from django.urls import path
from . import views
urlpatterns = [
path('home/',views.home,name="home"),
path('student_login/',views.student_login,name="student_login"),
path('student_dashboard/',views.student_dashboard,name="student_dashboard"),
path('logout/',views.logout,name="logout"),
path('exam/',views.exam,name="exam"),
path('result_exam_data/',views.result_exam_data,name="result_exam_data"),
path('answer_view/<int:num>/',views.answer_view,name="answer_view"),
path('student_login_dump/',views.student_login_dump,name="student_login_dump"),
path('exam_detail/',views.exam_detail,name="exam_detail"),
path('result/',views.result,name="result"),
path('exam_results/',views.exam_results,name="exam_results"),
path('top_scorer_view/',views.top_scorer_view,name="top_scorer_view"),
path('all_user_scores/',views.all_user_scores,name="all_user_scores"),
path('',views.enter_msg,name="enter_msg"),
path('score_board/',views.score_board,name="score_board"),
]


