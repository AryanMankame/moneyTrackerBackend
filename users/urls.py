from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('login',views.login_user,name="login"),
    path('register',views.register_user,name="register_user"),
    path('show',views.show_transact,name="show_transact"),
    path('delete/<int:user_id>',views.delete_transact,name="delete_transact"),
    path('add',views.add_transact,name="add_transact"),
    path('show_pending',views.show_pending,name='show_pending'),
    path('add_pending',views.add_pending,name="add_pending"),
    path('del_pending/<int:pend_id>',views.del_pending,name="del_pending")
]
urlpatterns += staticfiles_urlpatterns()