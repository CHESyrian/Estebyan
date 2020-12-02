from django.shortcuts import render, reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Accounts.models import Profiles
from .models import Questionnaires, Qs_Shares, Shares
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
        quest_path      = settings.RESOURCES_ROOT.replace('\\', '/') + "/questionnaires/"
        data_path       = settings.RESOURCES_ROOT.replace('\\', '/') + "/data/"
        title           = request.POST.get('Title')
        describtion     = request.POST.get('Description')
        Ques_Model      = Questionnaires.objects.create(
            UserName = user_instance,
            Qs_Name  = f"{usrnm}_{title}",
            Qs_Title = title,
            Qs_Dcrb  = describtion,
            Qs_Path  = quest_path
        )
        Questions_Count = int(request.POST.get('Questions_Num'))
        Ques = {}
        for n in range(1, Questions_Count + 1):
            str_n = str(n)
            key = "Question_%s"%str_n
            Ques[key] = {
            "Keyword" : request.POST.get('Keyword%s_Input'%str_n),
            "Question" : request.POST.get('Q%s_Input'%str_n),
            "Type" : request.POST.get('AnswerType_%s'%str_n),
            "Answers" : []
            }
            if Ques[key]['Type'] == "select":
                Answers_Count = int(request.POST.get('Q%s_Choices_Num'%str_n))
                for m in range(1, Answers_Count + 1):
                    str_m = str(m)
                    Ques[key]['Answers'].append(request.POST.get('Q%s_CH%s_Input'%(str_n, str_m)))
        ques_json = json.dumps(Ques, indent=4)
        with open('%s%s_%s.json'%(quest_path, request.user.username, title), 'w+') as file:
            file.write(ques_json)
            file.close()
        Data = {
            'Questions' : [],
            'Keywords'  : [],
            'Answers'   : {}
        }
        for n in range(1, Questions_Count + 1):
            str_n = str(n)
            Data['Questions'].append(request.POST.get('Q%s_Input'%str_n))
            Data['Keywords'].append(request.POST.get('Keyword%s_Input'%str_n))
        Data['Answers']['Total'] = 0
        data_json = json.dumps(Data, indent=4)
        with open('%s%s_%s.json'%(data_path, request.user.username, title), 'w+') as data_file:
            data_file.write(data_json)
            data_file.close()
        Profiles.objects.filter(UserName=user_instance.id).update(Questionnaires=ques_num+1)
        Ques_Model.save()
        Qs_Sh = Questionnaires.objects.get(Qs_Name=f"{usrnm}_{title}")
        Share = Qs_Shares.objects.create(
            Questionnaire = Qs_Sh,
        )
        Share.save()
        return HttpResponseRedirect(reverse('MyProfile', args=[usrnm]))
    else:
        return HttpResponse('Not Permissions')


@login_required(login_url='/authentication/login/')
def Show_Questionnaire(request, usrnm, qs_title):
    file_path = settings.RESOURCES_ROOT.replace('\\', '/') + f"/questionnaires/{usrnm}_{qs_title}.json"
    with open(file_path, 'rb') as file:
        json_file = json.load(file)
        file.close()
    Context = {
        "Author"    : usrnm,
        "Title"     : qs_title,
        "Questions" : json_file.values()
    }
    return render(request, 'Questionnaire/show_questionnaire.html', Context)


@login_required(login_url='/authentication/login/')
def Save_Answers(request, usrnm, qs_title):
    auth_id       = User.objects.get(username=usrnm).id
    user_instance = User.objects.get(username=request.user.username)
    ques_instance = Questionnaires.objects.get(UserName=auth_id)
    check_share   = Shares.objects.filter(UserName=user_instance.id, Questionnaire=ques_instance.id).exists()
    if not check_share:
        shares_num    = Qs_Shares.objects.get(Questionnaire=ques_instance.id).Shares_Num + 1
        prof_shares   = Profiles.objects.get(UserName=user_instance.id).Qs_Shares + 1
        shares        = Shares.objects.create(
            UserName      = user_instance,
            Questionnaire = ques_instance
        )
        Qs_Shares.objects.filter(Questionnaire=ques_instance.id).update(Shares_Num=shares_num)
        Profiles.objects.filter(UserName=user_instance.id).update(Qs_Shares=prof_shares)
        shares.save()
        return HttpResponse('Done')
    else:
        return HttpResponse('Sorry,You shared in this questionnaire.')


@login_required(login_url='/authentication/login/')
def Download_Data(request, usrnm, filename, filetype):
    if request.user.username == usrnm:
        file_path = os.path.join(settings.RESOURCES_ROOT, 'data/' + filename + '.json')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                if filetype == "csv":
                    print("Convert to CSV and Save as File then return it.")
                    raise Http404
                elif filetype == "excel":
                    print("Convert to Excel and Save as File then return it.")
                    raise Http404
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


@login_required(login_url='/authentication/login/')
def Search(request, usrnm, keyword):
    pass
