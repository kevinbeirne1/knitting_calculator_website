from django import forms


class CalcForm(forms.Form):
    start_stitches = forms.IntegerField()
    inc_dec_choice = forms.CharField(
        label="Do you want to do an increase or decrease",
        widget=forms.Select(choices=[('inc', "Increase"), ('dec', 'Decrease')])
    )
    final_target_choices = [('final', 'Final Stitch Count'), ('change', 'Change Amount')]

    final_or_target_stitches = forms.CharField(
        label='Do you want to list the final stitch count or the change amount',
        widget=forms.Select(choices=final_target_choices)
    )
    end_stitches = forms.IntegerField(label="Enter target stitch change/count")


