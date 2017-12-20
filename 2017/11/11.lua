function readAll(file)
  local f = assert(io.open(file, "rb"))
  local content = f:read("*all")
  f:close()
  return content
end

local input = readAll("input11.txt")

--------------------------
----- DAY 11 -------------
--------------------------

-- final coords
local coords = {
  x = 0,
  y = 0,
  z = 0
}

--MaxDistance
local maxDist = 0

local function getDistance()
  local dist = math.max(math.abs(coords['x']),math.abs(coords['y']),math.abs(coords['z']))
  maxDist = (maxDist < dist) and dist or maxDist
  return math.max(math.abs(coords['x']),math.abs(coords['y']),math.abs(coords['z']))
end

local function addCoords(x,y,z)
  coords['x'] = coords['x'] + x
  coords['y'] = coords['y'] + y
  coords['z'] = coords['z'] + z
end

local function newCoords(dir)
  if     dir == 'n'  then addCoords( 0, 1,-1)
  elseif dir == 'ne' then addCoords( 1, 0,-1)
  elseif dir == 'nw' then addCoords(-1, 1, 0)
  elseif dir == 's'  then addCoords( 0,-1, 1)
  elseif dir == 'se' then addCoords( 1,-1, 0)
  elseif dir == 'sw' then addCoords(-1, 0, 1)
  end
end

for dir in input:gmatch("%a+") do
  newCoords(dir)
  getDistance()
end

print('MaxDist   : '..maxDist)
print('FinalDist : '..getDistance())
