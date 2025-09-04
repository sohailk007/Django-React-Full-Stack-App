from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    
    def __str__(self):
        return self.title
    

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    introducer = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="introduced"
    )
    beneficiary = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="beneficiaries"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.introducer:
            introducer_obj = self.introducer
            # how many people introducer has already introduced
            introduced_count = Account.objects.filter(introducer=introducer_obj).count() + 1

            if introduced_count % 2 == 1:  # odd -> beneficiary = introducer
                self.beneficiary = introducer_obj
            else:  # even -> introducer's introducer beneficiary
                if introducer_obj.introducer and introducer_obj.introducer.beneficiary:
                    self.beneficiary = introducer_obj.introducer.beneficiary
                else:
                    self.beneficiary = introducer_obj  # fallback
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Account {self.account_id}"


    