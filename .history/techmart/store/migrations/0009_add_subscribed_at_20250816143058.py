# store/migrations/000X_add_subscribed_at.py
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('store', 'XXXX_previous_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersubscriber',
            name='subscribed_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
