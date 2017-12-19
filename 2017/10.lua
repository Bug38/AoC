local input = "192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12"
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

print("Input :")
print(unpack(input))
print("Input size : "..#input)

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
  for i=1,#tab do
    res = bit.bxor(res,tab[i])
  end
  return res
end

local hash = {}
for i=0,15 do
  local tmp = {}
  for j=1,16 do
    tmp[j] = list[(i)*16 + j]
  end
  hash[i+1] = bitwiseblock(tmp)
end

local function hashString(hash)
  local out = ""
  for i=1,#hash do
    out = out .. string.format("%.2x", hash[i])
  end
  return out
end

print(unpack(hash))
print(hashString(hash))


--print(list[1]*list[2])