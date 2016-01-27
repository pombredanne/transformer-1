from transformer.registry import register
from transformer.transforms.base import BaseTransform

class StringReplaceTransform(BaseTransform):

    category = 'string'
    name = 'replace'
    label = 'Replace'
    help_text = 'Replace any character, word or phrase in the text with another character, word or phrase'

    def transform(self, str_input, old, new=u'', **kwargs):
        return str_input.replace(old, new) if str_input and old else u''

    def fields(self, *args, **kwargs):
        return [
            {
                'type': 'unicode',
                'required': True,
                'key': 'old',
                'label': 'Find',
            },
            {
                'type': 'unicode',
                'required': False,
                'key': 'new',
                'label': 'Replace',
                'help_text': 'Leave blank to delete the found text'
            },
        ]

register(StringReplaceTransform())
