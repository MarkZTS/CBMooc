from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import ChoiceQuestion, Choice
from courses.models import Course

# Create your views here.


class PraticeListView(View):
    '''
    在线练习列表
    '''
    def get(self, request):
        choice_questions = ChoiceQuestion.objects.all()

        hot_questions = ChoiceQuestion.objects.all().order_by("-click_nums")[:3]

        # 题库排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_course = choice_questions.order_by("-students")
            elif sort == "hot":
                all_course = choice_questions.order_by("-click_nums")

        # 对题库进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(choice_questions, 6, request=request)

        choice_questions = p.page(page)

        return render(request, "practice-list.html", {
            "choice_questions": choice_questions,
            "hot_questions": hot_questions,
            "sort": sort,
        })


class PracticeDetailView(View):
    '''
    题库详情页
    '''
    def get(self, request, choice_id):
        # 当前题库
        choice_question = ChoiceQuestion.objects.get(id=int(choice_id))
        # 该题库所属的课程
        choice_course = choice_question.course.id

        # 课程的所有题库
        all_course_questions = ChoiceQuestion.objects.filter(course_id=choice_course)
        print(all_course_questions)

        relate_questions = all_course_questions[:3]

        return render(request, "practice-bank-detail.html", {
            "choice_question": choice_question,
            "relate_questions": relate_questions,
        })


class PraticeInfoView(View):
    '''
    做题界面
    '''
    def get(self, request, choice_id):
        choice_question = ChoiceQuestion.objects.get(id=int(choice_id))

        choice_num = Choice.objects.get(choicequestion_id=choice_id)

        return render(request, 'practice-choice-detail.html', {
            "choice_question": choice_question,
            "choice_num": choice_num,
        })

