# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ('shuup_testing', '0001_initial'),
        ('shuup_testing', '0002_add_filters'),
        ('shuup_testing', '0003_update_managers'),
    ]

    dependencies = [
        ('shuup', '0001_squashed_0039_alter_names'),
        ('campaigns', '0001_squashed_0011_alter_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarrierWithCheckoutPhase',
            fields=[
                ('customcarrier_ptr', models.OneToOneField(
                    serialize=False,
                    to='shuup.CustomCarrier',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('shuup.customcarrier', )),
        migrations.CreateModel(
            name='ExpensiveSwedenBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(
                    serialize=False,
                    to='shuup.ServiceBehaviorComponent',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('shuup.servicebehaviorcomponent', )),
        migrations.CreateModel(
            name='PaymentWithCheckoutPhase',
            fields=[
                ('custompaymentprocessor_ptr', models.OneToOneField(
                    serialize=False,
                    to='shuup.CustomPaymentProcessor',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('shuup.custompaymentprocessor', ), ),
        migrations.CreateModel(
            name='PseudoPaymentProcessor',
            fields=[
                ('paymentprocessor_ptr', models.OneToOneField(
                    serialize=False,
                    to='shuup.PaymentProcessor',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
                ('bg_color', models.CharField(
                    blank=True,
                    max_length=20,
                    verbose_name='Payment Page Background Color',
                    default='white')),
                ('fg_color', models.CharField(
                    blank=True,
                    max_length=20,
                    verbose_name='Payment Page Text Color',
                    default='black')),
            ],
            options={
                'abstract': False,
            },
            bases=('shuup.paymentprocessor', ), ),
        migrations.CreateModel(
            name='UltraFilter',
            fields=[
                ('catalogfilter_ptr', models.OneToOneField(
                    serialize=False,
                    to='campaigns.CatalogFilter',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
                ('categories', models.ManyToManyField(
                    to='shuup.Category', related_name='ultrafilter2')),
                ('category', models.ForeignKey(
                    to='shuup.Category', null=True,
                    related_name='ultrafilte5')),
                ('contact', models.ForeignKey(null=True, to='shuup.Contact')),
                ('derp', models.ForeignKey(
                    to='shuup.Category',
                    null=True,
                    related_name='ultrafilte55')),
                ('product', models.ForeignKey(null=True, to='shuup.Product')),
                ('product_type', models.ForeignKey(
                    null=True, to='shuup.ProductType')),
                ('product_types', models.ManyToManyField(
                    to='shuup.ProductType', related_name='ultrafilter3')),
                ('products', models.ManyToManyField(
                    to='shuup.Product', related_name='ultrafilter1')),
                ('shop_product', models.ForeignKey(
                    null=True, to='shuup.ShopProduct')),
                ('shop_products', models.ManyToManyField(
                    to='shuup.ShopProduct', related_name='ultrafilter4')),
            ],
            options={
                'abstract': False,
            },
            bases=('campaigns.catalogfilter', )),
    ]