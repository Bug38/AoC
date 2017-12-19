function readAll(file)
  local f = assert(io.open(file, "rb"))
  return f:read("*all"), f:close()
end

local input = readAll("input3.txt")

--input = '^v^v^v^v'

coordsR = {
  ns = 0,
  we = 0
}
coordsS = {
  ns = 0,
  we = 0
}

local homesS = {["0;0"] = 0}
local homesR = {["0;0"] = 0}
local homes_R = 1
local homes_S = 1

for i = 1, #input do
  local char = input:sub(i, i)
  if i % 2 == 0 then
    if char == '>' then
      coordsR['we'] = coordsR['we'] + 1
    elseif char == '<' then
      coordsR['we'] = coordsR['we'] - 1
    elseif char == '^' then
      coordsR['ns'] = coordsR['ns'] + 1
    elseif char == 'v' then
      coordsR['ns'] = coordsR['ns'] - 1
    end
    local home = coordsR['ns'] .. ";" .. coordsR['we']

    print("Robot : "..home)
    if homesR[home] then
      homesR[home] = homesR[home] + 1
      print("\told")
    else
      print("\tnew")
      homes_R = homes_R + 1
      homesR[home] = 1
    end
  else
    if char == '>' then
      coordsS['we'] = coordsS['we'] + 1
    elseif char == '<' then
      coordsS['we'] = coordsS['we'] - 1
    elseif char == '^' then
      coordsS['ns'] = coordsS['ns'] + 1
    elseif char == 'v' then
      coordsS['ns'] = coordsS['ns'] - 1
    end
    local home = coordsS['ns'] .. ";" .. coordsS['we']
    print("Santa : "..home)
    if homesS[home] then
      homesS[home] = homesS[home] + 1
      print("\told")
    else
      print("\tnew")
      homes_S = homes_S + 1
      homesS[home] = 1
    end
  end
end

print(homes_S,homes_R)

for i,j in pairs(homesR) do
  if homesS[i] == nil then print("Add "..i) homes_S = homes_S + 1 end
end

print(homes_S)