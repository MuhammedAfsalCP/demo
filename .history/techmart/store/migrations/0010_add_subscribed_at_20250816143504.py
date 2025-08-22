# store/migrations/0010_add_subscribed_at.py
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_previous_migration_name'),  # <-- replace with your last migration
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersubscriber',
            name='subscribed_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
