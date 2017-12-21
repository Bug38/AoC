local rules = {}

for line in io.lines("input21.txt") do
  local rule = {
    iT = {},
    oT = {}
  }
  local sep1, sep2 = line:find(" => ")
  for row in line:sub(1, sep1 - 1):gmatch("[.#]+") do
    local r = {}
    for char in row:gmatch(".") do table.insert(r, char) end
    table.insert(rule.iT, r)
  end
  for row in line:sub(sep2 + 1, #line):gmatch("[.#]+") do
    local r = {}
    for char in row:gmatch(".") do table.insert(r, char) end
    table.insert(rule.oT, r)
  end
  table.insert(rules, rule)
end

input = {
  { ".","#","." },
  { ".",".","#" },
  { "#","#","#" },
}

local function printInput(t)
  for i = 1, #t do
    local out = ""
    for j = 1, #t[i] do out = out .. " " .. tostring(t[i][j]) end
    print(out)
  end
end

local function areEqual(t1, t2)
  if #t1 ~= #t2 then return false end
  local equal = true
  for i = 1, #t1 do
    for j = 1, #t1 do
      if t1[i][j] ~= t2[i][j] then return false end
    end
  end
  return true
end

local function rotateRight(t)
  local rotRight = {}
  for i = 1, #t do
    rotRight[i] = {}
  end
  for i = 1, #t do
    for j = 1, #t do
      rotRight[j][#t - (i - 1)] = t[i][j]
    end
  end
  return rotRight
end

local function flipH(t)
  local flip = {}
  for i = 1, #t do
    flip[#t - (i - 1)] = t[i]
  end
  return flip
end

local function flipV(t)
  local flip = {}
  for i = 1, #t do
    flip[i] = {}
    for j = 1, #t do
      flip[i][#t - (j - 1)] = t[i][j]
    end
  end
  return flip
end

local function areEquiv(t1, t2)
  if #t1 ~= #t2 then return false end

  -- Without conversion
  local equal = areEqual(t1, t2)

  -- With rotation
  if not equal then
    local rotRight = t1
    for rot = 1, 3 do
      rotRight = rotateRight(rotRight)
      if areEqual(rotRight, t2) then
        equal = true
        break
      end
    end
  end

  -- With flip
  if not equal then
    equal = areEqual(flipH(t1), t2) or areEqual(flipV(t1), t2)
  end

  -- Both
  if not equal then
    equal = areEqual(flipH(rotateRight(t1)), t2)
    or areEqual(flipV(rotateRight(t1)), t2)
    or areEqual(rotateRight(flipV(t1)), t2)
    or areEqual(rotateRight(flipH(t1)), t2)
  end
  return equal
end

local function transformTable(t)
  for i = 1, #rules do
    if areEquiv(t, rules[i].iT) then
      return rules[i].oT
    end
  end
  print("ERROR, can't find equiv for table :")
  printInput(t)
  return nil
end

local function newInput(x)
  local output = {}
  for i=1,#input*(x+1)/x do
    output[i] = {}
  end
  local offsetRow, offsetColumn = 0, 0
  for i = 1, #input - (x-1), x do
    for j = 1, #input - (x-1), x do
      local tmp = {}
      for k=1,x do
        tmp[k] = {}
        for l=1,x do
          tmp[k][l] = input[i+(k-1)][j+(l-1)]
        end
      end
      tmp = transformTable(tmp)
      for i=1,#tmp do
        for j=1,#tmp do
          output[i+offsetRow][j+offsetColumn] = tmp[i][j]
        end
      end
      offsetColumn = offsetColumn + x+1
    end
    offsetColumn = 0
    offsetRow = offsetRow + x+1
  end
  return output
end

print("Start input :")
printInput(input)
print("Start input :")

for loop = 1, 18 do
  if #input % 2 == 0 then
    input = newInput(2)
  elseif #input % 3 == 0 then
    input = newInput(3)
  end

  local cpt = 0
  for i=1,#input do
    for j=1,#input do
      if input[i][j] == "#" then cpt = cpt + 1
      end
    end
  end
  print("After cycle "..loop..", "..cpt.." lights stay on.")
end
