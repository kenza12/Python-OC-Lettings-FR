from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

def copy_profile_data(apps, schema_editor):
    Profile = apps.get_model('profiles', 'Profile')
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')

    for old_profile in OldProfile.objects.all():
        Profile.objects.create(
            id=old_profile.id,
            user_id=old_profile.user_id,
            favorite_city=old_profile.favorite_city,
        )

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_city', models.CharField(blank=True, max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.User')),
            ],
        ),
        migrations.RunPython(copy_profile_data),
    ]