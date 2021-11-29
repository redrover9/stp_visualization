

class Cable:

    def link(self, local_switch, local_port, remote_switch, remote_port):
        port = [[local_switch, local_port], [remote_switch, remote_port]]
        return port
