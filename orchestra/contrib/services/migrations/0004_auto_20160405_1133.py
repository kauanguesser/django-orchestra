# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20150917_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='periodic_update',
            field=models.BooleanField(default=False, verbose_name='periodic update', help_text='Whether a periodic update of this service orders should be performed or not. Needed for <tt>match</tt> definitions that depend on complex model interactions.'),
        ),
        migrations.AlterField(
            model_name='service',
            name='rate_algorithm',
            field=models.CharField(choices=[('orchestra.contrib.plans.ratings.match_price', 'Match price'), ('orchestra.contrib.plans.ratings.best_price', 'Best price'), ('orchestra.contrib.plans.ratings.step_price', 'Step price')], verbose_name='rate algorithm', help_text='Algorithm used to interprete the rating table.<br>&nbsp;&nbsp;Match price: Only <b>the rate</b> with a) inmediate inferior metric and b) lower price is applied. Nominal price will be used when initial block is missing.<br>&nbsp;&nbsp;Best price: Produces the best possible price given all active rating lines (those with quantity lower or equal to the metric).<br>&nbsp;&nbsp;Step price: All rates with a quantity lower or equal than the metric are applied. Nominal price will be used when initial block is missing.', default='orchestra.contrib.plans.ratings.step_price', max_length=64),
        ),
    ]
