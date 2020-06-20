from django.urls import path
from . import views

urlpatterns = [
    path('my/', views.test_list, name='my-test-list'),
    path('my/create_test/', views.test_create, name='my-test-create'),
    path('my/<int:test_id>/update/', views.test_update, name='my-test-update'),
    path('my/<int:test_id>/delete/', views.test_delete, name='my-test-delete'),

    path('my/<int:test_id>/', views.question_list, name='question-list'),
    path('my/<int:test_id>/create_question/', views.question_create, name='question-create'),
    path('my/<int:test_id>/<int:question_id>/update_question/', views.question_update, name='question-update'),
    path('my/<int:test_id>/<int:question_id>/delete_question/', views.question_delete, name='question-delete'),


    path('my/<int:test_id>/<int:question_id>/create_answer/', views.answer_create, name='answer-create'),
    path('my/<int:test_id>/<int:answer_id>/update_answer/', views.answer_update, name='answer-update'),
    path('my/<int:test_id>/<int:answer_id>/delete_answer/', views.answer_delete, name='answer-delete'),

    path('', views.TestListView.as_view(), name='test-list'),
    path('<int:test_id>/', views.TestDetailView.as_view(), name='test-detail'),


]