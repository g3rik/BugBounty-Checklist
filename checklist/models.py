from django.db import models

class Website(models.Model,):
    name = models.CharField(max_length=255)
    url = models.URLField()
    
    def __str__(self):
        return self.name

class MasterTopic(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):  
        return self.title
    

class MasterChecklist(models.Model):
    title = models.CharField(max_length=255)
    payload = models.TextField(blank=True)
    topic = models.ForeignKey(MasterTopic, on_delete=models.CASCADE, null=True)

    def __str__(self):  
        return self.title
    
class Result(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    checkpoint = models.ForeignKey(MasterChecklist, on_delete=models.CASCADE)
    output = models.TextField()
    
    # def __str__(self):  
    #     return self.website.name + " - " + self.checkpoint.title