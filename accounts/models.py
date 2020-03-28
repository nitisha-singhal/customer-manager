from django.db import models

class user(models.Model):
    firstname = forms.CharField(max_length=20, required=True)
    lastname = forms.CharField(max_length=20, required=True)
    skills = forms.CharField(label="Your Skills",
                            widget=CKEditorWidget,
                            required=True)
    country = forms.CharField(max_length=50)
    company = forms.CharField(max_length=20, required=False)
    city = forms.CharField(max_length=50)
    email = forms.EmailField()

class upcoming(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    comm_via = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class running(models.Model):
    title = models.CharField(max_length=100)
    progress = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class pending(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    client = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class deadlines(models.Model):
    client = models.CharField(max_length=50)
    deadline = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.client