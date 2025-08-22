from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20250816_0730'),  # actual last migration
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersubscriber',
            name='subscribed_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]