import csv
with open('moolya.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title=(row['title'])
        string = row['subnodes']
        string =map(str.strip, string.split(','))
        for each in string:
            print each
        fp = open (title+".mm", "w")       
        def write_mm (string, endofline=True):
            string = string.replace ("&", "&amp;")
            fp.write (string)
            if endofline:
                fp.write ('\n')

        write_mm ('<?xml version="1.0" encoding="utf-8" standalone="no"?>')
        write_mm ('<map version="0.8.1">')
        write_mm ('<node TEXT="' + title + '">')
        try:
            for each in string:
                write_mm('<node TEXT="' + each+ '">')
                write_mm ('</node>')
        except:
            pass
        write_mm ('</node>')
        write_mm ('</map>')
        print title+ "Mindmap Created!!"