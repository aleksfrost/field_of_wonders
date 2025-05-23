# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cards(models.Model):
    card_id = models.IntegerField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards'


class Categories(models.Model):
    categorie_id = models.AutoField(primary_key=True)
    categorie_name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GameRounds(models.Model):
    game = models.ForeignKey('Games', models.DO_NOTHING, blank=True, null=True)
    round = models.ForeignKey('Rounds', models.DO_NOTHING, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'game_rounds'


class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    word = models.ForeignKey('Words', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    letters = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class Prises(models.Model):
    prise_id = models.AutoField(primary_key=True)
    prise_description = models.CharField(blank=True, null=True)
    discount_value = models.IntegerField(blank=True, null=True)
    price_in_scores = models.IntegerField(blank=True, null=True)
    categorie = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    to_show = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prises'


class Rounds(models.Model):
    round_id = models.AutoField(primary_key=True)
    round_scores = models.IntegerField(blank=True, null=True)
    is_word_guessed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'rounds'


class Scores(models.Model):
    score_id = models.AutoField(primary_key=True)
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scores'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, blank=True, null=True)
    password = models.CharField(blank=True, null=True)
    is_admin = models.BooleanField()
    scores = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersPrises(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    prise = models.ForeignKey(Prises, models.DO_NOTHING)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'users_prises'


class Words(models.Model):
    word_id = models.AutoField(primary_key=True)
    word = models.CharField(unique=True)
    description = models.CharField()
    difficulty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'words'
