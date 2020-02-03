import csv
import re
import os
from datetime import datetime
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize

# 0.0 Open the parameters.csv, log.csv, and results.csv files, then get a list of available field names from the parameters file and create a dictionary containing the index and value of each field for every row in the file.
def object_engine_main():
    with open('/Users/justinfilip/Documents/GitHub/Object_Engine/Params/parameters.csv', 'r', encoding='UTF-8') as parameters, open('/Users/justinfilip/Documents/GitHub/Object_Engine/Logs/log.csv', "a", encoding='UTF-8') as logs:
        try:
            param_reader = csv.reader(parameters, dialect='excel', skipinitialspace=True, delimiter=',', quotechar='"')
            param_field_selections = {}

            for param_index, param_field in enumerate(param_reader):
                object_parameters = []

                if param_index == 0:
                    param_field_selections.update({param_index:param_field})
                    continue

                else:
                    # convert the selected objects in the parameters record (values) from the dictionary to a list
                    object_parameters = param_field[2].split("#")

                    for object_string_index, object_string in enumerate(object_parameters):
                        object_parameters[object_string_index] = object_string.strip()

                # 0.1 Get a list of files in the directory defined in the current batch of the parameters file (customer), create a second list containing the file names that end in .csv with the file extention removed (objects) and a dictionary containing an index and filename.
                files = os.listdir('/Users/justinfilip/Documents/GitHub/Object_Engine/Objects/' + str(param_field[6]) + '/')
                file_list = []
                objects = []
                file_objects = {}

                for file in files:
                    if file.endswith(".csv"):
                        file_list.append(file)
                        objects.append(file[-4])

                    else:
                        continue

                for object_index, object_item in enumerate(file_list):
                    file_objects.update({object_index:object_item})

                # 1.0 Collect target objects, fields, search string, and desired return parameters from the parameters file.

                # populate the dictionary (target_objects) to store objects and indicies where the indicies of the available objects matched the indicies of the objects in the parameters record (batch)
                target_objects = {}

                for o, ob in enumerate(object_parameters):
                    target_objects.update({o:file_objects[int(ob)]})

                # populate the dictionary (return_parameters) to store fields and indicies where the indicies of the available field matched the indicies of the fields in the parameters record (batch)
                return_parameters_field = param_field[4].split("|")
                return_parameters = {}

                for rp_index, rp_value in enumerate(return_parameters_field):
                    return_parameters[rp_index] = rp_value.strip()

                # get a list of selected target fields within the selected object to execute the search on from the parameters record (batch)
                field_parameters_field = param_field[3].split("|")
                field_parameters = {}

                for fp_index, fp_value in enumerate(field_parameters_field):
                    field_parameters[fp_index] = fp_value.strip()


                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -       
# METHOD 0      # BEGINNING OF STRING / REGEX SEARCH FUNCTION AGAINST SELECTED FIELD
                #
                if int(param_field[1]) == 0:
                    # 2.0 Begin processing batch matching string or regex against selected target fields

                    # for each index, object in target_objects
                    for to_index, to_object in target_objects.items():

                        with open('/Users/justinfilip/Documents/GitHub/Object_Engine/Objects/' + str(param_field[6]) + '/' + str(to_object), 'r', encoding='UTF-8') as engaged_object, open('/Users/justinfilip/Documents/GitHub/Object_Engine/Search Results/' + str(param_field[6]) + '_' + str(target_objects[to_index]) + '_' + str(datetime.now()) + '.csv', "w+", encoding='UTF-8') as results:
                            filtered_object = (line.replace('\n' or '\r', '') for line in engaged_object)
                            object_reader = csv.reader(filtered_object, dialect='excel', skipinitialspace=True, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                            results_writer = csv.writer(results, dialect='excel', skipinitialspace=True, delimiter=',', quotechar='"')
                            row_data = {}

                            if to_object.endswith(".csv"):

                                for n, row in enumerate(engaged_object):

                                    if n > 0:
                                        row_fields = list(next(object_reader))

                                        for rf_index, rf_content in enumerate(row_fields):
                                            rf_content_stripped = re.split(r'\W|\d', rf_content)
                                            rf_content_strung = ' '.join(rf_content_stripped)
                                            rf_content_remnlc = rf_content_strung.replace('(\n|,)', '')
                                            rf_content_cleaned = rf_content_remnlc.replace('  ', ' ')
                                            row_data.update({rf_index:rf_content_cleaned})

                                            for entity, field_parameter in field_parameters.items():
                
                                                if (int(rf_index) == int(field_parameter)):

                                                    # if the selected field contains the search criteria from the parameters file
                                                    if re.match('.*' + param_field[5] + '.*', rf_content_cleaned):
                                                        result_list = []

                                                        # write the selected return field to the search results file
                                                        for x, rp in return_parameters.items():

                                                            if rp == field_parameter:
                                                                result_list.append(row_data[rf_index])

                                                            else:
                                                                try:
                                                                    result_list.append(row_fields[int(rp)])
                                                                except Exception as e:
                                                                    continue

                                                        results_writer.writerow(result_list)

                                                    else:
                                                        pass
                                                else:
                                                    continue
                                    else:
                                        row_fields = row.rstrip().split(',')
                                        first_row = []

                                        for ri, r in return_parameters.items():
                                            field_name = str(row_fields[int(r)]).replace('"', '')
                                            first_row.append(field_name)

                                        results_writer.writerow(first_row)

                            elif to_object.endswith(".xml"):
                                pass

                            else:
                                pass 

                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -       
# METHOD 1      # BEGINNING OF KEYWORD RANKING AGAINST SELECTED FIELD - verified but not using filtered Named Entities yet
                #
                if int(param_field[1]) == 1:
                    # 2.0 Begin processing batch matching string or regex against selected target fields

                    # for each index, object in target_objects
                    for to_index, to_object in target_objects.items():

                        with open('/Users/justinfilip/Documents/GitHub/Object_Engine/Objects/' + str(param_field[6]) + '/' + str(to_object), 'r', encoding='UTF-8') as engaged_object, open('/Users/justinfilip/Documents/GitHub/Object_Engine/Search Results/' + str(param_field[6]) + '_' + str(target_objects[to_index]) + '_' + str(datetime.now()) + '.csv', "w+", encoding='UTF-8') as results:
                            object_reader = csv.reader(engaged_object, dialect='excel', skipinitialspace=True, delimiter=',', quotechar='"')
                            results_writer = csv.writer(results, dialect='excel', skipinitialspace=True, delimiter=',', quotechar='"')
                            row_data = {}

                            if to_object.endswith(".csv"):
                                print(to_object)

                                for n, row in enumerate(engaged_object):

                                    if n > 0:
                                        row_fields = list(next(object_reader))

                                        for rf_index, rf_content in enumerate(row_fields):
                                            rf_content_stripped = re.split(r'\W|\d', rf_content)
                                            rf_content_strung = ' '.join(rf_content_stripped)
                                            rf_content_remnlc = rf_content_strung.replace('(\n|,)', '')
                                            rf_content_cleaned = rf_content_remnlc.replace('  ', ' ')
                                            row_data.update({rf_index:rf_content_cleaned})

                                            for entity, field_parameter in field_parameters.items():
                
                                                if (int(rf_index) == int(field_parameter)):

                                                    result_list = []

                                                    # write the selected return field to the search results file
                                                    for x, rp in return_parameters.items():

                                                        if rp == field_parameter:

                                                            try:

                                                                tokenized_field = word_tokenize(rf_content_cleaned)

                                                                counts = Counter(tokenized_field).most_common(5)
                                                                

                                                            except Exception as e:
                                                                print(e)


                                                            result_list.append(counts)

                                                        else:
                                                            try:
                                                                result_list.append(row_fields[int(rp)])
                                                            except Exception as e:
                                                                continue

                                                    results_writer.writerow(result_list)

                                                else:
                                                    continue
                                    else:
                                        row_fields = row.rstrip().split(',')
                                        first_row = []

                                        for ri, r in return_parameters.items():
                                            field_name = str(row_fields[int(r)]).replace('"', '')
                                            first_row.append(field_name)

                                        results_writer.writerow(first_row)

                            elif to_object.endswith(".xml"):
                                print(to_object)

                            else:
                                pass

                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -       
# METHOD 2      # BEGINNING OF SENTIMENT ANALYSIS AGAINST SELECTED FIELD
                #
                elif int(param_field[1]) == 2:
                    # TOKENIZE EACH SENTENCE - POSITIVE / NEGATIVE - OVERALL CASE / MESSAGE SENTIMENT
                    # TOKENIZE EACH WORD - POSITIVE / NEGATIVE - OVERALL CASE / MESSAGE SENTIMENT
                    # SEE WHICH OF THE ABOVE IS MORE ACCURATE 
                    pass

                else:
                    pass

        except Exception as e:

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -       
    # build logging here
    #
            pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -       
# Functions:
#
object_engine_main() #Execute selected method in parameters record against the selected field

