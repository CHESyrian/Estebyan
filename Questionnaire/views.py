from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.conf import settings
from django.contrib.auth.decorators import login_required
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
        #Q1_CH1_Input, Q1_Input, AnswerType_1, Questions_Num, Keyword1_Input
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
        target_path = settings.BASE_DIR.replace('\\', '/') + "/resources/questionnaires/"
        title = request.POST.get('Title')
        json_object = json.dumps(Data, indent=4)
        with open('%s%s_%s.json'%(target_path, request.user.username, title), 'w+') as file:
            file.write(json_object)
            file.close()
        return JsonResponse(Data)
    else:
        return HttpResponse('Not Permissions')


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
