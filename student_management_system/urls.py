"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from student_management_app import views, HodViews, StaffViews, StudentViews
from student_management_app.EditResultVIewClass import EditResultViewClass
from student_management_system import settings

urlpatterns = [
    path('demo',views.showDemoPage),
    path('signup_admin',views.signup_admin,name="signup_admin"),
    path('do_admin_signup',views.do_admin_signup,name="do_admin_signup"),
    path('signup_student',views.signup_student,name="signup_student"),
    path('do_signup_student',views.do_signup_student,name="do_signup_student"),
    path('signup_staff',views.signup_staff,name="signup_staff"),
    path('do_staff_signup',views.do_staff_signup,name="do_staff_signup"),
    path('admin/', admin.site.urls),
    # path('accounts/',include('django.contrib.auth.urls')),
    
    path('',views.ShowLoginPage,name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_home',HodViews.admin_home,name="admin_home"),
    path('add_staff',HodViews.add_staff,name="add_staff"),
    path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    path('delete_staff/<staff_id>/', HodViews.delete_staff, name="delete_staff"),

    path('delete_country/<country_id>/', HodViews.delete_country, name="delete_country"),
    path('delete_state/<state_id>/', HodViews.delete_state, name="delete_state"),
    path('add_country', HodViews.add_country, name="add_country"),

    path('add_state', HodViews.add_state, name="add_state"),
    path('add_exam_course', HodViews.add_exam_course,name="add_exam_course"),
    path('exam_course_save', HodViews.exam_course_save,name="exam_course_save"),
    path('add_course', HodViews.add_course,name="add_course"),
    path('add_course_save', HodViews.add_course_save,name="add_course_save"),
    path('add_country_save', HodViews.add_country_save,name="add_country_save"),

    path('add_state_save', HodViews.add_state_save,name="add_state_save"),
    path('delete_student_offer_letter_fees/<letter_id>/', HodViews.delete_student_offer_letter_fees, name="delete_student_offer_letter_fees"),
    path('delete_student_payment_receive/<student_payment_id>/',HodViews.delete_student_payment_receive, name="delete_student_payment_receive"),
    path('add_student', HodViews.add_student,name="add_student"),
    path('add_student_save', HodViews.add_student_save,name="add_student_save"),
    path('delete_course/<course_id>/', HodViews.delete_course, name="delete_course"),


    path('ajax/load-states/', HodViews.load_states, name='ajax_load_states'), # AJAX

    path('ajax/states_change/', views.change_states, name='ajax_change_states'), # AJAX

    # student section
    path('ajax/change-states/', StudentViews.states_change, name='ajax_states_change'), # AJAX

    path('add_subject', HodViews.add_subject,name="add_subject"),
    path('add_semester', HodViews.add_semester,name="add_semester"),
    path('admin_notice', HodViews.admin_notice,name="admin_notice"),
    path('add_subject_save', HodViews.add_subject_save,name="add_subject_save"),
    path('add_semester_save', HodViews.add_semester_save,name="add_semester_save"),
    path('delete_subject/<subject_id>/', HodViews.delete_subject, name="delete_subject"),


    path('delete_student/<student_id>/', HodViews.delete_student, name="delete_student"),
    path('manage_staff', HodViews.manage_staff,name="manage_staff"),
    path('manage_student', HodViews.manage_student,name="manage_student"),
    path('pending_approve_users', HodViews.pending_approval_users,name="pending_approve_users"),

    path('college_student', HodViews.college_student,name="college_student"),
    path('manage_course', HodViews.manage_course,name="manage_course"),
    path('manage_exam_course', HodViews.manage_exam_course,name="manage_exam_course"),
    path('manage_subject', HodViews.manage_subject,name="manage_subject"),
    path('manage_semester', HodViews.manage_semester,name="manage_semester"),

    path('manage_country', HodViews.manage_country,name="manage_country"),
    path('manage_state', HodViews.manage_state,name="manage_state"),

    path('edit_staff/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),
    path('edit_student/<str:student_id>', HodViews.edit_student,name="edit_student"),
    path('student_profile_view/<str:student_id>', HodViews.student_profile_view, name="student_profile_view"),
    path('show_student/<str:student_id>', HodViews.show_student, name="show_student"),
    path('add_student_offer_letter/<str:student_id>',HodViews.add_student_offer_letter_fees, name="add_student_offer_letter_fees"), 
    path('add_student_offer_letter_fees_save', HodViews.add_student_offer_letter_fees_save, name="add_student_offer_letter_fees_save"),

    path('edit_student_offer_letter/<str:letter_id>',HodViews.edit_student_offer_letter_fees, name="edit_student_offer_letter_fees"), 
    path('edit_student_offer_letter_fees_save', HodViews.edit_student_offer_letter_fees_save, name="edit_student_offer_letter_fees_save"),

    path('add_student_payment_receive/<str:student_id>', HodViews.add_student_payment_receive,name="add_student_payment_receive"),
    path('add_student_payment_receive_save',HodViews.add_student_payment_receive_save, name="add_student_payment_receive_save"),
    path('change_password/<str:student_id>', HodViews.change_password,name="change_password"),
    path('hod_document/<str:student_id>', HodViews.hod_document,name="hod_document"),
    path('college_document/<str:student_id>', HodViews.college_document,name="college_document"),
    path('hod_document_save', HodViews.hod_document_save,name="hod_document_save"),
    path('college_document_save', HodViews.college_document_save,name="college_document_save"),

    path('edit_student_save', HodViews.edit_student_save,name="edit_student_save"),
    path('change_password_save', HodViews.change_password_save,name="change_password_save"),
    path('edit_subject/<str:subject_id>', HodViews.edit_subject,name="edit_subject"),
    path('edit_semester/<str:semester_id>', HodViews.edit_semester,name="edit_semester"),
    path('edit_subject_save', HodViews.edit_subject_save,name="edit_subject_save"),
    path('edit_semester_save', HodViews.edit_semester_save,name="edit_semester_save"),
    path('edit_course/<str:course_id>', HodViews.edit_course,name="edit_course"),
    path('edit_exam_course/<str:exam_course_id>', HodViews.edit_exam_course,name="edit_exam_course"),
    path('edit_custom_user/<str:custom_user_id>', HodViews.edit_custom_user,name="edit_custom_user"),

    path('edit_course_save', HodViews.edit_course_save,name="edit_course_save"),
    path('edit_exam_course_save', HodViews.edit_exam_course_save,name="edit_exam_course_save"),
    path('edit_custom_user_save', HodViews.edit_custom_user_save,name="edit_custom_user_save"),

    path('edit_country/<str:country_id>', HodViews.edit_country,name="edit_country"),
    path('edit_state/<str:state_id>', HodViews.edit_state,name="edit_state"),
    path('edit_country_save',HodViews.edit_country_save,name="edit_country_save"),
    path('edit_state_save',HodViews.edit_state_save,name="edit_state_save"),

    path('manage_session', HodViews.manage_session,name="manage_session"),
    path('add_session', HodViews.add_session, name="add_session"),
    path('add_session_save', HodViews.add_session_save,name="add_session_save"),
    path('edit_session/<session_id>', HodViews.edit_session, name="edit_session"),
    path('edit_session_save', HodViews.edit_session_save, name="edit_session_save"),
    path('delete_session/<session_id>', HodViews.delete_session, name="delete_session"),
    path('delete_semester/<semester_id>', HodViews.delete_semester, name="delete_semester"),

    path('check_email_exist', HodViews.check_email_exist,name="check_email_exist"),
    path('check_username_exist', HodViews.check_username_exist,name="check_username_exist"),
    path('check_course_exist', HodViews.check_course_exist,name="check_course_exist"),
    path('check_exam_course_exist', HodViews.check_exam_course_exist,name="check_exam_course_exist"),

    path('check_country_exist', HodViews.check_country_exist,name="check_country_exist"),
    path('check_state_exist', HodViews.check_state_exist,name="check_state_exist"),

    path('admin_profile', HodViews.admin_profile,name="admin_profile"),
    path('admin_profile_save', HodViews.admin_profile_save,name="admin_profile_save"),

    path('hod_class_links', HodViews.hod_class_links,name="hod_class_links"),
    path('edit_class_links/<str:link_id>', HodViews.edit_class_links,name="edit_class_links"),
    path('edit_class_links_save', HodViews.edit_class_links_save,name="edit_class_links_save"),

    path('hod_payment_links', HodViews.hod_payment_links,name="hod_payment_links"),
    path('edit_payment_links/<str:link_id>', HodViews.edit_payment_links,name="edit_payment_links"),
    path('edit_payment_links_save', HodViews.edit_payment_links_save,name="edit_payment_links_save"),

    path('hod_student_links', HodViews.hod_student_links,name="hod_student_links"),
    path('edit_student_links/<str:link_id>', HodViews.edit_student_links,name="edit_student_links"),
    path('edit_student_links_save', HodViews.edit_student_links_save,name="edit_student_links_save"),
    path('add_link', HodViews.add_link,name="add_link"),
    path('imp_link_save', HodViews.imp_link_save,name="imp_link_save"),
    path('cls_link_save', HodViews.cls_link_save,name="cls_link_save"),
    path('pay_link_save', HodViews.pay_link_save,name="pay_link_save"),

    path('delete_link/<link_id>/', HodViews.delete_link, name="delete_link"),
    path('delete_notice/<notice_id>/', HodViews.delete_notice, name="delete_notice"),
    path('student_doc_approve/<int:document_id>/', HodViews.student_doc_approve, name="student_doc_approve"),
    path('student_doc_disapprove/<int:document_id>/', HodViews.student_doc_disapprove,name="student_doc_disapprove"),
    
    



    #staff and student urls
    path('staff_home', StaffViews.staff_home, name="staff_home"),
    path('student_exam', StaffViews.student_exam, name="student_exam"),
    path('save_student_result', StaffViews.save_student_result, name="save_student_result"),
    path('edit_student_result',EditResultViewClass.as_view(), name="edit_student_result"),
    path('fetch_result_student',StaffViews.fetch_result_student, name="fetch_result_student"),
    
    path('staff_take_attendance', StaffViews.staff_take_attendance, name="staff_take_attendance"),
    path('staff_update_attendance', StaffViews.staff_update_attendance, name="staff_update_attendance"),
    path('get_students', StaffViews.get_students, name="get_students"),
    path('get_subjects', StaffViews.get_subjects, name="get_subjects"),
    path('get_semesters', StaffViews.get_semesters, name="get_semesters"),
    path('get_subjects_semester', StaffViews.get_subjects_semester, name="get_subjects_semester"),

    path('get_attendance_dates', StaffViews.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student', StaffViews.get_attendance_student, name="get_attendance_student"),
    path('save_attendance_data', StaffViews.save_attendance_data, name="save_attendance_data"),
    path('save_updateattendance_data', StaffViews.save_updateattendance_data, name="save_updateattendance_data"),
    path('staff_profile', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_save', StaffViews.staff_profile_save, name="staff_profile_save"),




    path('student_home', StudentViews.student_home, name="student_home"),
    path('student_notice', StudentViews.student_notice,name="student_notice"),
    path('student_view_result',StudentViews.student_view_result,name="student_view_result"),
    path('student_view_account',StudentViews.student_view_account,name="student_view_account"),
    path('view_marksheet/<int:semester_id>',StudentViews.view_marksheet,name="view_marksheet"),
    # path('view_marksheet/',StudentViews.view_marksheet,name="view_marksheet"),
    

    path('important_links', StudentViews.student_links,name="student_links"),
    path('payment_links', StudentViews.payment_links,name="payment_links"),
    path('class_links', StudentViews.class_links,name="class_links"),

    path('student_view_attendance', StudentViews.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave', StudentViews.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
    path('student_feedback_save', StudentViews.student_feedback_save, name="student_feedback_save"),
    path('student_profile', StudentViews.student_profile, name="student_profile"),
    path('view_profile', StudentViews.view_profile, name="view_profile"),
    path('student_dashboard', StudentViews.student_dashboard, name="student_dashboard"),
    path('student_document', StudentViews.student_document, name="student_document"),
    path('institute_document', StudentViews.institute_document, name="institute_document"),
    path('student_document_save', StudentViews.student_document_save,name="student_document_save"),
    path('student_profile_save', StudentViews.student_profile_save, name="student_profile_save"),

    # password reset links
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_complete"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

