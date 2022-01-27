import time

import pybullet as p
import pybullet_data

# Start it up
pc = p.connect(p.GUI)
# Make it o that you can use the included demo models (not used rn)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load the demo urdf
p.loadURDF('finger.urdf', useFixedBase=True)

# Some extras if you want them
# p.loadURDF('plane.urdf')
p.setGravity(0, 0, -10)

# Just some prints and apply some force/velocity idk to the joints
print(p.getNumBodies(), p.getNumJoints(0), p.getJointInfo(0, 1))
p.setJointMotorControl2(0, 1, p.VELOCITY_CONTROL, targetVelocity=-0.5, force=100)
p.setJointMotorControl2(0, 3, p.VELOCITY_CONTROL, targetVelocity=0, force=0)

# the loop - runs at 120Hz and exits safely on Ctrl-C, though for me it hangs on closing the window which is a pain
try:
    while p.isConnected():
        p.stepSimulation()
        time.sleep(1/120)
except KeyboardInterrupt:
    p.disconnect()
    print('Out!')
