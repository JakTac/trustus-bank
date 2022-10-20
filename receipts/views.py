from receipts.models import Receipt
from django.shortcuts import render


def receipt_list(request):
    receipt = Receipt.objects.all()
    context = {
        "receipt_list": receipt,
    }
    return render(request, "receipts/list.html", context)
