from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import datetime
from ...models import Question, Choice

fake = Faker()


class Command(BaseCommand):
    help = "Generate fake data"

    def add_arguments(self, parser):
        parser.add_argument(
            "num_questions", type=int, help="Number of fake questions to generate"
        )
        parser.add_argument(
            "num_choices", type=int, help="Number of fake choices per question"
        )

    def handle(self, *args, **options):
        num_questions = options["num_questions"]
        num_choices = options["num_choices"]

        for _ in range(num_questions):
            question_text = fake.sentence(nb_words=6, variable_nb_words=True)
            pub_date = fake.date_time_between(start_date="-1y", end_date="now")
            question = Question(question_text=question_text, pub_date=pub_date)
            question.save()

            for _ in range(num_choices):
                choice_text = fake.sentence(nb_words=3, variable_nb_words=True)
                votes = fake.random_int(min=0, max=1000)
                choice = Choice(question=question, choice_text=choice_text, votes=votes)
                choice.save()

        self.stdout.write(self.style.SUCCESS("Successfully generated fake data."))
