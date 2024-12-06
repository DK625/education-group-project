from django.urls import path
from .views import QuizListView, QuestionCreateView,ListQuizView,DetailQuiz,SubmitQuiz,CheckSubmit,ManageQuizView, ManageQuestionView,ManageOptionView

urlpatterns = [
    path('questions/', QuizListView.as_view(), name='questions-by-course'),
    path('courses/questions/', QuestionCreateView.as_view(), name='questions-by-course'),
    path('list-quiz/', ListQuizView.as_view(), name='questions-by-course'),
    path('quiz/detail/<int:quiz_id>/', DetailQuiz.as_view(), name='quiz-questions'),
    path('submit-quiz/<int:quiz_id>/', SubmitQuiz.as_view(), name='submit-quiz'),
    path('check-submit/<int:quiz_id>/', CheckSubmit.as_view(), name='submit-quiz'),
    # path('courses/<int:course_id>/quizzes/', ManageQuizView.as_view()),  # Thêm quiz
    # path('quizzes/<int:quiz_id>/', ManageQuizView.as_view()),           # Sửa, xóa quiz

    path('quiz/<int:course_id>/', ManageQuizView.as_view(), name='manage_quiz'),  # For creating a new quiz

    path('all-quiz/<int:course_id>/', ManageQuizView.as_view(), name='manage_quiz'),
    path('quiz/<int:quiz_id>/questions/', ManageQuestionView.as_view(), name='add_question'),
    # For adding questions to a quiz
    path('question/<int:question_id>/options/', ManageOptionView.as_view(), name='add_option'),
    # For adding options to a question

]
