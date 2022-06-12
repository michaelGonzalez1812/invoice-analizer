from xml.etree.ElementTree import *

file_name_old = '07-05-2022.xml'
file_name_new = '04-06-2022.xml'

doc_xml_old = parse(file_name_old)
doc_xml_new = parse(file_name_new)

root_old = doc_xml_old.getroot()
root_new = doc_xml_new.getroot()

detail_old = doc_xml_old.find('DetalleServicio')
detail_new = doc_xml_new.find('DetalleServicio')

for child_old in detail_old:
    old_code = child_old.find('CodigoComercial').find('Codigo').text
    for child_new in detail_new:
        new_code = child_new.find('CodigoComercial').find('Codigo').text
        if new_code == old_code:
            name_old = child_old.find('Detalle').text
            name_new = child_new.find('Detalle').text
            amount_old = child_old.find('PrecioUnitario').text
            amount_new = child_new.find('PrecioUnitario').text
            if amount_old != amount_new:
                print("OLD amount: " + amount_old + " code: " + old_code + " name: " + name_old)
                print("NEW amount: " + amount_new + " code: " + new_code + " name: " + name_new)
                print()
