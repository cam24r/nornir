import csv
import json
import os


'''
Declaring dictionary and list variables, used for grouping devices, test ceses and storing device output.
'''
groups = []
cases = []
device_data_json = {}


'''
This function displays the format that must be followed so the Testbeds can ge generated.
'''
def intro_inventory():
    print('Your CSV file must be in the following format:')
    print('''
    hostname  IP Address    Port    Username    Password    Group   Type
    R1        192.168.1.1   22      cisco       Cisco123.   Core    ios
    R2        192.168.1.2   22      cisco       Cisco123.   Edge    ios-xe
    R3        192.168.1.3   22      cisco       Cisco123.   Edge    ios-xe
    R4        192.168.1.4   22      cisco       Cisco123.   Core    ios
    R4        192.168.1.4   22      cisco       Cisco123.   DC1     ios
    R3        192.168.1.3   22      cisco       Cisco123.   DC2     ios-xe
    
Note: If you need a device to be in multiple groups, duplicate the device changing the Group value.
	
    ''')

'''
This function reads the CSV and splits the rows by ,
Then, it assigns a key to every field in the CSV
A dictionary is then created using the host as the dictionary key
A default All_testbed is created as well as a testbed for every group found in the CSV Inventory File
'''
def csv_to_testbed():
    csv_file = input('Enter the name of your CSV Inventory file:')
    hosts = {}
    with open(csv_file, "r") as csv_input:
        next(csv_input)
        for line in csv_input:
            # save the csv as a dictionary
            host, ip, port, username, password, group, os_type = line.replace(' ', '').strip().split(',')
            hosts[host] = {'IP': ip, 'Port' : port, 'Username': username, 'Password': password, 'Group': group, 'Type': os_type}
            #print (hosts[host]['Group'])
            if (hosts[host]['Group'] not in groups):
                groups.append(hosts[host]['Group'])
    os.system('clear')

    '''
    This function displays the format that must be followed so the Testbeds can ge generated.
    '''
    with open("hosts.yml", 'w') as default_testbed:
        default_testbed.write("---\n")
        for element in hosts:
            default_testbed.write(element + ":\n")
            default_testbed.write("    hostname: " + hosts[element]['IP'] + "\n")
            default_testbed.write("    port: " + hosts[element]['Port'] + "\n")
            default_testbed.write("    username: " + hosts[element]['Username'] + "\n")
            default_testbed.write("    password: " + hosts[element]['Password'] + "\n")
            default_testbed.write("    platform: " + hosts[element]['Type'] + "\n")
            default_testbed.write("    groups:\n")
            default_testbed.write("        - " + hosts[element]['Group'] + "\n")

    print ("Done!")
if __name__ == "__main__":
    intro_inventory()
    csv_to_testbed()