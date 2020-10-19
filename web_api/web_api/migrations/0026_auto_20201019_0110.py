# Generated by Django 3.0.3 on 2020-10-19 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_api', '0025_auto_20200902_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stripecustomerinformation',
            name='customer_currency',
        ),
        migrations.RemoveField(
            model_name='stripecustomerinformation',
            name='payment_method_card_brand',
        ),
        migrations.RemoveField(
            model_name='stripecustomerinformation',
            name='payment_method_card_exp_month',
        ),
        migrations.RemoveField(
            model_name='stripecustomerinformation',
            name='payment_method_card_exp_year',
        ),
        migrations.RemoveField(
            model_name='stripecustomerinformation',
            name='payment_method_card_last4',
        ),
        migrations.RemoveField(
            model_name='stripecustomerinformation',
            name='payment_method_id',
        ),
        migrations.AddField(
            model_name='stripecustomerinformation',
            name='plan_product_name',
            field=models.CharField(help_text="The product's name. Displayed to users.", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stripecustomerinformation',
            name='subscription_cancel_at',
            field=models.IntegerField(help_text='A date in the future at which the subscription will automatically get canceled.', null=True),
        ),
        migrations.AddField(
            model_name='stripecustomerinformation',
            name='subscription_cancel_at_period_end',
            field=models.BooleanField(help_text='If the subscription has been canceled with the at_period_end flag set to true, cancel_at_period_end on the subscription will be true.', null=True),
        ),
        migrations.AddField(
            model_name='stripecustomerinformation',
            name='subscription_canceled_at',
            field=models.IntegerField(help_text='If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with cancel_at_period_end, canceled_at will still reflect the date of the initial cancellation request, not the end of the subscription period when the subscription is automatically moved to a canceled state.', null=True),
        ),
        migrations.AddField(
            model_name='stripecustomerinformation',
            name='upcoming_invoice_total',
            field=models.IntegerField(help_text='total cost in cents to be billed to customer via next subscription invoice.', null=True),
        ),
    ]
