#!/usr/bin/env python3 

import subprocess
import unittest
import sys
import os
import hashlib
import urllib.request


class lab4e(unittest.TestCase):
    """All test cases for lab4e - string formatting"""

    def test_0(self):
        """[Lab 4 Extras] - [Investigation 1] - [Part 2] - String Formatting - Test for file creation: ./lab4e.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab4e.py'), msg=error_output)

    def test_a(self):
        """[Lab 4 Extras] - [Investigation 1] - [Part 2] - String Formatting - Test for errors running: ./lab4e.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab4e.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 4 Extras] - [Investigation 1] - [Part 2] - String Formatting - Test for correct shebang line: ./lab4e.py"""
        lab_file = open('./lab4e.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_b(self):
        """[Lab 4 Extras] - [Investigation 1] - [Part 2] - String Formatting - Test for correct output: ./lab4X.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab4e.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        expected_output = b'|-------------Seneca College-------------|\n|      Address          70 The Pond Rd   |\n|      Province               ON         |\n|    Postal Code            M3J3M6       |\n|        City              Toronto       |\n|      Country              Canada       |\n|----------------------------------------|\n'
        error_output = 'your program does not have the correct output(HINT: )'
        self.assertEqual(expected_output, stdout, msg=error_output)


def ChecksumLatest(url=None):
    dat = ''
    with urllib.request.urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            dat = dat + line
    checksum = hashlib.sha256(dat.encode('utf-8')).digest()
    #print("internet", checksum)
    return checksum

def ChecksumLocal(filename=None):
    fil = open(filename, 'r', encoding='utf-8')
    dat = fil.readlines()
    textdata = ''
    for line in dat:
        textdata = textdata + line
    checksum = hashlib.sha256(textdata.encode('utf-8')).digest()
    #print("local", checksum)
    return checksum

def CheckForUpdates():
    try:
        lab_name = 'CheckLab4Extras.py'
        lab_num = 'lab4'
        print('Checking for updates...')
        if ChecksumLatest(url='https://raw.githubusercontent.com/Seneca-CDOT/ops435/master/LabCheckScripts/' + lab_name) != ChecksumLocal(filename='./' + lab_name):
            print()
            print(' There is a update available for ' + lab_name + ' please consider updating:')
            print(' cd ~/ops435/' + lab_num + '/')
            print(' pwd  #   <-- i.e. confirm that you are in the correct directory')
            print(' rm ' + lab_name)
            print(' ls ' + lab_name + ' || wget https://raw.githubusercontent.com/Seneca-CDOT/ops435/master/LabCheckScripts/' + lab_name)
            print()
            return
        print('Running latest version...')
        return
    except:
        # Cleanly skip updating if any errors occur for offline or matrix issues
        print('No connection made...')
        print('Skipping updates...')
        return

if __name__ == '__main__':
    CheckForUpdates()
    wait = input('Press ENTER to run the Lab Check...')
    unittest.main()


