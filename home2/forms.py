from django import forms

from .models import Availstatic

# Django form for the Availstatic Table

class AvailForm(forms.ModelForm):
    class Meta:
        model = Availstatic
        fields = ('row_date', 'director','manager', 'analyst','logid','starttime_utc','scheduled_start','scheduled_stop','interval_time','duration','total_interval_time','total_productive_status','availability_adherence','total_acd_time','outbound_call','hold_time','total_acw_time','ring_time','available_time','staffed_time','internal_aux_time','aux_default','first_break','second_break','training','lunch','meeting','personal','project','case_management','third_break','coaching','outbound_voice','get_next','vip_escalation','handling_escalation','acdcalls','da_acdcalls','total_acd_other_time','total_acd_aux_out_time','total_acd_aux_in_time','total_aux_in_time','modfied')