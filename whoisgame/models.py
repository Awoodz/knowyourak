from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    das = models.IntegerField()
    gender = models.BooleanField(default=False)
    spawn_counter = models.IntegerField(default=0)
    bad_answer_counter = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Photograph(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    employee_number = models.IntegerField()
    employees = models.ManyToManyField(Employee, through="Order")

    def __str__(self):
        return (f"Photo {self.id} - {self.name}")


class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photograph, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return (f"Ordre {self.photo} - {self.employee}")
