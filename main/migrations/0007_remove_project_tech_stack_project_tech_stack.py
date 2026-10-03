from django.db import migrations, models


def migrate_tech_stacks(apps, schema_editor):
    Project = apps.get_model("main", "Project")
    TechStack = apps.get_model("main", "TechStack")

    for project in Project.objects.all():
        if not project.tech_stack_old:
            continue

        tech_stacks = [
            tech.strip()
            for tech in project.tech_stack_old.split(",")
            if tech.strip()
        ]

        for tech_name in tech_stacks:
            tech_stack, created = TechStack.objects.get_or_create(
                name=tech_name
            )
            project.tech_stack.add(tech_stack)


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_techstack"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="tech_stack",
            new_name="tech_stack_old",
        ),

        migrations.AddField(
            model_name="project",
            name="tech_stack",
            field=models.ManyToManyField(
                to="main.techstack"
            ),
        ),

        migrations.RunPython(
            migrate_tech_stacks,
            migrations.RunPython.noop,
        ),

        migrations.RemoveField(
            model_name="project",
            name="tech_stack_old",
        ),
    ]