from django.db import models
import datetime

# Django Model for the sample Db table

class Availstatic(models.Model):
    row_date = models.DateField(blank=True, null=True)
    director = models.CharField(db_column='Director', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=50, blank=True, null=True)  # Field name made lowercase.
    analyst = models.CharField(db_column='Analyst', max_length=101, blank=True, null=True)  # Field name made lowercase.
    logid = models.CharField(max_length=15, blank=True, null=True)
    starttime_utc = models.BigIntegerField(blank=True, null=True)
    scheduled_start = models.CharField(db_column='Scheduled Start', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scheduled_stop = models.CharField(db_column='Scheduled Stop', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    interval_time = models.CharField(db_column='Interval Time', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duration = models.TimeField(blank=True, null=True)
    total_interval_time = models.BigIntegerField(db_column='Total Interval Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_productive_status = models.TimeField(db_column='Total Productive Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    availability_adherence = models.DecimalField(db_column='Availability Adherence', max_digits=41, decimal_places=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_acd_time = models.TimeField(db_column='Total ACD Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    outbound_call = models.TimeField(db_column='Outbound Call', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hold_time = models.TimeField(db_column='Hold Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_acw_time = models.TimeField(db_column='Total ACW Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ring_time = models.TimeField(db_column='Ring Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    available_time = models.TimeField(db_column='Available Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    staffed_time = models.TimeField(db_column='Staffed Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_aux_time = models.TimeField(db_column='Internal AUX Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aux_default = models.TimeField(db_column='AUX Default', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_break = models.TimeField(db_column='First Break', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    second_break = models.TimeField(db_column='Second Break', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    training = models.TimeField(db_column='Training', blank=True, null=True)  # Field name made lowercase.
    lunch = models.TimeField(db_column='Lunch', blank=True, null=True)  # Field name made lowercase.
    meeting = models.TimeField(db_column='Meeting', blank=True, null=True)  # Field name made lowercase.
    personal = models.TimeField(db_column='Personal', blank=True, null=True)  # Field name made lowercase.
    project = models.TimeField(db_column='Project', blank=True, null=True)  # Field name made lowercase.
    case_management = models.TimeField(db_column='Case Management', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    third_break = models.TimeField(db_column='Third Break', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coaching = models.TimeField(db_column='Coaching', blank=True, null=True)  # Field name made lowercase.
    outbound_voice = models.TimeField(db_column='Outbound Voice', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    get_next = models.TimeField(db_column='Get Next', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vip_escalation = models.TimeField(db_column='VIP Escalation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    handling_escalation = models.TimeField(db_column='Handling Escalation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    acdcalls = models.SmallIntegerField(blank=True, null=True)
    da_acdcalls = models.SmallIntegerField(blank=True, null=True)
    total_acd_other_time = models.TimeField(db_column='Total ACD Other Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_acd_aux_out_time = models.TimeField(db_column='Total ACD/AUX Out Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_acd_aux_in_time = models.TimeField(db_column='total ACD/AUX In Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_aux_in_time = models.TimeField(db_column='Total AUX in Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modfied = models.DateTimeField(db_column='Modfied', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return u'%s' %(self.director)
        
    class Meta:
        managed = False
        db_table = 'availstatic'

    # Auto updates the modfied column after the change
    
    def save(self):
        self.modfied = datetime.datetime.today()
        super(Availstatic, self).save()