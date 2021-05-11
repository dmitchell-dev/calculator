from django import forms


class HomeForm(forms.Form):
    fcf = forms.FloatField(required=False, initial=1000, label="Company's Free Cash Flow")
    fcf_growth = forms.IntegerField(required=False, initial=6, label="Percent annual free cash flow growth")
    short_term_years = forms.IntegerField(required=False, initial=10, label="Short term years")
    short_discount_rate = forms.FloatField(required=False, initial=10, label="Short term discount rate")
    long_discount_rate = forms.FloatField(required=False, initial=3, label="Long term discount rate")
    shares_outstanding = forms.IntegerField(required=False, initial=1000, label="Common shares outstanding")
    share_price = forms.FloatField(required=False, initial=25.04, label="Share price")
