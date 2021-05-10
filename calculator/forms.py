from django import forms


class HomeForm(forms.Form):
    fcf = forms.FloatField(required=False, initial=8091.9, label="Company's Free Cash Flow")
    fcf_growth = forms.IntegerField(required=False, initial=25, label="Percent annual free cash flow growth")
    short_term_years = forms.IntegerField(required=False, initial=3, label="Short term years")
    short_discount_rate = forms.IntegerField(required=False, initial=10, label="Short term discount rate")
    long_discount_rate = forms.IntegerField(required=False, initial=3, label="Long term discount rate")
    shares_outstanding = forms.IntegerField(required=False, initial=3283, label="Common shares outstanding")
    share_price = forms.FloatField(required=False, initial=75.02, label="Share price")
