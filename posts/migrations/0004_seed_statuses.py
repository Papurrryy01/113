from django.db import migrations


def seed_statuses(apps, schema_editor):
    Status = apps.get_model("posts", "Status")
    defaults = {
        "draft": "Draft post",
        "archived": "Archived post",
        "published": "Published post",
    }
    for name, description in defaults.items():
        Status.objects.get_or_create(name=name, defaults={"description": description})


def unseed_statuses(apps, schema_editor):
    Status = apps.get_model("posts", "Status")
    Status.objects.filter(name__in=["draft", "archived", "published"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_post_status"),
    ]

    operations = [
        migrations.RunPython(seed_statuses, unseed_statuses),
    ]
