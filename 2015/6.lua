local lights = {}
for i = 1, 1000 do
  lights[i] = {}
  for j = 1, 1000 do
    lights[i][j] = 0
  end
end

--[[PART 1]]

--for line in io.lines("input6.txt") do
--  table.insert(lights, line)
--  local order, imin, jmin, imax, jmax = line:match("([%a ]+)(%d+),(%d+) through (%d+),(%d+)")
--  if order:find("turn on") then
--    for i = imin+1, imax+1 do
--      for j = jmin+1, jmax+1 do
--        lights[i][j] = 1
--      end
--    end
--  elseif order:find("turn off") then
--    for i = imin+1, imax+1 do
--      for j = jmin+1, jmax+1 do
--        lights[i][j] = 0
--      end
--    end
--  elseif order:find("toggle") then
--    for i = imin+1, imax+1 do
--      for j = jmin+1, jmax+1 do
--        if lights[i][j] == 0 then
--          lights[i][j] = 1
--        else
--          lights[i][j] = 0
--        end
--      end
--    end
--  end
--end
--
--local cpt = 0
--for i = 1, 1000 do
--  for j = 1, 1000 do
--    cpt = cpt + lights[i][j]
--  end
--end

--[[PART 2]]

for line in io.lines("input6.txt") do
  table.insert(lights, line)
  local order, imin, jmin, imax, jmax = line:match("([%a ]+)(%d+),(%d+) through (%d+),(%d+)")
  if order:find("turn on") then
    for i = imin+1, imax+1 do
      for j = jmin+1, jmax+1 do
        lights[i][j] = lights[i][j] + 1
      end
    end
  elseif order:find("turn off") then
    for i = imin+1, imax+1 do
      for j = jmin+1, jmax+1 do
        lights[i][j] = lights[i][j] - 1
        if lights[i][j] < 0 then lights[i][j] = 0 end
      end
    end
  elseif order:find("toggle") then
    for i = imin+1, imax+1 do
      for j = jmin+1, jmax+1 do
        lights[i][j] = lights[i][j] + 2
      end
    end
  end
end

local cpt = 0
for i = 1, 1000 do
  for j = 1, 1000 do
    cpt = cpt + lights[i][j]
  end
end

print(cpt)