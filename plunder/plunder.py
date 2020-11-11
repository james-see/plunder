"""Uses brand new features of Python 3"""
import argparse
import threading
from concurrent.futures import ThreadPoolExecutor
import os
import socket
import sys
import time
try:
    from __version__ import __version__
except ModuleNotFoundError:
    from plunder.__version__ import __version__


def getInput(currentip, thread_count):
    """
    Get user input ip address or use default.
    """
    currentnum = 1
    userinput = input(
        f'What query do you want to run? (default {currentip}): ') or currentip
    start_time = time.time()
    print(f'\nChecking for delicious pi around {userinput}...')
    if userinput.endswith('/24'):
        limit = 255
    if limit == 1:
        checkip = userinput.rsplit('.', 1)[0] + f'.{currentnum}'
        checkMacs(checkip)
        print("--- %s seconds ---" % (time.time() - start_time))
        sys.exit(0)
    ip_list = []
    # nice way to fill up the list with the full range
    ip_list.extend([userinput.rsplit('.', 1)[0] +
                    f'.{i}' for i in range(limit)])
    # multi-threading the modern way ;)
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        {executor.submit(checkMacs, ip) for ip in ip_list}
        executor.shutdown(wait=False)
    # always print the time it took to complete
    print("--- %s seconds ---" % (time.time() - start_time))


def prep():
    """
    Get the args and set them.
    """
    parser = argparse.ArgumentParser(description='How to run plunder.')
    parser.add_argument('-q', '--query', help='Your query to search', dest="query", default=".php?id=1")
    parser.add_argument('-v', '--version', action='version',
                        version=__version__)
    parser.add_argument('-j','--json', help='Output in JSON file, otherwise output to screen only.', dest="json_out", action='store_true', default=False)
    args = parser.parse_args()
    return args


def checkMacs(ip_address):
    """
    Checks if mac address found using get_mac_address threaded function.
    Accepts: ip_address var as string
    Returns: nothing
    Prints: found ip of pi if found
    """
    macaddress = str()
    th = threading.Thread(target=ThreadId, args=(ip_address, macaddress))
    th.start()
    th.join(timeout=0.5)
    return


logo = """
                                         
 ____ ____ ____ ____ ____ ____ ____      
||P |||L |||U |||N |||D |||E |||R ||     
||__|||__|||__|||__|||__|||__|||__||     
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|     
                                         
                                                                                                                                                        
"""


def main():
    """
    Main function that runs everything.
    """
    args = prep()
    getInput(args.query)


if __name__ == "__main__":
    print(logo)
    main()
