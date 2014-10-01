from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML, Fieldset
from crispy_forms.bootstrap import PrependedText

COMPOUND_PERIOD = (
    (1, u"Annually"),
    (2, u"Semi Annually"),
    (4, u"Quarterly"),
    (12, u"Monthly"),
)


class RealCostForm(forms.Form):
    net_price = forms.DecimalField(label='Vehicle net price',
                                   decimal_places=2,
                                   help_text=u"Net price is the amount to be borrowed "
                                             u"and includes applicable government sales taxes, "
                                             u"licensing, fuel fill charge, insurance, dealer PDI, PPSA, "
                                             u"administration fees, and any other applicable environmental "
                                             u"charges/fees and taxes, minus any down payment.")
    rebate = forms.DecimalField(label='Cash rebate',
                                decimal_places=2,
                                help_text=u"The dollar amount of the rebate when using cash or "
                                          u"non-dealership loan.")
    bank_borrowing_rate = forms.DecimalField(label='Bank APR',
                                             decimal_places=2,
                                             help_text=u"The interest rate the bank is offering for a loan.")
    dealership_borrowing_rate = forms.DecimalField(label='Dealership APR',
                                                   decimal_places=2,
                                                   help_text=u"The interest rate the dealership is offering "
                                                             u"for a loan.")
    months_borrowed = forms.ChoiceField(choices=((x, x) for x in range(1, 85)))

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.disable_csrf = False
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Fieldset(
                    'Compare Bank vs Dealership Car Loan',
                    Div(
                        Div(PrependedText('net_price', '$', placeholder='Net price'), css_class="col-lg-12"),
                        Div(PrependedText('rebate', '$', placeholder='Cash rebate'), css_class="col-lg-12"),
                        Div(PrependedText('bank_borrowing_rate', '%', placeholder='Bank borrowing rate'), css_class="col-lg-6"),
                        Div(PrependedText('dealership_borrowing_rate', '%', placeholder='Dealership borrowing rate'), css_class="col-lg-6"),
                        Div(Field('months_borrowed'), css_class="col-lg-12"),
                        css_class="row"
                    ),
                ),
            ),
            Div(
                Div(
                    HTML('<input title="Calculate" type="submit" name="submit" value="Calculate" class="btn btn-primary btn-lg"/>'),
                    css_class="col-lg-12",
                ),
                css_class="row",
            ),
        )
        super(RealCostForm, self).__init__(*args, **kwargs)
