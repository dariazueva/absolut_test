import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from survey.models import (BusinessType,
                           BusinessDirection,
                           Survey,
                           Question)


def load_csv_data(file_name, model_class, fields_mapping):
    path = os.path.join(settings.BASE_DIR, 'data', file_name)
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data = {field: row[index] if index is not None and row[index] != '' else None
                    for field, index in fields_mapping.items()}
            model_class.objects.get_or_create(**data)


class Command(BaseCommand):
    help = 'Load data from CSV files'

    def handle(self, *args, **options):
        self.load_business_types()
        self.load_business_directions()
        self.load_surveys()
        self.load_main_questions()
        self.load_restaurant_survey()
        self.load_cafe_survey()
        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))

    def load_business_types(self):
        load_csv_data('business_types.csv', BusinessType, {'name': 1})

    def load_business_directions(self):
        load_csv_data('business_directions.csv', BusinessDirection,
                      {'name': 1, 'business_type_id': 2})

    def load_surveys(self):
        load_csv_data('surveys_collection.csv', Survey,
                      {'title': 1, 'business_type_id': 2,
                       'business_direction_id': 3})

    def load_main_questions(self):
        load_csv_data('main_questions.csv', Question,
                      {'text': 1, 'dynamic': 2, 'parent_question_id': 3,
                       'survey_id': 4})

    def load_restaurant_survey(self):
        load_csv_data('restaurant_survey.csv', Question,
                      {'text': 1, 'dynamic': 2, 'parent_question_id': 3,
                       'survey_id': 4})

    def load_cafe_survey(self):
        load_csv_data('cafe_survey.csv', Question,
                      {'text': 1, 'dynamic': 2, 'parent_question_id': 3,
                       'survey_id': 4})

