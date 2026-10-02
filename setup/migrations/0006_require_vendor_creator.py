from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def assign_missing_creators(apps, schema_editor):
    Vendor = apps.get_model("setup", "Vendor")
    user_model = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
    david = user_model.objects.filter(username="david").first()

    if david is None:
        raise RuntimeError("Cannot require vendor creator: user 'david' does not exist.")

    Vendor.objects.filter(created_by__isnull=True).update(created_by=david)


class Migration(migrations.Migration):

    dependencies = [
        ("setup", "0005_vendor_created_at_vendor_created_by_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(assign_missing_creators, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="vendor",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="vendors_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]