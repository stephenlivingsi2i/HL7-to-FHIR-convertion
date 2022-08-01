import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
import subprocess
import os

@api_view(['GET'])
def hl7_to_fhir_conversion(request, template_name, resource_name):
    print(request.data)
    os.chdir('C:\\Users\\Lenovo\\Documents\\Fhir convertion')
    exe_cmd = "Microsoft.Health.Fhir.Liquid.Converter.Tool.exe convert "
    hl7_data = "-n C:\\Users\\Lenovo\\Documents\\HL7-to-FHIR\\FHIR-Converter\\data\\SampleData\\Hl7v2\\ADT-A01-01.hl7 "
    fhir_template = "-d C:\\Users\\Lenovo\\Documents\\HL7-to-FHIR\\FHIR-Converter\\data\\Templates\\" + template_name + " "
    output_file_path = "-f C:\\Users\\Lenovo\\Documents\\HL7-to-FHIR\\FHIR-Converter\\data\\output\\ADT-A01-01.json "
    conversion_resource_type = "-r " + resource_name

    s = subprocess.check_output(exe_cmd +
                                hl7_data +
                                fhir_template +
                                output_file_path +
                                conversion_resource_type, shell=True)

    output_file_read = 'C:\\Users\\Lenovo\\Documents\\HL7-to-FHIR\\FHIR-Converter\\data\\output\\ADT-A01-01.json'
    with open(output_file_read, 'r',
              encoding="utf8") as f:
        output = json.load(f)
    return Response({"string": output})
