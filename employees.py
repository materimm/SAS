import tests as t
import unittest


def get_employee_birthdays(month, employees):
    if month is None:
        return 'ERROR: Month input is invalid.'
    elif employees is None:
        return 'ERROR: Employees list input is invalid.'
    elif type(month) != int:
        return 'ERROR: Month input is an invalid type.'
    elif type(employees) != list:
        return 'ERROR: Employees list input is an invalid type.'
    elif len(employees) == 0:
        return 'ERROR: No employees found.'

    bd_list = []
    for e in employees:
        if all (key in e for key in ['first_name', 'last_name', 'birthday']):
            bd = e.get('birthday')
            birth_month = bd.split('/')[0]
            if int(birth_month) == month:
                bd_list.append(e.get('first_name') + ' ' + e.get('last_name'))
        else:
            print('missing key')
            continue

    return bd_list


# r = get_employee_birthdays(5, t.get_employee_array())
# print(r)

class TestEmployeeBirthdays(unittest.TestCase):
    def get_simple_employee_list(self):
        return [
            {
                'id':1,
                'first_name': 'Maurice',
                'last_name': 'Materise',
                'birthday': '5/16/1993'
            },
            {
                'id':2,
                'first_name': 'Larkin',
                'last_name': 'Materise',
                'birthday': '7/4/2019'
            },
            {
                'id':3,
                'first_name': 'Smalls',
                'last_name': 'Materise',
                'birthday': '3/15/2013'
            },
            {
                'id':4,
                'first_name': 'John',
                'last_name': 'Smith',
                'birthday': '5/1/1982'
            },
            {
                'id':5,
                'first_name': 'Jane',
                'last_name': 'Doe',
                'birthday': '3/3/1989'
            },
        ]


    def test_basic_success(self):
        e = self.get_simple_employee_list()
        actual = get_employee_birthdays(5, e)
        expected = ['Maurice Materise', 'John Smith']
        self.assertEqual(actual, expected)


    def test_null_month(self):
        e = self.get_simple_employee_list()
        actual = get_employee_birthdays(None, e)
        expected = 'ERROR: Month input is invalid.'
        self.assertEqual(actual, expected)


    def test_null_employees(self):
        actual = get_employee_birthdays(5, None)
        expected = 'ERROR: Employees list input is invalid.'
        self.assertEqual(actual, expected)


    def test_bad_month_type(self):
        e = self.get_simple_employee_list()
        actual = get_employee_birthdays('5', e)
        expected = 'ERROR: Month input is an invalid type.'
        self.assertEqual(actual, expected)


    def test_bad_employee_type(self):
        actual = get_employee_birthdays(5, 5)
        expected = 'ERROR: Employees list input is an invalid type.'
        self.assertEqual(actual, expected)


    def test_empty_list(self):
        actual = get_employee_birthdays(5, [])
        expected = 'ERROR: No employees found.'
        self.assertEqual(actual, expected)