class Configuration:
    confs = {}

    default_conf_file = "../conf"

    ##initialize with file name and read in file
    def __init__(self, conf_file=default_conf_file, confs=None):
        if conf_file is not None:
            self.conf_file = conf_file
        if confs is not None:
            self.confs = confs
        self.initialize()

    def initialize(self):
        try:
            file = open(self.conf_file, "r")
            lines = file.readlines()
            for line in lines:
                # this line is comment
                if line.startswith("#"):
                    pass
                ##this line does not follow typical configuration
                elif "=" not in line:
                    pass
                else:
                    key = line.split("=")[0].strip()
                    value = line.split("=")[1].strip()
                    ##if value contains more options
                    value_list = []
                    if "," in value:
                        l = value.split(",")
                        value_list = list(map(lambda x: x.strip(), l))
                    else:
                        value_list.append(value)

                    self.confs[key] = value_list
        except (IOError, OSError) as error:
            print "error during initialize configure %s", error
            return False
        return True

        ## get configuration value corresponding to key

    def get(self, key):
        if self.confs.get(key) is None:
            return None
        try:
            if self.confs[key] is not None:
                return self.confs[key]
            else:
                return None
        except KeyError as error:
            print "error when try to get by key", error
        return None

    def set(self, key, values=None):
        if not values:
            return
        l = values.split(",")
        value_list = list(map(lambda x: x.strip(), l))
        self.confs[key] = value_list

    def print_conf(self):
        print (self.confs)
        print (self.conf_file)