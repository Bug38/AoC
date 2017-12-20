function code10(input)
  local list = "0"
  for i=1,255 do
    list = list..","..i
  end

  --input = "1,2,4"
  --list  = "0,1,2,3,4"

  function string:split(sep)
    local sep, fields = sep or "\n", {}
    local pattern = string.format("([^%s]+)", sep)
    self:gsub(pattern, function(c) fields[#fields+1] = c+0 end)
    return fields
  end

  local function createInput(str)
    local tb = {}
    for i=1,#str do
      tb[i] = str:byte(i)
    end
    table.insert(tb,17)
    table.insert(tb,31)
    table.insert(tb,73)
    table.insert(tb,47)
    table.insert(tb,23)
    return tb
  end

  input = createInput(input)
  list  = list:split(",")

  --print("Input :")
  --print(unpack(input))
  --print("Input size : "..#input)

  local skipSize = 0
  local currentPos = 0
  local currentLenght = 0

  local function revert(buff)
    local tmpbuff = {}
    for i=1,#buff do
      tmpbuff[#buff-i+1] = buff[i]
    end
    --print(unpack(tmpbuff))
    return tmpbuff
  end

  for cpt = 1,64 do --64 rounds
    for i=1,#input do
      currentLenght = input[i]
      --print("Pos: "..currentPos.." ; Len: "..currentLenght.." ; Skip: "..skipSize)
      if currentLenght > 1 then
        local buffer = {}
        for j=0,currentLenght-1 do
          buffer[j+1] = list[((j + currentPos) % #list) + 1]
        end
        buffer = revert(buffer)
        for j=0,currentLenght-1 do
          list[((j + currentPos) % #list) + 1] = buffer[j+1]
        end
      end
      currentPos = (currentLenght + currentPos + skipSize) % #list
      skipSize = skipSize + 1
    end
    --print(unpack(list))
  end

  --print(unpack(list))

  local function bitwiseblock(tab)
    local res = 0
    for i=1,#tab do res = bit.bxor(res,tab[i]) end
    return res
  end

  local hash = {}
  for i=0,15 do
    local tmp = {}
    for j=1,16 do tmp[j] = list[(i)*16 + j] end
    hash[i+1] = bitwiseblock(tmp)
  end

  local function hashString(hash)
    local out = ""
    for i=1,#hash do
      out = out .. string.format("%.2x", hash[i])
    end
    return out
  end

  return hashString(hash)
end

local input = "xlqgujun"
--input = "flqrgnkx"

local hdd = {}
local usedCases = 0
local hex2bin = {
	["0"] = "0000",
	["1"] = "0001",
	["2"] = "0010",
	["3"] = "0011",
	["4"] = "0100",
	["5"] = "0101",
	["6"] = "0110",
	["7"] = "0111",
	["8"] = "1000",
	["9"] = "1001",
	["a"] = "1010",
  ["b"] = "1011",
  ["c"] = "1100",
  ["d"] = "1101",
  ["e"] = "1110",
  ["f"] = "1111"
	}

for i=0,127 do
  local str = code10(input.."-"..tostring(i))
  local tmpOut = {}
  for i in str:gmatch(".") do
    i = string.lower(i)
    for j in hex2bin[i]:gmatch(".") do
      table.insert(tmpOut,j)
      if j == '1' then usedCases = usedCases + 1 end
    end
  end
  hdd[i+1] = tmpOut
end


local groups = 0

local function floodfill(x,y,char)
  if hdd[x] then
    if hdd[y] then
      local actual = hdd[x][y]
      if actual == '1' then
        hdd[x][y] = '#'
        floodfill(x-1,y,'1')
        floodfill(x+1,y,'1')
        floodfill(x,y-1,'1')
        floodfill(x,y+1,'1')
        return true
      end
    end
  end
end

--for i=1,#hdd do
--  print(table.concat(hdd[i]))
--end

for i=1,#hdd do
  --print("line "..i)
  for j=1,#hdd[i] do
    if floodfill(i,j,'1') then groups = groups + 1 end
    end
end

--for i=1,#hdd do
--  print(table.concat(hdd[i]))
--end

print("Groups     : "..groups)
print("Used cases : "..groups)
