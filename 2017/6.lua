local input = "14 0 15 12 11 11 3 5 1 6 8 4 9 1 8 4"

--input = "0 2 7 0"

function string:split(sep)
  local sep, fields = sep or "\n", {}
  local pattern = string.format("([^%s]+)", sep)
  self:gsub(pattern, function(c) fields[#fields+1] = c+0 end)
  return fields
end

local memoryStates = {}
local alreadySeen = 0 --Part2

local function isKnown(memoryState)
  for i=1,#memoryStates do
    if memoryStates[i] == table.concat(memoryState) then alreadySeen = i --[[Part2]] return true end
  end
  memoryStates[#memoryStates+1] = table.concat(memoryState)
end

local function findMax(table)
  local index = 1
  for i=2,#table do
    if table[i] > table[index] then index = i end
  end
  return index
end

local cycles = 0
local bank = input:split(" ")

while not ok do
  local maxIndex = findMax(bank)
  local processes = bank[maxIndex]
  bank[maxIndex] = 0
  local indexRedist = (maxIndex+1 > #bank) and 1 or maxIndex+1
  while processes > 0 do
    bank[indexRedist] = bank[indexRedist] + 1
    processes = processes - 1
    indexRedist = (indexRedist+1 > #bank) and 1 or indexRedist+1
  end
  cycles = cycles + 1
  if isKnown(bank) then ok = 1 end
end

print(cycles-alreadySeen)