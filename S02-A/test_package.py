# Import whole module
import mon_package as mp
# Import only one method
from mon_package.operation import add_2

print(mp.operation.add_2(4))
print(add_2(4))
