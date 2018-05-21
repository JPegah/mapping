import json
import glob

ref_map = dict()
# create the dictionary
with open('yearly_keys.txt') as f:
    for line in f:
        ind = line.find(' ')
        if ind == -1:
            print 'so strange'
            continue
        js_obj = json.loads(line[ind+1:])
        key = int(line[:ind+1])
        info = js_obj['provenance']
        ref_map[(info['filename'], info['sheet'], info['row'])] = key


print 'successfully created the mapping!'

output = open('yearly_mapping', mode='w')

for filename in glob.iglob('*.jl'):
    f = open(filename)
    for line in f:
        js = json.loads(line)
        prov_file = js['provenance_filename'][0]
        prov_sheet = js['provenance_sheet'][0]
        prov_row = js['provenance_row'][0]
        if (prov_file, prov_sheet, prov_row) in ref_map.keys():
            output.write(str(ref_map[(prov_file, prov_sheet, prov_row)]))
            output.write(' ')
            output.write(js['doc_id'])
            output.write('\n')

output.close()