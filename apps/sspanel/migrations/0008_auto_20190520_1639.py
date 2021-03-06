# Generated by Django 2.1.7 on 2019-05-20 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("sspanel", "0007_auto_20190420_2043")]

    operations = [
        migrations.AlterModelOptions(
            name="invitecode",
            options={"ordering": ("used", "-created_at"), "verbose_name_plural": "邀请码"},
        ),
        migrations.RenameField(
            model_name="invitecode", old_name="isused", new_name="used"
        ),
        migrations.RenameField(
            model_name="invitecode", old_name="code_id", new_name="user_id"
        ),
        migrations.RenameField(
            model_name="invitecode", old_name="time_created", new_name="created_at"
        ),
        migrations.RenameField(
            model_name="user", old_name="invited_by", new_name="inviter_id"
        ),
        migrations.RenameField(
            model_name="rebaterecord", old_name="rebatetime", new_name="created_at"
        ),
        migrations.RemoveField(model_name="user", name="invitecode"),
    ]
