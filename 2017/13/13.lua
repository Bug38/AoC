function readAll(file)
  local f = assert(io.open(file, "rb"))
  local content = f:read("*all")
  f:close()
  return content
end

local input = readAll("input13.txt")

--input = [[0: 3
--1: 2
--4: 4
--6: 4]]

--------------------------
----- DAY 13 -------------
--------------------------

local layers = {}

local toplayer   = 0
local picoSecond = 0
local severity   = 0
local delay      = 0

-- populate layers
for line in input:gmatch("[^\n.]*") do
  if #line > 0 then
    local depth, range = line:match("(%d+): (%d+)")
    layers[tonumber(depth)] = tonumber(range)
    toplayer = toplayer > tonumber(depth) and toplayer or tonumber(depth)
  end
end

--print("Top layer : "..toplayer)

local function printLayers()
  for i = 0, toplayer do
    if layers[i] then
      print("layer " .. i .. " : " .. layers[i])
    else
      print("empty")
    end
  end
end
--print(toplayer)

while true do
  local caught = false
  picoSecond = delay
  for i=0,toplayer do
    if layers[i] then
      if picoSecond % (layers[i]*2-2) == 0 then
        --print("Caught !")
        caught = true
        break
      end
    end
    picoSecond = picoSecond + 1
  end
  delay = delay + 1
  if caught == false then
    print(delay - 1)
    break
  end
end