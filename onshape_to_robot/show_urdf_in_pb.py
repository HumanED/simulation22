import os.path as path
import sys
import time

import pybullet as p
import pybullet_data

# Process the argument and set urdf_file accordingly
if len(sys.argv) != 2:
    raise Exception('The script needs exactly one argument - the name of the folder to load the model from')

passed_path = path.join(path.curdir, sys.argv[1])
file_options = [passed_path, path.join(passed_path, 'robot.urdf')]
urdf_file = None
for file_option in file_options:
    if path.exists(file_option) and (path.splitext(file_option)[-1] == '.urdf'):
        urdf_file = file_option
        print(f'Loading {urdf_file}')
        break
if not urdf_file:
    raise Exception(f'No valid urdf file found, tried {file_options}')

# Start it up
pc = p.connect(p.GUI)
# Make it o that you can use the included demo models (not used rn)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# Load the requested urdf
p.loadURDF(urdf_file, useFixedBase=True)

# The rest is just left over but kept cause it might be useful

# Some extras if you want them
# p.loadURDF('plane.urdf')
# p.setGravity(0, 0, -10)

# Just some prints and apply some force/velocity idk to the joints
# print(p.getNumBodies(), p.getNumJoints(0), p.getJointInfo(0, 1))
# p.setJointMotorControl2(0, 1, p.VELOCITY_CONTROL, targetVelocity=-0.5, force=100)
# p.setJointMotorControl2(0, 3, p.VELOCITY_CONTROL, targetVelocity=0, force=0)

# the loop - runs at 120Hz and exits safely on Ctrl-C, though for me it hangs on closing the window which is a pain
try:
    while p.isConnected():
        p.stepSimulation()
        time.sleep(1/120)
except KeyboardInterrupt:
    p.disconnect()
