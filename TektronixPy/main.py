import pyvisa
from tektronix import TektronixDSO, TektronixMSO, TektronixPortable

def main():
    rm = pyvisa.ResourceManager()

    # Replace 'Your_VISA_Resource_Name' with the VISA resource name of your oscilloscope
    resource_name = 'Your_VISA_Resource_Name'

    # Choose the appropriate oscilloscope class for your device
    oscilloscope = TektronixDSO(rm, resource_name)

    oscilloscope.connect()
    print(oscilloscope.get_idn())
    oscilloscope.disconnect()

if __name__ == '__main__':
    main()
