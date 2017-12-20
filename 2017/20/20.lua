local particules = {}

for line in io.lines("input20.txt") do
  local pX, pY, pZ, vX, vY, vZ, aX, aY, aZ = line:match("p=<([-%d]+),([-%d]+),([-%d]+)>, v=<([-%d]+),([-%d]+),([-%d]+)>, a=<([-%d]+),([-%d]+),([-%d]+)>")
  local part = {
    coords = { pX,pY,pZ },
    velocity = { vX,vY,vZ },
    acceleration = { aX,aY,aZ },
    dist = math.abs(pX) + math.abs(pY) + math.abs(pZ),
  }
  table.insert(particules, part)
end

function newVelocity(v,a)
  local vX,vY,vZ = unpack(v)
  local aX,aY,aZ = unpack(a)
  return vX+aX,vY+aY,vZ+aZ
end

function newCoords(p,v)
  local pX,pY,pZ = unpack(p)
  local vX,vY,vZ = unpack(v)
  return pX+vX,pY+vY,pZ+vZ
end

for g=1,1000 do
  local miniDist = particules[1].dist
  for i = 1, #particules do
    if particules[i] then
      local aX, aY, aZ = unpack(particules[i].acceleration)
      local vX, vY, vZ = unpack(particules[i].velocity)
      local pX, pY, pZ = unpack(particules[i].coords)

      particules[i].velocity = {newVelocity(particules[i].velocity,particules[i].acceleration)}
      particules[i].coords = {newCoords(particules[i].coords,particules[i].velocity)}

      particules[i].dist = math.abs(particules[i].coords[1]) + math.abs(particules[i].coords[2]) + math.abs(particules[i].coords[3])

      if particules[i].dist < miniDist then
        nearest = i
        miniDist = particules[i].dist
      end
    end
  end
end

print(nearest-1)