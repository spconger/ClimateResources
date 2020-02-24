from django.db import models

# Create your models here.
# lookup models
class PersonType(models.Model):
    persontypename=models.CharField(max_length=255)
    persontypedescription =models.TextField(null=True, blank=True)

    def __str__(self):
        return self.persontypename

    class Meta:
        db_table='persontype'

class MediaType(models.Model):
    mediatypename=models.CharField(max_length=255)
    mediatypedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.mediatypename
    
    class Meta:
        db_table='mediatype'
        
class EventType(models.Model):
    eventtypename=models.CharField(max_length=255)
    eventtypedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.eventtypename

    class Meta:
        db_table='eventtype'

class Topic(models.Model):
    topicname=models.CharField(max_length=255)
    topicdescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return sel.topicname

    class Meta:
        db_table='topic'
    
# domain models
class Location(models.Model):
    address1=models.CharField(max_length=255)
    address2=models.CharField(max_length=255, null=True, blank=True)
    city=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    postalcode=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.address1 + ', ' + self.city
    

class ContentPublisher(models.Model):
    publishername=models.CharField(max_length=255)
    publishersemail=models.CharField(max_length=255, null=True, blank=True)
    publisherurl=models.URLField(null=True, blank=True)
    publisheraddress=models.ManyToManyField(Location)
    publisherdescription=models.TextField(null=True, blank=True)
    publisherdateadded=models.DateField(auto_now=True)

    def __str__(self):
        return self.publishername

    class Meta:
        db_table='contentpublisher'



class Person(models.Model):
    personname=models.CharField(max_length=255)
    personemail=models.CharField(max_length=255, null=True, blank=True)
    persontype=models.ManyToManyField(PersonType)
    persontitle=models.CharField(max_length=255, null=True, blank=True)
    persondescription=models.TextField(null=True, blank=True)
    personDateEntered=models.DateField(auto_now=True)

    def __str__(self):
        return self.personname

    class Meta:
        db_table='person'
        verbose_name_plural='people'

class Institution(models.Model):
    institutionname=models.CharField(max_length=255)
    institutionlocation=models.ManyToManyField(Location)
    institutionemail=models.CharField(max_length=255, null=True, blank=True)
    institutionphone=models.CharField(max_length=255, null=True, blank=True)
    institutiondescription=models.TextField(null=True, blank=True)
    institutiondateentered=models.DateField(auto_now=True)

    def __str__(self):
        return self.institutionname
    
    class Meta:
        db_table='institution'

class Event(models.Model):
    eventname=models.CharField(max_length=255)
    eventlocation=models.ManyToManyField(Location)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventtopic=models.ManyToManyField(Topic)
    eventinstitutionid=models.ManyToManyField(Institution)
    contentpublisherid=models.ManyToManyField(ContentPublisher)
    eventdescription=models.TextField()

    def __str__(self):
        return self.eventname

    class Meta:
        db_table='event'

class Media(models.Model):
    title=models.CharField(max_length=255)
    mtype=models.ForeignKey(MediaType, on_delete=models.DO_NOTHING)
    mediapublisher=models.ForeignKey(ContentPublisher, on_delete=models.DO_NOTHING)
    mediaperson=models.ManyToManyField(Person)
    mediatopics=models.ManyToManyField(Topic)
    mediadescription=models.TextField()
    mediadateentered=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table='media'



