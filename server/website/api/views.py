from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from . import dao


def index(request):
    return HttpResponse("Welcome to eHospital !!!")


@staff_member_required
def get_stats_categories(request):
    amount = [data["amount"]
              for data in dao.count_by_category()]
    labels = [data["name"]
              for data in dao.count_by_category()]

    return JsonResponse({
        "data":  {
            "labels": labels,
            "datasets": [{
                "data": amount,
                "label": "Amount"
            }]
        },
    })
