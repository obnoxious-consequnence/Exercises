import re

if __name__ == '__main__':
    with open('./addresses.txt') as f:
        addresses = f.read()

    #ALL NAMES TODO returns an emtpy li
    names = re.compile(r'\n\n((\w+ ){1,3}\w+)\n') 
    allNames = names.findall(addresses)
    print('All names: {}'.format(allNames))
    print('--------------------------------------------------')

    # ALL PHONE NUMBERS
    phone = re.compile(r'\d{2} \d{2} \d{2} \d{2}')
    allPhones = phone.findall(addresses)
    print('All phones: {}'.format(allPhones))
    print('--------------------------------------------------')

    #ALL ZIPCODES
    zip = re.compile(r'\n(\d{4})')
    allZips = zip.findall(addresses)
    print('All zips: {}'.format(allZips))
    print('--------------------------------------------------')

    #ALL ZIPCODES WITH CITY NAMES TODO Crashes after hitting æøå
    zipCity = re.compile(r'\d{4} [a-zA-ZæøåÆØÅ]+ *[a-zA-ZæøåÆØÅ]+')
    allZipCities = zipCity.findall(addresses)
    print('All zipCities: {}'.format(allZipCities))

    print('--------------------------------------------------')
    #ALL STREET NAMES TODO Dosnt work properly
    streets = re.compile(r'\n([a-zA-ZæøåÆØÅ]+)')
    allStreets = streets.findall(addresses)
    print('All street names: {}'.format(allStreets))

