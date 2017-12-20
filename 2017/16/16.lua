function readAll(file)
  local f = assert(io.open(file, "rb"))
  local content = f:read("*all")
  f:close()
  return content
end

local input = readAll("input16.txt")

--input = "s12"

local initPrograms = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p" }
local programs = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p" }

print(table.concat(programs, ""))

function string:split(sep)
  local sep, fields = sep or "\n", {}
  local pattern = string.format("([^%s]+)", sep)
  self:gsub(pattern, function(c)
    fields[#fields + 1] = c
  end)
  return fields
end

input = input:split(",")

local function spin(num)
  num = tonumber(num)
  local tmpProgs = {}
  for i = 1, #programs do
    tmpProgs[((i + num - 1) % #programs) + 1] = programs[i]
  end
  programs = tmpProgs
end

local function swap(pos1, pos2)
  pos1, pos2 = tonumber(pos1), tonumber(pos2)
  programs[pos2], programs[pos1] = programs[pos1], programs[pos2]
end

print(1000000000%36)

for cpt = 1, 1000000000%36 do
  for i = 1, #input do
    local orderLine = input[i]
    local ordertype = orderLine:sub(1, 1)
    if ordertype == "s" then
      spin(orderLine:match("%d+"))
    elseif ordertype == "x" then
      pos1, pos2 = orderLine:match("(%d+)/(%d+)")
      swap(pos1 + 1, pos2 + 1)
    elseif ordertype == "p" then
      local prog1, prog2 = orderLine:sub(2, #orderLine):match("(%a+)/(%a+)")
      local pos1, pos2
      for i = 0, #programs do
        if programs[i] == prog1 then
          pos1 = i
        end
        if programs[i] == prog2 then
          pos2 = i
        end
      end
      swap(pos1, pos2)
    end
  end
  if cpt%1000000 == 0 then print(cpt) end
  if table.concat(programs, "") == table.concat(initPrograms, "") then
    print(cpt)
  end
end

print(table.concat(programs, ""))
