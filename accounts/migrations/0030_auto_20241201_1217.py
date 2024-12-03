# Generated by Django 5.1.3 on 2024-12-01 12:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0029_remove_account_accounts_ac_text_4d0dfa_idx_and_more"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
              CREATE TRIGGER accounts_search_vector_trigger
              BEFORE INSERT OR UPDATE OF username, username_at_instance, display_name, instance, search
              ON accounts_account
              FOR EACH ROW EXECUTE PROCEDURE
              tsvector_update_trigger(
                search, 'pg_catalog.english', username, username_at_instance, display_name, instance
              );
            """,
            reverse_sql="""
              DROP TRIGGER IF EXISTS accounts_search_vector_trigger
              ON accounts_account;
            """,
        ),
    ]