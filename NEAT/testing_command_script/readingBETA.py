import sys
sys.path.append("/home/suvinit/NEAT/testing_command_script/test_command")
import test_command as tc_file
#
def HelloThereGeneralKenobi():
    try:
        with open('config.txt', 'r') as f:
            print("Does this work? #1\n")
            print("\nreadlines makes:\n")
            print(f.readlines())
            f.seek(0)
            print("\nCheck 1\n")
            #
            print("\nThis is where the fun begins\n")
            Text = ["0"]
            Text_Cur = ""
            for i in range (len(f.readlines())):
                print("length of text inside the document is " + f"{len(f.readlines())}" )
                Text[i] = f.readlines()[i]
                Text_Cur = Text[Text.find("@")+1:].split()
                print("\n" + Text_Cur + "\n")
            print("Bah-weep-Graaaaagnah wheep ni ni bong")
            #
            print("read makes:\n")
            f.seek(0)
            print(f.read())
            f.seek(0)
            print("\nPost 2\n")
            #
        #
        '''
        with open('config.txt', 'r') as f:import /home/suvinit/NEAT/testing_command_script/test_command
            f.seek(0)
            print("Does this work? #1\n")
            print("The config file contains the following:\n")
            #to print out the array of all lines with brackets, use:print(f.readline())
            #to print out every line print(f.readline())
            print(f.read())
            #print()
            #f.seek(0)
            ###
            r = tc_file.file_path
            R = tc_file.read_length
            o = tc_file.output_path
            print('the value of r is %s\n' % str(r))
            print('the value of R is %s\n' % int(R))
            print('the value of o is %s\n' % str(o))
            print('the value of bam is %s\n' % bool(tc_file.bam))
            '''
            #
        #

    except FileNotFoundError:
            print("There is a FileNotFoundError\n")
    print("\nHi Josh!")

if __name__ == '__main__':
	HelloThereGeneralKenobi()
