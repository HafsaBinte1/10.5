from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.


def main(request):

    context = {
        'name_list': ['Hafsa', 'changed', 'a', 'better'],
        'data_filter': datetime.now(),
        'default_use': 'Changed Value',
        'add_filter_int': 20,
        'capfirst_filter': 'Bangladesh',
        'cut_filter': "Changed Hafsa",
        'dictsort_filter': [
            {'name': 'Changed', 'age': 21},
            {'name': 'Values', 'age': 27},
            {'name': 'Here', 'age': 26},
            {'name': 'Now', 'age': 29},
        ],
        'escape_filter': "<strong> Changed </strong> is Better < BOY",
        'first_filter': ['Banana', 'Grapes', 'Pineapple'],
        'last_filter': ['Banana', 'Grapes', 'Pineapple'],
        'length_filter': ['Banana', 'Grapes', 'Pineapple', 'Strawberry', 'Blueberry'],
        'line_numbers_filter': '"Updated Line \nSecond Line \nThird Line',
        'lower_filter': 'BETTER Hafsa',
        'upper_filter': 'changed is doing better',
        'title_filter': 'changed is doing better in Title',
        'random_filter': ['x', 'y', 'z', 'p', 'q'],
        'slice_filter': ['x', 'y', 'z', 'p', 'q'],
        'time_filter': datetime.now(),
        'timesince_filter': datetime.now() - timedelta(days=5),
        'truncatechars_filter': "Changed Hafsa is a better boy",
        'wordcount_filter': "Changed is a better person. He can do more",
        'truncatewords_filter': "Changed is a better person. He can do more",
        'striptags_filter': "<i>Changed</i> <button>improved</button> <span>skills</span>",
        'pluralize_filter': 10,
        'make_list_filter': "Improved",
        'addslashes': "I'm Changed",
        'center_filter': "Improved",
        'divisible_by': 9,
        'filesizeformat': 987654321,
        'slugify': "Changed is number 2 slug",
        'list_of_value': ['Subject', 'Cost', 'Availability'],
        'list_of_value_course_name': ['Java', 'JavaScript', 'React', 'Django'],
    }

    return render(request, 'main.html',context)

