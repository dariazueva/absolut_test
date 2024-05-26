import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from survey.models import Answer, Question


def load_csv_data(file_name, model_class, fields_mapping,
                  with_foreign_keys=False):
    path = os.path.join(settings.BASE_DIR, 'data', file_name)
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data = {}
            for field, index in fields_mapping.items():
                if index is not None:
                    if with_foreign_keys and field in ['next_question',
                                                       'question']:
                        data[field] = Question.objects.get(
                            pk=int(row[index])
                        ) if row[index] else None
                    else:
                        if field not in ['next_question',
                                         'question'] or row[index]:
                            data[field] = row[index] if row[
                                index] != '' else None
            if with_foreign_keys:
                model_class.objects.update_or_create(id=row[0], defaults=data)
            else:
                if 'next_question' in data:
                    del data['next_question']
                model_class.objects.update_or_create(id=row[0], defaults=data)


class Command(BaseCommand):
    help = 'Load data from CSV files'

    def handle(self, *args, **options):
        self.load_questions(with_foreign_keys=False)
        self.load_questions(with_foreign_keys=True)
        self.load_answers()
        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))

    def load_questions(self, with_foreign_keys):
        fields_mapping = {'id': 0, 'text': 1, 'question_type': 2,
                          'next_question': 3}
        load_csv_data('questions.csv', Question, fields_mapping,
                      with_foreign_keys)

    def load_answers(self):
        fields_mapping = {'id': 0, 'text': 1, 'question': 2,
                          'next_question': 3}
        load_csv_data('answers.csv', Answer, fields_mapping,
                      with_foreign_keys=True)
