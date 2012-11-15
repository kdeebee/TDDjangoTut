"""
you can delete the example test that Django put in there.
In this test, we'll create a Poll and save it to the database,
then retrieve it again to check the poll was saved properly.

You'll notice that in this test we don't use Selenium,
instead we interact with our application at a much lower level.
"""

from django.test import TestCase
from django.utils import timezone
from polls.models import Choice, Poll
from polls.forms import PollVoteForm


class PollsVoteFormTest(TestCase):

    def test_form_renders_poll_choices_as_radio_inputs(self):
        # set up a poll with a couple of choices
        poll1 = Poll(question='6 times 7', pub_date=timezone.now())
        poll1.save()
        choice1 = Choice(poll=poll1, choice='42', votes=0)
        choice1.save()
        choice2 = Choice(poll=poll1, choice='The Ultimate Answer', votes=0)
        choice2.save()

        # set up another poll to make sure we only see the right choices
        poll2 = Poll(question='time', pub_date=timezone.now())
        poll2.save()
        choice3 = Choice(poll=poll2, choice='PM', votes=0)
        choice3.save()

        # build a voting form for poll1
        form = PollVoteForm(poll=poll1)

        # check it has a single field called 'vote', which has right choices:
        self.assertEquals(form.fields.keys(), ['vote'])

        # choices are tuples in the format (choice_number, choice_text):
        self.assertEquals(form.fields['vote'].choices, [
            (choice1.id, choice1.choice),
            (choice2.id, choice2.choice),
            ])

        # check it uses radio inputs to render
        self.assertIn('input type="radio"', form.as_p())
