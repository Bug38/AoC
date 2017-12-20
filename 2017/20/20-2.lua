local particules = {}

for line in io.lines("input20.txt") do
  local pX, pY, pZ, vX, vY, vZ, aX, aY, aZ = line:match("p=<([-%d]+),([-%d]+),([-%d]+)>, v=<([-%d]+),([-%d]+),([-%d]+)>, a=<([-%d]+),([-%d]+),([-%d]+)>")
  local part = {
    coords = { pX,pY,pZ },
    velocity = { vX,vY,vZ },
    acceleration = { aX,aY,aZ },
  }
  table.insert(particules, part)
end

function areEqualCoords(c1, c2)
  return c1[1] == c2[1] and c1[2] == c2[2] and c1[3] == c2[3]
end

function removeParticules()
  local toRemove = {}
  for i = 1, #particules do
    local toDelete = false
    for j = i+1, #particules do
      if i ~= j then
        if particules[i] and particules[j] then
          if areEqualCoords(particules[i].coords, particules[j].coords) then
            particules[j]=nil
            toDelete = true
          end
        end
      end
    end
    if toDelete == true then
      particules[i] = nil
    end
  end
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

for g=1,100 do
  removeParticules()
  for i = 1, #particules do
    if particules[i] then
      local aX, aY, aZ = unpack(particules[i].acceleration)
      local vX, vY, vZ = unpack(particules[i].velocity)
      local pX, pY, pZ = unpack(particules[i].coords)

      particules[i].velocity = {newVelocity(particules[i].velocity,particules[i].acceleration)}
      particules[i].coords = {newCoords(particules[i].coords,particules[i].velocity)}
    end
  end
end

local cpt = 0
for i=1,#particules do
  if particules[i] ~= nil then cpt = cpt + 1 end
end

print(cpt)