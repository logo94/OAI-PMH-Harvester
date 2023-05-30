# Importazione librerie
from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader
from csv import writer
from datetime import date
from time import sleep

url = input("OAI endpoint: ")

def oaiReq(url):
    registry = MetadataRegistry()
    registry.registerReader('oai_dc', oai_dc_reader)
    client = Client(url, registry)
    metadata = client.listRecords(metadataPrefix='oai_dc')
    return metadata

# Apertura foglio Excel di scrittura
with open(date.today().strftime("%d_%m_%y") + '.csv', 'w+', encoding='utf8') as csv_file:

    thewriter = writer(csv_file)
    headerow = ['Identifier', 'Title', 'Creator', 'Publisher', 'Contributor', 'Date', 'Type', 'Format', 'DOI', 'Source', 'Language', 'Relation', 'Coverage', 'Rights', 'Description', 'Subjects']
    thewriter.writerow(headerow)

    for record in oaiReq(url):

        #provare array push
        row = []
        element = record[1].getMap()

        dc_identifier = element['identifier']
        dc_title = element['title']
        dc_creator = element['creator']
        dc_publisher = element['publisher']
        dc_contributor = element['contributor']
        dc__date = element['date']
        dc__type = element['type']
        dc__format = element['format']
        dc_doi = element['identifier']
        dc_source = element['source']
        dc_language = element['language']
        dc_relation = element['relation']
        dc_coverage = element['coverage']
        dc_rights = element['rights']
        dc_descriptions = element['description']   
        dc_subjects = element['subject']

        # ID
        if len(dc_identifier) > 0:
            identifier = dc_identifier[0]
        else: identifier = ""
        row.append(identifier)

        # DC:TITLE
        if len(dc_title) > 0:
            title = element['title'][0]
        else: title = ""
        row.append(title.strip().replace(u'\n', u' ').replace(u'\t', u' '))

        # DC:CREATOR
        if len(dc_creator) > 0:
            creator = element['creator'][0].strip()
        else: creator = ""
        row.append(creator)

        # DC:PUBLISHER
        if len(dc_publisher) > 0:
            publisher = element['publisher'][0]
        else: publisher = ""
        row.append(publisher)

        # DC:CONTRIBUTOR
        if len(dc_contributor) > 0:
            contributor = element['contributor'][0]
        else: contributor = ""
        row.append(contributor)

        # DC:DATE
        if len(dc__date) > 0:
            dc_date = element['date'][0]
        else: dc_date = ""
        row.append(dc_date)

        # DC:TYPE
        if len(dc__type) > 0:
            dc_type = element['type'][0]
        else: dc_type = ""
        row.append(dc_type)

        # DC:FORMAT
        if len(dc__format) > 0:
            dc_format = element['format'][0]
        else: dc_format = ""
        row.append(dc_format)

        # DOI
        if len(dc_doi) > 1:
            doi = element['identifier'][1]
        else: doi = ""
        row.append(doi)

        # DC:SOURCE
        if len(dc_source) > 0:
            source = element['source'][0]
        else: source = ""
        row.append(source)

        # DC:LANGUAGE
        if len(dc_language) > 0:
            language = element['language'][0]
        else: language = ""
        row.append(language)

        # DC:RELATION
        if len(dc_relation) > 0:
            relation = element['relation'][0]
        else: relation = ""
        row.append(relation)

        # DC:COVERAGE
        if len(dc_coverage) > 0:
            coverage = element['coverage'][0]
        else: coverage = ""
        row.append(coverage)

        # DC:RIGHTS
        if len(dc_rights) > 0:
            rights = element['rights'][0]
        else: rights = ""
        row.append(rights)

        # DC:DESCRIPTION
        if len(dc_descriptions) > 0:
            description = element['description'][0]
        row.append(description.replace('\n', ' ').replace('\t', ' '))

        # DC:SUBJECT       
        sublist = len(dc_subjects)
        if sublist > 0:
            for x in range(0, sublist):
                row.append(dc_subjects[x])
        else:
            subject = ""
            row.append(subject)
                
        thewriter.writerow(row)
        sleep(0.1)

print('Operazione completata')
