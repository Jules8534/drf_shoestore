from django.core.management.base import BaseCommand
from shoedata.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Adds initial data to ShoeType and ShoeColor database tables.'

    
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

        for shoe_type in shoe_types:
            ShoeType.objects.create(
                style=shoe_type

            )
                
        for color_choice in color_choices:
            ShoeColor.objects.create(
                    color_name=color_choice
                )

        # if pre_existing_types:
        #     self.stdout.write(self.style.ERROR(
        #         'The following shoe types already existed: "%s"'
        #         % pre_existing_types))

        # if pre_existing_colors:
        #     self.stdout.write(self.style.ERROR(
        #         'The following shoe colors already existed: "%s"'
        #         % pre_existing_colors))
        
        self.stdout.write(self.style.SUCCESS('Bootstrap_data complete!!!'))
            
            