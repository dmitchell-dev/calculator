from django.views.generic import TemplateView
from django.shortcuts import render
from calculator.forms import HomeForm

import numpy as np

# Create your views here.
class HomePage(TemplateView):
    template_name = "calculator/home.html"

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            intrinsic_value_share = self._dcf_calc(form)
            form = HomeForm()

        args = {"form": form, "result": intrinsic_value_share}
        return render(request, self.template_name, args)

    def _dcf_calc(self, form):
        base_year_fcf_value = form.cleaned_data["fcf"]
        growth_rate_value = form.cleaned_data["fcf_growth"]/100
        short_term_years = form.cleaned_data["short_term_years"]
        discount_rate_value = form.cleaned_data["short_discount_rate"]/100
        longterm_growth_rate_value = form.cleaned_data["long_discount_rate"]/100
        shares_outstanding_value = form.cleaned_data["shares_outstanding"]
        share_price = form.cleaned_data["share_price"]

        year_list = np.array(list(range(1, short_term_years+1)))

        # Caclulation
        fcf = np.sum(
            (base_year_fcf_value * pow((1 + growth_rate_value), year_list))
            / pow((1 + discount_rate_value), year_list)
        )
        dpcf = (
            (
                base_year_fcf_value
                * pow((1 + growth_rate_value), short_term_years+1)
                * (1 + longterm_growth_rate_value)
            )
            / (discount_rate_value - longterm_growth_rate_value)
        ) * (1 / pow((1 + discount_rate_value), short_term_years+1))
        intrinsic_value_share = (fcf + dpcf) / shares_outstanding_value

        return intrinsic_value_share
