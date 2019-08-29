# from django.http import request
from django.shortcuts import render
from QuestionManagement.models import QuestionTypeList, QuestionBank, ChoiceBank

# Create your views here.
def createQuiz(request):
    question_type = QuestionTypeList.objects.all()
    test_txt = "hi this is js"
    # print("the first quest type ", question_type[0].question_type_txt)
    createquiz_dict = {"question_type": question_type, "test_txt": test_txt}
    #print(question_type)
    if request.method == "POST":
        print("POST RRQ VAL", request.POST)
        print("question type", request.POST['Ques-Type'])
        #from django.db import connection
        #cursor = connection.cursor()
        #cursor.execute('select coalesce(max(question_id),0) as max_ques_id from question_bank')
        #max_ques = cursor.fetchone()[0] + 1
        choice_ans_str = ""
        choice_50_str = ""
        choice_oth_str = ""
        ques_type_obj = QuestionTypeList.objects.get(question_type_txt=request.POST['Ques-Type'])
        Q = QuestionBank.objects.create(question_type_id=ques_type_obj, question_txt=request.POST['question'], remaining_choice="")
        max_ques = Q.question_id
        #print(max_ques)
        for dict_key in request.POST:
            if "choice-type" in dict_key:
                choice_num = int(dict_key.split("-")[-1])
                choice_new_id = (str(max_ques) + "_" + str(choice_num))
                if request.POST[dict_key] == "CC":
                    choice_ans_str = choice_new_id + "~|~" + choice_ans_str
                elif request.POST[dict_key] == "50-50":
                    choice_50_str = choice_new_id + "~|~" + choice_50_str
                elif request.POST[dict_key] == "OC":
                    choice_oth_str = choice_new_id + "~|~" + choice_oth_str
                choice_new_val = request.POST["choice-value-"+str(choice_num)]
                ChoiceBank.objects.create(choice_id=choice_new_id, choice_txt=choice_new_val, created_user_id="ajcs", updated_user_id="ajcs")

        Q.answer_id = choice_ans_str
        Q.choice_50_50 = choice_50_str
        Q.remaining_choice = choice_oth_str
        Q.save()

        print("max question number", max_ques)


    return render(request, 'QuestionManagement/add_questions.html', context=createquiz_dict)
