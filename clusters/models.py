from django.db import models

class CloudProvider(models.Model):
    CloudProvider = models.TextField(max_length=50,default="AWS")

class Aplication(models.Model):
    aplicationName = models.TextField(max_length=100,default="OpenFaaS")

class Cluster(models.Model):
    cloudProvider = models.ForeignKey(CloudProvider,on_delete=models.CASCADE)
    aplication = models.ForeignKey(Aplication,on_delete=models.CASCADE) 
    clusterName = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    clusterCpu = models.IntegerField(default=0)
    clusterRam = models.IntegerField(default=1024)

class Node(models.Model):
    nodeName = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    cluster = models.ForeignKey(Cluster,on_delete=models.CASCADE)