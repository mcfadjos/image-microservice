import rpyc

c = rpyc.connect("localhost", 18861)
print(c.root.exposed_get_image("Forest", "C:\\Temp"))
