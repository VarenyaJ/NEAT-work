import /home/suvinit/NEAT/testing_command_script/test_command
#
def HelloThereGeneralKenobi():
    try:
        #with open('config.txt', 'r') as f:import /home/suvinit/NEAT/testing_command_script/test_command
            #f.seek(0)
            '''
            print("Does this work? #1\n")
            print("The config file contains the following:\n")
            #to print out the array of all lines with brackets, use:print(f.readline())
            #to print out every line print(f.readline())
            print(f.read())
            #print()
            #f.seek(0)
            '''
            r = file_path
            R = read_length
            o = output_path
            print('the value of r is %s\n' % str(r))
            print('the value of R is %s\n' % int(R))
            print('the value of o is %s\n' % str(o))
            #

    except FileNotFoundError:
            print("There is a FileNotFoundError\n")
    print("\nHi Josh!")

if __name__ == '__main__':
	HelloThereGeneralKenobi()
