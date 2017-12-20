local clock = os.clock
function sleep(n)
  -- seconds
  local t0 = clock()
  while clock() - t0 <= n do
  end
end

input = {}

for line in io.lines("input19.txt") do
  local tabLine = {}
  for char in line:gmatch('.') do
    table.insert(tabLine, char)
  end
  table.insert(input, tabLine)
end

--input = {
--  { " "," "," "," "," ","|",},
--  { " "," "," "," "," ","|"," "," ","+","-","-","+",},
--  { " "," "," "," "," ","A"," "," ","|"," "," ","C",},
--  { " ","F","-","-","-","|","-","-","-","-","E","|","-","-","+",},
--  { " "," "," "," "," ","|"," "," ","|"," "," ","|"," "," ","D",},
--  { " "," "," "," "," ","+","B","-","+"," "," ","+","-","-","+",},
--}

local letters = ""

local continue = true

local i, j = 1, 1

local dir = "vrt" -- start with vertical, then hrz for horizontal
local from = "top"

-- Find entry point
for tmp = 1, #input[i] do
  if input[i][tmp] ~= " " then
    j = tmp
    break
  end
end

function log(...)
  print(...)
end

function printres(...)
  --io.write(...)
end

local cpt = 0

while continue do
  cpt = cpt+1
  log(i, j, input[i][j])
  if dir == "vrt" then
    --vertical search
    if from == "top" then
      i = i + 1
      if input[i][j] == "+" then
        dir = "hrz"
        if input[i][j + 1] and input[i][j + 1] ~= " " then
          from = "left"
          log("Go right")
        elseif input[i][j - 1] and input[i][j - 1] ~= " " then
          from = "right"
          log("Go left")
        else
          log("error. dir = " .. tostring(dir) .. ", from = " .. tostring(from) .. ", i:j = " .. tostring(i) .. ":" .. tostring(j))
          continue = false
        end
      elseif input[i][j]:find("%a") then
        letters = letters .. input[i][j]
        printres(input[i][j])
      elseif input[i][j] == " " then
        continue = false
      end
    elseif from == "bot" then
      i = i - 1
      if input[i][j] == "+" then
        dir = "hrz"
        if input[i][j + 1] and input[i][j + 1] ~= " " then
          from = "left"
          log("Go right")
        elseif input[i][j - 1] and input[i][j - 1] ~= " " then
          from = "right"
          log("Go left")
        else
          log("error. dir = " .. tostring(dir) .. ", from = " .. tostring(from) .. ", i:j = " .. tostring(i) .. ":" .. tostring(j))
          continue = false
        end
      elseif input[i][j]:find("%a") then
        letters = letters .. input[i][j]
        printres(input[i][j])
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
          log("Go down")
        elseif input[i - 1] and input[i - 1][j] and input[i - 1][j] ~= " " then
          from = "bot"
          log("Go up")
        else
          log("error. dir = " .. tostring(dir) .. ", from = " .. tostring(from) .. ", i:j = " .. tostring(i) .. ":" .. tostring(j))
          continue = false
        end
      elseif input[i][j]:find("%a") then
        letters = letters .. input[i][j]
        printres(input[i][j])
      elseif input[i][j] == " " then
        continue = false
      end
    elseif from == "right" then
      j = j - 1
      if input[i][j] == "+" then
        dir = "vrt"
        if input[i + 1] and input[i + 1][j] and input[i + 1][j] ~= " " then
          from = "top"
          log("Go down")
        elseif input[i - 1] and input[i - 1][j] and input[i - 1][j] ~= " " then
          from = "bot"
          log("Go up")
        else
          log("error. dir = " .. tostring(dir) .. ", from = " .. tostring(from) .. ", i:j = " .. tostring(i) .. ":" .. tostring(j))
          continue = false
        end
      elseif input[i][j]:find("%a") then
        letters = letters .. input[i][j]
        printres(input[i][j])
      elseif input[i][j] == " " then
        continue = false
      end
    end
  else
    log("error. dir = " .. tostring(dir) .. ", from = " .. tostring(from) .. ", i:j = " .. tostring(i) .. ":" .. tostring(j))
    continue = false
  end
  --sleep(0.05)
end

print(letters,cpt)