# main_with_ini.py
from OCR.libs.cStringEx import cStringEx
from backports import configparser

cse = cStringEx()
cfg = configparser.ConfigParser()
cfg.read('config.ini')

for option in cfg['DEFAULT']:
    cse.cprint("DEFAULT {0} : {1} : {2}".format(option,
                                                cfg.get('DEFAULT', option),
                                                cfg['DEFAULT'][option]))

for option in cfg['TEST']:
    cse.cprint("TEST {0} : {1} : {2}".format(option,
                                             cfg.get('TEST', option),
                                             cfg['TEST'][option]), 'yellow')

for option in cfg['CI']:
    cse.cprint("CI {0} : {1} : {2}".format(option,
                                           cfg.get('CI', option),
                                           cfg['CI'][option]), 'blue')

'''
#cse.cprint("Start config read....", 'yellow')

cfg = exConfig('config.ini')
sectionList = cfg.getSectionList()

#cse.cprint("config data : %s " % sectionList, 'yellow')

for section in sectionList:
    #cse.cprint("section data : %s " % section, 'yellow')
    sectionlen = cfg.getSectionlength(section)
    for i in range(0, sectionlen):
        cse.cprint("section data : %s " % cfg.getSectionData(section, i), 'red')

    #for ld in len(section):
     #   cse.cprint("section : %s " % section[ld], 'blue')
'''

'''
cfg = configparser.ConfigParser()
cfg.read('config.ini')

cse.cprint("cfg.sections : %s" % cfg.sections(), 'blue')
'''
#secret_key = config['DEFAULT']['SECRET_KEY'] # 'secret-key-of-myapp'
#ci_hook_url = config['CI']['HOOK_URL'] # 'web-hooking-url-from-ci-service'

#print("%s" % sessionList)

#    for option in config['DEFAULT']:
#        print("DEFAULT {0} : {1} : {2}".format(option, config.get('DEFAULT', option), config['DEFAULT'][option]))
#    print("====================================================================")
#    print("%s" % len(config['CI']))

'''
for i in config.sections():
    print("TEST {0} : {1} : {2}".format(i, config.get('TEST', i), config['TEST'][i]))
print("====================================================================")


for j in config['CI']:
    print("CI {0} : {1} : {2}".format(j, config.get('CI', j), config['CI'][j]))
print("====================================================================")
'''