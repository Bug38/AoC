input = {}

for line in io.lines("input19.txt") do
  local tabLine = {}
  for char in line:gmatch('.') do
    table.insert(tabLine, char)
  end
  table.insert(input, tabLine)
end

local letters = "" -- PART 1
local cpt     = 0  -- PART 2

local continue = true

local i, j = 1, 1

local dir  = "vrt" -- start with vertical direction
local from = "top" -- start at top

-- Find entry point
for tmp = 1, #input[i] do
  if input[i][tmp] ~= " " then
    j = tmp
    break
  end
end

while continue do
  cpt = cpt+1
  if dir == "vrt" then
    if from == "top" then
      i = i + 1
      if input[i][j] == "+" then
        dir = "hrz"
        if input[i][j + 1] and input[i][j + 1] ~= " " then
          from = "left"
        elseif input[i][j - 1] and input[i][j - 1] ~= " " then
          from = "right"
        else
          continue = false
        end
      elseif input[i][j]:find("%a") then
        letters = letters .. input[i][j]
      elseif input[i][j] == " " then
        continue = false
      end
    elseif from == "bot" then
      i = i - 1
      if input[i][j] == "+" then
        dir = "hrz"
        if input[i][j + 1] and input[i][j + 1] ~= " " then
          from = "left"
        elseif input[i][j - 1] and input[i][j - 1] ~= " " then
          from = "right"
        else
          continue = false
        end
      elseif input[i][j]:find("%a") then
        letters = letters .. input[i][j]
      elseif input[i][j] == " " then
        continue = false
      end
    end
  elseif dir == "hrz" then
    if from == "left" then
      j = j + 1
      if input[i][j] == "+" then
        dir = "vrt"
        if input[i + 1] and input[i + 1][j] and input[i + 1][j] ~= " " then
          from = "top"
        elseif input[i - 1] and input[i - 1][j] and input[i - 1][j] ~= " " then
          from = "bot"
        else
          continue = false
        end
      elseif input[i][j]:find("%a") then
        letters = letters .. input[i][j]
      elseif input[i][j] == " " then
        continue = false
      end
    elseif from == "right" then
      j = j - 1
      if input[i][j] == "+" then
        dir = "vrt"
        if input[i + 1] and input[i + 1][j] and input[i + 1][j] ~= " " then
          from = "top"
        elseif input[i - 1] and input[i - 1][j] and input[i - 1][j] ~= " " then
          from = "bot"
        else
          continue = false
        end
      elseif input[i][j]:find("%a") then
        letters = letters .. input[i][j]
      elseif input[i][j] == " " then
        continue = false
      end
    end
  else
    continue = false
  end
end

print(letters,cpt)