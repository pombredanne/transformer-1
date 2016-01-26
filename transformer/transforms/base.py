from transformer.util import APIError

class BaseTransform:
    category = ''
    name = ''
    label = ''
    help_text = ''

    ### Primary interface transforms are concerned about

    def transform(self, value, **kwargs):
        """
        Responsible for performing the transformation on the data.
        Is given a single value and expected to return the desired output.
        """
        self.raise_exception('Must implement transform method')

    def fields(self, *args, **kwargs):
        """
        Allows the transform to define additional fields it needs besides the
        default "input" field.
        """
        return []

    ### Other methods that can be overwritten by transforms in special cases

    def transform_many(transform, inputs, data):
        """
        Takes input values (possibly as a single value, a list, or a dictionary)
        and runs each one through the transform individually.

        The returned output structure will match the input structure. Examples:
        a -> A
        [a, b] -> [A, B]
        {'first': a, 'second': b} -> {'first': A, 'second': B}
        """

        data = data or {}

        if isinstance(inputs, dict):
            outputs = {}
            for k, v in inputs.iteritems():
                outputs[k] = transform.transform(v, **data)
        elif isinstance(inputs, list):
            outputs = []
            for v in inputs:
                outputs.append(transform.transform(v, **data))
        else:
            outputs = transform.transform(inputs, **data)
        return outputs

    def all_fields(self, *args, **kwargs):
        """
        Provides the complete list of field definitions for the transform.
        Defaults to prepending the standard input field to the transform's
        custom-defined fields.

        If you need to override the ordering of the fields displayed to the
        user, you can override this method to have complete control.
        """
        return [
            self.build_input_field(),
        ] + self.fields(*args, **kwargs)

    ### Helpers

    def raise_exception(self, message, status=400):
        raise APIError(message, status)

    @property
    def key(self):
        return '{}.{}'.format(self.category, self.name)

    def to_dict(self):
        return {
            'key': self.key,
            'label': self.label,
            'name': self.name,
            'category': self.category,
            'help_text': self.help_text,
            'type': 'transform'
        }

    def build_input_field(self):
        '''
        Returns the definition for the default "input" field.
        '''

        return {
            'type': 'unicode',
            'required': True,
            'key': 'inputs',
            'label': 'Input',
            'help_text': 'Value you would like to transform.'
        }

    def build_list_input_field(self):
        '''
        Returns the definition for the default "input" field, modified so it
        accepts multiple values.
        '''

        field = self.build_input_field()

        field['list'] = True
        field['help_text'] = 'Values you would like to transform.'
        return field
