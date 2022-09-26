import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.deltapltda.com.br/')
except urllib.error.URLError:
    print('\033[0;31mO site da Delta P Eletromecânica não está funcionando no momento!\033[m')
else:
    print('\033[0;32mO site da Delta P Eletromecânica está funciondo normalmente!\033[m')
