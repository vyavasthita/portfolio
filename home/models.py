from django.db import models


class SkillType(models.Model):
    name                =           models.CharField(max_length=100)

    def __str__(self):
        return (self.name)


class Skill(models.Model):
    skill_type          =           models.ForeignKey(SkillType, on_delete=models.CASCADE)
    name                =           models.CharField(max_length=50)
    experience          =           models.CharField(max_length=50)
    proficiency         =           models.IntegerField()
    remarks             =           models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return (self.name)

class Company(models.Model):
    name                =           models.CharField(max_length=100, verbose_name="Organization Name")
    from_date           =           models.DateField(verbose_name="From")
    to_date             =           models.DateField(verbose_name="To")
    location            =           models.CharField(max_length=100, verbose_name="Location")

    def __str__(self):
        return (self.name)

    def __iter__(self):
        for field in self._meta.fields():
            yield (field.verbose_name, field.value_to_string(self))

class ProfessionalProject(models.Model):
    company             =           models.ForeignKey(Company, on_delete=models.CASCADE)
    designation         =           models.CharField(max_length=50, verbose_name="Designation")
    title               =           models.CharField(max_length=100, verbose_name="Title")
    client              =           models.CharField(max_length=100, verbose_name="Client")
    team_size           =           models.IntegerField(verbose_name="Team Size")
    description         =           models.TextField(verbose_name="Description")
    role                =           models.CharField(max_length=100, verbose_name="Role")
    responsibilities    =           models.TextField(verbose_name="Responsibilities")
    environment         =           models.CharField(max_length=200, verbose_name="Environment")
    remarks             =           models.CharField(max_length=100, blank=True, null=True, verbose_name="Remarks")

    def __str__(self):
        return str(self.company) + '_' + str(self.title)

    def __iter__(self):
        for field in self._meta.fields:
            yield (field.verbose_name, field.value_to_string(self))
