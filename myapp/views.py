# myapp/views.py

from django.shortcuts import render
from .forms import TicketForm

def ticket_form_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            pnr = form.cleaned_data['pnr']
            option = form.cleaned_data['option']
            ticket_number = form.cleaned_data['ticket_number']
            date = form.cleaned_data['date']
            # Process the form data here, like saving to the database or printing it
            print(f"PNR: {pnr}, Option: {option}, Ticket Number: {ticket_number}, Date: {date}")
    else:
        form = TicketForm()

    return render(request, 'ticket_form.html', {'form': form})
