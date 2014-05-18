from __future__ import division

import vector
class Vehicle(object):
    def __init__(self, x, y, maxSpeed, mass):
        self.maxSpeed=maxSpeed
        self.mass=mass
        self.pos=vector.Vector(x, y)
        self.velocity=vector.Vector(0,0)
    def update(self):
        #change velocity
        self.pos+=self.velocity
def seek(agent, target):
    desired_velocity=(target.pos-agent.pos).normalize()*agent.maxSpeed
    return desired_velocity-agent.velocity
def flee(agent, target):
    desired_velocity=(agent.pos-target.pos).normalize()*agent.maxSpeed
    return desired_velocity-agent.velocity
def arrive(agent, target, deceleration):
    toTarget=target.pos-agent.pos
    dist=toTarget.magnitude()
    if (dist>0):
        tweaker=0.3
        speed=dist/(deceleration*tweaker)
        speed=min(speed, agent.maxSpeed)
        desired_velocity=(toTarget*speed)*(1/dist)
        return desired_velocity-agent.velocity
    return vector.Vector(0,0)
