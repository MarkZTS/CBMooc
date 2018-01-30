from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Teacher
from courses.models import Course
from operation.models import UserFavorite

# Create your views here.


class TeacherListView(View):
    '''
    课程讲师列表页
    '''
    def get(self, request):
        all_teachers = Teacher.objects.all()

        # 讲师排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "hot":
                all_teachers = all_teachers.order_by("-click_nums")

        sorted_teacher = Teacher.objects.all().order_by("-click_nums")[:3]

        # 对讲师进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_teachers, 1, request=request)

        all_teachers = p.page(page)

        return render(request, "teachers-list.html", {
            "all_teachers": all_teachers,
            "sorted_teacher": sorted_teacher,
            "sort": sort,
        })


class TeacherDetailView(View):
    '''
    课程详情页
    '''
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))
        all_courses = Course.objects.filter(teacher=teacher)

        # 是否收藏
        has_teacher_faved = False
        if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=teacher.id):
            has_teacher_faved = True

        # 讲师排行
        sorted_teacher = Teacher.objects.all().order_by("-click_nums")[:3]

        # 对讲师课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 3, request=request)

        all_courses = p.page(page)
        return render(request, "teacher-detail.html", {
            "teacher": teacher,
            "all_courses": all_courses,
            "sorted_teacher": sorted_teacher,
            "has_teacher_faved": has_teacher_faved,
        })

