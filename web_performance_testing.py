import socket, time, requests
from sys import getsizeof
from termcolor import colored
import os
os.system('color')

def set_hostname(url):
    runCheck = input(colored("\nChoose an opiton (1 or 2): ",'green'))
    print(colored("\n1. Default run",'yellow'))
    print(colored("\n2. Other",'yellow'))
    global url_input
    if runCheck == '1':
        for _ in url:
            if url[4] == 's' and url[5] == ':' and url[-4] == '.':
                hostname = url.replace('https://www.','')
                url_input = url
                break

            if url[4] == 's' and url[5] == ':' and url[-3] == '.':
                hostname = url.replace('https://www.','')
                url_input = url
                break

            if url[4] == 's' and url[5] == ':' and url[-4] != '.':
                hostname = url.replace('https://www.','')
                url_input = url+'.com'
                break

            if url[4] == 's' and url[5] == ':' and url[-3] != '.':
                hostname = url.replace('https://www.','')
                url_input = url+'.com'
                break

            if url[3] == 'p' and url[4] == ':' and url[-4] == '.':
                hostname = url.replace('http://www.','')
                url_input = url
                break

            if url[3] == 'p' and url[4] == ':' and url[-3] == '.':
                hostname = url.replace('http://www.','')
                url_input = url
                break

            if url[3] == 'p' and url[4] == ':' and url[-4] != '.':
                hostname = url.replace('http://www.','')
                url_input = url+'.com'
                break

            if url[3] == 'p' and url[4] == ':' and url[-3] != '.':
                hostname = url.replace('http://www.','')
                url_input = url+'.com'
                break

            if url[2] == 'w' and url[3] == '.':
                hostname = url.replace('www.','')
                url_input = 'http://'+url
                break

            if url[4] != ':' and url[-3] == '.':
                hostname = url
                url_input = 'http://www.'+url
                break

            if url[4] != ':' and url[-4] == '.':
                hostname = url
                url_input = 'http://www.'+url
                break

            if url[4] != ':' and url[-3] != '.':
                hostname = url+'.com'
                url_input = 'http://www.'+url+'.com'
                break

            if url[4] != ':' and url[-4] != '.':
                hostname = url+'.com'
                url_input = 'http://www.'+url+'.com'
                break
        return hostname
    elif runCheck == '2':
        for _ in url:
            if url[4] == 's' and url[5] == ':':
                hostname = url.replace('https://','')
                url_input = url
                break
            if url[3] == 'p' and url[4] == ':':
                hostname = url.replace('http://','')
                url_input = url
                break
        return hostname

ip_addr = ''
def dns_check(hname):
    global dns_start, dns_stop, ip_addr
    try:
        dns_start = time.time()
        ip_addr = socket.gethostbyname(hname)
        dns_stop = time.time()
    except:
        dns_stop = dns_start
        print(colored('-----------------------------','cyan'))
        print(colored('[-] hostname not found: ', 'red')+colored(hname, 'cyan'))

def response_check(url):
    global handshake_start, handshake_stop, response, data_length, response_time
    try:
        handshake_start = time.time()
        response = requests.get(url)
        handshake_stop = time.time()
        data_length = getsizeof(response.text)
        response_time = response.elapsed.total_seconds()
    except:
        handshake_stop = handshake_start
        response_time = 0
        data_length = 0
        print(colored('[-] no response from ', 'red')+colored(url, 'cyan'))
        print(colored('-----------------------------','cyan'))

#------ EXECTUE ------#
status = True
while status:
    print('\n')
    print(colored('-------------------------------', 'cyan'))
    print(colored('|  Performance Testing (URL)  |', 'cyan'))
    print(colored('-------------------------------', 'cyan'))
    print(colored("Note:- '.com is the default'", 'yellow'))
    print('\n')
    url_input = input(colored('Enter URL: ', 'green')).lower()
    host_name = set_hostname(url_input)
    print('\n')
    dns_check(host_name)
    response_check(url_input)
    print(colored('-----------------------------','cyan'))
    print(colored('[+] IP Address: ', 'magenta')+colored(str(ip_addr), 'cyan'))
    print(colored('[+] URL: ', 'magenta')+colored(url_input, 'cyan'))
    print(colored('-----------------------------','cyan'))
    print('\n')
    print(colored('***** URL Performance Test Result *****', 'green'))
    print(colored('---------------------------------------', 'green'))
    print(colored('[>] DNS time             = %.2f ms', 'yellow') % ((dns_stop - dns_start) * 1000))
    print(colored('[>] HTTP handshake time  = %.2f ms', 'yellow') % ((handshake_stop - handshake_start) * 1000))
    print(colored('[>] HTTP data time       = %.2f ms', 'yellow') % (response_time))
    print(colored('[>] Data received        = %d bytes', 'yellow') % (data_length))

    check = True
    while check:
        loop = input(colored('\nDo you want to continue? (Y or N): ', 'magenta')).lower()
        if loop == 'y':
            check = False
            status = True
        elif loop == 'n':
            check = False
            status = False
        else:
            print(colored('Incorrect option! Try again..','red'))
            check = True
