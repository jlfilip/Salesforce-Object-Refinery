import csv
import re
import os
from datetime import datetime

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# function to process the batches in the parameters file

#def process_batch():

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    # verified
    # 0.0 Open the parameters.csv, log.csv, and results.csv files, then get a list of available field names from the parameters file and create a dictionary containing the index and value of each field for every row in the file.

with open('/Users/justinfilip/Desktop/files/Python/Object Engine/Params/parameters.csv', 'r') as parameters, open('/Users/justinfilip/Desktop/files/Python/Object Engine/Logs/log.csv', "a") as logs:
    param_reader = csv.reader(parameters)
    #writer = csv.writer(results , dialect='excel')
    param_field_selections = {}

    for param_index, param_field in enumerate(param_reader):
        object_parameters = []
        #batch_param_selections = {}

        if param_index == 0:
            param_field_selections.update({param_index:param_field})
            continue
        else:
            #batch_param_selections.update({param_index:param_field})

            # convert the selected objects in the parameters record (values) from the dictionary to a list
            object_parameters = param_field[1].split("#")

            for object_string_index, object_string in enumerate(object_parameters):
                object_parameters[object_string_index] = object_string.strip()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # verified
    # 0.1 Get a list of files in the directory defined in the current batch of the parameters file (customer), create a second list containing the file names that end in .csv with the file extention removed (objects) and a dictionary containing an index and filename.
            
        files = os.listdir('/Users/justinfilip/Desktop/files/Python/Object Engine/Objects/' + str(param_field[5]) + '/')
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

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    # verified
    # 1.0 Collect target objects, fields, search string, and desired return parameters from the parameters file.

        # populate the dictionary (target_objects) to store objects and indicies where the indicies of the available objects matched the indicies of the objects in the parameters record (batch)
        target_objects = {}

        for o, ob in enumerate(object_parameters):
            target_objects.update({o:file_objects[int(object_parameters[o])]})

        # populate the dictionary (return_parameters) to store fields and indicies where the indicies of the available field matched the indicies of the fields in the parameters record (batch)
        return_parameters_field = param_field[3].split("|")
        return_parameters = {}

        for rp_index, rp_value in enumerate(return_parameters_field):
            return_parameters[rp_index] = rp_value.strip()

        # get a list of selected target fields within the selected object to execute the search on from the parameters record (batch)
        field_parameters_field = param_field[2].split("|")
        field_parameters = {}

        for fp_index, fp_value in enumerate(field_parameters_field):
            field_parameters[fp_index] = fp_value.strip()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    # verified
    # 2.0 Begin processing search batch

        # for each index, object in target_objects
        for to_index, to_object in target_objects.items():
            with open('/Users/justinfilip/Desktop/files/Python/Object Engine/Objects/' + str(param_field[5]) + '/' + str(target_objects[to_index]), 'r') as engaged_object, open('/Users/justinfilip/Desktop/files/Python/Object Engine/Search Results/' + str(param_field[5]) + '_' + str(target_objects[to_index]) + '_' + str(datetime.now()) + '.csv', "w+") as results:
                object_reader = csv.reader(engaged_object)
                results_writer = csv.writer(results, dialect='excel')
                row_headers = {}

                for n, row in enumerate(engaged_object):
                    row_fields = list(next(object_reader))
                    
                    if n > 0:
                        for rf_index, rf_content in enumerate(row_fields):
                            row_headers.update({rf_index:rf_content})

                            for entity, field_parameter in field_parameters.items():
                                if (int(rf_index) == int(field_parameter)):
                                    
                                    # if the selected field contains the search criteria from the parameters file
                                    if re.match(".*" + param_field[4] + ".*", rf_content):
                                        # write the selected return field to the search results file
                                        results_writer.writerow([str(row_headers[0]), str(rf_content)])
                                    else:
                                         pass
                                else:
                                    continue
                    else:
                        for rf_index, rf_content in enumerate(row_fields):
                            row_headers.update({rf_index:rf_content})
                            break















