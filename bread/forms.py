from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):

    class Meta:
        model = Orders
        fields = ('customer', 'order_date', 'order_slot', 'order_details',)

    def clean_order_slot(self):
        data = self.cleaned_data['order_slot']
        if "morning" not in data and "evening" not in data:
            raise forms.ValidationError("Please specify a 'morning' or 'evening' delivery.")
        return data


    def clean_customer(self):
        data = self.cleaned_data['customer']
        if data == None:
            raise forms.ValidationError("Cannot be left blank.")
        return data


"""
widgets = {
    'text': forms.fields.TextInput(attrs={
        'placeholder': 'Enter a to-do item',
        'class': 'form-control input-lg',
    }),
    }
error_messages = {'text': {'required':EMPTY_ITEM_ERROR}}
"""
