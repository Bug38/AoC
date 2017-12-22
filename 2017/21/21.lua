local start_time = os.clock()

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

local function hash(t)
  local out = ""
  for i=1,#t do
    for j=1,#t do
      out = out .. t[i][j]
    end
  end
  return out
end

local function printInput(t)
  for i = 1, #t do
    local out = ""
    for j = 1, #t[i] do out = out .. " " .. tostring(t[i][j]) end
    print(out)
  end
end

input = {
  { ".","#","." },
  { ".",".","#" },
  { "#","#","#" },
}

local match = {}

local function rotate(t)
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
      tmp = match[hash(tmp)]
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

print(string.format("[%f] Data loaded", os.clock() - start_time))

for i=1,#rules do
  match[hash(rules[i].iT)] = rules[i].oT
  match[hash(flipH(rules[i].iT))] = rules[i].oT
  match[hash(flipV(rules[i].iT))] = rules[i].oT
  match[hash(rotate(rules[i].iT))] = rules[i].oT
  match[hash(rotate(rotate(rules[i].iT)))] = rules[i].oT
  match[hash(rotate(rotate(rotate(rules[i].iT))))] = rules[i].oT
  match[hash(flipH(rotate(rules[i].iT)))] = rules[i].oT
  match[hash(flipV(rotate(rules[i].iT)))] = rules[i].oT
end

print(string.format("[%f] Map built", os.clock() - start_time))

--print()
--print("Start input :")
--printInput(input)
print()

print("Reset cpt, starting alorithm")
start_time = os.clock()
print()

for loop = 1, 22 do
  if #input % 2 == 0 then
    input = newInput(2)
  elseif #input % 3 == 0 then
    input = newInput(3)
  end
  print(string.format("[%f] %2d -> size = %5d", os.clock() - start_time,loop,#input))
end

local cpt = 0
for i=1,#input do
  for j=1,#input do
    if input[i][j] == "#" then cpt = cpt + 1
    end
  end
end

print("Lights on : "..cpt)
print()