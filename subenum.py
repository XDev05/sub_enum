import requests
print("hello bro let's begin our awesome work")
print('''
███████╗██╗   ██╗██████╗         ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██╔════╝██║   ██║██╔══██╗        ██╔════╝████╗  ██║██║   ██║████╗ ████║
███████╗██║   ██║██████╔╝        █████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
╚════██║██║   ██║██╔══██╗        ██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
███████║╚██████╔╝██████╔╝███████╗███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝                                                                    
''') 
domain=input("Put Domain Name:")
#read all subdomains in this list -- you can put any list you want.
file = open("/home/xdev05/Downloads/sub_enum/subdomains-10000.txt")
#now we will open the content of our subomains file.
content = file.read()
#split by newlines.
subdomains = content.splitlines()
for subdomain in subdomains:
    # construct the url
    url = f"http://{subdomain}.{domain}"

    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        pass
    else:
        print("[--->] Discovered subdomain:", url)
