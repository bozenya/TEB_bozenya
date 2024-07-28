# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArcherPerson(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'archer_person'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Celownik(models.Model):
    id_celownik = models.AutoField(db_column='ID_celownik', primary_key=True)  # Field name made lowercase.
    rodzaj = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celownik'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

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


class Klient(models.Model):
    id_klient = models.AutoField(db_column='ID_klient', primary_key=True)  # Field name made lowercase.
    id_zakup = models.ForeignKey(DjangoMigrations, models.DO_NOTHING, db_column='ID_zakup', to_field=None, blank=True, null=True)  # Field name made lowercase.
    imie = models.CharField(blank=True, null=True)
    nazwisko = models.CharField(blank=True, null=True)
    e_mail = models.CharField(blank=True, null=True)
    haslo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'klient'


class Luki(models.Model):
    id_³uk = models.AutoField(db_column='ID_³uk', primary_key=True)  # Field name made lowercase.
    id_w³aœciwoœci = models.ForeignKey('Wlasciwosci', models.DO_NOTHING, db_column='ID_w³aœciwoœci', blank=True, null=True)  # Field name made lowercase.
    id_uzbrojenie = models.IntegerField(db_column='ID_uzbrojenie', blank=True, null=True)  # Field name made lowercase.
    rodzaj = models.CharField()
    producent = models.CharField(blank=True, null=True)
    model = models.CharField(blank=True, null=True)
    lata_gwarancji = models.IntegerField(blank=True, null=True)
    koszt = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    numer_lokalizacji = models.CharField(unique=True, blank=True, null=True)
    dostêpnoœæ = models.BooleanField()
    opis = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'luki'


class Magazyn(models.Model):
    id_magazyn = models.AutoField(db_column='ID_magazyn', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    nazwa = models.TextField(blank=True, null=True)
    miejscowosc = models.TextField(blank=True, null=True)
    ulica = models.TextField(blank=True, null=True)
    dostepnosc_produktu = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'magazyn'


class MagazynLuk(models.Model):
    id_magazyn_³uk = models.AutoField(db_column='ID_magazyn_³uk', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    id_³uk = models.ForeignKey(Luki, models.DO_NOTHING, db_column='ID_³uk', blank=True, null=True)  # Field name made lowercase.
    id_magazyn = models.ForeignKey(Magazyn, models.DO_NOTHING, db_column='ID_magazyn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'magazyn_luk'

class OpinieLuki(models.Model):
    ID_³uk = models.IntegerField()
    rodzaj = models.CharField(max_length=255, default='Inne')
    producent = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    opinie = models.TextField(null=True, blank=True)
    data_dodania_opinii = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'opinie_luki'

class Podstawka(models.Model):
    id_podstawka = models.AutoField(db_column='ID_podstawka', primary_key=True)  # Field name made lowercase.
    rodzaj = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'podstawka'


class Producent(models.Model):
    id_producenta = models.AutoField(db_column='ID_producenta', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    nazwa = models.CharField(blank=True, null=True)
    kraj = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producent'


class ProducentDoLuk(models.Model):
    id_producenta_do_³uk = models.AutoField(db_column='ID_producenta_do_³uk', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    id_producenta = models.ForeignKey(Producent, models.DO_NOTHING, db_column='ID_producenta', blank=True, null=True)  # Field name made lowercase.
    id_³uk = models.ForeignKey(Luki, models.DO_NOTHING, db_column='ID_³uk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producent_do_luk'


class Rodzaj(models.Model):
    id_rodzaj = models.AutoField(db_column='ID_rodzaj', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    nazwa = models.CharField(blank=True, null=True)
    specyfikacja = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rodzaj'


class RodzajDoLuk(models.Model):
    id_rodzaj_do_³uk = models.AutoField(db_column='ID_rodzaj_do_³uk', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    id_rodzaj = models.ForeignKey(Rodzaj, models.DO_NOTHING, db_column='ID_rodzaj', blank=True, null=True)  # Field name made lowercase.
    id_³uk = models.ForeignKey(Luki, models.DO_NOTHING, db_column='ID_³uk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rodzaj_do_luk'


class Serwis(models.Model):
    id_klient = models.IntegerField(db_column='ID_klient')  # Field name made lowercase.
    id_typ_serwis = models.ForeignKey('TypSerwisowania', models.DO_NOTHING, db_column='ID_typ_serwis', blank=True, null=True)  # Field name made lowercase.
    data_serwisu = models.DateField(blank=True, null=True)
    gwarancja = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serwis'


class Spust(models.Model):
    id_spust = models.AutoField(db_column='ID_spust', primary_key=True)  # Field name made lowercase.
    rodzaj = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spust'


class Stabilizator(models.Model):
    id_stabilizator = models.AutoField(db_column='ID_stabilizator', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    rodzaj = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stabilizator'


class Strzay(models.Model):
    id_strza³y = models.AutoField(db_column='ID_strza³y', primary_key=True)  # Field name made lowercase.
    rodzaj = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strza³y'


class TypSerwisowania(models.Model):
    id_typ_serwis = models.AutoField(db_column='ID_typ_serwis', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    nazwa = models.CharField(blank=True, null=True)
    opis = models.CharField(blank=True, null=True)
    zmienione_uzbrojenie = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typ_serwisowania'


class UsunieteLuki(models.Model):
    id_³uk = models.IntegerField(db_column='ID_³uk')  # Field name made lowercase.
    id_w³aœciwoœci = models.IntegerField(db_column='ID_w³aœciwoœci', blank=True, null=True)  # Field name made lowercase.
    id_uzbrojenie = models.IntegerField(db_column='ID_uzbrojenie', blank=True, null=True)  # Field name made lowercase.
    rodzaj = models.CharField()
    producent = models.CharField(blank=True, null=True)
    model = models.CharField(blank=True, null=True)
    lata_gwarancji = models.IntegerField(blank=True, null=True)
    koszt = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    numer_lokalizacji = models.CharField(unique=True, blank=True, null=True)
    dostêpnoœæ = models.BooleanField()
    opis = models.IntegerField(blank=True, null=True)
    czas_usuniêcia = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'usuniete_luki'


class Uzbrojenie(models.Model):
    id_uzbrojenie = models.AutoField(db_column='ID_uzbrojenie', primary_key=True)  # Field name made lowercase.
    id_celownik = models.IntegerField(db_column='ID_celownik', blank=True, null=True)  # Field name made lowercase.
    id_podstawka = models.IntegerField(db_column='ID_podstawka', blank=True, null=True)  # Field name made lowercase.
    id_stabilizator = models.IntegerField(db_column='ID_stabilizator', blank=True, null=True)  # Field name made lowercase.
    id_spust = models.IntegerField(db_column='ID_spust', blank=True, null=True)  # Field name made lowercase.
    id_strza³y = models.IntegerField(db_column='ID_strza³y', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uzbrojenie'


class Wlasciwosci(models.Model):
    id_w³aœciwoœci = models.AutoField(db_column='ID_w³aœciwoœci', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    min_draw_weight = models.IntegerField(blank=True, null=True)
    max_draw_weight = models.IntegerField(blank=True, null=True)
    min_draw_lenght = models.IntegerField(blank=True, null=True)
    max_draw_lenght = models.IntegerField(blank=True, null=True)
    ata = models.IntegerField(db_column='ATA', blank=True, null=True)  # Field name made lowercase.
    brace_height = models.IntegerField(blank=True, null=True)
    let_off = models.IntegerField(blank=True, null=True)
    typ_bloczków = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wlasciwosci'


class Zakup(models.Model):
    id_zakup = models.AutoField(db_column='ID_zakup', primary_key=True)  # Field name made lowercase.
    id_³uk = models.ForeignKey(Luki, models.DO_NOTHING, db_column='ID_³uk', blank=True, null=True)  # Field name made lowercase.
    data_zakupu = models.DateField(blank=True, null=True)
    czas_gwarancji = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zakup'
