import argparse
# import sys
import os.path as path
import time

import pybullet as p
import pybullet_data

parser = argparse.ArgumentParser(description='Script for quick displaying of a urdf file in pybullet.')
parser.add_argument('passed_path_str', nargs=1, type=str,
        help='path to the urdf file or a folder in which there is a \'robot.urdf\' file')
parser.add_argument('-nf', '--not-fixed', action='store_true', default=False,
        help='disable fixed base')

args = parser.parse_args()

passed_path = path.join(path.curdir, args.passed_path_str[0])
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
p.loadURDF(urdf_file, useFixedBase=not args.not_fixed)

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
