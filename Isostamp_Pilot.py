from bin.isostamp_search import run as run_isostamp
from bin.database_combine import run as run_database_combine
import sys

run_isostamp(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))

if len(sys.argv) == 11:
	run_database_combine(sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])
else:
	run_database_combine(sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], '', sys.argv[9])