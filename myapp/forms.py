# myapp/forms.py

from django import forms

class TicketForm(forms.Form):
    pnr = forms.CharField(max_length=20, label='PNR', widget=forms.TextInput(attrs={'placeholder': 'Enter PNR'}))
    
    OPTION_CHOICES = [
        ('boss', 'Boss'),
        ('eda', 'Eda'),
        ('all', 'All'),
    ]
    option = forms.ChoiceField(choices=OPTION_CHOICES, initial='all', label='Option')
    
    ticket_number = forms.CharField(max_length=20, label='Ticket Number', widget=forms.TextInput(attrs={'placeholder': 'Enter Ticket Number'}))
    
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
