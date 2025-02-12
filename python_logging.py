import logging
import math
# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
DAT_FORMAT = "%d.%m.%Y %H:%M:%S"

logging.basicConfig ( filename = "basicLogging.log",
					  level = logging.DEBUG,
					  format = LOG_FORMAT,
					  datefmt = DAT_FORMAT,
					  filemode = 'w' )

# Create a new instance					   
logger = logging.getLogger()

# example usage of the logging module

def quadratic_formula ( a, b, c):
	""" Returns the solutions to the equation ax^2 + bx + c = 0."""
	logger.info ( "quadratic_formula({0}, {1}, {2})".format ( a, b, c))
	
	# Compute the discriminant
	logger.debug( "# Compute the discriminant" )
	disc = b**2 - 4*a*c

	# Compute the roots
	logger.debug ( "# Compute the roots" )
	root1 = (-b + math.sqrt(disc)) / (2*a)
	root2 = (-b - math.sqrt(disc)) / (2*a)

	# Return the roots
	logger.debug ( "# Compute the roots" )
	return ( root1, root2 )

roots = quadratic_formula ( 1, 0, -4)
print ( roots )