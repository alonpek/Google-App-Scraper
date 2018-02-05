
from Naked.toolshed.shell import muterun_js
import demjson
import csv
import os
import sys
import shutil

term_list = ["emotion tracking", "emotion", "mood tracking", "mood", "stress", "stress tracking"]


# If unhandledPromiseRejectionWarning is raised, connect to a different IP address



for term in term_list:
    print("term:", term)

    res_stdout = muterun_js('general_info.js', term).stdout.decode('utf-8')

    try:
        app_data = demjson.decode(res_stdout)
    except demjson.JSONDecodeError:
        print("PROBLEM: Blocked by app store, please change IP address")
        break

    # Make a folder for each search term
    if os.path.exists(term):
        shutil.rmtree(term)
    os.makedirs(term)

    # open a file for writing
    path = os.path.join(term, term + '.csv')
    with open(path, 'w') as app_csv:

        # create the csv writer object
        writer = csv.writer(app_csv)
        count = 0
        for app in app_data:
            # Get review information
            if count == 0:
                header = app.keys()
                writer.writerow(header)
                count += 1
            writer.writerow(app.values())

    for app in app_data:
        if not os.path.exists(os.path.join(term, 'reviews')):
            os.makedirs(os.path.join(term, 'reviews'))
            #shutil.rmtree(os.path.join(term, 'reviews'))
       # os.makedirs(os.path.join(term, 'reviews'))


        path = os.path.join(term, 'reviews', app['title'] + '.csv')

        with open(path, 'w') as rev_csv:
            writer = csv.writer(rev_csv)
            count = 0

            # For each file, make a csv with reviews of that app. Csv name is app name
            rev_stdout = muterun_js('app_reviews.js', app['appId']).stdout.decode('utf-8')
            # print(rev_stdout)
            rev_data = demjson.decode(rev_stdout)

            for rev in rev_data:
                # Get review information
                if count == 0:
                    header = rev.keys()
                    writer.writerow(header)
                    count += 1
                writer.writerow(rev.values())
