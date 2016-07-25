import unittest
import phone

class TestPhoneNumberFormattingTransform(unittest.TestCase):
    def test_phone(self):
        transformer = phone.PhoneNumberFormattingTransform()

        tests = [
            # input, format, expected output
            ('8005551212', '0', '+18005551212'),
            ('8005551212', '1', '+1 800-555-1212'),
            ('8005551212', '2', '(800) 555-1212'),
            ('8005551212', '3', '+1-800-555-1212'),
            ('8005551212', '4', '800-555-1212'),
            ('8005551212', '5', '+1 800 555 1212'),
            ('8005551212', '6', '800 555-1212'),

            ('18005551212', '0', '+18005551212'),
            ('18005551212', '1', '+1 800-555-1212'),
            ('18005551212', '2', '(800) 555-1212'),
            ('18005551212', '3', '+1-800-555-1212'),
            ('18005551212', '4', '800-555-1212'),
            ('18005551212', '5', '+1 800 555 1212'),
            ('18005551212', '6', '800 555-1212'),

            ('(800) 555-1212', '0', '+18005551212'),
            ('(800) 555-1212', '1', '+1 800-555-1212'),
            ('(800) 555-1212', '2', '(800) 555-1212'),
            ('(800) 555-1212', '3', '+1-800-555-1212'),
            ('(800) 555-1212', '4', '800-555-1212'),
            ('(800) 555-1212', '5', '+1 800 555 1212'),
            ('(800) 555-1212', '6', '800 555-1212'),

            ('+448005551212', '0', '+448005551212'),
            ('+448005551212', '1', '+44 800 555 1212'),
            ('+448005551212', '2', '(0800) 555 1212'),
            ('+448005551212', '3', '+44-800-555-1212'),
            ('+448005551212', '4', '800 555 1212'),
            ('+448005551212', '5', '+44 800 555 1212'),
            ('+448005551212', '6', '0800 555 1212'),

            ('+4 48 005 551 212', '0', '+448005551212'),
            ('+4 48 005 551 212', '1', '+44 800 555 1212'),
            ('+4 48 005 551 212', '2', '(0800) 555 1212'),
            ('+4 48 005 551 212', '3', '+44-800-555-1212'),
            ('+4 48 005 551 212', '4', '800 555 1212'),
            ('+4 48 005 551 212', '5', '+44 800 555 1212'),
            ('+4 48 005 551 212', '6', '0800 555 1212'),

            ('+44 (800) 5551212', '0', '+448005551212'),
            ('+44 (800) 5551212', '1', '+44 800 555 1212'),
            ('+44 (800) 5551212', '2', '(0800) 555 1212'),
            ('+44 (800) 5551212', '3', '+44-800-555-1212'),
            ('+44 (800) 5551212', '4', '800 555 1212'),
            ('+44 (800) 5551212', '5', '+44 800 555 1212'),
            ('+44 (800) 5551212', '6', '0800 555 1212'),


        ]

        for input_number, format_string, expected_output in tests:
            self.assertEqual(expected_output, transformer.transform(input_number, format_string=format_string))

    def test_invalid_phone(self):
        transformer = phone.PhoneNumberFormattingTransform()

        tests = [
            # invalid phone numbers
            # input, format, expected output
            ('5551212', '1', '5551212'),
            ('555-1212', '1', '555-1212'),
            ('1555-1212', '1', '555-1212'),
            ('1-22-555-1212', '1', '555-1212'),
        ]

        for input_number, format_string, expected_output in tests:
            out = transformer.transform(input_number, format_string=format_string)
            self.assertEqual(out, input_number)

    def test_empty_phone(self):
        transformer = phone.PhoneNumberFormattingTransform()

        out = transformer.transform(None, format_string='1')
        self.assertEqual(out, '')

        out = transformer.transform('', format_string='1')
        self.assertEqual(out, '')

        out = transformer.transform('Something', format_string='1')
        self.assertEqual(out, 'Something')
