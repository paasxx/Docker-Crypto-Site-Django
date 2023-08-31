# Generated by Django 4.2.1 on 2023-08-28 22:11

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ada",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "ADA",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Avax",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "AVAX",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Bnb",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "BNB",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Btc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "BTC",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Busd",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "BUSD",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Dai",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "DAI",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Doge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "DOGE",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Dot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "DOT",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Etc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "ETC",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Eth",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "ETH",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Hex",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "HEX",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Leo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "LEO",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Ltc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "LTC",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Matic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "MATIC",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Shib",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "SHIB",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Sol",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "SOL",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Steth",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "STETH",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Trx",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "TRX",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Usdc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "USDC",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Usdt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "USDT",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Wbtc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "WBTC",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Wtrx",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "WTRX",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Xrp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True, db_column="Date", null=True)),
                ("open", models.FloatField(blank=True, db_column="Open", null=True)),
                ("high", models.FloatField(blank=True, db_column="High", null=True)),
                ("low", models.FloatField(blank=True, db_column="Low", null=True)),
                ("close", models.FloatField(blank=True, db_column="Close", null=True)),
                (
                    "adj_close",
                    models.FloatField(blank=True, db_column="Adj Close", null=True),
                ),
                (
                    "volume",
                    models.BigIntegerField(blank=True, db_column="Volume", null=True),
                ),
            ],
            options={
                "db_table": "XRP",
                "managed": True,
            },
            managers=[
                ("crypto_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]