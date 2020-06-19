from django.core.management.base import BaseCommand
from shoedata.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Adds initial data to ShoeType and ShoeColor database tables.'

    def add_arguments(self, parser):
        parser.add_argument('--bootstrap_data', action='store_true')

    def handle(self, *args, **options):
        shoe_types = ['sneaker',
                      'boot',
                      'sandal',
                      'dress',
                      'other',
                        ]
        color_choices = [
            'Red',
            'Orange',
            'Yellow',
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            'White',
            'Black',
        ]

        pre_existing_types =[]
        pre_existing_colors = []

        for shoe_type in shoe_types:
            try:
                ShoeType.objects.get(style=shoe_type)
                pre_existing_types.append(shoe_type)
            except Exception:
                self.stdout.write(self.style.SUCCESS(
                    'Adding type: %s' % shoe_type))
                new_type = ShoeType.objects.create(
                    style=shoe_type
                )
                new_type.save()

        for color_choice in color_choices:
            try:
                ShoeColor.objects.get(color_name=color_choice)
                pre_existing_colors.append(color_choice)
            except Exception:
                self.stdout.write(self.style.SUCCESS(
                    'Adding color: %s' %color_choice))
                new_color = ShoeColor.objects.create(
                    color_name=color_choice
                )
                new_color.save()

        if pre_existing_types:
            self.stdout.write(self.style.ERROR(
                'The following shoe types already existed: "%s"'
                % pre_existing_types))

        if pre_existing_colors:
            self.stdout.write(self.style.ERROR(
                'The following shoe colors already existed: "%s"'
                % pre_existing_colors))
        
        self.stdout.write(self.style.SUCCESS('Bootstrap_data complete!!!'))
            
            