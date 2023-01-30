from django.db import models


class Project(models.Model):
    Project_name = models.CharField(max_length=64, primary_key=True, unique=True)
    repo_link = models.URLField(max_length=500)
    permitted_users = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
    )


class Users(models.Model):
    user_id = models.IntegerField(MinValueValidator=0, unique=True)
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)


class TODO(models.Model):
    Project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
    )
    note_text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user_created = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
    )
    ACTIVE = 'Active',
    Closed = 'Closed'
    status_choice = [
        (ACTIVE, 'Active'),
        (Closed, 'Closed'),
    ]
    status = models.CharField(
        max_length=50,
        choices=status_choice,
        default='Status',
    )
