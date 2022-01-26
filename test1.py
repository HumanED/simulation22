import time

import pybullet as p
import pybullet_data

FPS = 100

pc = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.loadURDF('plane.urdf')

p.loadURDF('finger.urdf', useFixedBase=True)
p.loadURDF('robot.urdf', useFixedBase=True, basePosition=[-0.2, -0.2, 0])

# p.setGravity(0, 0, -10)

# print(p.getNumBodies(), p.getNumJoints(0), p.getJointInfo(0, 1))
# p.setJointMotorControl2(0, 1, p.VELOCITY_CONTROL, targetVelocity=-0.5, force=100)
# p.setJointMotorControl2(0, 3, p.VELOCITY_CONTROL, targetVelocity=0, force=0)

try:
    while p.isConnected():
        # print(p.getConnectionInfo())
        p.stepSimulation()
        time.sleep(1/FPS)
except KeyboardInterrupt:
    p.disconnect()
    print('Out!')
