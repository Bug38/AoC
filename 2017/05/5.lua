
function readAll(file)
  local f = assert(io.open(file, "rb"))
  local content = f:read("*all")
  f:close()
  return content
end

local input = readAll("input5.txt")

--input = [[0
--3
--0
--1
---3]]

function string:split(sep)
  local sep, fields = sep or "\n", {}
  local pattern = string.format("([^%s]+)", sep)
  self:gsub(pattern, function(c) fields[#fields+1] = c end)
  return fields
end

local count = 0
local instr = input:split()
local i=1

while i <= #instr do
  local tmpInstr = instr[i]

--[[PART 1]]--
--  instr[i] = instr[i] +1

--[[PART 2]]--
  instr[i] = (tonumber(instr[i]) >= 3) and (instr[i] - 1) or (instr[i] +1)

  i = i + tmpInstr
  count = count + 1
end

print(count)