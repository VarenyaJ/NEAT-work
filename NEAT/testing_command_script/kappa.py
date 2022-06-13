import click
import os.path
@click.command()
#combine code from readingBETA
def read_back_cfg():
	print("Check 2.1")
	try:
		mylines = []
		with open ('neat.cfg', "rt") as myfile:
			for line in myfile:
				mylines.append(line)
			print("\nCheck 2.2\n")
			for element in mylines:
				if "@" in mylines:
				    element=mylines[mylines.find("@")+1:].split()[0]
				else:
				    element=element
				print(element)
				print("\nCheck 2.3\n")
			print("\nCheck 2.4\n")
			myfile.seek(0)
			for line in myfile:
				print(mylines[0].find(" = "))
			print("\nCheck 2.5\n")
	except FileNotFoundError:
            print("There is a FileNotFoundError\n")
            print("\nHi Josh!")

if __name__ == '__main__':
	print("\nThis is where the pain begins\n")
	read_back_cfg()
	print("\nBah-weep-Graaaaagnah weep ni ni bong\n")
################################<THOUGHTS BELOW>################################
#When opening config.txt in write-mode
#Realized that the config file only opens in same directory as script
#Maybe change that?
#In progress...
