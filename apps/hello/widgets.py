from django import forms


class DatePickerWidget(forms.DateInput):
    class Media:
        css = {'all': ('css/bootstrap-datetimepicker.min.css',)}
        js = ['moment.min.js',
              'bootstrap.min.js',
              'bootstrap-datetimepicker.min.js',
              'datepicker.js']
