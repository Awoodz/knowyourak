from django.http import HttpResponse
from django.template import loader
import whoisgame.models as wm
import whoisgame.tools as wt
import json


def index(request):
    """Index page"""
    template = loader.get_template("whoisgame/index.html")
    return HttpResponse(template.render(request=request))


def easy(request):
    template = loader.get_template("whoisgame/easy.html")
    photo, employee_block, answer_list = wt.randomize_game(1)
    answer_list = json.dumps(answer_list)
    return HttpResponse(template.render(
        {
            "photo": photo,
            "employee_block": employee_block,
            "answer_list": answer_list,
        },
        request=request))


def statistic_spawn(request):
    pass