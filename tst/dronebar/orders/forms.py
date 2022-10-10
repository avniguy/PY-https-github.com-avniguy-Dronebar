from django import forms
from .models import Order
from shops.models import Shop


class OrderModelForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class ShopOptionForm(forms.Form):
    shops = Shop.objects.all()

    shop_select = list()
    shop_select.append(('-----','-----'))

    for s in shops:
        tuple1=(s.id,s.name)
        shop_select.append(tuple1)

    shop = forms.ChoiceField(choices=shop_select)
    user_id = forms.CharField(max_length=3,label="User Id", required=False)
