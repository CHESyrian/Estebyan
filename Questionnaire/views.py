from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Accounts.models import Profiles
from .models import Questionnaires
import os, json, csv, tablib


@login_required(login_url='/authentication/login/')
def Add_Questionnaire(request, usrnm):
    if request.user.username == usrnm:
        return render(request, 'Questionnaire/add_questionnaire.html')
    else:
        return HttpResponse('Not Permissions')


@login_required(login_url='/authentication/login/')
def Make_Questionnaire(request, usrnm):
    if request.user.username == usrnm:
        user_instance   = User.objects.get(username=usrnm)
        ques_num        = Profiles.objects.get(UserName=user_instance.id).Questionnaires
        target_path     = settings.RESOURCES_ROOT.replace('\\', '/') + "/questionnaires/"
        title           = request.POST.get('Title')
        describtion     = request.POST.get('Description')
        Ques_Model      = Questionnaires.objects.create(
            UserName = user_instance,
            Qs_Name  = f"{usrnm}_{title}.json",
            Qs_Title = title,
            Qs_Dcrb  = describtion,
            Qs_Path  = target_path
        )
        Questions_Count = int(request.POST.get('Questions_Num'))
        Data = {}
        for n in range(1, Questions_Count + 1):
            str_n = str(n)
            key = "Question_%s"%str_n
            Data[key] = {
            "Keyword" : request.POST.get('Keyword%s_Input'%str_n),
            "Question" : request.POST.get('Q%s_Input'%str_n),
            "Type" : request.POST.get('AnswerType_%s'%str_n),
            "Answers" : []
            }
            if Data[key]['Type'] == "select":
                Answers_Count = int(request.POST.get('Q%s_Choices_Num'%str_n))
                for m in range(1, Answers_Count + 1):
                    str_m = str(m)
                    Data[key]['Answers'].append(request.POST.get('Q%s_CH%s_Input'%(str_n, str_m)))
        json_object = json.dumps(Data, indent=4)
        with open('%s%s_%s.json'%(target_path, request.user.username, title), 'w+') as file:
            file.write(json_object)
            file.close()
        Profiles.objects.filter(UserName=user_instance.id).update(Questionnaires=ques_num+1)
        Ques_Model.save()
        return JsonResponse(Data)
    else:
        return HttpResponse('Not Permissions')


@login_required(login_url='/authentication/login/')
def Show_Questionnaire(request, usrnm, qs_title):
    file_path = settings.RESOURCES_ROOT.replace('\\', '/') + f"/questionnaires/{usrnm}_{qs_title}.json"
    with open(file_path, 'rb') as file:
        json_file = json.load(file)
        file.close()
    Context = {
        "Title" : qs_title,
        "Questions" : json_file.values()
    }
    return render(request, 'Questionnaire/show_questionnaire.html', Context)
    #if usrnm != request.user.username:
    #
    #else:
    #    return HttpResponse('You can\'t share in your questionnaire')


@login_required(login_url='/authentication/login/')
def Search(request, usrnm, keyword):
    pass


@login_required(login_url='/authentication/login/')
def Download_Data(request, usrnm, filename, filetype):
    if request.user.username == usrnm:
        file_path = os.path.join(settings.RESOURCES_ROOT, 'data/' + filename + '.json')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                if filetype == "csv":
                    "Convert to CSV and Save as File then return it."
                    pass
                elif filetype == "excel":
                    "Convert to Excel and Save as File then return it."
                    pass
                elif filetype == "json":
                    json_file = file.read()
                    response  = HttpResponse(json_file, content_type='application/json')
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                    return response
                else:
                    raise Http404
        else:
            raise Http404
    else:
        return HttpResponse('Not Permissions')
