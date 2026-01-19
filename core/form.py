from django import  forms

from .models import Entreprise, AddressEntreprise, Contacts, Contenu


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['name', 'description', 'country', 'city', 'email']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'mt-1 block w-full border \
                border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                                            "placeholder": "Entrez le nom de l'entreprise"}),
            'description': forms.Textarea(attrs={'class': 'mt-1 block w-full border \
                border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                                            "placeholder": "Une description court de entreprise "}),
            'country': forms.TextInput(attrs={'class': 'mt-1 block w-full border \
                border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                                            "placeholder": "Entrez le pays"}),
            'city': forms.TextInput(attrs={'class': 'mt-1 block w-full border \
                border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                                            "placeholder": "Entrez la ville "}),
            'email': forms.EmailInput(attrs={'class': 'mt-1 block w-full border \
                border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                                            "placeholder": "Entrez email de l'entreprise, ex:entreprise@exemple.con"}),
        }


class AddressEntrepriseForm(forms.ModelForm):
    class Meta:
        model = AddressEntreprise
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'mt-1 block w-full border \
                border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                                            "placeholder": "Entrez l'adresse de l'entreprise"}),
        }


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'phone']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'mt-1 block w-full border \
                border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                                            "placeholder": "Entrez le nom du contact"}),
            'phone': forms.TextInput(attrs={'class': 'mt-1 block w-full border \
                border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                                            "placeholder": "Entrez le numéro de téléphone"}),
        }


class ContenuForm(forms.ModelForm):
    class Meta:
        model = Contenu
        fields = ['title', 'body', 'is_principal', 'is_active', 'file']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 block w-full border \
                border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                                            "placeholder": "Entrez le titre du contenu"}),
            'body': forms.Textarea(attrs={'class': 'mt-1 block w-full border \
                border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                                            "placeholder": "Entrez le corps du contenu"}),
            'is_principal': forms.CheckboxInput(attrs={'class': 'h-6 w-6 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'}),
            'file': forms.ClearableFileInput(attrs={'class': 'mt-1 block w-full text-sm text-gray-500 \
                file:mr-4 file:py-2 file:px-4 \
                file:rounded-full file:border-0 \
                file:text-sm file:font-semibold \
                file:bg-blue-50 file:text-blue-700 \
                hover:file:bg-blue-100'}),
        }


