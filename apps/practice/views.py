import json

from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import ChoiceQuestion, Choice, ErrorQuestion
from courses.models import Course
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.


class PraticeListView(LoginRequiredMixin, View):
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


class PracticeDetailView(LoginRequiredMixin, View):
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

        relate_questions = all_course_questions[:3]

        return render(request, "practice-bank-detail.html", {
            "choice_question": choice_question,
            "relate_questions": relate_questions,
        })


class PraticeInfoView(LoginRequiredMixin, View):
    '''
    做题界面
    '''
    def get(self, request, choice_id, question_id):
        choice_question = ChoiceQuestion.objects.get(id=int(choice_id))

        choice_title = Choice.objects.filter(choicequestion_id=choice_id)
        this_question = Choice.objects.get(id=question_id)
        all_question = Choice.objects.all().count()
        print(all_question)
        if int(question_id) == 1:
            request.session['right_count'] = 0
        is_last = False
        if int(question_id) == all_question:
            is_last = True
        return render(request, 'practice-choice-detail.html', {
            "choice_question": choice_question,
            "choice_title": choice_title,
            "this_question": this_question,
            "is_last": is_last,
            "choice_id":choice_id,
        })



class NextQuestionView(LoginRequiredMixin, View):
    '''
    下一题
    '''
    def post(self, request):
        this_question = request.POST.get("practice_num", 1)
        user_answer = request.POST.get("user_answer", "")
        print(user_answer)
        print(type(user_answer))
        choice_id = request.POST.get("practice_bank_id", 1)
        next_question = int(this_question) + 1
        print("123", user_answer)
        if int(user_answer) != -1:
            # 得到本题的正确答案
            right = Choice.objects.get(id=int(this_question))
            right_answer = right.right_choice
            if int(user_answer) == right_answer:
                print("答对本题")
                request.session['right_count'] = request.session.get('right_count', default=0) + 1
            else:
                print("本题错误")
                error_question = ErrorQuestion()
                error_question.user = request.user
                choicequestion = ChoiceQuestion.objects.get(id=int(choice_id))
                choice = Choice.objects.get(id=int(this_question))
                try:
                    ErrorQuestion.objects.get(user=request.user, choicequestion=choicequestion, choice=choice)
                except ErrorQuestion.DoesNotExist:
                    error_question.choicequestion = choicequestion
                    error_question.choice = choice
                    error_question.save()
            value = {"status":"success", "next_question":next_question, "choice_id":choice_id}
            print("session",request.session['right_count'])
            return HttpResponse(json.dumps(value), content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"没有进行选择"}', content_type='application/json')


class ResultView(LoginRequiredMixin, View):
    '''选择题提交'''
    def get(self, request, choice_id):
        print("进来没有")

        right_nums = request.session.get('right_count', default=0)
        all_questions = Choice.objects.filter(choicequestion_id=choice_id).count()
        right_rate = int(int(right_nums)/int(all_questions) * 100)
        print(right_rate)

        return render(request, "practice-choice-result.html", {
            "choice_id": choice_id,
            "right_nums": right_nums,
            "right_rate": right_rate
        })


