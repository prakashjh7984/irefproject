from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from student_management_app.forms import EditResultForm
from student_management_app.models import Courses, Semesters, Students, Subjects, StudentResult


class EditResultViewClass(View):
    def get(self,request,*args,**kwargs):
        staff_id=request.user.id
        edit_result_form=EditResultForm(staff_id=staff_id)
        return render(request,"staff_template/edit_student_result.html",{"form":edit_result_form})

    def post(self,request,*args,**kwargs):
        form=EditResultForm(staff_id=request.user.id,data=request.POST)
        if form.is_valid():
            student_admin_id = form.cleaned_data['student_ids']
            # exam_months = form.cleaned_data['exam_months']
            subject_credits = form.cleaned_data['subject_credits']
            internal_marks = form.cleaned_data['internal_marks']
            external_marks = form.cleaned_data['external_marks']
            subject_id = form.cleaned_data['subject_id']
            course_id = form.cleaned_data['course_id']
            semester_id = form.cleaned_data['semester_id']

            student_obj = Students.objects.get(admin=student_admin_id)
            course_obj = Courses.objects.get(id=course_id)
            subject_obj = Subjects.objects.get(id=subject_id)
            semester_obj = Semesters.objects.get(id=semester_id)
            result=StudentResult.objects.get(course_id=course_obj,subject_id=subject_obj,semester_id=semester_obj,student_id=student_obj)
            # result.exam_months=exam_months
            result.subject_credits=subject_credits
            result.subject_internal_marks=internal_marks
            result.subject_external_marks=external_marks
            result.save()
            messages.success(request, "Successfully Updated Result")
            return HttpResponseRedirect(reverse("edit_student_result"))
        else:
            messages.error(request, "Failed to Update Result")
            form=EditResultForm(request.POST,staff_id=request.user.id)
            return render(request,"staff_template/edit_student_result.html",{"form":form})


