
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import QA,Interview
from django.contrib.auth.models import User
from .utils import interview_startter_templete,get_ans_review,gpt_rep
import PyPDF2

# Create your views here.
class start_interview(APIView):
    def get(self,request):
        interview = Interview.objects.create(user= User.objects.filter(id=request.GET.get('user'))[0],title=request.GET.get('title'))
        Start = interview_startter_templete(request.GET.get('field'),request.GET.get('level'))
        qa1 = QA.objects.create(interview=interview,question="",answer=Start,hidden=True)
        qa1.save()
        resp = gpt_rep([{"role": "user", "content":Start}])
        qa2 = QA.objects.create(interview=interview,question=resp[0],answer="",hidden=False)
        qa2.save()
        return Response({"interview_id":interview.id,"questionId":qa2.id,"question":qa2.question})
class get_next_question(APIView):
    def post(self,request):
        data = request.data
        qa = QA.objects.get(id=data["questionId"])
        
        
        hsistory = QA.objects.filter(interview=qa.interview).order_by("created_at")
        hist_arr = []
        for i in hsistory:
            if i.hidden:
                hist_arr.append({"role": "user", "content":i.answer})
            else:
                hist_arr.append({"role": "assistant", "content":i.question})
                hist_arr.append({"role": "user", "content":i.answer})
                

        
        
        qa2 = QA.objects.create(interview=qa.interview,question="",answer="",hidden=False)
        hist_arr.append({"role": "user", "content":get_ans_review(data["answer"])})
        
        review =  gpt_rep( hist_arr )
        qa.answer = data["answer"]
        qa.save()
        print("rivew",review)
        try:
            qa.score = eval(review[1])
        except:
            qa.score = 0
        qa.save()
        qa2.question = review[0]
        qa2.save()
        return Response({"questionId":qa2.id,"question":qa2.question})
        
class end_interview(APIView):
    def get(self,request):
        qa = QA.objects.filter(interview = Interview.objects.filter(id=request.GET.get('id'))[0] )
        
        strring ="" 
        for content in qa:
            strring += content.question + "\n" + content.answer + "\n" + "\n"
            # Create a new page
        filer = open("report.txt", 'w+')
        filer.write(strring)
        filer.close()
        return Response({"message":"done"})

class Compare(APIView):
    def post(self,request):
        data = request.data
        qa = QA.objects.get(id=data["questionId"])
        
        
        return Response({"questionId":qa2.id,"question":qa2.question})
        