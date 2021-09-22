import os
import sys

print('Is now running Anaconda: ' + str(os.path.exists(os.path.join(sys.prefix, 'conda-meta'))))
