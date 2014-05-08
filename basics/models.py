from django.db import models

class IP(models.Model):
    addr = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    browser = models.CharField(max_length=200)        

    def __unicode__(self):
        return self.browser
        
    
