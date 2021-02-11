from Tests.tests_validators import *
from Tests.tests_repo import *
from Tests.tests_domain import *
from Tests.tests_services import *
from Tests.tests_utils import *

from UI.console import Console

######################################################################################################################

try:
    srv_main()
    repo_main()
    domain_main()
    validators_main()
    utils_main()
except:
    pass

c = Console()
c.run()
