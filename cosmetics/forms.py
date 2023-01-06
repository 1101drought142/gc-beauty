from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, help_text = "Имя")
    phone = forms.CharField(max_length=100, required=True, help_text = "Номер")

class OrderForm(forms.Form):
    
    name = forms.CharField(max_length=100, required=True, help_text = "Имя")
    mail = forms.CharField(max_length=100, required=True, help_text = "e-mail")
    phone = forms.CharField(max_length=100, required=True, help_text = "Номер")

    city = forms.CharField(max_length=100, required=True, help_text = "Город")
    street = forms.CharField(max_length=100, required=True, help_text = "Улица")

    index = forms.IntegerField(required=True, help_text = "Индекс")
    house = forms.IntegerField(required=True, help_text = "Дом")
    flat = forms.IntegerField(required=True, help_text = "Квартира")

    payment_type = forms.CharField(max_length=100, required=True, help_text = "Cпособ оплаты")
