#!/usr/bin/env python3

import sys, os, re, subprocess
import logging

""" TODO.TXT Group VIew
USAGE:
    t lsgp -- view by project
    t lspc -- view by context

"""

logging.basicConfig(level=logging.ERROR)

class bcolors:
    HEADER = '\033[0;37m'
    OKBLUE = '\033[0;34m'
    OKGREEN = '\033[0;32m'
    WARNING = '\033[0;33m'
    FAIL = '\033[0;31m'
    ENDC = '\033[0m'

HIGHLIGHTS = (
    ('(A)', bcolors.OKBLUE),
    ('(B)', bcolors.OKGREEN),
    ('(C)', bcolors.WARNING),
    ('(D)', bcolors.HEADER))
# TODO: use colors from todo.sh script or config file ?

COLUMN_W = 40
SPLIT_COLUMNS = True # TODO: change to argument
TERM_W = int(os.popen('stty size', 'r').read().split()[1])
logging.info(f'Terminal width is {TERM_W}')
TODOSH_DIR = '/usr/local/bin' # TODO: change to argument

def main(argv):
    contexts = []
    context_lines = []

    if len(argv) < 2:
        logging.error('ERROR: Missing arguments')
        exit()

    # contexts or projects
    pre = '\+' if '-p' in argv else '@'

    # this ignores final filter and stuff
    """
    with open(argv[0], "r") as f:
        lines = f.readlines()
        # append to end here and switch to front after sorting
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '') + ' ' + ('%02d' % (i + 1))
    """

    # filter for only the actual lines
    # get no colors because strings are weird
    # lines = [l for l in subprocess.check_output(['./todo.sh', '-p', 'ls'], cwd=TODOSH_DIR).split('\n')
            # if len(re.findall('^\d+', l)) > 0]
    lines = subprocess.check_output(['./todo.sh', '-p', 'ls'], cwd=TODOSH_DIR, text=True).split('\n')
    lines = lines[:len(lines) - 3] # get rid of the last unnecessary lines
    logging.info(f'{lines}')
    logging.info('----------------------')

    # numbers from start to end so you can sort later on
    for i in range(len(lines)):
        num = re.findall('^\d+', lines[i])[0]
        lines[i] = re.sub('^\d+', '', lines[i])
        lines[i] = lines[i] + ' ' + num

    # roll through list and add projects into array if they're not there
    for l in lines:
        for r in re.findall('(' + pre + '[a-zA-Z0-9~@#$^*()_=[\]{}|\\,.?:-]*)', l):
            if r not in contexts:
                contexts.append(r)
                context_lines.append([])
            context_lines[contexts.index(r)].append(l.strip())

    logging.info(context_lines)
    logging.info('----------------------')

    # finally add in all the untagged ones
    # contexts.append('')
    # context_lines.append([])
    # for l in lines:
    # 	if len(re.findall('(' + pre + '[A-Za-z0-9]*)', l)) == 0:
    # 		context_lines[-1].append(l.strip())


    context_lengths = sorted([len(c) for c in context_lines])
    logging.info(context_lengths)
    logging.info('----------------------')

    # balance the context list if context is 2x as big as next one
    # TODO /!\ DOES NOT WORK FOR SMALL NUMBER OF PROJECTS (ITEMS <= 1) ?
    if SPLIT_COLUMNS and (context_lengths[-1] * 2 > context_lengths[-2]):
        # find the index of biggest
        # you don't need next here because you know that you're gonna get something
        biggest = [i for i in range(len(context_lines))
                if len(context_lines[i]) == context_lengths[-1]][0]

        chunk1 = context_lines[biggest][:int(context_lengths[-1] / 2)]
        chunk2 = context_lines[biggest][int(context_lengths[-1] / 2):]

        context_lines[biggest] = chunk1
        context_lines.insert(biggest, chunk2)

        # copy biggest over one
        contexts.insert(biggest, contexts[biggest])
        logging.info('split %s into 2 sections.' % contexts[biggest])
        logging.info('----------------------')

    #try:
    # sort lines
    for i in range(len(context_lines)):
        context_lines[i] = sorted(context_lines[i])
        logging.info('Sort context lines ...')
        logging.info(context_lines[i])
        logging.info('----------------------')

    # move number from end
    for i in range(len(context_lines)):
        for j in range(len(context_lines[i])):
            context_lines[i][j] = context_lines[i][j].split()[-1] \
            + ' ' + ' '.join(context_lines[i][j].split()[:-1])
            logging.info('Sort context lines ...')
            logging.info(context_lines[i][j])
            logging.info('TRY 2 ----------------------')

    # columns that will fit
    logging.info('Printing result ...')
    column_offset = 0
    columns = TERM_W / COLUMN_W
    logging.info(f'Columns = {columns} .................')
    while column_offset + columns < len(context_lines) + columns:
        # titles
        logging.info('"TITLES"')
        logging.info(f'column_offset = {column_offset}')
        logging.info(f'column_offset + columns = {column_offset + columns}')
        logging.info(f'len(context_lines) = {len(context_lines)}')
        logging.info(f'min(column_offset + columns, len(context_lines)) = {min(column_offset + columns, len(context_lines))}')
        for i in range(int(column_offset), int(min(column_offset + columns, len(context_lines)))):
            print(contexts[i][:COLUMN_W].ljust(COLUMN_W),end=" ")
        print('')

        count = 0
        empty = False
        while not empty:
            logging.info('"ROWS IN THE SECTION"')
            # all the rows in this section
            empty = True
            for i in range(int(column_offset), int(min(column_offset + columns, len(context_lines)))):
                text = ''
                if count < len(context_lines[i]):
                    empty = False
                    text = context_lines[i][count]
                    text = text.replace(contexts[i] + ' ', '')

                text = text[:COLUMN_W]
                text = text.ljust(COLUMN_W)
                logging.info(f'text is of type {type(text)}')
                logging.info(text)
                logging.info('----------------------')

                logging.info(HIGHLIGHTS)
                for h in HIGHLIGHTS:
                    logging.info(f'h is of type {type(h)}')
                    logging.info(f'h = {h}')
                    logging.info(f'h([0] is of type {type(h[0])}')
                    logging.info(f'h[0] = {h[0]}')
                    text = text.replace(h[0], h[0] + h[1])
                text = text + bcolors.ENDC
                print(f'{text}',end=" ")

            count += 1
            print('')

        column_offset += columns
    #except:
        # logging.error('ERROR')
        # exit()


if __name__ == "__main__":
    main(sys.argv[1:])
