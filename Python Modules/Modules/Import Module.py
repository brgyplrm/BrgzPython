# USE A MODULE

import Modules

Modules.greeting("Jonathan")

#Variables in Modules
import Modules

a = Modules.person1["age"]
print(a)

#RENAMING A MODULE - Modules AS MX
import Modules as mx

a = mx.person1["age"]
print(a)

# BUILT IN MODULES
import platform

x = platform.system()
print(x)

# USING dir() FUNCTION
import platform

x = dir(platform)
print(x)

# IMPORT USING "FROM" FROM MODULES

from Modules import person1

print (person1["age"])