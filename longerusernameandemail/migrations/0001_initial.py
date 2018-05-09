# encoding: utf-8
from django.db import models
from longerusernameandemail import MAX_EMAIL_LENGTH, MAX_USERNAME_LENGTH, REQUIRE_UNIQUE_EMAIL
from longerusernameandemail import MAX_FIRST_NAME_LENGTH, MAX_LAST_NAME_LENGTH
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Changing field 'User.username'
        db.alter_column('auth_user', 'username', models.CharField(max_length=MAX_USERNAME_LENGTH()))
        # Increase length of email field to match
        db.alter_column('auth_user', 'email', models.CharField(max_length=MAX_EMAIL_LENGTH()))

        db.alter_column('auth_user', 'first_name', models.CharField(max_length=MAX_FIRST_NAME_LENGTH()))
        db.alter_column('auth_user', 'last_name', models.CharField(max_length=MAX_LAST_NAME_LENGTH()))

        # Add an index to make email field unique
        db.create_index('auth_user', ['email'], unique=REQUIRE_UNIQUE_EMAIL())

    def backwards(self, orm):

        # Changing field 'User.username'
        db.alter_column('auth_user', 'username', models.CharField(max_length=35))
        db.alter_column('auth_user', 'email', models.CharField(max_length=75))
        db.alter_column('auth_user', 'first_name', models.CharField(max_length=30))
        db.alter_column('auth_user', 'last_name', models.CharField(max_length=30))
        db.delete_index(
            'auth_user',
            ['email'],
        )

    models = {}

    complete_apps = ['django_monkeypatches']
