from django.urls import path
from . import views

urlpatterns = [
    path('my/', views.my_test_list, name='my-test-list'),
    path('my/create_test/', views.my_test_create, name='my-test-create'),
    path('my/<int:test_id>/update/', views.my_test_update, name='my-test-update'),
    path('my/<int:test_id>/delete/', views.my_test_delete, name='my-test-delete'),

    path('my/<int:test_id>/', views.question_list, name='question-list'),
    path('my/<int:test_id>/create_question/', views.question_create, name='question-create'),
    path('my/<int:test_id>/<int:question_id>/update_question/', views.question_update, name='question-update'),
    path('my/<int:test_id>/<int:question_id>/delete_question/', views.question_delete, name='question-delete'),

    path('my/<int:test_id>/<int:question_id>/create_answer/', views.answer_create, name='answer-create'),
    path('my/<int:test_id>/<int:answer_id>/update_answer/', views.answer_update, name='answer-update'),
    path('my/<int:test_id>/<int:answer_id>/delete_answer/', views.answer_delete, name='answer-delete'),

    path('my/<int:test_id>/create_result/', views.score_record, name='result-create'),
    path('my/<int:test_id>/create/user_answer/', views.user_answer_record, name='user-answer-create'),

    path('', views.tests_list, name='test-list'),
    path('<int:test_id>/', views.test_detail, name='test-detail'),

    path('category/<int:category_id>/', views.category_detail, name='category-detail'),

    path('my/<int:test_id>/info', views.test_info, name='test-info'),
    path('my/<int:test_result_id>/info/detail/', views.test_info_detail, name='test-info-detail'),
]
