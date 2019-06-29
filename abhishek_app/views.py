from django.shortcuts import render
from abhishek_app.models import News_Data

# Create your views here.
def index(request):

    news_list = News_Data.objects.all()
    for news in news_list:
        print (news.title)
        print (news.body)


    params = { 'news_list':news_list }

    return render(request,'index.html',params)


    #
    # if request.method=="POST":
    #     Sname = request.POST.get('assignmentname', '')
    #     Semail = request.POST.get('exampleInputEmail1', '')
    #     Econtact = request.POST.get('assignmentcontact', '')
    #     Image = request.POST.get('assignmentimage', '')
    #     print("Iam here")
    #     Student_data = Student_Data(Sname=Sname, Semail=Semail, Econtact=Econtact)
    #     Student_data.save()
    #
