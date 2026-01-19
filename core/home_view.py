from django.http.response import HttpResponse
from django.shortcuts import render, redirect, resolve_url

from core.models import Entreprise


def list_entreprise(request):
    entreprise = Entreprise.objects.filter(is_active=True).prefetch_related('adresses', 'contacts', 'contenus')
    context = {
        "entreprises": entreprise
    }
    return render(request, "core/public_view/home/liste_entrepirse.html", context)

def entreprise_detail_public(request, pk):
    try:
        entreprise = Entreprise.objects.prefetch_related('adresses', 'contacts', 'contenus').get(pk=pk, is_active=True)
    except Entreprise.DoesNotExist:
        return HttpResponse("Entreprise not found", status=404)

    context = {
        "entreprise": entreprise
    }
    return render(request, "core/public_view/home/entreprise_detail.html", context)