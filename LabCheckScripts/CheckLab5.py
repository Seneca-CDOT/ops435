#!/usr/bin/env python3

import subprocess
import unittest
import sys
import os
import hashlib
import urllib.request

class lab5a(unittest.TestCase):
    """All test cases for lab5a - sets"""
    
    def test_0(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - Test for file creation: ./lab5a.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab5a.py'), msg=error_output)

    def test_a(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - Test for errors running: ./lab5a.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab5a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - Test for correct shebang line: ./lab5a.py"""
        lab_file = open('./lab5a.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_a_function_read_file_string(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - function read_file_string fails without 1 argument"""
        with self.assertRaises(Exception) as context:
            import lab5a as lab5aStudent
            lab5aStudent.read_file_string()
    
    def test_b_function_read_file_list(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - function read_file_list fails without 1 argument"""
        with self.assertRaises(Exception) as context:
            import lab5a as lab5aStudent
            lab5aStudent.read_file_list()

    def test_c_file_data_txt_exists(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - Test for file creation: ./data.txt"""
        error_output = 'your file data.txt cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./data.txt'), msg=error_output)
    
    def test_d_file_data_txt_has_correct_text(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - Test for correct contents: ./data.txt"""
        error_output = 'your file data.txt has the wrong text(HINT: check that data.txt has the same text it should have from the lab)'
        with open('data.txt') as f:
            string1 = f.read()
        answer = 'Hello World\nThis is the second line\nThird line\nLast line\n'
        self.assertEqual(string1, answer, msg=error_output)

    def test_e_function_read_file_string_correct_output(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - Test for output: ./lab5a.py"""
        try:
            import lab5a as lab5aStudent
        except:
            self.fail('lab5a.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output or file contents(HINT: compare your output to sample output and check data.txt for correct text)'
        filename = 'data.txt'
        answer = 'Hello World\nThis is the second line\nThird line\nLast line\n'
        self.assertEqual(lab5aStudent.read_file_string(filename), answer, msg=error_output)
    
    def test_f_function_read_file_list_correct_output(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - Test for output: ./lab5a.py"""
        try:
            import lab5a as lab5aStudent
        except:
            self.fail('lab5a.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: there is an extra item in the list, do no use split() to create the list)'
        filename = 'data.txt'
        answer = ['Hello World', 'This is the second line', 'Third line', 'Last line', '']
        self.assertNotEqual(lab5aStudent.read_file_list(filename), answer, msg=error_output)
    
    def test_g_function_read_file_list_correct_output(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - Test for output: ./lab5a.py"""
        try:
            import lab5a as lab5aStudent
        except:
            self.fail('lab5a.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: the items in the list have new-line characters in them try removing them with strip())'
        filename = 'data.txt'
        answer = ['Hello World\n', 'This is the second line\n', 'Third line\n', 'Last line\n']
        self.assertNotEqual(lab5aStudent.read_file_list(filename), answer, msg=error_output)


    def test_h_function_read_file_list_correct_output(self):
        """[Lab 5] - [Investigation 1] - [Part 1] - Files - Test for output: ./lab5a.py"""
        try:
            import lab5a as lab5aStudent
        except:
            self.fail('lab5a.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: make sure your function has the exact output)'
        filename = 'data.txt'
        answer = ['Hello World', 'This is the second line', 'Third line', 'Last line']
        self.assertEqual(lab5aStudent.read_file_list(filename), answer, msg=error_output)


class lab5b(unittest.TestCase):
    """All test cases for lab5b - files"""
    
    def test_0(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for file creation: ./lab5b.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab5b.py'), msg=error_output)

    def test_a(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for errors running: ./lab5b.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab5b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for correct shebang line: ./lab5b.py"""
        lab_file = open('./lab5b.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_a_function_read_file_string(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - function read_file_string fails without 1 argument"""
        with self.assertRaises(Exception) as context:
            import lab5b as lab5bStudent
            lab5bStudent.read_file_string()
    
    def test_b_function_read_file_list(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - function read_file_list fails without 1 argument"""
        with self.assertRaises(Exception) as context:
            import lab5b as lab5bStudent
            lab5bStudent.read_file_list()
    
    def test_a_function_append_file_string(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - function append_file_string fails without 2 argument"""
        with self.assertRaises(Exception) as context:
            import lab5b as lab5bStudent
            lab5bStudent.append_file_string()
    
    def test_c_function_write_file_list(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - function write_file_list fails without 2 argument"""
        with self.assertRaises(Exception) as context:
            import lab5b as lab5bStudent
            lab5bStudent.write_file_list()
    
    def test_d_function_copy_file_add_line_numbers(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - function copy_file_add_line_numbers fails without 2 argument"""
        with self.assertRaises(Exception) as context:
            import lab5b as lab5bStudent
            lab5bStudent.copy_file_add_line_numbers()

    def test_e_file_data_txt_exists(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for file creation: ./data.txt"""
        error_output = 'your file data.txt cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./data.txt'), msg=error_output)
    
    def test_f_file_data_txt_has_correct_text(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for correct contents: ./data.txt"""
        error_output = 'your file data.txt has the wrong text(HINT: check that data.txt has the same text it should have from the lab)'
        with open('data.txt') as f:
            string1 = f.read()
        answer = 'Hello World\nThis is the second line\nThird line\nLast line\n'
        self.assertEqual(string1, answer, msg=error_output)

    def test_g_function_read_file_string_correct_output(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for output: ./lab5b.py"""
        try:
            import lab5b as lab5bStudent
        except:
            self.fail('lab5b.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output or file contents(HINT: compare your output to sample output and check data.txt for correct text)'
        filename = 'data.txt'
        answer = 'Hello World\nThis is the second line\nThird line\nLast line\n'
        self.assertEqual(lab5bStudent.read_file_string(filename), answer, msg=error_output)
    
    def test_h_function_read_file_list_correct_output(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for output: ./lab5b.py"""
        try:
            import lab5b as lab5bStudent
        except:
            self.fail('lab5b.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: make sure your function removes new line characters and exact output)'
        filename = 'data.txt'
        answer = ['Hello World', 'This is the second line', 'Third line', 'Last line']
        self.assertEqual(lab5bStudent.read_file_list(filename), answer, msg=error_output)

    def test_i_function_append_file_string_correct_output_1(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for output: ./lab5b.py"""
        try:
            import lab5b as lab5bStudent
        except:
            self.fail('lab5b.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: make sure function is appending and not overwriting)'
        filename = 'seneca1.txt.checkscript'
        string1 = 'First Line\nSecond Line\nThird Line\n'
        f = open(filename, 'w')
        f.close()
        lab5bStudent.append_file_string(filename, string1)
        lab5bStudent.append_file_string(filename, string1)
        answer = 'First Line\nSecond Line\nThird Line\nFirst Line\nSecond Line\nThird Line\n'
        self.assertEqual(lab5bStudent.read_file_string(filename), answer, msg=error_output)
    
    def test_i_function_append_file_string_correct_output_2(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for output: ./lab5b.py"""
        try:
            import lab5b as lab5bStudent
        except:
            self.fail('lab5b.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: make sure function is appending and not overwriting)'
        filename = 'seneca1.txt.checkscript'
        string1 = 'First Line\nSecond Line\nThird\n'
        f = open(filename, 'w')
        f.close()
        lab5bStudent.append_file_string(filename, string1)
        lab5bStudent.append_file_string(filename, string1)
        answer = 'First Line\nSecond Line\nThird\nFirst Line\nSecond Line\nThird\n'
        self.assertEqual(lab5bStudent.read_file_string(filename), answer, msg=error_output)
    
    
    def test_j_function_write_file_list_correct_output_1(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for output: ./lab5b.py"""
        try:
            import lab5b as lab5bStudent
        except:
            self.fail('lab5b.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: make sure output shows exactly)'
        filename = 'seneca2.txt.checkscript'
        list1 = ['Line 1', 'Line 2', 'Line 3']
        f = open(filename, 'w')
        f.close()
        lab5bStudent.write_file_list(filename, list1)
        answer = 'Line 1\nLine 2\nLine 3\n'
        self.assertEqual(lab5bStudent.read_file_string(filename), answer, msg=error_output)

    def test_j_function_write_file_list_correct_output_2(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for output: ./lab5b.py"""
        try:
            import lab5b as lab5bStudent
        except:
            self.fail('lab5b.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: make sure to write to file NOT append )'
        filename = 'seneca2.txt.checkscript'
        list1 = ['Line 1', 'Line 2', 'Line 5']
        f = open(filename, 'w')
        f.close()
        lab5bStudent.write_file_list(filename, list1)
        lab5bStudent.write_file_list(filename, list1)
        answer = 'Line 1\nLine 2\nLine 5\n'
        self.assertEqual(lab5bStudent.read_file_string(filename), answer, msg=error_output)

    def test_k_function_copy_file_add_line_numbers_correct_output_1(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for output: ./lab5b.py"""
        try:
            import lab5b as lab5bStudent
        except:
            self.fail('lab5b.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: make sure output shows exactly)'
        filename = 'seneca2.txt.checkscript'
        tempfile = 'seneca3.txt.checkscript'
        f = open(tempfile, 'w')
        f.close()
        lab5bStudent.copy_file_add_line_numbers(filename, tempfile)
        answer = '1:Line 1\n2:Line 2\n3:Line 5\n'
        self.assertEqual(lab5bStudent.read_file_string(tempfile), answer, msg=error_output)
    
    def test_k_function_copy_file_add_line_numbers_correct_output_2(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for output: ./lab5b.py"""
        try:
            import lab5b as lab5bStudent
        except:
            self.fail('lab5b.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: make sure to write to file NOT append )'
        filename = 'seneca2.txt.checkscript'
        tempfile = 'seneca3.txt.checkscript'
        f = open(tempfile, 'w')
        f.close()
        lab5bStudent.copy_file_add_line_numbers(filename, tempfile)
        lab5bStudent.copy_file_add_line_numbers(filename, tempfile)
        answer = '1:Line 1\n2:Line 2\n3:Line 5\n'
        self.assertEqual(lab5bStudent.read_file_string(tempfile), answer, msg=error_output)
    
    def test_k_function_copy_file_add_line_numbers_correct_output_3(self):
        """[Lab 5] - [Investigation 1] - [Part 2] - Files - Test for output: ./lab5b.py"""
        try:
            import lab5b as lab5bStudent
        except:
            self.fail('lab5b.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: read instructions again and confirm code follows correctly)'
        filename = 'seneca3.txt.checkscript'
        tempfile = 'seneca4.txt.checkscript'
        lab5bStudent.copy_file_add_line_numbers(filename, tempfile)
        answer = '1:1:Line 1\n2:2:Line 2\n3:3:Line 5\n'
        self.assertEqual(lab5bStudent.read_file_string(tempfile), answer, msg=error_output)


class lab5c(unittest.TestCase):
    """All test cases for lab5c - files"""
    
    def test_0(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - Test for file creation: ./lab5c.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab5c.py'), msg=error_output)

    def test_a(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - Test for errors running: ./lab5c.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab5c.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - Test for correct shebang line: ./lab5c.py"""
        lab_file = open('./lab5c.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_a_function_add(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - function add fails without 2 argument"""
        with self.assertRaises(Exception) as context:
            import lab5c as lab5cStudent
            lab5cStudent.add()
    
    def test_b_function_read_file(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - function read_file fails without 1 argument"""
        with self.assertRaises(Exception) as context:
            import lab5c as lab5cStudent
            lab5cStudent.read_file()

    def test_c_function_add_correct_output_1(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - Test for output: ./lab5c.py"""
        try:
            import lab5c as lab5cStudent
        except:
            self.fail('lab5c.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: compare your output to sample output)'
        answer = 15
        self.assertEqual(lab5cStudent.add(5, 10), answer, msg=error_output)
    
    def test_c_function_add_correct_output_2(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - Test for output: ./lab5c.py"""
        try:
            import lab5c as lab5cStudent
        except:
            self.fail('lab5c.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: make sure you try and convert strings to numbers with int())'
        answer = 10
        self.assertEqual(lab5cStudent.add(5, '5'), answer, msg=error_output)
    
    def test_c_function_add_correct_output_3(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - Test for output: ./lab5c.py"""
        try:
            import lab5c as lab5cStudent
        except:
            self.fail('lab5c.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: should give error message check for correct output)'
        answer = 'error: could not add numbers'
        self.assertEqual(lab5cStudent.add('hello', 10), answer, msg=error_output)
    
    def test_c_function_add_correct_output_4(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - Test for output: ./lab5c.py"""
        try:
            import lab5c as lab5cStudent
        except:
            self.fail('lab5c.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: should give error message check for correct output)'
        answer = 'error: could not add numbers'
        self.assertEqual(lab5cStudent.add(10, 'world'), answer, msg=error_output)
    
    def test_d_function_read_file_correct_output_1(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - Test for output: ./lab5c.py"""
        try:
            import lab5c as lab5cStudent
        except:
            self.fail('lab5c.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: )'
        filename = 'seneca2.txt'
        answer = ['Line 1\n', 'Line 2\n', 'Line 3\n']
        self.assertEqual(lab5cStudent.read_file(filename), answer, msg=error_output)
    
    def test_d_function_read_file_correct_output_2(self):
        """[Lab 5] - [Investigation 2] - [Part 1] - Files - Test for output: ./lab5c.py"""
        try:
            import lab5c as lab5cStudent
        except:
            self.fail('lab5c.py contains errors(HINT: run the function and fix errors')
        error_output = 'incorrect output(HINT: should give error message)'
        filename = 'seneca100000.txt'
        answer = 'error: could not read file'
        self.assertEqual(lab5cStudent.read_file(filename), answer, msg=error_output)

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
        lab_name = 'CheckLab5.py'
        lab_num = 'lab5'
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


