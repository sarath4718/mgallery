from typing import Any
from django import forms

class MovieForm(forms.Form):
    
    title=forms.CharField()

    options=(
        ("Action","Action"),
        ("Romance","Romance"),
        ("Thriller","Thriller")
    )

    genre=forms.ChoiceField(choices=options)

    language=forms.CharField()

    year=forms.CharField()

    run_time=forms.IntegerField()

    director=forms.CharField()

    def clean(self):

        cleaned_data=super().clean()

        year=cleaned_data.get("year")

        run_time=cleaned_data.get("run_time")

        if run_time>210:
            error_message1= "Run time should be lesser than 210 minutes"
            self.add_error("run_time",error_message1)

        elif run_time<60:
            error_message2="Run time should be greater than 60 minutes"

            self.add_error("run_time",error_message2)

        if int(year)<1990:

            error_message="year should be >1990"

            self.add_error("year",error_message)

