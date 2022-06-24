import sys
sys.path.append("/home/suvinit/NEAT/testing_command_script/test_command")
#
def HelloThereGeneralKenobi():
    try:
        with open('config.txt', 'rt') as FILEREAD:
            print("Does this work? #1\n")
            print("\nreadlines makes:\n")
            print(FILEREAD.readlines())
            FILEREAD.seek(0)
            print("\nCheck 1\n")
            #
            print("\nThis is where the fun begins:\n")
            read_vars = FILEREAD.read()
            print("\n" + f"{read_vars}")
            #
            '''
            print("\nCheck 2\n")
            read_line_by_line = FILEREAD.readlines()
            print("\nreading lines:")
            print("\nCheck 3\n")
            for read_line_by_line in FILEREAD:
                print("\n" + f"{read_line_by_line}")
            print("\nCheck 4\n")
            '''
            ####    ASK JOSH FOR HELP WITH THIS PART    ####
        #Strip Newlines
        mylines = []
        with open ('config.txt', "rt") as myfile:
            for line in myfile:
                mylines.append(line)
            print("\nCheck 4.1\n")
            for element in mylines:
                print(element)
            print("\nCheck 5\n")
            myfile.seek(0)
            for line in myfile:
                print(mylines[0].find(" = "))
        print("\nCheck 6\n")
                #
            #
    except FileNotFoundError:
            print("There is a FileNotFoundError\n")
            print("\nHi Josh!")
            #
        #
    #
#
if __name__ == '__main__':
    print("Check 0\n")
    HelloThereGeneralKenobi()
    #print("Bah-weep-Graaaaagnah wheep ni ni bong")

