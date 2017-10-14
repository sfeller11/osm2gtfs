# coding=utf-8
import sys

class Debug(object):
    """The Debug class contains special functions used for debugging

    """ 

    def __init__(self, args):
        """Contructor function
        """
        # Load config file from argument of standard location
        self.debug_level = self._define_debug_level(args)

    @staticmethod
    def print_shape_for_leaflet(shape):
        print "var shape = [",
        i = 0
        for node in shape:
            print "new L.LatLng(" + str(node["lat"]) + ", " + str(node["lon"]) + ")",
            if i != len(shape) - 1:
                print ",",
            i += 1
        print "];"
        i = 0
        for node in shape:
            print "L.marker([" + str(node["lat"]) + ", " + str(node["lon"]) + "]).addTo(map)"
            print "    .bindPopup(\"" + str(i) + "\").openPopup();"
            i += 1

    def write(self,message_type, message):
        
        if message_type == 'warning' and self.debug_level in [0,1]:
            sys.stderr.write(message)
        
        elif message_type == 'error' and self.debug_level == 2:
            sys.stderr.write(message)
        
        elif message_type == 'debug'and self.debug_level == 3:
            print message


    def _define_debug_level(self,args):

         if args.debug is not None:
            return args.debug
         else:
            return 0
    






