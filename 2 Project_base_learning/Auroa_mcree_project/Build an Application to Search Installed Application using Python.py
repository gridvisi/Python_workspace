# https://www.geeksforgeeks.org/build-an-application-to-search-installed-application-using-python/?ref=rp

# import modules
import winapps

# get each application with list_installed()
for item in winapps.list_installed():
    print(item)