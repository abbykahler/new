from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    
def __repr__(self):
        return f"<Dojo object: {self.name} ({self.city}, {self.state}) [{self.id}]>"
    
class Ninja(models.Model):
    f_name = models.CharField(max_length = 255)
    l_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    
    def __repr__(self):
        return f"<Ninja object: {self.first_name} {self.last_name} ({self.id})>"