from django import forms
from .models import Appointments, Service

class appointForm(forms.ModelForm):
    BookingD=forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'dateselect'}))

    class Meta:
        model=Appointments
        fields=['Name','ServiceName','Age','BookingD','BookingT']
        # widgets = {
        #     'Booking': forms.DateTimeField()
        # }
        # widgets = {
        # # 'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        #     'Name': forms.CharField(attrs={'class': 'col-md-12 form-group'}),
        #     'Age':forms.IntegerField(attrs={'class': 'col-md-12 form-group'}),
        #     'Description': forms.Textarea(attrs={'class': 'col-md-12 form-group'})
        #
        # }
#
# class appointForm(forms.Form):
#     Name = forms.CharField()
#     ServiceName = forms.ModelChoiceField(queryset=Service.objects.all())
#     Age = forms.IntegerField()
#     Booking = forms.DateTimeField()
#     Description = forms.TextField()
