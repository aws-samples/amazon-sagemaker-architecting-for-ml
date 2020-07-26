import csv
import os

def initialize_output(outfile_name):
    '''
    Writes a new file to disk. Adds two header cols.
    '''
    with open(outfile_name, 'w') as f:
#         writer = csv.writer(f, delimiter='\t')
        f.write(' ') 
    return

def write_rows(rows, data, output_file, bucket, patb):
    '''
    Takes the pair indices, data object and output file name
        Gets the content from the data
        Writes the pair to the outfile
    '''
    
    with open(output_file, 'a') as f:
        
        # loop through rows
        for idx, r in enumerate(rows):
        
            # get the end of this segment
            if idx < (len(rows)-1):
                end_of_snippet = int(rows[idx+1].split('_')[0])
            else:
                end_of_snippet = None
                
            if 'markdown' in r:
                m_idx = int(r.split('_')[0])
                markdown_content = get_markdown(data[m_idx:end_of_snippet])

                f.write(markdown_content)

                f.write('\n')

            elif 'code' in r:
                c_idx = int(r.split('_')[0])

                code_content = get_code(data[c_idx: end_of_snippet])

                f.write('\n')

                f.write(code_content)
                
    os.system('aws s3 cp {} s3://{}/{}/'.format(output_file, bucket, path))
    

def get_code(code_list):
    '''
    Takes the code provided from the NB as a list, converts it to a clean str
    '''
    str_index = code_list.index('   "source": [\n') + 1

    str_rt = ''
    
    for each in code_list[str_index:]:
        
        for b in ['##', '###', ']', "{", "}", '\"', "\\n"]:
            each = each.replace(b, '')

        str_rt += ' {}'.format(each)
    
    return str_rt


def get_markdown(markdown_content):
    '''
    Takes the markdown provided from the NB as a list, converts it to a clean str
    '''
    str_index = markdown_content.index('   "source": [\n') + 1
    
    str_rt = ''
    
    for each in markdown_content[str_index:]:
        
        for b in ['#', '##', '###', '\n', '\\n', ']', "{", "}", '\"']:
            each = each.replace(b, '')

        str_rt += ' {}'.format(each)
            
    return str_rt


def get_cell_placements(file_name):
    '''
    Takes an ipython notebook filename, reads the file, figures out which cells have markdown and code
    '''

    placements = {}
    
    place_list = []
    
    with open(file_name) as f:   
        data = f.readlines()
        
        for idx, row in enumerate(data):

            if 'cell_type' in row: 

                if 'markdown' in row:
                    placements[idx] = 'markdown'
                    
                    add_str = str(idx) + '_markdown'
                    place_list.append(add_str)
                    
                elif 'code' in row:
                    placements[idx] = 'code'
                    add_str = str(idx) + '_code'
                    place_list.append(add_str)
                    
    return data, placements, place_list


def get_rows(placements, place_list):
    '''
    Takes placements and a list, figures out which are markdown/code rows
    '''
    rt = []

    for idx, each in enumerate(place_list):
        if 'code' in each or 'markdown' in each:
            rt.append(each)
                
    return rt

# only look at markdwn directly in front of code
# also drop cases of multiple code cells 

def parse_notebook(input_file, output_file, bucket, path):
    '''
    Main function to parse a single notebook file
        Finds the placements
        Finds the clean rows
        Writes these to a tsv file, then to S3
    '''    
    
    # data is all of the raw data from the file
    # placements is a hashmap of indices within that massive object, specifying markdown or code
    # place list is a str combining the two
    data, placements, place_list = get_cell_placements(input_file)
    
    # returns only the cell indices for clean markdown and/or code
    rows = get_rows(placements, place_list)
    
    write_rows(rows, data, output_file, bucket, path)
        
    return 