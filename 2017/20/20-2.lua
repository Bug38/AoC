local particules = {}

for line in io.lines("input20.txt") do
  --p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
  local pX, pY, pZ, vX, vY, vZ, aX, aY, aZ = line:match("p=<([-%d]+),([-%d]+),([-%d]+)>, v=<([-%d]+),([-%d]+),([-%d]+)>, a=<([-%d]+),([-%d]+),([-%d]+)>")
  local part = {
    coords = { pX,pY,pZ },
    velocity = { vX,vY,vZ },
    acceleration = { aX,aY,aZ },
    --dist = math.abs(pX) + math.abs(pY) + math.abs(pZ),
  }
  table.insert(particules, part)
end

--local oldNearest = 1
--local nearest
local deleted = 0
local oldDeleted = 0

function areEqualCoords(c1, c2)
  return c1[1] == c2[1] and c1[2] == c2[2] and c1[3] == c2[3]
end

function removeParticules()
  local toRemove = {}
  -- Remove particules that collide
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
  --print(vX,vY,vZ)
  --print(aX,aY,aZ)
  vX,vY,vZ = vX+aX,vY+aY,vZ+aZ
  --print(vX,vY,vZ)
  return vX,vY,vZ
end
function newCoords(p,v)
  local pX,pY,pZ = unpack(p)
  local vX,vY,vZ = unpack(v)
  --print(pX,pY,pZ)
  --print(vX,vY,vZ)
  pX,pY,pZ = pX+vX,pY+vY,pZ+vZ
  --print(pX,pY,pZ)
  return pX,pY,pZ
end

for g=1,100 do
  --local miniDist = particules[1].dist
  removeParticules()
  -- Calculate new pos
  for i = 1, #particules do
    if particules[i] then
      local aX, aY, aZ = unpack(particules[i].acceleration)
      local vX, vY, vZ = unpack(particules[i].velocity)
      local pX, pY, pZ = unpack(particules[i].coords)

      particules[i].velocity = {newVelocity(particules[i].velocity,particules[i].acceleration)}
      particules[i].coords = {newCoords(particules[i].coords,particules[i].velocity)}

      --particules[i].dist = math.abs(particules[i].coords[1]) + math.abs(particules[i].coords[2]) + math.abs(particules[i].coords[3])

      --if particules[i].dist < miniDist then
      --  nearest = i
      --  miniDist = particules[i].dist
      --end
    end
  end
  --if oldNearest ~= nearest then
  --  print("Particule " .. nearest .. " at distance " .. miniDist .. "(old was " .. oldNearest .. ")")
  --end
  --oldNearest = nearest
  if oldDeleted ~= deleted then
    print("Particules : " .. #particules - deleted)
    oldDeleted = deleted
  end
end

local cpt = 0
for i=1,#particules do
  if particules[i] ~= nil then cpt = cpt + 1 end
end

print(cpt)