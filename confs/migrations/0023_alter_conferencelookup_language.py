# Generated by Django 5.1.3 on 2024-12-03 11:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("confs", "0022_alter_conferencelookup_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conferencelookup",
            name="language",
            field=models.CharField(
                choices=[
                    ("python", "Python"),
                    ("typescript", "TypeScript"),
                    ("javascript", "JavaScript"),
                    ("rust", "Rust"),
                    ("ruby", "Ruby"),
                    ("golang", "Golang"),
                    ("java", "Java"),
                    ("kotlin", "Kotlin"),
                    ("scala", "Scala"),
                    ("swift", "Swift"),
                    ("csharp", "C#"),
                    ("fsharp", "F#"),
                    ("cpp", "C++"),
                    ("css", "CSS"),
                    ("php", "PHP"),
                    ("haskell", "Haskell"),
                    ("ocaml", "OCaml"),
                    ("nix", "Nix"),
                    ("julia", "Julia"),
                    ("django", "Django"),
                    ("flask", "Flask"),
                    ("fastapi", "FastAPI"),
                    ("rails", "Rails"),
                    ("laravel", "Laravel"),
                    ("symfony", "Symfony"),
                    ("kubernetes", "Kubernetes"),
                    ("spring", "Spring"),
                    ("htmx", "HTMX"),
                    ("react", "React"),
                    ("vue", "Vue"),
                    ("angular", "Angular"),
                    ("nextjs", "Next.js"),
                    ("svelte", "Svelte"),
                    ("tailwind", "Tailwind"),
                    ("bootstrap", "Bootstrap"),
                    ("dotnet", ".NET"),
                    ("opensource", "Open Source"),
                    ("linux", "Linux"),
                    ("security", "Security"),
                    ("machinelearning", "Machine Learning"),
                    ("bsd", "BSD"),
                    ("android", "Android"),
                    ("postgres", "Postgres"),
                    ("flutter", "Flutter"),
                ],
                max_length=55,
            ),
        ),
    ]
