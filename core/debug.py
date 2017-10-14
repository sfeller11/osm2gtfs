# coding=utf-8


class Debug(object):
    """The Debug class contains special functions used for debugging

    """

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

    def write(message_type, message, debug_level):
        
        if message_type = 'warning' and debug_level in ['','warning']:
            sys.stderr.write(message)
        
        elif message_type = 'error' and debug_level in ['','error']:
            sys.stderr.write(message)
        
        elif message_type = 'debug'and debug_level in ['','debug']:
            print message


        



