# main_with_ini.py
import exConfig

config = exConfig.init('config.ini')
sessionList = config.getSessionList()

#secret_key = config['DEFAULT']['SECRET_KEY'] # 'secret-key-of-myapp'
#ci_hook_url = config['CI']['HOOK_URL'] # 'web-hooking-url-from-ci-service'

print("%s" % sessionList)

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