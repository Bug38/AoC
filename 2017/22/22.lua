input = {}

for line in io.lines("input22.txt") do
  local tabLine = {}
  for char in line:gmatch('.') do
    table.insert(tabLine, char)
  end
  table.insert(input, tabLine)
end

local cpt = 0  -- PART 1

local nodes = {}
for i = 1, #input do
  for j = 1, #input[i] do
    nodes[j .. ";" .. i] = input[i][j]
  end
end

local coords = {
  x = math.floor(#input / 2) + 1,
  y = math.floor(#input / 2) + 1
}

local function changeStatus()
  if nodes[coords.x .. ";" .. coords.y] == 'W' then
    nodes[coords.x .. ";" .. coords.y] = '#'
    cpt = cpt + 1
  elseif nodes[coords.x .. ";" .. coords.y] == '#' then
    nodes[coords.x .. ";" .. coords.y] = 'F'
  elseif nodes[coords.x .. ";" .. coords.y] == 'F' then
    nodes[coords.x .. ";" .. coords.y] = '.'
  else
    nodes[coords.x .. ";" .. coords.y] = 'W'
  end
end

local dir = 0

for loop = 1, 10000000 do

  if     nodes[coords.x .. ";" .. coords.y] == '#' then dir = (dir + 1) % 4
  elseif nodes[coords.x .. ";" .. coords.y] == 'F' then dir = (dir + 2) % 4
  elseif nodes[coords.x .. ";" .. coords.y] == 'W' then -- Don't change
  else                                                  dir = (dir - 1) % 4
  end

  changeStatus()

  if     dir == 0 then coords.y = coords.y - 1
  elseif dir == 1 then coords.x = coords.x + 1
  elseif dir == 2 then coords.y = coords.y + 1
  elseif dir == 3 then coords.x = coords.x - 1
  end

end

print(cpt)
