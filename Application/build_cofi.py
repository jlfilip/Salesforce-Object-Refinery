import csv
import os

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# function to build the customer object-field index for each object directory within the Object Engine/Objects/ directory.
def build_object_field_indicies():
    with open('/Users/justinfilip/Desktop/files/Python/Object Engine/Objects/customers', 'w+') as customers:
        cust_writer = csv.writer(customers, dialect='excel')
        folders = next(os.walk('/Users/justinfilip/Desktop/files/Python/Object Engine/Objects/'))[1]

        for f, directory in enumerate(folders):
            cust_writer.writerow([directory])
            files = os.listdir('/Users/justinfilip/Desktop/files/Python/Object Engine/Objects/' + str(directory) + '/')
            file_list = []
            file_objects = {}
            field_index = {}

            for file in files:
                if file.endswith(".csv"):
                    file_list.append(file)
                else:
                    continue

            with open('/Users/justinfilip/Desktop/files/Python/Object Engine/Objects/' + str(directory) + '/cofi', 'w+') as cofi:
                cofi_writer = csv.writer(cofi, dialect='excel')

                for object_index, object_item in enumerate(file_list):

                    with open('/Users/justinfilip/Desktop/files/Python/Object Engine/Objects/' + str(directory) + '/' + str(file_list[object_index]), 'r') as cofi_target:
                        cofi_reader = csv.reader(cofi_target)
                        field_items = list(next(cofi_reader))
                        cofi_target.seek(0)
                        available_fields = {}

                        for cofi_field_index, cofi_field_content in enumerate(field_items):
                            cofi_row = [object_index, object_item, cofi_field_index, cofi_field_content]
                            cofi_writer.writerow(cofi_row)
                            file_objects.update({object_index:object_item})
                            available_fields.update({cofi_field_index:cofi_field_content})

build_object_field_indicies()