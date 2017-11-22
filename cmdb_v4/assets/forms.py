# coding:utf-8
from django import forms
from assets.models import Host, IDC, Service, Project




#class HostForm(forms.ModelForm):
#    class Meta:
#        model = Host
        #fields = ["node_name", "idc", "room_number", "eth1", "eth2", "mac", "internal_ip", "room_number", "cabinet",
        #         "server_cabinet_id", "number", "business", "service", "env", "status",
        #          "cpu", "hard_disk", "memory", "system", "system_cpuarch", "vm", "Services_Code",
        #          "host_application", "guarantee_date", "server_sn", "idle", "editor"]

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ["node_name", "idc", "eth1", "internal_ip", "remote_port", "business", "service", "env", "status","cpu", "hard_disk", "memory", "system", "system_cpuarch", "vm", "host_application", "idle", "editor","user_root","user_weblogic","user_bqadm","user_deploy","user_wls81","user_oracle"]

class IdcForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = ['name', "bandwidth", "operator", 'type', 'linkman', 'phone', 'network', 'address', 'comment']
		
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['service_name', "aliases_name", "project_contact", 'project_contact_backup', 'description', 'sort']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'port', 'remark']


#class Project_docForm(forms.ModelForm):
#   class Meta:
#        model = Project
#        fields = ["description"]
