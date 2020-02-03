import csv
import re
import xml.etree.ElementTree as ET
import os

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# function to build the customer object-field index for each object directory within the Object Engine/Objects/ directory.
def build_object_field_indicies():
    # with open('/Users/justinfilip/Documents/GitHub/Object_Engine/Objects/customers.csv', 'w+') as customers:
    #     cust_writer = csv.writer(customers, dialect='excel')
    folders = next(os.walk('/Users/justinfilip/Documents/GitHub/Object_Engine/Objects/'))[1]

    for f, directory in enumerate(folders):
        try:
            files = os.listdir('/Users/justinfilip/Documents/GitHub/Object_Engine/Objects/' + str(directory) + '/')
            customer_index_string = str(f)
            file_list = []
            file_objects = {}
            field_index = {}

            for file in files:
                if file.endswith(".csv"):
                    file_list.append(file)
                elif file.endswith(".xml"):
                    file_list.append(file)
                else:
                    continue

            customer_guid_zeros = ""
            for i in range(31 - len(customer_index_string)):
                customer_guid_zeros += "0"

            with open('/Users/justinfilip/Documents/GitHub/Object_Engine/Objects/cofi.csv', 'w+') as cofi:
                cofi_writer = csv.writer(cofi, dialect='excel')

                for object_index, object_item in enumerate(file_list):

                    if object_item.endswith(".csv"):

                        with open('/Users/justinfilip/Documents/GitHub/Object_Engine/Objects/' + str(directory) + '/' + str(file_list[object_index]), 'r') as cofi_target:
                            cofi_reader = csv.reader(cofi_target)
                            field_items = list(next(cofi_reader))
                            cofi_target.seek(0)
                            available_fields = {}

                            # if object_item.endswith(".csv"):

                            for cofi_field_index, cofi_field_content in enumerate(field_items):
                                object_index_string = str(object_index)
                                field_index_string = str(cofi_field_index)

                                object_index_zeros = ""
                                for i in range(30 - len(customer_index_string + object_index_string)):
                                    object_index_zeros += "0"    

                                field_index_zeros = ""
                                for i in range(30 - len(customer_index_string + object_index_string + field_index_string)):   
                                    field_index_zeros += "0"

                                cofi_row = [

                                #build customer guid
                                customer_index_string, 

                                directory, 

                                #build object guid
                                object_index_string, 

                                object_item, 

                                #build field guid
                                field_index_string, 
                                
                                cofi_field_content,

                                #build customer guid
                                "C" + customer_index_string + customer_guid_zeros, 

                                #build object guid
                                "OI" + customer_index_string + object_index_string + object_index_zeros,  

                                #build field guid
                                "FI" + customer_index_string + object_index_string + field_index_zeros + field_index_string, 

                                ]

                                cofi_writer.writerow(cofi_row)
                                file_objects.update({object_index:object_item})
                                available_fields.update({cofi_field_index:cofi_field_content})

                    elif object_item.endswith(".xml"):
                        #parse xml and assign indecies to fields 

                        tree = ET.parse('/Users/justinfilip/Documents/GitHub/Object_Engine/Objects/' + str(directory) + '/' + str(file_list[object_index]))
                        root = tree.getroot()

                        list_of_matches = [item.tag for item in root[1]]
                        list_of_fields = []

                        for match in list_of_matches:
                            list_of_fields.append(re.match("(}\K\w+)", str(match)).group(2))

                        print(list_of_fields)

                        for child in root: 
                            # print(child[2].text)

                            # child_content_stripped = re.split(r'\W|\d', child[3].text)
                            # child_content_strung = ' '.join(child_content_stripped)

                            # print(child[2].tag)
                            pass

                    else:
                        pass

        except Exception as e:
            break

build_object_field_indicies()