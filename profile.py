import geni.portal as portal
import geni.rspec.pg as pg

pc = portal.Context()
request = pc.makeRequestRSpec()

node = request.XenVM("head")

node.cores = 32
node.ram = 64000
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
node.routable_control_ip = "true"

node.addService(pg.Execute(shell="/bin/sh",command="sudo bash /local/repository/install_docker.sh"))

pc.printRequestRSpec(request)