from django.urls import path
from .views import search,search_dept_lect,home, add_stu,add_dpt,add_lect,show_stu,show_dpt,show_lect,update_stu,update_lect,update_dpt,delete_lect,delete_stu,delete_dpt, search_dept_stu

urlpatterns = [
    path('add_stu/', add_stu, name = 'add_stu'),
    path('show_stu/', show_stu, name='show_stu'),
    path('update_stu/<int:id_f>/', update_stu, name = 'update_stu'),
    path('delete_stu/<int:id_f>/', delete_stu, name = 'delete_stu'),

    path('add_lect/', add_lect, name = 'add_lect'),
    path('show_lect/', show_lect, name='show_lect'),
    path('update_lect/<int:id_f>/', update_lect, name = 'update_lect'),
    path('delete_lect/<int:id_f>/', delete_lect, name = 'delete_lect'),

    path('add_dpt/', add_dpt, name = 'add_dpt'),
    path('show_dpt/', show_dpt, name='show_dpt'),
    path('update_dpt/<int:id_f>/', update_dpt, name = 'update_dpt'),
    path('delete_dpt/<int:id_f>/', delete_dpt, name = 'delete_dpt'),

    path('home/', home, name = 'home'),
    path('showdeptstud/<int:id>/', search_dept_stu, name='showdeptstud'),
    path('showdeptlect/<int:id>/', search_dept_lect, name='showdeptlect'),
    path('search/', search, name='search'),

]