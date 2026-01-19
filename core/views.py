from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, resolve_url

from core.form import EntrepriseForm, AddressEntrepriseForm, ContactsForm, ContenuForm
from core.models import Entreprise


# Create your views here.

@login_required
def home(request):
    return render(request, 'core/home.html')




#entreprise views
@login_required
def entreprise_list(request):
    context = {
        'entreprises': Entreprise.objects.filter(user=request.user).prefetch_related('adresses', 'contacts', 'contenus')
    }
    return render(request, 'core/private_view/entreprise_list.html', context)

@login_required
def entreprise_detail(request, pk):
    entreprise = Entreprise.objects.filter(id=pk).first()
    adresse_entrprise = entreprise.adresses.first()
    contact_entrprise = entreprise.contacts.all()


    context = {
        "entreprise": entreprise,
        "adresse_entrprise": adresse_entrprise,
        "address_form": AddressEntrepriseForm(instance=adresse_entrprise),
        "contacts_entreprise": contact_entrprise,
        "contact_form": ContactsForm(),
        "contenu_form": ContenuForm(),
    }
    return render(request, 'core/private_view/entreprise/detail.html', context)

@login_required
@transaction.atomic
def entreprise_create(request):
    context = {
        'form_entreprise' :EntrepriseForm()
    }

    if request.method == 'POST':
        form = EntrepriseForm(request.POST)
        if form.is_valid():
            f =form.save(commit=False)
            f.user = request.user
            f.save()

            # URL de destination
            redirect_url = resolve_url('core:entreprise_detail', pk=f.id)  # ou '/chemin-statique/'

            response = HttpResponse(
                status=200)  # 204 No Content est souvent utilisé pour les réponses HTMX sans contenu à échanger
            response['HX-Redirect'] = redirect_url
            return response
            # Redirect or render success message here
    return render(request, 'core/private_view/entreprise/add_entreprise.html', context)

@login_required
def entreprise_update(request, pk):
    return render(request, 'core/entreprise_form.html')

@login_required
def entreprise_archive(request, pk):
    return render(request, 'core/entreprise_confirm_archive.html')


#adresse entreprise views
@login_required
def address_entreprise_list(request, pk):
    return render(request, 'core/address_entreprise_list.html')


def add_address_entreprise(request, pk):
    entreprise = Entreprise.objects.filter(id=pk).first()
    adresse_entrprise = entreprise.adresses.first()
    form = AddressEntrepriseForm(instance=adresse_entrprise)
    if request.method == 'POST':
        form = AddressEntrepriseForm(request.POST, instance=adresse_entrprise)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.entreprise = entreprise
            f.save()

            adresse_entrprise = f

    context = {
        "entreprise": entreprise,
        "adresse_entrprise": adresse_entrprise,
        "address_form": form
    }
    return render(request, 'core/private_view/partial/entreprise/details/address.html', context)




# contact views
@login_required
def contact_list(request, pk):
    entreprise = Entreprise.objects.filter(id=pk).first()
    contact_entrprise = entreprise.contacts.all()
    form = ContactsForm()

    print("contact ", contact_entrprise)
    context = {
        "entreprise": entreprise,
        "contacts_entreprise": contact_entrprise,
        "contact_form": form
    }
    return render(request, 'core/private_view/partial/entreprise/details/contact.html', context)

@login_required
def add_contact_entreprise(request, pk):
    entreprise = Entreprise.objects.filter(id=pk).first()
    form = ContactsForm()
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.entreprise = entreprise
            f.save()

            print("contact saved ", f)
    contact_entrprise = entreprise.contacts.all()
    context = {
        "entreprise": entreprise,
        "contacts_entreprise": contact_entrprise,
        "contact_form": form
    }
    return render(request, 'core/private_view/partial/entreprise/details/contact.html', context)


#contenu views
@login_required
def list_contenu_entreprise(request, pk):
    entreprise = Entreprise.objects.filter(id=pk).first()
    contenu_entrprise = entreprise.contenus.all()
    context = {
        "entreprise": entreprise,
        "contenus_entreprise": contenu_entrprise,
        # "contenu_form": form
    }
    return render(request, "core/private_view/partial/entreprise/details/contenue/list_contenu.html", context)

@login_required
def add_contenu_entreprise(request, pk):
    entreprise = Entreprise.objects.filter(id=pk).first()
    form = ContenuForm()
    if request.method == 'POST':
        form = ContenuForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.entreprise = entreprise
            f.save()

            print("contenu saved ", f)
    contenu_entrprise = entreprise.contenus.all()
    context = {
        "entreprise": entreprise,
        "contenus_entreprise": contenu_entrprise,
        "contenu_form": form
    }
    return render(request, "core/private_view/partial/entreprise/details/contenue/list_contenu.html", context)