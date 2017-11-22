# coding:utf-8
from django import forms
from ticket.models import WorkSheet

class WorkSheetForm(forms.ModelForm):
    class Meta:
        model = WorkSheet
        fields = ['user','work_title','project_name','version','script_path','approval_user','stream_num','malfunction_content',
                  'version_path','online_date','version_update_content','initial_state','opinion','test_report','type']

